from Connector import Connector
from NetScaner import NetScaner
import sys 
import time
from PyQt5 import QtWidgets
import mainscreen, alert
import ast

class Alert(QtWidgets.QMainWindow, alert.Ui_MainWindow):
    def __init__(self, parent=None, msg=''):
        super(Alert, self).__init__(parent)
        self.setupUi(self)
        self.plainTextEdit.insertPlainText(msg)


class MainScren(QtWidgets.QMainWindow, mainscreen.Ui_SpotifyParser):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit_2.setText('Поиск сервера...')
        self.pushButton_2.clicked.connect(self.connect)

    def scan(self):
        ns = NetScaner()
        ips = ns.iplist()
        ip = ns.scanIps(ips)
        return ip

    def getAlarms(self, con):
        res = con.sendCommand('shAlarm all', 1024)
        result = res.decode("utf-8")
        x = ast.literal_eval(u'' + result)
        self.listWidget.clear()
        for r in x:
            self.listWidget.addItem(str(r))

    def connect(self):
        ip = self.scan()
        if ip != 0:
            self.lineEdit_2.setText('Подключение установленно!')
            self.lineEdit_2.setText('connected-> ip: ' + str(ip) + ' port: 5005')
            con = Connector(ip, 5005)
            self.getAlarms(con)
            self.sendId(con)
            self.lineEdit_2.setText('connected-> ip: ' + str(ip) + ' port: 5005')
        else:
            self.lineEdit_2.setText('Подключение не установленно! Проверьте сервер.')
    
    def sendId(self, con):
        inputText = self.lineEdit.text()
        if inputText == '':
            Alert(self, "Поле не может быть пустым").show()
        else:
            self.lineEdit_2.setText('Загрузка')
            time = self.alarmTime.text().replace('.', '-').replace(' ', '-').replace(':', '-')
            res = con.sendCommand('setAlarm ' + time + ' ' + self.lineEdit.text(), 1024)

            if res.decode("utf-8") == 'problem with spotify':
                Alert(self, "Персер вернул 404, используйте vpn или proxy").show()
            else:
                Alert(self, "Бyдильник добавлен").show()
            

def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = MainScren()  
    window.show()  
    app.exec_()
       

if __name__ == '__main__':  
    main()  

#
# https://open.spotify.com/playlist/0LFWbKOrdXAqrZ5fCWqOyi
# 0LFWbKOrdXAqrZ5fCWqOyi