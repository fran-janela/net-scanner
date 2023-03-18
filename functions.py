import requests
import socket
from scapy.all import ARP, Ether, srp
import nmap
import time
from prints import *

def get_network_scan(mac_finder, target_ip):
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    print("\nScanning network... (this may take a while)\n")

    start_time = time.time()
    result = srp(packet, timeout=3, verbose=0)[0]
    end_time = time.time()

    print("Done!")
    print_elapsed_time(end_time - start_time)

    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc, 'hostname': mac_finder.get_manuf(received.hwsrc)})

    return clients

def get_host_scan(port_scanner, target_ip, is_well_known_ports_scan, ports):
    if is_well_known_ports_scan:
        print("\nScanning Well Known Ports... (this may take a while)\n")

        start_time = time.time()
        WELL_KNOW_PORTS = "0,1,5,7,18,20,21,22,23,25,29,37,42,43,49,53,69,70,79,80,88,106,110,111,113,119,135,137,138,139,143,161,162,179,194,389,443,445,465,512,513,514,515,530,531,532,540,542,544,546,547,548,554,587,631,636,873,902,989,990,993,995,1025"
        result = port_scanner.scan(target_ip, arguments=f"-sV -p {WELL_KNOW_PORTS}")
        end_time = time.time()

        print("Done!")
        print_elapsed_time(end_time - start_time)
        return result
    
    print("\nScanning Ports... (this may take a while)\n")

    start_time = time.time()
    result = port_scanner.scan(target_ip, arguments=f"-sV -p {ports}")
    end_time = time.time()

    print("Done!")
    print_elapsed_time(end_time - start_time)
    return result