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
    print ("\t1 - phishing")
    print ("\t2 - sqlmap")
    print ("\t3 - Force Brute (facebook) ")
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

    elif opcionMenu=="9":
               os.system("exit")

    else:
     print ("")
     input("\ninvalid opcion press enter to back")
 