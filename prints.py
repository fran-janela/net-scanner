from time import sleep
import pyfiglet
from colorama import Fore, Style


def print_banner():
    print("\n" + Fore.LIGHTBLACK_EX + Style.BRIGHT + "_"*65 + Style.RESET_ALL + "\n")
    ascii_banner = pyfiglet.figlet_format("NET SCANNER")
    print(ascii_banner)

def print_disclaimer():
    print(Fore.RED + Style.BRIGHT + "DISCLAIMER: " + Style.RESET_ALL + Fore.RED + "Esta ferramenta é para estudo e não verifica se as" + "\n" + "conexões de rede estão bem feitas, nem questiona a escolha do" + "\n" + "usuário, portanto se atente ao modo de escrita e à configuração" + "\n" + "do seu ambiente, por favor." + Style.RESET_ALL)

def print_not_valid_option():
    print("\n" + Fore.RED + Style.BRIGHT + "Opção inválida!" + Style.RESET_ALL + "\n" + "Por favor, Tente novamente." + "\n")
    sleep(2)

def print_error(error_text):
    print("\n" + Fore.RED + Style.BRIGHT + "Erro!" + Style.RESET_ALL + "\n" + error_text + "\n" + "Por favor, Tente novamente." + "\n")
    sleep(2)

def print_good_bye():
    print("\n" + Fore.LIGHTBLACK_EX + Style.BRIGHT + "_"*65 + Style.RESET_ALL + "\n")
    print("Obrigado por usar o " + Fore.BLUE + Style.BRIGHT + "Net Scanner" + Style.RESET_ALL + "! Até à próxima.")
    print("\n" + Fore.LIGHTBLACK_EX + Style.BRIGHT + "_"*65 + Style.RESET_ALL + "\n")
    sleep(2)

def choose_scan_option():
    print("\n" + Fore.LIGHTBLACK_EX + Style.BRIGHT + "_"*65 + "\n" +"Escolha uma opção:" + Style.RESET_ALL + "\n")
    print(Fore.BLUE + Style.BRIGHT + "1 - " + Style.RESET_ALL + "Scan de rede")
    print(Fore.BLUE + Style.BRIGHT + "2 - " + Style.RESET_ALL + "Scan de host")
    print("Ou saia do programa com " + Fore.RED + Style.BRIGHT + "exit" + Style.RESET_ALL + ".")
    opcao = input("\n" + Fore.BLUE + Style.BRIGHT + ">>" + Style.RESET_ALL + " ")
    return opcao

def print_network_scan_intro():
    print("\n\n" + Fore.LIGHTBLACK_EX + Style.BRIGHT + "_"*65 + Style.RESET_ALL + "\n")
    print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "Escaneamento de Rede" + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "_"*65 + Style.RESET_ALL + "\n")

def input_target_ip_scan_network():
    print("Digite o IP da rede e a máscara que deseja escanear:")
    print(Style.BRIGHT + "Ex: " + Style.RESET_ALL + "192.168.50.0/16")
    target_ip = input("\n" + Fore.BLUE + Style.BRIGHT + ">>" + Style.RESET_ALL + " ")
    return target_ip

def print_elapsed_time(delta_time):
    print(Fore.GREEN + Style.BRIGHT + "Tempo: " + Style.RESET_ALL + str(round(delta_time, 2)) + " segundos" + "\n")

def print_network_scan_result(hosts):
    print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "_"*65 + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "Resultados do Scan" + Style.RESET_ALL + "\n")
    print("IP" + "\t\t\t" + "MAC" + "\t\t\t" + "Hostname")
    print("-"*65)
    for host in hosts:
        print(host['ip'] + "\t" + host['mac'] + "\t\t" + host['hostname'] if host['hostname'] != None else "Não encontrado")
    print("\n")

def wait_user_enter():
    input("\n" + Fore.BLUE + Style.BRIGHT + "Pressione ENTER para continuar..." + Style.RESET_ALL + "\n")

def print_host_scan_intro():
    print("\n\n" + Fore.LIGHTBLACK_EX + Style.BRIGHT + "_"*65 + Style.RESET_ALL + "\n")
    print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "Escaneamento de Host" + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "_"*65 + Style.RESET_ALL + "\n")

