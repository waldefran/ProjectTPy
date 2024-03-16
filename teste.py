import requests
import pandas as pd

# Função para obter os dados da API do IBGE
def get_ibge_data():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def json_to_csv():
    data = get_ibge_data()
    if data is not None:
        df = pd.DataFrame(data)
        df.to_csv('ibge_data.csv', index=False)
        print(df.columns)
    else:
        print("No data to save")

json_to_csv()