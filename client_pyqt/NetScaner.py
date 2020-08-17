from socket import *
from progress.bar import IncrementalBar
import time
from multiprocessing.pool import ThreadPool

class NetScaner(object):
    def __init__(self, *args,):
        super().__init__(*args)

    def iplist(self, ipMaxValue=255):
        localip = gethostbyname(gethostname()).split('.')
        ipPattern = localip[0] + '.' + localip[1] + '.' + localip[2] + '.'
        ipTable = []

        for i in range(0, ipMaxValue):
            ipTable.append(ipPattern + str(i))

        ipTable.append('127.0.0.1')
        
        return ipTable

    def portChecker(self, ip):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.3)
        conn = s.connect_ex((ip, 5005))
        if(conn == 0):
            s.close()
            return ip
        else:
            s.close()
            return 0
    
    def scanIps(self, ipTable):
        pool = ThreadPool(processes=4)
        suffix = '%(percent)d%% [%(elapsed_td)s / %(eta)d / %(eta_td)s]'
        bar = IncrementalBar('scanning', max = len(ipTable), suffix=suffix)
        for ip in ipTable:
            pf = pool.apply_async(self.portChecker, args=(ip,)) 
            pfres = pf.get()
            if( pfres == 0):
                bar.next()
                continue
            else:
                break
                bar.finish()
                return pfres  
        bar.finish()
        return 0
        



