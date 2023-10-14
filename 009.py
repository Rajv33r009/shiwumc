import mechanize
import os
import sys
from time import sleep
import requests

browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
browser.set_handle_refresh(False)
url = 'https://m.facebook.com/login.php'

def openlink(msg4):
    r = browser.open(msg4)
    
    def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def sp(stri):
    for letter in stri:
        print(letter, end = "")
        sys.stdout.flush()
        sleep(0.03)

logo =  """\033[1;37;1m     
  
██████╗ ██╗██╗██╗  ██╗ █████╗ ██████╗ ██╗
██╔══██╗██║██║██║  ██║██╔══██╗██╔══██╗██║
██████╔╝██║██║███████║███████║██████╔╝██║
██╔══██╗██║██║██╔══██║██╔══██║██╔══██╗██║
██████╔╝██║██║██║  ██║██║  ██║██║  ██║██║
╚═════╝ ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝
                                         
██████╗ ██╗   ██╗██╗     ███████╗██╗  ██╗
██╔══██╗██║   ██║██║     ██╔════╝╚██╗██╔╝
██████╔╝██║   ██║██║     █████╗   ╚███╔╝ 
██╔══██╗██║   ██║██║     ██╔══╝   ██╔██╗ 
██║  ██║╚██████╔╝███████╗███████╗██╔╝ ██╗
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                                         

-----------------------------------------------"""

def menu():
	os.system('clear')
	print(logo)
	print('[1] Random Uid Crack')
	print('[2] Contact To Owner')
	print('[0] Exit')
	print(47*"-")
	opt = input('[?] Choose : ')
	if opt =='1':
		md()
	elif opt =='2':
		Contact()
	elif opt =='0':
		exit()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		menu()

def aclass():
    browser.open(url)
    browser.select_form(nr=0)
    browser.form['email'] = emailx
    browser.form['pass'] = pwx
    r = browser.submit()
    browser.select_form(nr=0)
    msg1 = str(input("➣Enter 2 step google code : "))
    print(msg1)
    browser.form['approvals_code'] = msg1
    r = browser.submit()
    browser.select_form(nr=0)
    browser.form['name_action_selected'] = ['save_device']
    r = browser.submit()

def poct(comment):
    browser.select_form(nr=0)
    browser.form['comment_text'] = comment
    r = browser.submit()

def is_network_available():
    try:
        # Try to make a simple HTTP request to a known server (e.g., Google)
        response = requests.get("https://www.google.com", timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

print("[-[ TH3 T00L  CR34T3 BY R4JV33R SINGH4NIY4]-]")
emailx = str(input("➣Enter email : "))
pwx = str(input("➣Enter pswrd : "))
aclass()
msg4 = str(input("➣Enter post link : "))
np1 = str(input("➣Enter Hetter Name : "))
msg5 = str(input("➣Enter notepad link : "))
f = open(msg5, 'r')
lines = f.readlines()
f.close()
msg6 = int(input("➣Enter TIME : "))
os.system('clear')
sys.stdout.flush()
print('RajveeR Baap HeRe v1.0')
count = 0

while True:
    for line in lines:
        if len(line) > 3:
            if count != 0:
                sleep(msg6)

            while not is_network_available():
                print("Waiting for network connection to be restored...")
                sleep(10)

            openlink(msg4)
            poct(np1+line)
            print("--> Rajveer Own FiiRe :v ::-->> ", np1, line, "\n")
            count += 1
            if count % 10 == 0:
                sleep(1)