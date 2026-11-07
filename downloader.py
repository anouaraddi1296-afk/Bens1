import requests

url = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png"
print("Downloading image...")

response = requests.get(url)
if response.status_code == 200:
    with open("google_logo.png", "wb") as f:
        f.write(response.content)
    print("Image downloaded and saved successfully as google_logo.png!")
else:
    print("Download failed, status code:", response.status_code)

