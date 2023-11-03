import requests
import json

# Essa variável vai ser utilizado como secret ou no airflow ou no rancher onde esse código irá rodar.
MAPS_API_KEY = 'MAPS_API_KEY'

#baseado no que foi colocado nas coordenadas do outro código
origem = ['Diadema', 'São José dos Campos']
destino = ['São José dos Campos', 'Diadema']
resultados = []
maps_api_url = 'https://maps.googleapis.com/maps/api/directions/json?'

def consultar_temperatura(origem, destino, response):
    i = 0 
    for i  in range(len(origem)):
        response = requests.get(maps_api_url+f'&origin={str(origem[i])}'+f'&destination={str(destino[i])}'+f'&key={MAPS_API_KEY}')
        result = json.loads(response.text)
        resultados.append(result)
    resultados
