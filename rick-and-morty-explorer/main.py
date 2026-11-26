import requests

url = "https://rickandmortyapi.com/api/character/1"
response = requests.get(url)

print(response.status_code)

character = response.json()

print("====FICHA DO PERSONAGEM====")

print(f"Nome: {character["name"]}")
print(f"Status: {character["status"]}")
print(f"Genero: {character["gender"]}")
print(f"Espécie: {character["species"]}")

