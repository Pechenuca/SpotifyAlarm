from SpotifyParser import SpotifyParser 
from MusicDownloader import MusicDownloader
from Db import Db 
from threading import Thread
from pygame import mixer 
import os
import time
import datetime
import shutil

mixer.init()
class AlarmChecker(Thread):
    """
    Класс для работы с будильником
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_running = True
        self.dbClass = Db()
        self.dbClass.create()

    def timeChecker(self):
        """
        Метод для проверки времени, значение берет из бд
        """
        dateNow = datetime.datetime.now()
        res = self.dbClass.select('all')
        if (res != []):
            for i in range(0, len(res)):
                dateListDb = []
                dateListNow = []
                count = 0

                for j in range(0, 5):
                    dateListDb.append(int(res[i][1].split('-')[j]))

                for attr in [ 'year', 'month', 'day', 'hour', 'minute']:
                    dateListNow.append(getattr(dateNow, attr))

                for z in range(0, len(dateListDb)):
                    if (dateListNow[z] == dateListDb[z]):
                        count = count + 1

                if (count == 5):
                    self.dbClass.delete(res[0])
                    tmpFiles = os.listdir("tmp")
                    
                    for i in range(len(tmpFiles)):
                        mixer.music.load('tmp/' + tmpFiles[i])
                        mixer.music.play()
                    
                        while mixer.music.get_busy():
                            time.sleep(1)
                
            print(count)
        else:
            self.terminate()
        

    def run(self):
        """
        Метод запускает цикл
        """
        while self.is_running:
            self.timeChecker()
            time.sleep(2)

    def terminate(self):
        """
        Метод останавливает трэд
        """
        self.is_running = False

class ComandManager(object):
    """
    Класс обработчик команд клиента
    """
    def __init__(self, com):
        self.com = com
        self.dbClass = Db()
        self.dbClass.create()
        
    
    def checkAtrs(self, atr):
        """
        Проверка цельности комманды
        """
        try:
            atr[1]
        except IndexError:
            return 0
    
    def commandSelect(self):
        """
        Метод который выполняет нужный метод исходя из команды
        """
        if(self.com[0] == ''):
            return 'Hello from server'
        if(self.com[0] == 'setAlarm'):
            if(self.checkAtrs(self.com) != 0):
                alarmArgs = [ self.com[1], self.com[2] ]
                return self.setAlarm(alarmArgs)

        elif(self.com[0] == 'delAlarm'):
             if(self.checkAtrs(self.com) != 0):
                return self.setAlarm(self.com[1])

        elif(self.com[0] == 'shAlarm'):
            if(self.checkAtrs(self.com) != 0):
                return self.shAlarm(self.com[1])
        
        elif(self.com[0] == 'stopMusic'):
            if(self.checkAtrs(self.com) == 0):
                return self.stopMusic()
        
    
    def setAlarm(self, *args):
        """
        поставить будильник
        """
        
        self.dbClass.insert(args[0])
        self.dwnMusic(args[1])

        return 'setAlarmOk'
    
    def delAlarm(self, atr):
        """
        удалить будильник
        """
        self.dbClass.delete(atr)

        return 'delAlarmOk'

    def clsTmp(self):
        """
        удалить папку с музыкой
        """
        shutil.rmtree('tmp')
    
    def shAlarm(self, atr):
        """
        показать будильники
        """
        res = self.dbClass.select(atr)
        return str(res)


    def stopMusic(self):
        """
        Остановить будильник
        """
        mixer.quit()
        time.sleep(60)
        self.clsTmp()
        mixer.init()
        return 'stopMusicOk'
        
    
    def dwnMusic(self, playlistId):
        """
        скачать музыку
        """
        
        #get playlist
        sp = SpotifyParser(playlistId) #'5VFBiAtuHsUK7FFxYkKJ9u'
        spotifySongsArray = sp.getSongs()

        #donload songs
        for i in range(0, len(spotifySongsArray)):
            md = MusicDownloader(spotifySongsArray[i])
            toDownload = md.findVideo()
            print(toDownload)
            md.dnSong(toDownload)
        
        #rename all files

        tmpFiles = os.listdir("tmp")

        for index, file in enumerate(tmpFiles):
            os.rename(os.path.join("tmp", file), os.path.join("tmp", ''.join([str(index), '.mp3'])))
        
        return 'dwnMusicOk'
