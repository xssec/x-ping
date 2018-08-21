#!/usr/bin/python
#Bulk Ping Script

import sys
import os
import platform
import subprocess
import threading
import argparse

__author__ = 'xs|sec'

parser = argparse.ArgumentParser(description='This is a bulk ping script by xssec.')
parser.add_argument('-f','--file', help='Input file name',required=True)
args = parser.parse_args()



def banner():
        print("\t\t\033[93m                 __                 \033[1;m")
        print("\t\t\033[97m   _  _______\033[1;m   \033[93m/ /\033[1;m  \033[97m________  _____\033[1;m")
        print("\t\t\033[97m  | |/_/ ___/\033[1;m  \033[93m/ /\033[1;m  \033[97m/ ___/ _ \/ ___/\033[1;m")
        print("\t\t\033[97m _>  <(__  )\033[1;m  \033[93m/ /\033[1;m  \033[97m(__  )  __/ /__  \033[1;m")
        print("\t\t\033[97m/_/|_/____/\033[1;m  \033[93m/ /\033[1;m  \033[97m/____/\___/\___/\033[1;m")
        print("\t\t\033[93m            /_/\033[1;m")
        print("\n\t\t\033[97m       D.H.L \033[1;m\033[1;31m|\033[1;31m\033[97m xssec.id\033[1;m")

banner()

print "\n"

plat = platform.system()
hostsFile = open(args.file, "r")
lines = hostsFile.readlines()

def ping(ip):
    if plat == "Windows":
        ping = subprocess.Popen(
            ["ping", "-n", "1", "-l", "1", "-w", "100", ip],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )

    if plat == "Linux":
        ping = subprocess.Popen(
            ["ping", "-c", "1", "-l", "1", "-s", "1", "-W", "1", ip],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )

    out, error = ping.communicate()

    hosts = ping.returncode
    if hosts == 0:
        print '\033[92mUp\033[0m    | Host %s' %ip
    else:
        print '\033[91mDown\033[0m  | Host %s' %ip

#    print out # uncomment this for details result
#    print error

for ip in lines:
    threading.Thread(target=ping, args=(ip,)).run()
