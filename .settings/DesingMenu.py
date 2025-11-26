import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd All-Tools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mDesing Menu 1")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mDesing Menu 2")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mDesing Menu 3")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mDesing Menu 4")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mExit System")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Sett1Ngs: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd All-Tools && mv MainMenu.py /data/data/com.termux/files/home/All-Tools/.temp/DesingTemp/ && cd && cd All-Tools && cd .settings && cd desing && mv MainMenu.py /data/data/com.termux/files/home/All-Tools/ && cd && cd All-Tools && cd .temp && cd DesingTemp && mv MainMenu.py /data/data/com.termux/files/home/All-Tools/.settings/desing/ && cd && cd All-Tools && bash .settings/Applined.sh")
elif(op==2):
 os.system("clear")
 os.system("cd && cd All-Tools && mv MainMenu.py /data/data/com.termux/files/home/All-Tools/.temp/ && cd && cd All-Tools && cd .settings && mv MainMenu.py /data/data/com.termux/files/home/All-Tools/ && cd && cd All-Tools && cd .temp && mv MainMenu.py /data/data/com.termux/files/home/All-Tools/.settings/ && cd && cd All-Tools && bash .settings/Applined.sh")
elif(op==3):
 os.system("clear")
 os.system("cd && cd All-Tools && mv MainMenu.py /data/data/com.termux/files/home/All-Tools/.temp/DesingTemp2/ && cd && cd All-Tools && cd .settings && cd desing2 && mv MainMenu.py /data/data/com.termux/files/home/All-Tools/ && cd && cd All-Tools && cd .temp && cd DesingTemp2 && mv MainMenu.py /data/data/com.termux/files/home/All-Tools/.settings/desing2/ && cd && cd All-Tools && bash .settings/Applined.sh")
elif(op==4):
 os.system("clear")
 os.system("cd && cd All-Tools && mv MainMenu.py /data/data/com.termux/files/home/All-Tools/.temp/DesingTemp3/ && cd && cd All-Tools && cd .settings && cd desing3 && mv MainMenu.py /data/data/com.termux/files/home/All-Tools/ && cd && cd All-Tools && cd .temp && cd DesingTemp3 && mv MainMenu.py /data/data/com.termux/files/home/All-Tools/.settings/desing3/ && cd && cd All-Tools && bash .settings/Applined.sh")
elif(op==5):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System...")
 sys.exit()
elif(op==6):
 os.system("cd")
 os.system("cd All-Tools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd All-Tools")
 os.system("python2 MainMenu.py")
