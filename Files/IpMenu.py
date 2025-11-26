import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mAstraNmap - Security scanner used to find hosts and services on a computer network")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mEvilURL - Generate unicode evil domains for IDN Homograph Attack and detect them")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mOSIF - Open Source Information Facebook")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mWeeman - HTTP server for phishing in python")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mMaxSubdoFinder - Tool for Discovering Subdomain")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mEasymap - Nmap Shortcut")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mTrape - People tracker on the Internet OSINT")
print("  \033[1;34m[ 08 ] >> \033[1;36;40mRed Hawk - Information Gathering, Vulnerability Scanning and Crawling")
print("  \033[1;34m[ 09 ] >> \033[1;36;40mLittleBrother - Information gathering (OSINT) on a person (EU)")
print("  \033[1;34m[ 10 ] >> \033[1;36;40mSeeker - Accurately Locate Smartphones and GPS")
print("  \033[1;34m[ 11 ] >> \033[1;36;40mReconDog - Reconnaissance Swiss Army Knife")
print("  \033[1;34m[ 12 ] >> \033[1;36;40mD-Tech - Pentesting the Modern Web")
print("  \033[1;34m[ 13 ] >> \033[1;36;40mWebKiller - Tool Information Gathering Write By Python")
print("  \033[1;34m[ 14 ] >> \033[1;36;40mIpHack - Track Location With Live Address And City in Termux")
print("  \033[1;34m[ 15 ] >> \033[1;36;40mNikto - Nikto web server scanner")
print("  \033[1;34m[ 16 ] >> \033[1;36;40miSMTP - SMTP Server Tester")
print("  \033[1;34m[ 17 ] >> \033[1;36;40mMailFinder - OSINT tool for finding email by first and last name")
print("  \033[1;34m[ 18 ] >> \033[1;36;40mExit System - log out AllHackingTools")
print("  \033[1;34m[ 19 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("1nf0RmatI0n: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd All-Tools && cd AstraNmap && bash astranmap.sh && cd && cd All-Tools && python3 src/Timer2.py && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd All-Tools && cd EvilURL && python3 evilurl.py && cd && cd All-Tools && python2 MainMenu.py")
elif(op==6):
 os.system("clear")
 os.system("cd && cd All-Tools && cd Easymap && php easymap.php && cd && cd All-Tools && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd All-Tools && cd OSIF && python2 osif.py && cd && cd All-Tools && python2 MainMenu.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd All-Tools && cd weeman && python2 weeman.py && cd && cd All-Tools && python2 MainMenu.py")
elif(op==5):
 os.system("clear")
 os.system("cd && cd All-Tools && cd MaxSubdoFinder && python2 maxteroit.py && cd && cd All-Tools && python3 src/Timer2.py && python2 MainMenu.py")
elif(op==7):
 os.system("clear")
 os.system("cd && cd All-Tools && cd trape && python trape.py && cd && cd All-Tools && python3 src/Timer2.py && python2 MainMenu.py")
elif(op==8):
 os.system("clear")
 os.system("cd && cd All-Tools && cd RED_HAWK && php rhawk.php && cd && cd All-Tools && python2 MainMenu.py")
elif(op==9):
 os.system("clear")
 os.system("cd && cd All-Tools && cd LittleBrother && python3 LittleBrother.py && cd && cd All-Tools && python2 MainMenu.py")
elif(op==10):
 os.system("clear")
 os.system("cd && cd All-Tools")
 print("Open a second window in Termux and run ngrok on port 8080: ./ngrok http 8080")
 print("Or use serveo.net free tunnel.")
 time.sleep(1.4)
 print("Warning All-Tools has already downloaded ngrok")
 time.sleep(2.3)
 os.system("cd seeker && python seeker.py -t manual && cd && cd All-Tools && python2 MainMenu.py")
elif(op==11):
 os.system("clear")
 os.system("cd && cd All-Tools && cd ReconDog && ./dog && cd && cd All-Tools && python2 MainMenu.py")
elif(op==12):
 os.system("clear")
 os.system("cd && cd All-Tools && cd D-Tech && python2 d-tect.py && cd && cd All-Tools && python2 MainMenu.py")
elif(op==13):
 os.system("clear")
 os.system("cd && cd All-Tools && cd webkiller && python3 webkiller.py && cd && cd All-Tools && python2 MainMenu.py")
elif(op==14):
 os.system("clear")
 os.system("cd && cd All-Tools && cd Files && bash IpHack.sh && python2 MainMenu.py")
elif(op==15):
 os.system("clear")
 os.system("cd && cd All-Tools && cd Files && bash Nikto.sh && echo done! && sleep 3 && cd && cd All-Tools && python2 MainMenu.py")
elif(op==16):
 os.system("clear")
 os.system("cd && cd All-Tools && cd Files && bash iSMTP.sh && echo done! && sleep 3 && cd && cd All-Tools && python2 MainMenu.py")
elif(op==17):
 os.system("clear")
 os.system("cd && cd All-Tools && cd MailFinder && python MailFinder.py && echo done! && sleep 3 && cd && cd All-Tools && python2 MainMenu.py")
elif(op==18):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System...")
 sys.exit()
elif(op==19):
 os.system("cd")
 os.system("cd All-Tools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd All-Tools")
 os.system("python2 Files/IpMenu.py")
