import socket

def port_scanner(host, start_port, end_port):
    """
    Scan a range of TCP ports on a given host.

    Allowed target:
        - scanme.nmap.org only
    """
    # Line below or Line11 Checks if the host is allowed; block anything except scanme.nmap.org
    if host != "scanme.nmap.org":
        raise ValueError("ERROR: This scanner is restricted to scanme.nmap.org only.")
    
    # Line below or Line15 will print the hostname being scanned
    print(f"Starting port range scan on: {host}")
    # Line below or Line17 will print the port range being scanned
    print(f"Port range: {start_port} to {end_port}\n")

    # Loop through each port from start_port to end_port
    for port in range(start_port, end_port + 1):
        scan_single_port(host, port)

    print("\nScan complete.") #This will print when the scan is complete

    #Code below is for single port scan
def scan_single_port(host, port):
    """
    Scan a *single* TCP port on scanme.nmap.org only.
    """

    if host != "scanme.nmap.org":
        raise ValueError("ERROR: This scanner is restricted to scanme.nmap.org only.")
    # Create a TCP (SOCK_STREAM) IPv4 (AF_INET) socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        result = sock.connect_ex((host, port))

        if result == 0:
            print(f"[OPEN]   Port {port}")
        else:
            print(f"[CLOSED] Port {port}")
    # This error occurs when the hostname cannot be resolved (DNS failure)
    except socket.gaierror:
        print(f"[ERROR] Hostname could not be resolved: {host}")
    # General socket errors (network issues, refused connections, etc.)
    except socket.error as e:
        print(f"[ERROR] Could not scan port {port}: {e}")
    #Closing socket
    finally:
        sock.close()


if __name__ == "__main__":
    # Line below or Line54 can port ranges
    port_scanner("scanme.nmap.org", 1, 2)

    # Line below or line57 can scan a single port of your choice
    scan_single_port("scanme.nmap.org", 80) 

    # Script below is trying to scan other website, server or system beside the allowed target
    try:
        scan_single_port("google.com", 80)
    except ValueError as e:
        print(e)
