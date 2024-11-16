import requests

x = requests.get(url="https://api.kanye.rest/")
x.raise_for_status()
data = x.json()
print(data["quote"])
