import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd All-Tools && clear && bash Logo.sh")
os.system("cd && bash All-Tools/.desing/SettingMenu1.sh")

op=int(raw_input("Sett1Ngs: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd All-Tools && cd .settings && python2 DesingLogo.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd All-Tools && cd .settings && python2 DesingMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd All-Tools && cd src && mv AnimationLoad1.sh /data/data/com.termux/files/home/All-Tools/.temp/ && cd && cd All-Tools && cd .settings && mv AnimationLoad1.sh /data/data/com.termux/files/home/All-Tools/src/ && cd && cd All-Tools && cd .temp && mv AnimationLoad1.sh /data/data/com.termux/files/home/All-Tools/.settings/ && cd && cd All-Tools && bash .settings/Applined.sh")
elif(op==4):
 os.system("cd && cd All-Tools && cd src && mv AnimationLoad1.sh /data/data/com.termux/files/home/All-Tools/.temp/DesingTemp4/ && mv AnimationLoad2.sh AnimationLoad1.sh && cd && cd All-Tools && cd .temp && cd DesingTemp4 && mv AnimationLoad1.sh AnimationLoad2.sh && mv AnimationLoad2.sh /data/data/com.termux/files/home/All-Tools/src/")
elif(op==5):
 os.system("clear")
 os.system("cd && cd All-Tools && cd .settings && python2 SpecialOpportunities.py")
elif(op==6):
 os.system("clear")
 os.system("cd && nano .zsh_history")
elif(op==7):
 os.system("clear")
 os.system("cd && rm -rf All-Tools/.settings/deletedfiles/.zsh_history && cd && mv .zsh_history All-Tools/.settings/deletedfiles/ && cd && cd All-Tools && python2 MainMenu.py")
elif(op==8):
 os.system("clear")
 os.system("cd && cd All-Tools && bash Logo.sh")
 time.sleep(0.2)
 print("\033[1;31;40mRestoring All-Tools backup...")
 os.system("cd /sdcard/ && cp -r All-Tools /data/data/com.termux/files/home/")
 os.system("cd && bash All-Tools/.settings/RestoreAll-ToolsBackup.sh")
 print("successfully restored backup in: sdcard...")
elif(op==9):
 os.system("clear")
 os.system("cd && cd All-Tools && bash Logo.sh")
 time.sleep(0.2)
 print("\033[1;31;40mWait A Bit For The Backup To Be Created...")
 os.system("cd && cd && cp -r All-Tools /sdcard/")
 print("successfully created a backup in: sdcard...")
elif(op==10):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System...")
 sys.exit()
elif(op==11):
 os.system("cd")
 os.system("cd All-Tools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd All-Tools")
 os.system("python2 MainMenu.py")
