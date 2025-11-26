import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd All-Tools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mAdminHack - Hack admin panel")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mSubDom - cname finder tool")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mBlazy - modern login bruteforcer")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mSqlMap - SQL injection and database takeover tool")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mWebSploit - An advanced MiTM Framework")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mSqlmate - A friend of SQLmap which will do what you always expected from SQLmap")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mSH33LL - A Easy Shell scanner")
print("  \033[1;34m[ 09 ] >> \033[1;36;40mUltraDDos - Tool for ddos web sites")
print("  \033[1;34m[ 10 ] >> \033[1;36;40mWhatWeb - Next generation web scanner")
print("  \033[1;34m[ 11 ] >> \033[1;36;40mWfuzz - Web application fuzzer")
print("  \033[1;34m[ 12 ] >> \033[1;36;40mExit System - log out All-Tools")
print("  \033[1;34m[ 13 ] >> \033[1;36;40mBack To MainMenu")


op=int(raw_input("Web-Hack1Ng: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd All-Tools && cd AdminHack && bash AdminHack.sh && cd && cd All-Tools && python3 src/Timer2.py && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd All-Tools && cd Files && bash SubDom.sh && cd && cd All-Tools && python3 src/Timer2.py && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd All-Tools && cd Blazy && python2 main.py && cd && cd All-Tools && python3 src/Timer2.py && python2 MainMenu.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd All-Tools && cd sqlmap-dev && python sqlmap.py -wizard && cd && cd All-Tools && python2 MainMenu.py")
elif(op==5):
 os.system("clear")
 os.system("cd && cd All-Tools && cd websploit && websploit && cd && cd All-Tools && python2 MainMenu.py")
elif(op==6):
 os.system("clear")
 os.system("cd && cd All-Tools && cd sqlmate && python2 sqlmate && cd && cd All-Tools && python2 MainMenu.py")
elif(op==7):
 os.system("clear")
 os.system("cd && cd All-Tools && cd SH33LL && python2 sh33l.py && cd && cd All-Tools && python2 MainMenu.py")
elif(op==8):
 os.system("clear")
 os.system("cd && cd All-Tools && cd py-ddoser && python ddos.py && cd && cd All-Tools && python2 MainMenu.py")
elif(op==9):
 os.system("clear")
 os.system("cd && cd All-Tools && cd Ultra-DDos && python2 main.py && cd && cd All-Tools && python2 MainMenu.py")
elif(op==10):
 os.system("clear")
 os.system("cd && cd All-Tools && cd Files && bash whatweb.sh && echo done! && cd && cd All-Tools && python3 src/Timer2.py && python2 MainMenu.py")
elif(op==11):
 os.system("clear")
 os.system("cd && cd All-Tools && cd Files && bash wfuzz.sh && echo done! && cd && cd All-Tools && python3 src/Timer2.py && python2 MainMenu.py")
elif(op==12):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System...")
 sys.exit()
elif(op==13):
 os.system("cd")
 os.system("cd All-Tools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd All-Tools")
 os.system("python2 Files/WebMenu.py")
