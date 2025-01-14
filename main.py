import sys
import socket
import argparse
from scanner import scan_ports, geolocation_lookup

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Scan ports on a target IP address or hostname.")
    parser.add_argument("target", help="Target IP address or hostname to scan.")
    parser.add_argument("-u", "--udp", action="store_true", help="Use UDP for scanning.")
    parser.add_argument("-s", "--summary", action="store_true", help="Print a summary of open ports.")
    parser.add_argument("--start-port", type=int, default=1, help="Starting port for scan (default: 1).")
    parser.add_argument("--end-port", type=int, default=65535, help="Ending port for scan (default: 65535).")
    parser.add_argument("--scan-all-ports", action="store_true", help="Scan all ports (default: scan major ports only).")
    args = parser.parse_args()

    target = args.target
    start_port = args.start_port
    end_port = args.end_port
    udp = args.udp
    verbose = args.summary
    scan_all_ports = args.scan_all_ports

    # Try resolving the target to an IP address if it's a hostname
    try:
        target_ip = socket.gethostbyname(target)
        print(f"Resolving {target} as hostname...")
    except socket.gaierror:
        print(f"Invalid IP address. Resolving {target} as hostname...")
        target_ip = target

    print(f"Scanning target: {target_ip}")

    # Perform geolocation lookup (optional, can be customized)
    geolocation_lookup(target_ip)

    # Scan the ports
    open_ports = scan_ports(target_ip, start_port, end_port, udp, verbose, scan_all_ports)

    # Print the summary of open ports
    if verbose:
        if open_ports:
            print(f"\nOpen ports found on {target_ip}:")
            for port in open_ports:
                print(f"Port {port}")
        else:
            print("No open ports found.")

if __name__ == "__main__":
    main()
