# TP5 Scaner Résaux

Notre outil est un sacn réseau qui prend en paramètre une commande, permettant de réaliser un scan réseau ou sacan d'une IP présice.


Pré-requis:

Un os Linux,
Python3
Pip
Netiface
Scapy

Lancement du programe:
```
sudo python scan.py
```

Contenu du -help:
```
This program is a network scanner
You have to run this program as root
Programm command list:
 -h  --help        Gives access to the list of commands and their uses.
 -a  --arp         Make a ARP ping request on all the whole network and write result in file. You can specify the interface you want to scan in argument.
 -t  --tcp         Gives from a list of ports the services that listen behind. You can specify the Ip you want to scan in argument.
 -os               Make a request to a specific Ip and return the os. You can specify the Ip you want to scan in argument.
 -p  --print       Print Save of specific interfaces. You can specify the interface you want to scan in argument.
```
