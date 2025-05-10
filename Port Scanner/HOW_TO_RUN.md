# How to Run the Port Scanner Project

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.6 or higher
- Required Python libraries:
  - `termcolor`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ethical-hacking-python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ethical-hacking-python/Port Scanner
   ```
3. Install the required dependencies:
   ```bash
   pip install termcolor
   ```

## How to Run
1. Open a terminal and navigate to the `Port Scanner` directory.
2. Run the script:
   ```bash
   python portscanner.py
   ```
3. Follow the prompts:
   - Enter the target IP addresses (comma-separated for multiple targets).
   - Enter the number of ports to scan.

## Example Inputs
### Single Target
- Input:
  ```
  [*] Enter Targets to Scan (split them by ,): 192.168.1.1
  [*] Enter how many ports you want to scan: 100
  ```
- Output:
  ```
  Starting Scan for ports in IP 192.168.1.1
  [+] Port Opened 22
  [+] Port Opened 80
  ```

### Multiple Targets
- Input:
  ```
  [*] Enter Targets to Scan (split them by ,): 192.168.1.1,192.168.1.2
  [*] Enter how many ports you want to scan: 50
  ```
- Output:
  ```
  [*] Scanning multiple targets
  Starting Scan for ports in IP 192.168.1.1
  [+] Port Opened 22
  Starting Scan for ports in IP 192.168.1.2
  [+] Port Opened 80
  ```

## Notes
- Ensure you have permission to scan the target systems.
- Use this tool responsibly and only in legal environments.
