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

    print("\nEscaneando Rede... (isto pode demorar)\n")

    start_time = time.time()
    result = srp(packet, timeout=3, verbose=0)[0]
    end_time = time.time()

    print("Feito!")
    print_elapsed_time(end_time - start_time)

    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc, 'hostname': mac_finder.get_manuf(received.hwsrc)})

    return clients

def get_host_scan(port_scanner, target_ip, is_well_known_ports_scan, ports):
    if is_well_known_ports_scan:
        print("\nEscaneando Well Known Ports... (isto pode demorar)\n")

        start_time = time.time()

        WELL_KNOWN_PORTS_IDS = "20,21,22,23,25,53,80,110,119,123,143,161,194,443,445,465,514,587,631,873,993,995,1080,1194,1433,1434,1521,1723,3306,3389,5432,5900,5901,5902,5903,6379,8080,8443,9000,9090,9091"

        result = port_scanner.scan(target_ip, arguments=f"-sV -p {WELL_KNOWN_PORTS_IDS}")
        end_time = time.time()

        print("Feito!")
        print_elapsed_time(end_time - start_time)
        return result
    
    print("\nEscaneando Portas... (isto pode demorar)\n")

    # make a try catch for the port_scanner
    try:
        start_time = time.time()
        result = port_scanner.scan(target_ip, arguments=f"-sV -p {ports}")
        end_time = time.time()

        print("Feito!")
        print_elapsed_time(end_time - start_time)
    except Exception:
        return None

    return result