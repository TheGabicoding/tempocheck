import requests
import sqlite3

#busca coordenadas da cidade usando a API de geocoding

def buscar_coordenadas(cidade):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=1"
    resposta = requests.get(url)
    dados = resposta.json()

    if "results" not in dados:
        raise ValueError("Cidade não encontrada.")

    local = dados["results"][0]
    return local["latitude"], local["longitude"]

#busca clima atual usando a API de forecast

def buscar_clima(latitude, longitude):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&current=temperature_2m,wind_speed_10m"
    )
    resposta = requests.get(url)
    dados = resposta.json()
    return dados["current"]


def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registros_clima (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cidade TEXT,
            latitude REAL,
            longitude REAL,
            temperatura REAL,
            vento REAL,
            data_hora TEXT DEFAULT (datetime('now', 'localtime'))
        )
    """)
    conexao.commit()


def salva_banco(conexao, cidade, latitude, longitude, temperatura, vento):
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO registros_clima (cidade, latitude, longitude, temperatura, vento)
        VALUES (?, ?, ?, ?, ?)
    """, (cidade, latitude, longitude, temperatura, vento))
    conexao.commit()
    print("Dados salvos com sucesso!")

#seleciona os dados do banco e mostra na tela
def mostrar_historico(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT cidade, temperatura, vento, data_hora FROM registros_clima ORDER BY id DESC")
    registros = cursor.fetchall()

    print("\n--- Histórico salvo no banco ---")
    for cidade, temperatura, vento, data_hora in registros:
        print(f"{data_hora} | {cidade}: {temperatura}°C, vento {vento} km/h")


if __name__ == "__main__":
    conexao = sqlite3.connect("clima.db")
    criar_tabela(conexao)

    cidade = input("Digite a cidade que deseja acompanhar: ")

    latitude, longitude = buscar_coordenadas(cidade)
    info_clima = buscar_clima(latitude, longitude)

    temperatura = info_clima["temperature_2m"]
    vento = info_clima["wind_speed_10m"]

    print(f"{cidade}: {temperatura}°C, vento {vento} km/h")

    salva_banco(conexao, cidade, latitude, longitude, temperatura, vento)
    mostrar_historico(conexao)
