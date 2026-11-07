import os
import requests

url = input("Enter the URL to download: ")
filename = input("Enter the output filename (e.g., image.png): ")

print("Downloading...")
try:
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Successfully downloaded and saved as {filename}!")
    else:
        print("Failed to download. Status code:", response.status_code)
except Exception as e:
    print("An error occurred:", e)
