import requests
import json

# Essa variável vai ser utilizado como secret ou no airflow ou no rancher onde esse código irá rodar.
WHEATER_API_KEY = "WHEATER_API_KEY"

#aqui utilizei variáveis, mas vale a pena esses arrays serem preenchidos pelo maps depois com uma nova função que pode ser implementada depois
latitudes = [-23.1895062,-23.6824124] 
longitudes = [-45.8630127,-46.5952992]
resultados = []
weather_api_url = "https://api.openweathermap.org/data/2.5/weather?&lang=pt_br&units=metric"


def consultar_clima(latitudes, longitudes, resultados,weather_api_url, WHEATER_API_KEY):
    i = 0 
    for i  in range(len(latitudes)):
        response = requests.get(weather_api_url+f'&lat={str(latitudes[i])}'+f'&lon={str(longitudes[i])}'+f'&appid={WHEATER_API_KEY}')
        result = json.loads(response.text)
        resultados.append(result)
    resultados

#aqui posteriormente na hora de escrever nos tópicos vamos ter que filtrar os campos e com isso, na minha concepção poderíamos fazer esse recorte:
# description = result['weather'][0]['description'] # descrição do tempo/aparência
# temp = result['main']['temp'] #temperatura atual 
# temp_min = result['main']['temp_min'] #temperatura mínima
# temp_max =result['main']['temp_max'] #temperatura máxima
# name = result['name'] # cidade que estamos analisando
# coord= result['coord'] #coordenadas da cidade que estamos analisando