import socket
import termcolor



def scan_port(ip_address,port):
    try:
        sock = socket.socket()
        sock.connect((ip_address, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        pass


def scan(ip_addr,ports):
    print("\n Starting Scan for ports in IP "+str(ip_addr))
    for port in range(1,ports):
        scan_port(ip_addr,port)


targets = input("[*] Enter Targets to Scan (split them by ,): ")
ports = int(input("[*] Enter how many ports you wan tot scan : "))
if ',' in targets:
    print(termcolor.colored(("[*] Scanning multiple targets"),"green"))
    for ip_addr in targets.split(","):
        scan(ip_addr.strip(" "),ports)
else:
    scan(targets,ports)