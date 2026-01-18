import urllib.request

url = "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png"

response = urllib.request.urlopen(url)
data = response.read()

with open("PNG_transparency_demonstration_1.png", "wb") as f:
    f.write(data)