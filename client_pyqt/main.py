from Connector import Connector

con = Connector('localhost', 5005)
res = con.sendCommand('dwnMusic 5VFBiAtuHsUK7FFxYkKJ9u', 1024)
print(res)