class initing ():
    import os as os
    import sys as sys
    import time as time
    
    sys_corect = "sys-start = yes"
    sys_not_correct = "sys-start = no"

    keys = "C:\\Users\\dedaf\\Desktop\\Wszystko\\App\\App"
    os.chdir(keys)
    key = open('key-ss.par')
    sys1 = key.read()

    if sys_corect == sys1:
        print("HEllO cmd")
        print("Do you want to run Terminal (Yes / No)")
        T_n = input("Do you want to run Terminal (Yes / No):")    
        if T_n == "Yes":
            terminal = "cmd.py"
            keys = "C:\\Users\\dedaf\\Desktop\\Wszystko\\App\\App"
            os.chdir(keys)
            os.startfile(terminal)    
        if T_n == "No":
            print("Ok I don't start Terminal")
            time.sleep(2.5)
            sys.exit()
    if sys_not_correct == sys1:
        print("Sorry i can't start the system because the file is not compatible!")
        time.sleep(2.5)
        sys.exit()
initing()