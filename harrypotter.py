import requests

url = "https://hp-api.herokuapp.com/api/characters"
response = requests.get(url)

potter = response.json()

print(potter[0]["name"])
print(potter[0]['image'])