# C:\Users\etien\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe
from scapy.all import ICMP, sr, IP, srloop, send, arping


def pingpong(theip):
    arping(theip)
    return

print("Entrez le réseau que vous voulez scannez sous la forme 00.00.00.00/00")
reseauscan = input()


print("\n L'ip que vous avez entrez est bien : ", reseauscan, " Y/N")
rep = input()

if (rep == "Y" or rep == "y"):
    if (rep.__contains__("/")):
        tabtestip = rep.split(".")
        if (tabtestip.len == 4):
            pingpong(reseauscan)
        else:
            "Votre Ip ne contient pas le bon format"
    else:
        "Votre Ip ne contient pas le bon format"

while (rep != "y" and rep.__contains__("/") == False and tabtestip.len != 4):
    print("Entrez le réseau que vous voulez scannez sous la forme 00.00.00.00/00")
    reseauscan = input()
    print("\n L'ip que vous avez entrez est bien : ", reseauscan, " Y/N")
    rep = input()
    if (rep == "Y" or rep == "y"):
        if (rep.__contains__("/")):
            tabtestip = rep.split(".")
            if (tabtestip.len == 4):
                pingpong(reseauscan)
            else:
                "Votre Ip ne contient pas le bon format"
        else:
            "Votre Ip ne contient pas le bon format"


