import socket
import termcolor

# Function to scan a single port on a given IP address
def scan_port(ip_address, port):
    try:
        # Create a socket object
        sock = socket.socket()
        # Attempt to connect to the target IP and port
        sock.connect((ip_address, port))
        # If successful, print that the port is open
        print("[+] Port Opened " + str(port))
        # Close the socket
        sock.close()
    except:
        # Ignore any exceptions (e.g., if the port is closed)
        pass

# Function to scan a range of ports on a given IP address
def scan(ip_addr, ports):
    print("\nStarting Scan for ports on IP " + str(ip_addr))
    # Loop through the range of ports and scan each one
    for port in range(1, ports):
        scan_port(ip_addr, port)

# Get user input for target IPs and the number of ports to scan
targets = input("[*] Enter Targets to Scan (split them by ,): ")
ports = int(input("[*] Enter how many ports you want to scan: "))

# Check if multiple targets are provided
if ',' in targets:
    print(termcolor.colored("[*] Scanning multiple targets", "green"))
    # Split the targets by comma and scan each one
    for ip_addr in targets.split(","):
        scan(ip_addr.strip(), ports)
else:
    # Scan a single target
    scan(targets, ports)