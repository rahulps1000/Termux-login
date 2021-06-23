#!/data/data/com.termux/files/usr/bin/env python

import getpass
import hashlib
import sys
import os

headtext = """
dP                          oo          
88                                      
88        .d8888b. .d8888b. dP 88d888b. 
88        88'  `88 88'  `88 88 88'  `88 
88        88.  .88 88.  .88 88 88    88 
88888888P `88888P' `8888P88 dP dP    dP 
                        .88             
                    d8888P              


"""

successtext = r"""
 __  _ _  __ __  ___  __  __ 
/ _|| | |/ _/ _|| __|/ _|/ _|
\_ \| U ( (( (_ | _| \_ \\_ \ 
|__/|___|\__\__||___||__/|__/

"""

failedtext = """
 ___  _   _  _    ___  __  
| __|/ \ | || |  | __||  \ 
| _|| o || || |_ | _| | o )
|_| |_n_||_||___||___||__/

"""

print(f"\u001b[34m{headtext}\u001b[0m")

password = getpass.getpass()

filepass = open("/data/data/com.termux/files/usr/share/login/.pass", "r")
filepass = filepass.read().split("\n")[0]

password = password.encode()
password = hashlib.sha1(password).hexdigest()

if password != filepass:
    print(f"\u001b[31m{failedtext}\u001b[0m")
    print("Invalid password")
    input()
    os.system("exit")
else:
    print(f"\u001b[32m{successtext}\u001b[0m")
    input()
    prefix = "/data/data/com.termux/files/usr"
    home = "/data/data/com.termux/files/home"
    motd = False
    hush = False

    os.system("clear")

    try:
        open(prefix + "/etc/motd")
        motd = True
    except:
        motd = False

    try:
        open(home + "/.hushlogin")
        hush = True
    except:
        hush = False

    if motd and not hush:
        print(open(prefix + "/etc/motd").read())
    
    os.system(sys.argv[1] + " " + sys.argv[2])
