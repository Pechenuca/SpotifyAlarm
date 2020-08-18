from Connector import Connector
from NetScaner import NetScaner

ns = NetScaner()
ips = ns.iplist()
ip = ns.scanIps(ips)

if(ip != 0):
    print(ip)
    con = Connector(ip, 5005)
    #res = con.sendCommand('setAlarm 2020-08-13-18-0-00 5VFBiAtuHsUK7FFxYkKJ9u', 1024)
    res = con.sendCommand('shAlarm all', 1024)
    #res = con.sendCommand('stopMusic', 1024)
    print(res)
else:
    print('Error during connection to server, please check your server')