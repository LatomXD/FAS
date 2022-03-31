#!/usr/bin/python3
# Author      : Fall Xavier
# Facebook : Fall Xavier FT Nakano Itsuki XV.
# Github      : https://github.com/Fall-Xavier/zmbf
# Recode Boleh Asal Jangan Ubah Nama Author Atau Github Author
import os, sys, re, time, requests, calendar, json
from datetime import datetime
from datetime import date

try:
	import requests
except ImportError:
	print(" [+] sedang mencoba menginstal module requests....")
	os.system("python -m pip install requests")
	
### GLOBAL WARNA ###
P = '\x1b[1;97m' # PUTIH			   
M = '\x1b[1;91m' # MERAH			
H = '\x1b[1;96m' # HIJAU.			  
K = '\x1b[1;93m' # KUNING.		   
B = '\x1b[1;94m' # BIRU.				 
U = '\x1b[1;95m' # UNGU.			   
O = '\x1b[1;96m' # BIRU MUDA.	 
N = '\x1b[0m'	# WARNA MATI

ses = requests.Session()
try:IP = ses.get("http://ip-api.com/json/").json()["query"]
except requests.exceptions.ConnectionError:exit(" [!] tidak ada koneksi internet")
id = []
komen = "Babas Ganteng"
ct = datetime.now()
n = ct.month
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
tgl = ("%s %s %s"%(ha, op, ta))

def satu():
	token = input(" [?] masukan token : ")
	try:
		nama = ses.get(f"https://graph.facebook.com/me?&access_token={token}").json()["name"]
		open("token.txt", "w").write(token)
		print(f"\n [+] selamat datang {K}{nama}{N} user premium")
		time.sleep(1)
		dua()
	except KeyError:
		exit(" [!] token tidak valid atau akun terkena checkpoint")
				
def dua():
	os.system("clear")
	print(f"""{H}                        ▒█▀▀▀   ░█▀▀█   ▒█▀▀▀█ 
                        ▒█▀▀▀   ▒█▄▄█   ░▀▀▀▄▄ 
                        ▒█░░░   ▒█░▒█   ▒█▄▄▄█
                    {K}Facebook Auto Share Version 1.0""")
	print(f"""{N} ---------------------------{M}[ Infomasi SC ]{N}----------------------------""")
	print(f"""{N}               = Author    : Rochmat Basuki XXY.""")
	print(f"""{N}               = Github    : https://github.com/Babas-XD""")
	print(f"               = Tanggal   : {tgl}")
	print(f"               = IP        : {IP}")
	print(" ----------------------------------------------------------------------")
	time.sleep(3)
	tiga()
		
ses = requests.Session()

def tiga():
	try:
		token = open("token.txt","r").read()
	except (KeyError,IOError):
		login()
	print("               = Masukan link post yang mau di spam share")
	idt = input("               = link post : ")
	limit = int(input("               • masukan limit : "))
	header = {'authority':'graph.facebook.com','cache-control':'max-age=0','sec-ch-ua-mobile':'?0','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36'}
	for x in range(limit):
		post = ses.post(f"https://graph.facebook.com/me/feed?link={idt}&published=0&access_token={token}",headers=header).text
		if 'id' in post:
			print(post)
		else:
			exit(" [!] gagal karena token tidak valid")
	exit("\n [#] selesai")
		
if __name__ == '__main__':
	dua()