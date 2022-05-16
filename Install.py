import os
import time

python_install = input("You have python installed?(Y or N):")

if python_install=="Y":
    print("okay the requirements will be installed ^^")
    time.sleep(3)

if python_install=="N":
    print("Oh so the latest version of python will be installed :D")
    time.sleep(3)
    os.system("sudo apt-get install python3.10.4")

if python_install=="y":
    print("okay the requirements will be installed ^^")
    time.sleep(3)

if python_install=="n":
    print("Oh so the latest version of python will be installed :D")
    time.sleep(3)
    os.system("sudo apt-get install python3.10.4")


else:
   Retry = input("MmMmMmM that is not a opcion Y or N?:")
   
   print("THAT IS NOT A OPCION, but only i will install python")
   time.sleep(4)
   os.system("sudo apt-get install python3.10.4")
   
   if Retry=="N":
        print("Oh so the latest version of python will be installed")
        time.sleep(3)
        os.system("sudo apt-get install python3.10.4")
   
   if Retry=="Y":
        print("okay the requirements will be installed")
        time.sleep(3)
   
   if Retry=="y":
       print("okay the requirements will be installed")
       time.sleep(3)

   if Retry=="n":
       print("Oh so the latest version of python will be installed")
       time.sleep(3)
       os.system("sudo apt-get install python3.10.4")


  
os.system("pip install colorama")

print("Installation was completed sucefully ^^")

Start = input("Do you want to start Xhacking? (Y or N):")

if Start=="Y":
    print("Ok! So if you like the proyect give a star ;)...")
    time.sleep(2)
    print("starting Xhacking...")
    os.system("python3.9 Xhacking.py")

if Start=="N":
    print("Okay exiting!...\nGood bye! ^^")
    time.sleep(2)
    os.system("exit")

if Start=="y":
    print("Ok! So if you like the proyect give a star ;)...")
    time.sleep(2)
    print("starting Xhacking...")
    os.system("python3.9 Xhacking.py")

if Start=="n":
    print("Okay exiting!...\nGood bye! ^^")
    time.sleep(2)
    os.system("exit")