def input_target_ip_scan_host():
    print("Digite o IP do host que deseja escanear:")
    print(Style.BRIGHT + "Ex: " + Style.RESET_ALL + "192.168.50.78")
    target_ip = input("\n" + Fore.BLUE + Style.BRIGHT + ">>" + Style.RESET_ALL + " ")

    print("\nDeseja fazer o escaneamento das portas mais usadas (Well-Know Ports)? [S/N]")
    is_well_know_port_scan_answer = input("\n" + Fore.BLUE + Style.BRIGHT + ">>" + Style.RESET_ALL + " ")

    if is_well_know_port_scan_answer in ['S', 's', 'y', 'Y']:
        return target_ip, True, None
    
    print("\nInforme a porta específica que deseja escanear:")
    print(Style.BRIGHT + "Para um intervalo de portas:   " + Style.RESET_ALL + "1-1024")
    print(Style.BRIGHT + "Para uma porta em específico:  " + Style.RESET_ALL + "80")
    port = input("\n" + Fore.BLUE + Style.BRIGHT + ">>" + Style.RESET_ALL + " ")
    return target_ip, False, port

def print_host_scan_result(result, target_ip):
    WELL_KNOW_PORTS = {
        20: 'FTP (File Transfer Protocol)',
        21: 'FTP (File Transfer Protocol)',
        22: 'SSH (Secure Shell)',
        23: 'Telnet',
        25: 'SMTP (Simple Mail Transfer Protocol)',
        53: 'DNS (Domain Name System)',
        80: 'HTTP (Hypertext Transfer Protocol)',
        110: 'POP3 (Post Office Protocol version 3)',
        119: 'NNTP (Network News Transfer Protocol)',
        123: 'NTP (Network Time Protocol)',
        143: 'IMAP (Internet Message Access Protocol)',
        161: 'SNMP (Simple Network Management Protocol)',
        194: 'IRC (Internet Relay Chat)',
        443: 'HTTPS (HTTP Secure)',
        445: 'SMB (Server Message Block)',
        465: 'SMTPS (Simple Mail Transfer Protocol Secure)',
        514: 'Syslog',
        587: 'SMTP (Mail Submission)',
        631: 'IPP (Internet Printing Protocol)',
        873: 'rsync',
        993: 'IMAPS (Internet Message Access Protocol Secure)',
        995: 'POP3S (Post Office Protocol version 3 Secure)',
        1080: 'SOCKS (SOCKetS)',
        1194: 'OpenVPN',
        1433: 'Microsoft SQL Server',
        1434: 'Microsoft SQL Server',
        1521: 'Oracle',
        1723: 'PPTP (Point-to-Point Tunneling Protocol)',
        3306: 'MySQL',
        3389: 'RDP (Remote Desktop Protocol)',
        5432: 'PostgreSQL',
        5900: 'VNC (Virtual Network Computing)',
        5901: 'VNC (Virtual Network Computing)',
        5902: 'VNC (Virtual Network Computing)',
        5903: 'VNC (Virtual Network Computing)',
        6379: 'Redis',
        8080: 'HTTP Alternate (http_alt)',
        8443: 'HTTPS Alternate (https_alt)',
        9000: 'Jenkins',
        9090: 'HTTP Alternate (http_alt)',
        9091: 'HTTP Alternate (http_alt)'
    }
    for scaninfo in result["nmap"]["scaninfo"]:
        if scaninfo == "error":
            print_error("Nao foi possivel escanear a(s) porta(s) especificada(s)")
            return "error"
    print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "_"*65 + Style.RESET_ALL + "\n")
    print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "Resultados do Scan" + Style.RESET_ALL)
    for connection in result["scan"][target_ip]["tcp"]:
        print("\n" + "_"*65)
        print("Porta: "+ Fore.BLUE + Style.BRIGHT + str(connection) + Style.RESET_ALL)
        print(" - " + "Status: " + Style.BRIGHT + result["scan"][target_ip]["tcp"][connection]["state"] + Style.RESET_ALL)
        print(" - " + "Serviço: " + Style.BRIGHT + result["scan"][target_ip]["tcp"][connection]["name"] + Style.RESET_ALL)
        print(" - " + "Versão: " + Style.BRIGHT + result["scan"][target_ip]["tcp"][connection]["version"] + Style.RESET_ALL)
        print(" - " + "Produto: " + Style.BRIGHT + result["scan"][target_ip]["tcp"][connection]["product"] + Style.RESET_ALL)
        print(" - " + "CPE: " + Style.BRIGHT + result["scan"][target_ip]["tcp"][connection]["cpe"] + Style.RESET_ALL)
        print(" - " + "Extrainfo: " + Style.BRIGHT + result["scan"][target_ip]["tcp"][connection]["extrainfo"] + Style.RESET_ALL)
        print(" - " + "Confiança: " + Style.BRIGHT + str(result["scan"][target_ip]["tcp"][connection]["conf"]) + Style.RESET_ALL)
        if connection in WELL_KNOW_PORTS:
            print(" - " + "Well Known Port for: " + Style.BRIGHT + WELL_KNOW_PORTS[connection] + Style.RESET_ALL)
    return "success"
    



