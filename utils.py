import socket
import requests
from geopy.geocoders import Nominatim

def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def resolve_hostname_to_ip(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.error:
        return None

def get_geolocation(ip):
    geolocator = Nominatim(user_agent="GeoScanner")
    try:
        location = geolocator.geocode(ip)
        if location:
            return {'city': location.address.split(',')[0], 'country': location.address.split(',')[-1], 
                    'latitude': location.latitude, 'longitude': location.longitude}
        return {'error': 'Geolocation not found'}
    except Exception as e:
        return {'error': str(e)}

def print_scan_results(results):
    print("Open Ports: ", results)
