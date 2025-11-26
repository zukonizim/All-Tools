cd
cd
cd All-Tools
python3 src/CheckVersion.py
sleep 3
clear
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
cd
cd
cd All-Tools 
cd Tool
mv MainMenu.py /data/data/com.termux/files/home/All-Tools
cd
cd All-Tools
clear
echo -e $b"[ ✔ ]"$g"succesfull verifined"$w
python3 MainMenu.py
