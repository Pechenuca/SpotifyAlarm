from Db import Db 
from threading import Thread
from playsound import playsound
import os
import time
import datetime


class AlarmChecker(Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_running = True
        self.dbClass = Db()

    def timeChecker(self):
        dateNow = datetime.datetime.now()
        res = self.dbClass.select(id)

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
                    al = Alarm()
                    al.songPlayer()
        else:
            self.terminate()

    def run(self):
        while self.is_running:
            self.timeChecker()
            time.sleep(5)

    def terminate(self):
        self.is_running = False

class Alarm(object):
    
    def __init__(self):
        self.dbClass = Db()
        self.dbClass.create()

    def setAlarm(self, time):
        self.dbClass.insert(time)
        thread = AlarmChecker(daemon=True)
        thread.start()   
       
    def delAlarm(self, id):
        self.dbClass.delete(id)

    def showAlarm(self, id):
        res = self.dbClass.select(id)
        return res
    
    def songPlayer(self):
        tmpFiles = os.listdir("tmp")
        
        for i in range(len(tmpFiles)):
            playsound('tmp/' + tmpFiles[i])
        
        
        
