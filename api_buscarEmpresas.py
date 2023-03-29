import requests
import json
from geopy.geocoders import Nominatim

# Insira sua chave de API do Google Maps aqui
google_maps_key ="t"

# Insira sua chave de API do Google Places aqui
google_places_key = "t"

# Endereço que você deseja buscar empresas
#endereco = 'Rua Santa Aurea, 253, São Paulo, São Paulo, Brasil'
geolocator = Nominatim(user_agent="geolocalização")
endereco = geolocator.geocode('Rua Santa Aurea, 253, São Paulo, São Paulo, Brasil')

# Usando a API do Google Maps para obter as coordenadas do endereço
url_maps = f'https://maps.googleapis.com/maps/api/geocode/json?address={endereco}&key={google_maps_key}'
response_maps = requests.get(url_maps)
result_maps = json.loads(response_maps.text)

# Obtendo as coordenadas do endereço
#lat = result_maps['results'][0]['geometry']['location']['lat']
#lng = result_maps['results'][0]['geometry']['location']['lng']




# Usando a API do Google Places para buscar empresas nas coordenadas
url_places = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={endereco.latitude},{endereco.longitude}&radius=500&type=establishment&key={google_places_key}'
response_places = requests.get(url_places)
result_places = json.loads(response_places.text)

# Extraindo nome e e-mail das empresas 
for place in result_places['results']:
    nome = place['name']
    endereco = place['vicinity']
    place_id = place['place_id']

    # Usando a API do Google Places para obter detalhes da empresa
    url_detail = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,email&key={google_places_key}'
    response_detail = requests.get(url_detail)
    result_detail = json.loads(response_detail.text)

    # Verificando se o e-mail está disponível nos detalhes da empresa
    if 'contato' in result_detail:
        email = result_detail['result']['email']
    else:
        email = 'E-mail não disponível'

    print(f'Nome: {nome}')
    print(f'Endereço: {endereco}')
    print(f'E-mail: {email}')
    print('\n') 