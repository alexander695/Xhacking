import webbrowser
import os
import time
from colorama import Fore
#banner#
print (Fore.YELLOW +  '   ▄█    █▄       ▄████████  ▄████████    ▄█   ▄█▄  ▄█  ███▄▄▄▄      ▄███████▄')          
print (Fore.YELLOW + '  ███    ███     ███    ███ ███    ███   ███ ▄███▀ ███  ███▀▀▀██▄   ███    ███')                   
print (Fore.YELLOW + '  ███    ███     ███    ███ ███    █▀    ███▐██▀   ███▌ ███   ███   ███    █▀')            
print (Fore.YELLOW + ' ▄███▄▄▄▄███▄▄   ███    ███ ███         ▄█████▀    ███▌ ███   ███  ▄███      ')                      
print (Fore.YELLOW + '▀▀███▀▀▀▀███▀  ▀███████████ ███        ▀▀█████▄    ███▌ ███   ███ ▀▀███ ████▄')                
print (Fore.YELLOW + '  ███    ███     ███    ███ ███    █▄    ███▐██▄   ███  ███   ███   ███    ███')                                
print (Fore.YELLOW + '  ███    ███     ███    ███ ███    ███   ███ ▀███▄ ███  ███   ███   ███    ███')                    
print (Fore.YELLOW + '  ███    █▀      ███    █▀  ████████▀    ███   ▀█▀ █▀    ▀█   █▀    ████████▀') 
print ("CODED BY KILLER")

def menu():
    print ("opcions")
    print ("\t1 - phishing(cheat website)")
    print ("\t2 - sqlmap (vulnerabiliti scan")
    print ("\t3 - Force Brute (facebook) ")
    print ("\t4 - nmap (port scanning)")
    print ("\t5 - PhoneXploit(device hacking)")
    print ("\t6 - python")
    print ("\t7 - python 2")
    print ("\t8 - WPS killer (web dumping)")
    print ("\t9 - exit")

    while True:

        menu()

        opcionMenu = input("select a opcion >>")

    if opcionMenu=="1":
        print ("Downloading...")
        os.system("git clone https://github.com/suljot/shellphish.git")
        os.system("cd shellphish")
        os.system("bash shellphish.sh")
        input("\npress enter to back")
        os.system("clear")
    
    if opcionMenu=="2":
        print("Downloading...")
        os.system("git clone https://github.com/sqlmapproject/sqlmap")
        os.system("cd sqlmap")
        os.system("python sqlmap.py -h")
        input("\npress enter to back")
        os.system("clear")

    if opcionMenu=="3": 
         print("Downloading...")
         os.system("git clone https://github.com/Gameye98/FBBrute")
         os.system(" python fbbrute.py")
         input("\npress enter to back")
         os.system("clear")

    if opcionMenu=="4":
        print("Downloading...")
        os.system("git clone https://github.com/nmap/nmap")
        os.system("cd nmap")
        os.system("./configure")
        os.system("make")
        os.system("make install")
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

    if opcionMenu=="6":
        print("Downloading...")
        os.system("git clone https://github.com/FDX100/WPS-KILLER")
        os.system("cd WPS-KILLER")
        os.system("python WPS-KILLER.py")
    
    if opcionMenu=="7":
        os.system("sudo dnf install python2")


    elif opcionMenu=="9":
                os.system("exit")
   
    else:

     print ("")
     input("\ninvalid opcion press enter to back")
