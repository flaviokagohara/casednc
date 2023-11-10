import requests
import json

# Essa variável vai ser utilizado como secret ou no airflow ou no rancher onde esse código irá rodar.
MAPS_API_KEY = 'MAPS_API_KEY'

#baseado no que foi colocado nas coordenadas do outro código
origem = ['Diadema', 'São José dos Campos']
destino = ['São José dos Campos', 'Diadema']
resultados = []
maps_api_url = 'https://maps.googleapis.com/maps/api/directions/json?'

def consultar_trajeto(origem, destino, response,maps_api_url, MAPS_API_KEY):
    i = 0 
    for i  in range(len(origem)):
        response = requests.get(maps_api_url+f'&origin={str(origem[i])}'+f'&destination={str(destino[i])}'+f'&key={MAPS_API_KEY}')
        result = json.loads(response.text)
        resultados.append(result)
    resultados

#aqui posteriormente na hora de escrever nos tópicos vamos ter que filtrar os campos e com isso, na minha concepção poderíamos fazer esse recorte:
#        result['routes'][0]['legs'][0]['duration']['text'] #tempo de viagem
#        result['routes'][0]['legs'][0]['distance']['text'] #distância
#        result['routes'][0]['legs'][0]['end_address'] #nome da cidade de partida
#        result['routes'][0]['legs'][0]['start_address'] #coordenadas da cidade de partida
#        result['routes'][0]['legs'][0]['end_location'] #nome da cidade de chegada
#        result['routes'][0]['legs'][0]['start_location'] #coordenadas da cidade de partida
