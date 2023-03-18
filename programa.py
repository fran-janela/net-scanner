import nmap
import manuf

from prints import *
from functions import *


scanner = nmap.PortScanner()

# =================================================================================
#  MAIN
# =================================================================================
def main():
    mac_finder = manuf.MacParser()
    port_scanner = nmap.PortScanner()

    running = True
    print_banner()
    print_disclaimer()
    while running:
        opcao = choose_scan_option()

        # -------------------------- SCAN DE REDE --------------------------
        if opcao == "1":
            print_network_scan_intro()
            target_ip = input_target_ip_scan_network()
            hosts = get_network_scan(mac_finder, target_ip)
            print_network_scan_result(hosts)
            wait_user_enter()
        
        # -------------------------- SCAN DE HOST --------------------------
        elif opcao == "2":
            print_host_scan_intro()
            target_ip, is_well_known_ports_scan, ports = input_target_ip_scan_host()
            result = get_host_scan(port_scanner, target_ip, is_well_known_ports_scan, ports)
            if result is None:
                print_error("Nao foi possivel escanear a(s) porta(s) especificada(s)")
                continue
            print_host_scan_result(result, target_ip)
            wait_user_enter()

        # ------------------------ SAIR DO PROGRAMA ------------------------
        elif opcao == "exit":
            running = False
            print_good_bye()
        else:
            print_not_valid_option()


if __name__ == "__main__":
    main()