import requests
import json

# Essa variável vai ser utilizado como secret ou no airflow ou no rancher onde esse código irá rodar.
WHEATER_API_KEY = "WHEATER_API_KEY"
weather_api_url = "https://api.openweathermap.org/data/2.5/weather?&lang=pt_br&units=metric"

#aqui utilizei variáveis, mas vale a pena esses arrays serem preenchidos pelo maps depois com uma nova função que pode ser implementada depois
latitudes = [-23.1895062,-23.6824124] 
longitudes = [-45.8630127,-46.5952992]
resultados = []

def consultar_clima(latitudes, longitudes, responses):
    i = 0 
    for i  in range(len(latitudes)):
        response = requests.get(weather_api_url+f'&lat={str(latitudes[i])}'+f'&lon={str(longitudes[i])}'+f'&appid={WHEATER_API_KEY}')
        result = json.loads(response.text)
        resultados.append(result)
    resultados
