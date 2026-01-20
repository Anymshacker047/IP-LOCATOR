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
    print(f"  │    {BOLD} IP-LOCATOR                    │")
    print(f"  │       {BOLD}SUBMITTED BY :-                   │")
    print(f"  │        MANAS DHINGRA                    │")
    print(f"  │       SANJAY SANWARIYA                  │")
    print(f"  │         HANIPH SHAH                     │")
    print(f"  └─────────────────────────────────────────┘\n")
    
if __name__ == "__main__":
    show_splash()
import requests
import socket
import datetime
from urllib.parse import urlparse
from flask import Flask, request, redirect

# --- HELPER FUNCTIONS ---

def get_location_data(ip):
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return {"status": "fail", "message": str(e)}

def print_details(data):
    if data.get("status") == "success":
        print("\n IP Location Details:")
        print(f"IP Address : {data['query']}")
        print(f"Country    : {data['country']}")
        print(f"Region     : {data['regionName']}")
        print(f"City       : {data['city']}")
        print(f"ISP        : {data['isp']}")
        print(f"Lat/Lon    : {data['lat']}, {data['lon']}")
    else:
        print(f"❌ Error: {data.get('message', 'You Entered a Wrong IP Brother')}")

# --- OPTION 2: TRACK EXISTING LINK ---

def track_link_and_redirect():
    link = input("\nEnter the URL to analyze (e.g., google.com): ").strip()
    if not link.startswith(('http://', 'https://')):
        link = 'https://' + link
    try:
        hostname = urlparse(link).hostname
        print(f"🔍 Resolving Host: {hostname}")
        ip_address = socket.gethostbyname(hostname)
        data = get_location_data(ip_address)
        print_details(data)
    except Exception as e:
        print(f"❌ Error: {e}")

# --- OPTION 3: GENERATE GRABBER LINK (FLASK) ---

app = Flask(__name__)
TARGET_GITHUB = "" # Will be set by user input

@app.route('/')
def grab_ip():
    # Capture visitor's IP
    visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Save to log file
    with open("log.txt", "a") as f:
        f.write(f"[{timestamp}] IP: {visitor_ip}\n")
    
    print(f"🚩 Captured IP: {visitor_ip} at {timestamp}")
    return redirect(TARGET_GITHUB)

def start_grabber_server():
    global TARGET_GITHUB
    TARGET_GITHUB = input("Enter the destination link (e.g. instagram.com ): ")
    if not TARGET_GITHUB.startswith('http'):
        TARGET_GITHUB = 'https://' + TARGET_GITHUB
    
    print("\n🚀 IP Grabber is starting...")
    print("⚠️  To make this a public link contact developer.")
    print("❌ Press CTRL+C to stop the server and return to menu.\n")
    
    # Run the Flask server
    app.run(host='127.0.0.1', port=7737)

# --- MAIN MENU ---

if __name__ == "__main__":
    while True:
        print("\n" + "="*30)
        print("  IP LOCATOR ")
        print("="*30)
        print("1. Track a specific IP address")
        print("2. Track IP of an existing Website")
        print("3. Create a Link")
        print("4. Exit")
        
        choice = input("\nSelect an option: ")
        
        if choice == '1':
            ip = input("Enter IP to track: ")
            print_details(get_location_data(ip))
        elif choice == '2':
            track_link_and_redirect()
        elif choice == '3':
            try:
                start_grabber_server()
            except KeyboardInterrupt:
                print("\nServer stopped. Returning to menu...")
        elif choice == '4':
            print("See You Soon Brother!")
            break
        else:
            print("Invalid selection.")
