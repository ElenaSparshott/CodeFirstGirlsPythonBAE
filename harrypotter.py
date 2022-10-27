import requests

url = "https://hp-api.herokuapp.com/api/characters"
response = requests.get(url)

potter = response.json()

print(potter[1]["name"])
print(potter[1]['image'])