from SpotifyParser import SpotifyParser 
from MusicDownloader import MusicDownloader
from Alarm import Alarm

class ComandManager(object):
    
    def __init__(self, com):
        self.com = com
        self.alarmClass = Alarm()
    
    def checkAtrs(self, atr):
        try:
            atr[1]
        except IndexError:
            return 0
    
    def commandSelect(self):
        if(self.com[0] == 'setAlarm'):
            if(self.checkAtrs(self.com) != 0):
                return self.setAlarm(self.com[1])

        elif(self.com[0] == 'delAlarm'):
             if(self.checkAtrs(self.com) != 0):
                return self.setAlarm(self.com[1])

        elif(self.com[0] == 'clsTmp'):
            if(self.checkAtrs(self.com) == 0):
                return self.clsTmp()

        elif(self.com[0] == 'shAlarm'):
            if(self.checkAtrs(self.com) != 0):
                return self.shAlarm(self.com[1])

        elif(self.com[0] == 'dwnMusic'):
            if(self.checkAtrs(self.com) != 0):
                return self.dwnMusic(self.com[1])
        
    
    def setAlarm(self, atr):
        """
        поставить будильник
        """
        self.alarmClass.setAlarm(atr)

        return 'setAlarmOk'
    
    def delAlarm(self, atr):
        """
        удалить будильник
        """
        self.alarmClass.delAlarm(atr)

        return 'delAlarmOk'

    def clsTmp(self):
        """
        удалить папку с музыкой
        """
        pass
    
    def shAlarm(self, atr):
        """
        показать будильники
        """
        res = self.alarmClass.showAlarm(atr)
        return str(res)
        
    
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
