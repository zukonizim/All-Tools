import time
import os 

R = '\033[31m'
G = '\033[32m' 
C = '\033[36m'
W = '\033[0m' 

# Secret folders
path1 = "/data/data/com.termux/files/home/All-Tools/.logs/"
path2 = "/data/data/com.termux/files/home/All-Tools/.settings/"
path3 = "/data/data/com.termux/files/home/All-Tools/.temp/"
path4 = "/data/data/com.termux/files/home/All-Tools/.check/"

# No secret folders
path5 = "/data/data/com.termux/files/home/All-Tools/Files/"
path6 = "/data/data/com.termux/files/home/All-Tools/src/"
path7 = "/data/data/com.termux/files/home/All-Tools/Tool/"
path8 = "/data/data/com.termux/files/home/All-Tools/Themes/"
path9 = "/data/data/com.termux/files/home/All-Tools/Castom/"

# check folders
if os.path.exists(path1):
    if os.path.exists(path2):
        if os.path.exists(path3):
            if os.path.exists(path4):
                if os.path.exists(path5):
                    if os.path.exists(path6):
                        if os.path.exists(path7):
                            if os.path.exists(path8):
                                if os.path.exists(path9):
                                    os.system("cd && cd All-Tools && cd src && bash starterUp.sh")
                                else:
                                    print(R + '[-] ' + C + 'Error code: 106 DNS server refused to connect')
                                    print(R + '[-] ' + C + 'Error code: 404 Not Found! No system folder')
                                    print(R + '[-] ' + C + 'Error code: 500 Unable to process request due to folder not found!')
                                    print("")
                                    print(R + '[-] ' + C + 'Try reinstalling the system, or restoring from a backup!')
                                    print(R + '[-] ' + C + 'Unable to start the system! Maybe the system files were damaged!')
                                    exit(0)

                            else:
                                print(R + '[-] ' + C + 'Error code: 106 DNS server refused to connect')
                                print(R + '[-] ' + C + 'Error code: 404 Not Found! No system folder')
                                print(R + '[-] ' + C + 'Error code: 500 Unable to process request due to folder not found!')
                                print("")
                                print(R + '[-] ' + C + 'Try reinstalling the system, or restoring from a backup!')
                                print(R + '[-] ' + C + 'Unable to start the system! Maybe the system files were damaged!')
                                exit(0)
                        else:
                            print(R + '[-] ' + C + 'Error code: 106 DNS server refused to connect')
                            print(R + '[-] ' + C + 'Error code: 404 Not Found! No system folder')
                            print(R + '[-] ' + C + 'Error code: 500 Unable to process request due to folder not found!')
                            print("")
                            print(R + '[-] ' + C + 'Try reinstalling the system, or restoring from a backup!')
                            print(R + '[-] ' + C + 'Unable to start the system! Maybe the system files were damaged!')
                            exit(0)
                    else:
                        print(R + '[-] ' + C + 'Error code: 106 DNS server refused to connect')
                        print(R + '[-] ' + C + 'Error code: 404 Not Found! No system folder')
                        print(R + '[-] ' + C + 'Error code: 500 Unable to process request due to folder not found!')
                        print("")
                        print(R + '[-] ' + C + 'Try reinstalling the system, or restoring from a backup!')
                        print(R + '[-] ' + C + 'Unable to start the system! Maybe the system files were damaged!')
                        exit(0)
                else:
                    print(R + '[-] ' + C + 'Error code: 106 DNS server refused to connect')
                    print(R + '[-] ' + C + 'Error code: 404 Not Found! No system folder')
                    print(R + '[-] ' + C + 'Error code: 500 Unable to process request due to folder not found!')
                    print("")
                    print(R + '[-] ' + C + 'Try reinstalling the system, or restoring from a backup!')
                    print(R + '[-] ' + C + 'Unable to start the system! Maybe the system files were damaged!')
                    exit(0)
            else:
                print(R + '[-] ' + C + 'Error code: 106 DNS server refused to connect')
                print(R + '[-] ' + C + 'Error code: 404 Not Found! No system folder')
                print(R + '[-] ' + C + 'Error code: 500 Unable to process request due to folder not found!')
                print("")
                print(R + '[-] ' + C + 'Try reinstalling the system, or restoring from a backup!')
                print(R + '[-] ' + C + 'Unable to start the system! Maybe the system files were damaged!')
                exit(0)
        else:
            print(R + '[-] ' + C + 'Error code: 106 DNS server refused to connect')
            print(R + '[-] ' + C + 'Error code: 404 Not Found! No system folder')
            print(R + '[-] ' + C + 'Error code: 500 Unable to process request due to folder not found!')
            print("")
            print(R + '[-] ' + C + 'Try reinstalling the system, or restoring from a backup!')
            print(R + '[-] ' + C + 'Unable to start the system! Maybe the system files were damaged!')
            exit(0)

    else:
        print(R + '[-] ' + C + 'Error code: 106 DNS server refused to connect')
        print(R + '[-] ' + C + 'Error code: 404 Not Found! No system folder')
        print(R + '[-] ' + C + 'Error code: 500 Unable to process request due to folder not found!')
        print("")
        print(R + '[-] ' + C + 'Try reinstalling the system, or restoring from a backup!')
        print(R + '[-] ' + C + 'Unable to start the system! Maybe the system files were damaged!')
        exit(0)
else:
    print("Folder .logs doesn't exists!")
    print(R + '[-] ' + C + 'Error code: 106 DNS server refused to connect')
    print(R + '[-] ' + C + 'Error code: 404 Not Found! No system folder')
    print(R + '[-] ' + C + 'Error code: 500 Unable to process request due to folder not found!')
    print("")
    print(R + '[-] ' + C + 'Try reinstalling the system, or restoring from a backup!')
    print(R + '[-] ' + C + 'Unable to start the system! Maybe the system files were damaged!')
    exit(0)
