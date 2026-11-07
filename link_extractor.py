import requests
from bs4 import BeautifulSoup

url = input("Enter a website URL (e.g., https://example.com): ")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    
    count = 0
    with open("links.txt", "w") as file:
        for link in links:
            href = link.get('href')
            if href and href.startswith("http"):
                file.write(href + "\n")
                count += 1
                
    print(f"\nSuccessfully saved {count} absolute links to 'links.txt'!")
except Exception as e:
    print(f"Error: {e}")

