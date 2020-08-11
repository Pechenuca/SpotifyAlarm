import sqlite3

class Db(object):
    
    def __init__(self, dbName=''):
        if (dbName == ''):
            self.dbName = 'database.db'
        else:
            self.dbName = dbName
    
    def connect(self):
        return sqlite3.connect(self.dbName)

    def create(self):
        db = self.connect()
        db.cursor().execute('''CREATE TABLE IF NOT EXISTS spotifyAlarms( id INTEGER PRIMARY KEY, alarmTime TEXT ) ''')
        db.commit()
        db.close()


    def insert(self, val):
        db = self.connect()
        db.cursor().execute("INSERT INTO spotifyAlarms (alarmTime) VALUES ('%s')" % val)
        db.commit()
        db.close()


    def select(self, id):
        db = self.connect()
        if(id != 'all'):
            res = db.cursor().execute("SELECT * FROM spotifyAlarms WHERE ('%s')" % id).fetchall()
        else:
            res = db.cursor().execute("SELECT * FROM spotifyAlarms ").fetchall()
            
        db.close()
        return res

    def delete(self, id):
        db = self.connect()
        result = db.cursor().execute("DELETE FROM spotifyAlarms WHERE id = '%s'" % id)
        db.commit()
        db.close()