import requests

url = "https://rickandmortyapi.com/api/character/1"
response = requests.get(url)

print(response.status_code)

character = response.json()

print(character["name"])
print(character["gender"])
print(character["species"])
