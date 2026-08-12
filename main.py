import requests

cidade = input("Digite a cidade que deseja acompanhar: ")

url_cidade = f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=1"

resposta = requests.get(url_cidade)

dados = resposta.json()

local = dados["results"] [0]

latitude = local["latitude"]
longitude = local["longitude"]

url_clima = (f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&current=temperature_2m,wind_speed_10m")

resposta_clima = requests.get(url_clima)

dados_clima = resposta_clima.json()

info_clima = dados_clima["current"]

temperatura = info_clima["temperature_2m"]
vento = info_clima["wind_speed_10m"]

print(temperatura, vento)


