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
    print(Fore.GREEN + Style.BRIGHT + "Ellapsed: " + Style.RESET_ALL + str(round(delta_time, 2)) + " segundos" + "\n")

def print_network_scan_result(hosts):
    print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "_"*65 + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "Resultados do Scan" + Style.RESET_AL + "\n")
    print("IP" + "\t\t\t" + "MAC" + "\t\t\t" + "Hostname")
    print("-"*65)
    for host in hosts:
        print(host['ip'] + "\t" + host['mac'] + "\t\t" + host['hostname'])
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

def print_host_scan_result(result):
    print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "_"*65 + Style.RESET_ALL + "\n")
    print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "Resultados do Scan" + Style.RESET_ALL)
    ## print dos dados das portas:
    



