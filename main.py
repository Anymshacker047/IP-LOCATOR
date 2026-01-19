import os
import sys

# Define Colors for the terminal
GREEN = '\033[92m'
RED = '\033[91m'
ORANGE = '\033[38;5;208m'
WHITE = '\033[97m'
BOLD = '\033[1m'
ENDC = '\033[0m'

def show_splash():
    # Clear the terminal screen
    os.system('clear')

    # Simulate the prompt
    print(f"{GREEN}     TEAM ANYMSHACKER047:=#{ENDC}")
    print(f"{GREEN}     Github.com/Anymshacker047{ENDC}\n")

    # The Main Header
    print(f"{RED}{BOLD}           *LORDS* {ENDC}")
    print(f"{RED}{BOLD}         UNIVERSITY      {ENDC}")
    print(f"{ORANGE}     IP LOCATOR IN CYBER SECURITY{ENDC}\n")

    # The Information Box
    print(f"  ┌─────────────────────────────────────────┐")
    print(f"  │     {GREEN}Github.com/Anymshacker047           │")
    print(f"  │                                         │")
    print(f"  │       {BOLD}SUBMITTED BY :-                   │")
    print(f"  │        MANAS DHINGRA                    │")
    print(f"  │       SANJAY SANWARIYA                  │")
    print(f"  │         HANIPH SHAH                     │")
    print(f"  └─────────────────────────────────────────┘\n")
    
if __name__ == "__main__":
    show_splash()
import requests
import socket
from urllib.parse import urlparse

def get_location_data(ip):
    """Fetches geolocation data for a given IP."""
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return {"status": "fail", "message": str(e)}

def print_details(data):
    """Formats and prints the IP metadata."""
    if data.get("status") == "success":
        print("\n📍 IP/Host Location Details:")
        print(f"IP Address : {data['query']}")
        print(f"Country    : {data['country']}")
        print(f"Region     : {data['regionName']}")
        print(f"City       : {data['city']}")
        print(f"ISP        : {data['isp']}")
        print(f"Lat/Lon    : {data['lat']}, {data['lon']}")
    else:
        print(f"❌ Error: {data.get('message', 'Invalid IP or Host')}")
        
def track_link_and_redirect():
    """Simulates 'Grabify' logic: Get IP from a domain and verify the end link."""
    link = input("\nEnter the URL to track (e.g., github.com/user/repo): ").strip()
    
    # Clean the URL to extract the hostname
    if not link.startswith(('http://', 'https://')):
        link = 'https://' + link
    
    try:
        hostname = urlparse(link).hostname
        print(f"🔍 Analyzing host: {hostname}")

        # 1. Get the IP address of the domain (DNS Lookup)
        ip_address = socket.gethostbyname(hostname)

        # 2. Get Geolocation of that IP
        data = get_location_data(ip_address)
        print_details(data)

        # 3. Reachable Check (Simulating the 'redirect' to the end link)
        print(f"\n🔗 Attempting to reach final destination: {link}")
        response = requests.get(link, timeout=10)

        if response.status_code == 200:
            print(f"✅ Success! Destination is reachable (Status: {response.status_code})")
        else:
            print(f"⚠️ Warning: Destination returned status code {response.status_code}")

    except socket.gaierror:
        print("❌ Error: Could not resolve hostname. Check the link.")
    except Exception as e:
        print(f"❌ Connection error: {e}")

if __name__ == "__main__":
    while True:
        print("\n--- IP Tracker ---")
        print("1. Track a specific IP address")
        print("2. Track IP from a Link ")
        print("3. Exit")

        choice = input("\nSelect an option: ")

        if choice == '1':
            ip = input("Enter IP address to track: ")
            data = get_location_data(ip)
            print_details(data)
        elif choice == '2':
            track_link_and_redirect()
        elif choice == '3':
            break
        else:
            print("Invalid selection.")
