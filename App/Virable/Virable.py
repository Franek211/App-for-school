import os as os

vir = "C://App//Virable"
boot_accept = "Start-Accept = Yes"

os.chdir(vir)
Viral = open(vir)
Virable = Viral.read()

if boot_accept == Virable:
    print("OK!")
    print("Ok I can start system.")
    os.chdir("C://App//App")

    os.startfile("class.py")
