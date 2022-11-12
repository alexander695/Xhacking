## -*- coding: utf-8 -*- ##
import os
import random
import time
import webbrowser

from colorama import Fore

#Prepar#
print(Fore.LIGHTMAGENTA_EX + "Preparing...")
time.sleep(3)
os.system("sudo apt-get install python3.9")
os.system("sudo apt-get install python3-pip")
os.system("pip install colorama")
os.system("pip install random")
os.system("pip install time")
os.system("clear")

#banners#
banner1 = (Fore.YELLOW +  """ ▄█    █▄       ▄████████  ▄████████    ▄█   ▄█▄  ▄█  ███▄▄▄▄      ▄███████▄          
 ███    ███     ███    ███ ███    ███   ███ ▄███▀ ███  ███▀▀▀██▄   ███    ███                   
 ███    ███     ███    ███ ███    █▀    ███▐██▀   ███▌ ███   ███   ███    █▀            
▄███▄▄▄▄███▄▄   ███    ███ ███         ▄█████▀    ███▌ ███   ███  ▄███                            
▀▀███▀▀▀▀███▀  ▀███████████ ███        ▀▀█████▄    ███▌ ███   ███ ▀▀███ ████▄                
  ███    ███     ███    ███ ███    █▄    ███▐██▄   ███  ███   ███   ███    ███                                
  ███    ███     ███    ███ ███    ███   ███ ▀███▄ ███  ███   ███   ███    ███                    
  ███    █▀      ███    █▀  ████████▀    ███   ▀█▀ █▀    ▀█   █▀    ████████▀    
 coded by piloxe ^^

      opcions
      \t1 - phishing(cheat website)"                         \t10 - Python3.9
      \t2 - sqlmap (vulnerability scan)                      \t11 - GOD-KILLER (Anon SMS and SMS spam)               
      \t3 - Force Brute (facebook)                           \t12 - Aircrack-ng (Wifi hack)                          
      \t4 - nmap (port scanning)")
      \t5 - PhoneXploit(device hacking)")
      \t6 - python")
      \t7 - python 2")
      \t8 - WPS killer (wifi dumping)")
      \t9 - IpLoger (Get Ip with fake website)               \t0 - Update              """)

      

    
banner2 = (Fore.LIGHTRED_EX + """\ \/ / | | |  / \  / ___| |/ /_ _| \ | |/ ___|
 \  /| |_| | / _ \| |   | ' / | ||  \| | |  _
 /  \|  _  |/ ___ \ |___| . \ | || |\  | |_| |
/_/\_\_| |_/_/   \_\____|_|\_\___|_| \_|\____|
coded by piloxe ^^

  opcions
  \t1 - phishing(cheat website)                          \t10 - Python3.9
  \t2 - sqlmap (vulnerability scan)                      \t11 - GOD-KILLER (Anon SMS and SMS spam)               
  \t3 - Force Brute (facebook)                           \t12 - Aircrack-ng (Wifi hack)                          
  \t4 - nmap (port scanning)
  \t5 - PhoneXploit(device hacking)
  \t6 - python
  \t7 - python 2
  \t8 - WPS killer (wifi dumping)
  \t9 - IpLoger (Get Ip with fake website)               \t0 - Update              """)

def menu_main():
    banners = [banner1, banner2]
    return random.choice(banners)


while True:
 
 print(menu_main())

 opcionMenu = input("select a opcion >>")

 if opcionMenu=="1":
        print("Downloading...")
        os.system("git clone https://github.com/suljot/shellphish.git")
        os.system("cd shellphish")
        os.system("bash shellphish.sh")
        
    
 elif opcionMenu=="2":
        print("Downloading...")
        os.system("git clone https://github.com/sqlmapproject/sqlmap")
        os.system("cd sqlmap")
        os.system("python sqlmap.py -h")
       

 elif opcionMenu=="3": 
         print("Downloading...")
         os.system("git clone https://github.com/Gameye98/FBBrute")
         os.system(" python fbbrute.py")
       

 elif opcionMenu=="4":
        print("Downloading...")
        os.system("git clone https://github.com/nmap/nmap")
        os.system("cd nmap")
        os.system("./configure")
        os.system("make")
        os.system("make install")
        print("intalled correctly")
        print("Usage:")
        print("\nifconfig to see your ip")
        print("nmap -sP (Ip)/24")
        input("\npress enter to back")
        os.system("clear")

 elif opcionMenu=="5":
        print("Downloading...")
        os.system("git clone https://github.com/dadi32/PhoneSploit")
        os.system("cd PhoneSploit")
        os.system("python2 main.py")
        
    
 elif opcionMenu=="6":
        print("Downloading...")
        os.system("git clone https://github.com/TheAlgorithms/Python")
        os.system("cd Python")
        os.system("./configure")
        os.system("make install")
        print("intalled correctly")
        input("\npress enter to back")
        os.system("clear")

 elif opcionMenu=="8":
        print("Downloading...")
        os.system("git clone https://github.com/FDX100/WPS-KILLER")
        os.system("cd WPS-KILLER")
        os.system("python WPS-KILLER.py")
    
 elif opcionMenu=="7":
        os.system("sudo dnf install python2")
        print("intalled correctly")
        input("\npress enter to back")
        os.system("clear")

 elif opcionMenu=="9":
       os.system("git clone https://github.com/alexander695/IPloger")
       os.system("cd IPloger")
       os.system("python3.9 IP.py")
 
 elif opcionMenu=="10":
        os.system("sudo apt install python3.9")
        os.system("python3.9 --version")
        print("intalled correctly")
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
       menu_main()
       

else:
        input("\na problem as ocurred press a key to restart")
        os.system("clear")
