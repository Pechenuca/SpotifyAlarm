from Connector import Connector

con = Connector('localhost', 5005)
#res = con.sendCommand('setAlarm 2020-08-09-00-50-50', 1024)
res = con.sendCommand('shAlarm all', 1024)
#res = con.sendCommand('dwnMusic 5VFBiAtuHsUK7FFxYkKJ9u', 1024)
print(res)