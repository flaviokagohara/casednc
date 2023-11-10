WEATHER_TOPIC_NAME = 'weather_api.distances'
MAPS_TOPIC_NAME = 'maps_api.temperatures'

from apis import weather, maps
from kafka import escrever_topico
from datetime import datetime

if __name__ == '__main__':
    created_at = datetime.now()
    updated_at = datetime.now()
    escrever_topico(MAPS_TOPIC_NAME,created_at,maps.consultar_trajeto(),updated_at)
    escrever_topico(WEATHER_TOPIC_NAME,created_at,weather.consultarclima(),updated_at)