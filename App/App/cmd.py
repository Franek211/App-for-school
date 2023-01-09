import time
import math
import os
import sys

key = "C:\\Users\\dedaf\\Desktop\\Wszystko\\App\\App"
os.chdir(key)
keys = open("KEY.key")
key_key_sys = keys.read()
boot_code = "JARVIS-Start-system = yes"
boot_code_no = "JARVIS-Start-system = no"
status = "?"
Algorytm = status


if key_key_sys == boot_code_no:
    print("Sorry I can't start system. File is not compatibile!!!")
    
if key_key_sys == boot_code:
    status = "Ok"
    Algorytm = status
    while status == Algorytm:
        command = input("New cmd command: ")

        if command == "echo Hello":
            print("Hello World I like English and I like coding in Python !!!")
            
        if command == "neofetch":
            os.chdir(key)
            os.startfile("neo.png")
        if command == "info":
            print("Version = 1, System = MS-BIOS, Author = Franek Deda, CMD-Version = 1")
        if command == "exit":
            sys.exit()
        if command == "start app visual studio code":
            os.chdir("C:\\Users\\dedaf\\Desktop\\Wszystko\\App\\Protocol\\Start-App")
            os.startfile("Visual-Code.py")
        if command == "start app putty":
            os.chdir("C:\\Users\\dedaf\\Desktop\\Wszystko\\App\\Protocol\\Start-App")
            os.startfile("PuTTy.py")
        if command == "security":
            if key_key_sys == boot_code:
                print("Ok all is correct")
            if key_key_sys == boot_code_no:
                    print("Oh on boot code is not correct")
                    sys.exit()
        if command == "start app sweet":
            os.chdir("C:\\Users\\dedaf\\Desktop\\Wszystko\\App\\Protocol\\Start-App")
            os.startfile("Sweet_Home_3D.py")
        