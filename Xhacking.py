## -*- coding: utf-8 -*-
import webbrowser
import os
import time
from colorama import Fore
#banner#
def menu():
    print (Fore.YELLOW +  '   ▄█    █▄       ▄████████  ▄████████    ▄█   ▄█▄  ▄█  ███▄▄▄▄      ▄███████▄')          
    print (Fore.YELLOW + '  ███    ███     ███    ███ ███    ███   ███ ▄███▀ ███  ███▀▀▀██▄   ███    ███')                   
    print (Fore.YELLOW + '  ███    ███     ███    ███ ███    █▀    ███▐██▀   ███▌ ███   ███   ███    █▀')            
    print (Fore.YELLOW + ' ▄███▄▄▄▄███▄▄   ███    ███ ███         ▄█████▀    ███▌ ███   ███  ▄███      ')                      
    print (Fore.YELLOW + '▀▀███▀▀▀▀███▀  ▀███████████ ███        ▀▀█████▄    ███▌ ███   ███ ▀▀███ ████▄')                
    print (Fore.YELLOW + '  ███    ███     ███    ███ ███    █▄    ███▐██▄   ███  ███   ███   ███    ███')                                
    print (Fore.YELLOW + '  ███    ███     ███    ███ ███    ███   ███ ▀███▄ ███  ███   ███   ███    ███')                    
    print (Fore.YELLOW + '  ███    █▀      ███    █▀  ████████▀    ███   ▀█▀ █▀    ▀█   █▀    ████████▀') 
    print ("CODED BY KILLER")

    print ("opcions")
    print ("\t1 - phishing(cheat website)"                            "\t10 - Python3.9")
    print ("\t2 - sqlmap (vulnerability scan")
    print ("\t3 - Force Brute (facebook) ")
    print ("\t4 - nmap (port scanning)")
    print ("\t5 - PhoneXploit(device hacking)")
    print ("\t6 - python")
    print ("\t7 - python 2")
    print ("\t8 - WPS killer (wifi dumping)")
    print ("\t9 - IpLoger (Get Ip with fake website)")


while True:

 menu()

 opcionMenu = input("select a opcion >>")

 if opcionMenu=="1":
        print ("Downloading...")
        os.system("git clone https://github.com/suljot/shellphish.git")
        os.system("cd shellphish")
        os.system("bash shellphish.sh")
        
    
 if opcionMenu=="2":
        print("Downloading...")
        os.system("git clone https://github.com/sqlmapproject/sqlmap")
        os.system("cd sqlmap")
        os.system("python sqlmap.py -h")
       

 if opcionMenu=="3": 
         print("Downloading...")
         os.system("git clone https://github.com/Gameye98/FBBrute")
         os.system(" python fbbrute.py")
       

 if opcionMenu=="4":
        print("Downloading...")
        os.system("git clone https://github.com/nmap/nmap")
        os.system("cd nmap")
        os.system("./configure")
        os.system("make")
        os.system("make install")
        print("intalled correctly")
        input("\npress enter to back")
        os.system("clear")

 if opcionMenu=="5":
        print("Downloading...")
        os.system("git clone https://github.com/dadi32/PhoneSploit")
        os.system("cd PhoneSploit")
        os.system("python2 main.py")
        
    
 if opcionMenu=="6":
        print("Downloading...")
        os.system("git clone https://github.com/TheAlgorithms/Python")
        os.system("cd Python")
        os.system("./configure")
        os.system("make install")
        print("intalled correctly")
        input("\npress enter to back")
        os.system("clear")

 if opcionMenu=="8":
        print("Downloading...")
        os.system("git clone https://github.com/FDX100/WPS-KILLER")
        os.system("cd WPS-KILLER")
        os.system("python WPS-KILLER.py")
    
 if opcionMenu=="7":
        os.system("sudo dnf install python2")
        print("intalled correctly")
        input("\npress enter to back")
        os.system("clear")

 if opcionMenu=="9":
       os.system("git clone https://github.com/alexander695/IPloger")
       os.system("cd IPloger")
       os.system("python3.9 IP.py")
 
 if opcionMenu=="10":
        os.system("sudo apt install python3.9")
        os.system("python3.9 --version")
        print("intalled correctly")
        input("\npress enter to back")
        os.system("clear")
 else:
      print ("")
      input("\na problem as ocurred press a key to restart")
