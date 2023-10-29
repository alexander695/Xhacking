## -*- coding: utf-8 -*- ##
import os
import random
import time

class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    END = "\033[0m"
    BOLD = "\033[1m"
    UND = "\033[4m"

#Prepar#
def install():
       print(f"{bcolors.WARNING}Preparing...{bcolors.END}")
       time.sleep(3)
       os.system("sudo apt-get install python3.9")
       os.system("sudo apt-get install python3-pip")
       os.system("pip install colorama")
       os.system("pip install random")
       os.system("pip install time")
       os.system("clear")

with open("bin1.txt", "wb") as bin:
      if bin == "0":
            install()
      else:
            pass
ip = os.popen("hostname -I").read()

#banners#
banner1 = (f"""{bcolors.HEADER}{bcolors.BOLD} \n▄█    █▄       ▄████████  ▄████████    ▄█   ▄█▄  ▄█  ███▄▄▄▄      ▄███████▄          
 ███    ███     ███    ███ ███    ███   ███ ▄███▀ ███  ███▀▀▀██▄   ███    ███                   
 ███    ███     ███    ███ ███    █▀    ███▐██▀   ███▌ ███   ███   ███    █▀            
▄███▄▄▄▄███▄▄   ███    ███ ███         ▄█████▀    ███▌ ███   ███  ▄███                            
▀▀███▀▀▀▀███▀  ▀███████████ ███        ▀▀█████▄    ███▌ ███   ███ ▀▀███ ████▄                
  ███    ███     ███    ███ ███    █▄    ███▐██▄   ███  ███   ███   ███    ███                                
  ███    ███     ███    ███ ███    ███   ███ ▀███▄ ███  ███   ███   ███    ███                    
  ███    █▀      ███    █▀  ████████▀    ███   ▀█▀ █▀    ▀█   █▀    ████████▀    
 coded by piloxe ^^{bcolors.END}""")
   
banner2 = (f"""{bcolors.HEADER}{bcolors.BOLD}\n\ \/ / | | |  / \  / ___| |/ /_ _| \ | |/ ___|
 \  /| |_| | / _ \| |   | ' / | ||  \| | |  _
 /  \|  _  |/ ___ \ |___| . \ | || |\  | |_| |
/_/\_\_| |_/_/   \_\____|_|\_\___|_| \_|\____|
coded by piloxe ^^{bcolors.END}""")

panel = (f"""{bcolors.OKGREEN}\n
\t{bcolors.UND}1{bcolors.END}{bcolors.OKGREEN} - phishing(cheat website)                          \t{bcolors.UND}10{bcolors.END}{bcolors.OKGREEN} - Python3.9 (for almost everything)
\t{bcolors.UND}2{bcolors.END}{bcolors.OKGREEN} - sqlmap (vulnerability scan)                      \t{bcolors.UND}11{bcolors.END}{bcolors.OKGREEN} - GOD-KILLER (Anon SMS and SMS spam)               
\t{bcolors.UND}3{bcolors.END}{bcolors.OKGREEN} - Force Brute (facebook)                           \t{bcolors.UND}12{bcolors.END}{bcolors.OKGREEN} - Aircrack-ng (Wifi hack)                          
\t{bcolors.UND}4{bcolors.END}{bcolors.OKGREEN} - nmap (port scanning)
\t{bcolors.UND}5{bcolors.END}{bcolors.OKGREEN} - PhoneXploit(device hacking)
\t{bcolors.UND}6{bcolors.END}{bcolors.OKGREEN} - python
\t{bcolors.UND}7{bcolors.END}{bcolors.OKGREEN} - python2 (Needed for PhoneXploit)
\t{bcolors.UND}8{bcolors.END}{bcolors.OKGREEN} - WPS killer (wifi dumping)
\t{bcolors.UND}9{bcolors.END}{bcolors.OKGREEN} - IpLoger (Get Ip with fake website)               \t0 - Update{bcolors.END}{bcolors.WARNING}{bcolors.BOLD}    THE FILES YOU  DOWNLOAD WILL BE STORED IN LOCAL PATH /Xhacking{bcolors.END}""") 

