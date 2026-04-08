from utils import scan_port, banner_grabbing, services

def scan_single_host(host):
    resultados = []
    
    print(f"\nEscaneando {host}...\n")
    
    for port in range(1, 1025):
        if scan_port(host, port):
            service = services.get(port, "Desconhecido")
            
            resultado = f"[+] Porta {port} aberta ({service})"
            print(resultado)
            resultados.append(resultado)
            
            banner = banner_grabbing(host, port)
            if banner:
                banner_msg = f"    Banner: {banner}"
                print(banner_msg)
                resultados.append(banner_msg)
                
    salvar = input("\nDeseja salvar os resultados? (s/n): ")
    if salvar.lower() == "s":
        with open("resultado.txt", "w") as file:
            for linha in resultados:
                file.write(linha + "\n")
        print("Resultados salvos em resultado.txt")
        
def scan_network(base_ip):
    print("\nEscaneando rede...\n")
    
    for i in range(1, 5): #pode aumentar depois
        host = base_ip + str(i)
        scan_single_host(host)
        

def menu():
    print("=== PORT SCANNER ===")
    print("1 - Scan de um host")
    print("2 - Scan de rede")
    
    opcao = input("Escolha: ")
    
    if opcao == "1":
        host = input("Digite o host (ex: scanme.nmap.org): ")
        scan_single_host(host)
    
    elif opcao == "2":
        host = input("Digite a base do IP (ex: 192.168.0.): ")
        scan_network(base_ip)
        
    else:
        print("Opção Inválida")
        
if __name__ == "__main__":
    menu()