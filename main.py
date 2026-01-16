import requests

def track_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        print("\n📍 IP Location Details:\n")
        print(f"IP Address : {data['query']}")
        print(f"Country    : {data['country']}")
        print(f"Region     : {data['regionName']}")
        print(f"City       : {data['city']}")
        print(f"ZIP        : {data['zip']}")
        print(f"ISP        : {data['isp']}")
        print(f"Latitude   : {data['lat']}")
        print(f"Longitude  : {data['lon']}")
    else:
        print("❌ Invalid IP Address")

if __name__ == "__main__":
    ip = input("Enter IP address to track: ")
    track_ip(ip)
