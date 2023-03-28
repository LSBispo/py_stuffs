from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geolocalização")
location = geolocator.geocode("R. Capote Valente, 39 - Pinheiros, São Paulo - SP")

#print((location.latitude, location.longitude))
print(location.latitude)