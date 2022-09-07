import requests

base_url ="https://rickandmortyapi.com/api/character"

lista_personajes = []

for i in range(1,10):
    c = f'https://rickandmortyapi.com/api/character/{i}'
    #print(f'{base_url}/{i}')
    r = requests.get(c)
    #print(r.text)
    ans = r.json()
    lista_personajes.append(ans["name"])

print(lista_personajes)

