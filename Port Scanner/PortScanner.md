# What is a Port Scanner?

A port scanner is a tool used to identify open ports and services available on a networked device. It is commonly used in cybersecurity to assess the security of a system by identifying potential vulnerabilities.

## How Does a Port Scanner Work?
Port scanners send packets to specific ports on a target system and analyze the responses to determine the status of the ports. Ports can be categorized as:
- **Open:** The port is actively accepting connections.
- **Closed:** The port is not accepting connections.
- **Filtered:** The port is protected by a firewall or other security mechanism.

## How This Python Program Works
This Python-based port scanner works as follows:
1. **Input:** The user provides the target IP address(es) and the range of ports to scan.
2. **Scanning:** The program iterates through the specified ports and attempts to establish a connection to each one.
3. **Output:** For each open port, the program prints a message indicating that the port is open.

### Key Features
- **Multiple Targets:** The program can scan multiple IP addresses in a single run.
- **Customizable Port Range:** Users can specify how many ports to scan.
- **Simple and Lightweight:** The program is easy to use and requires minimal setup.

### Real-World Applications
- **Vulnerability Assessment:** Identify open ports that could be exploited by attackers.
- **Network Troubleshooting:** Verify that specific services are running and accessible.
- **Learning Tool:** Understand the basics of network security and port scanning.

### Ethical Considerations
This tool is intended for educational purposes only. Always obtain proper authorization before scanning any network or system. Unauthorized scanning is illegal and unethical.
