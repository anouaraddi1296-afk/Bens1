import requests
import json

target = input("Enter IP address or domain (e.g., google.com): ")
url = f"http://ip-api.com/json/{target}"

try:
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'success':
        print(f"\n--- Info for {target} ---")
        print(f"IP: {data['query']}")
        print(f"Country: {data['country']}")
        print(f"City: {data['city']}")
        print(f"ISP: {data['isp']}")
        print("-------------------------")
    else:
        print("Error: Could not retrieve information.")
except Exception as e:
    print(f"Error: {e}")
