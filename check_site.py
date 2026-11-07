import requests

url = "https://www.google.com"
try:
    response = requests.get(url)
    if response.status_code == 200:
        print("Success! Status Code: 200")
    else:
        print(f"Status Code: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
