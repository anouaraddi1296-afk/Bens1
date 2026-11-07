import requests

print("--- Checking links from links.txt ---")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    with open("links.txt", "r") as file:
        links = file.readlines()

    for link in links[:5]:
        link = link.strip() 
        try:
            response = requests.get(link, headers=headers, timeout=5)
            print(f"[{response.status_code}] - {link}")
        except Exception as e:
            print(f"[ERROR] - {link}")

except FileNotFoundError:
    print("Error: links.txt not found. Please run link_extractor.py first.")
