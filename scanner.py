import socket
import requests
from socket import getservbyport, error
from concurrent.futures import ThreadPoolExecutor

# Predefined major ports (common well-known ports)
MAJOR_PORTS = [22, 23, 25, 53, 80, 443, 110, 143, 3306, 3389, 8080]


# Geolocation lookup function
def geolocation_lookup(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching geolocation for IP: {ip}")
            return None
    except requests.RequestException as e:
        print(f"Error during geolocation lookup: {e}")
        return None


# Mock function to check for CVEs (for demonstration purposes)
def check_cve(service_name, version):
    cve_url = f"https://cve.circl.lu/api/cve/search/{service_name}/{version}"
    try:
        response = requests.get(cve_url)
        if response.status_code == 200:
            return response.json()
        else:
            return []
    except requests.RequestException as e:
        print(f"Error fetching CVE data: {e}")
        return []


def get_service_name(port):
    try:
        service_name = getservbyport(port)
    except error:
        service_name = f"Port {port}"
    return service_name


# Version detection (simplified for demo)
def detect_service_version(target_ip, port):
    try:
        if port == 80 or port == 443:  # HTTP/HTTPS
            response = requests.get(f"http://{target_ip}:{port}")
            version = response.headers.get('Server', 'Unknown')
            return version
        elif port == 22:  # SSH
            return 'OpenSSH 8.4'  # Placeholder version
        else:
            return 'Unknown Version'
    except requests.RequestException:
        return 'Unable to detect version'


# Function to scan individual ports (TCP/UDP)
def scan_port(target_ip, port, udp):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Reduced timeout for faster scanning
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            sock.close()
            return port
        sock.close()
    except socket.error:
        pass
    return None


# Function to scan for open ports (with version and CVE detection)
def scan_ports(target_ip, start_port, end_port, udp, verbose, scan_all_ports):
    open_ports = []

    # Create a ThreadPoolExecutor to parallelize port scanning
    with ThreadPoolExecutor(max_workers=20) as executor:  # Use 20 threads for example
        futures = []

        if scan_all_ports:
            ports_to_scan = range(start_port, end_port + 1)
        else:
            # Scan major ports by default
            ports_to_scan = MAJOR_PORTS

        for port in ports_to_scan:
            futures.append(executor.submit(scan_port, target_ip, port, udp))

        for future in futures:
            port = future.result()
            if port:
                service_name = get_service_name(port)
                version = detect_service_version(target_ip, port)
                cve_info = check_cve(service_name, version)  # Get CVEs for the detected version

                open_ports.append((port, service_name, version, cve_info))

                if verbose:
                    print(f"Port {port} ({service_name}) open on {target_ip} with version {version}")
                    if cve_info:
                        print(f"  CVEs found: {cve_info}")

    return open_ports