while True:
 banners = [banner1, banner2]
 b = random.choice(banners)

 print(b + panel)

 opcionMenu = input("select a opcion >>")

 if opcionMenu=="1":
        print("Downloading...")
        os.system("git clone https://github.com/suljot/shellphish.git")
        os.system("cd shellphish")
        os.system("clear")
        os.system("bash shellphish.sh")
        
    
 elif opcionMenu=="2":
        print("Downloading...")
        os.system("git clone https://github.com/sqlmapproject/sqlmap")
        os.system("clear")
        os.system("python /sqlmap/sqlmap.py -h")
        
 elif opcionMenu=="3": 
         print("Downloading...")
         os.system("git clone https://github.com/Gameye98/FBBrute")
         os.system("clear")
         os.system("python /FBBrute/fbbrute.py")
       
 elif opcionMenu=="4":
        print("Downloading...")
        os.system("git clone https://github.com/nmap/nmap")
        os.system("cd nmap")
        os.system("./configure")
        os.system("make")
        os.system("make install")
        print(f"\n{bcolors.BOLD}{bcolors.OKGREEN}intalled correctly{bcolors.END}")
        print("Usage:")
        print("nmap -sP"+ ip + "/24")
        input("\npress enter to back")
        os.system("clear")

 elif opcionMenu=="5":
        print("Downloading...")
        os.system("git clone https://github.com/dadi32/PhoneSploit")
        os.system("python2 -m pip install Colorama")
        os.system("clear")
        os.system("python2 /PhoneSploit/main.py")
        
 elif opcionMenu=="6":
        print("Downloading...")
        os.system("git clone https://github.com/TheAlgorithms/Python")
        print("Algorithms of python")
        print(f"\n{bcolors.BOLD}{bcolors.OKGREEN}Downloaded correctly{bcolors.END}")
        input("\npress enter to back")
        os.system("clear")

 elif opcionMenu=="8":
        print("Downloading...")
        os.system("git clone https://github.com/FDX100/WPS-KILLER")
        os.system("cd WPS-KILLER")
        os.system("clear")
        os.system("python WPS-KILLER.py")
    
 elif opcionMenu=="7":
        os.system("sudo dnf install python2")
        print(f"\n{bcolors.BOLD}{bcolors.OKGREEN}intalled correctly{bcolors.END}")
        input("\npress enter to back")
        os.system("clear")

 elif opcionMenu=="9":
       os.system("git clone https://github.com/alexander695/IPloger")
       os.system("cd IPloger")
       os.system("clear")
       os.system("python3.9 IP.py")
 
 elif opcionMenu=="10":
        os.system("sudo apt install python3.9")
        os.system("python3.9 --version")
        print(f"\n{bcolors.BOLD}{bcolors.OKGREEN}intalled correctly{bcolors.END}")
        input("\npress enter to back")
        os.system("clear")
 
 elif opcionMenu=="11":
       os.system("git clone https://github.com/FDX100/GOD-KILLER.git")
       os.system("cd GOD-KILLER")
       os.system("python install.py")
       os.system("clear")
       os.system("GOD-KILLER")
 
 elif opcionMenu=="12":
       os.system("wget https://download.aircrack-ng.org/aircrack-ng-1.7.tar.gz")
       os.system("tar -zxvf aircrack-ng-1.7.tar.gz")
       os.system("cd aircrack-ng-1.7")
       os.system("autoreconf -i")
       os.system("./configure --with-experimental")
       os.system("make")
       os.system("make install")
       os.system("ldconfig")
       print("installed correctly")
       print("Tutorial: https://www.geeksforgeeks.org/kali-linux-hacking-wi-fi/")
       print("Credits to @manav014")
       input("\npress enter to back")
       os.system("clear")
 
 elif opcionMenu=="0":
       print("You need to be connected to internet")
       input("Enter to proceed")
       os.system("git pull")
       time.sleep(2)
       os.system("clear")
 else:
        input("\na problem as ocurred. Intenet conection?")
        os.system("clear")
