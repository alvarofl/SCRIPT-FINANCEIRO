import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_opcoes_statusinvest():
    url = "https://statusinvest.com.br/opcoes/petr4"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    tabela = soup.find("table")
    linhas = tabela.find_all("tr")

    dados = []

    for linha in linhas[1:]:
        colunas = linha.find_all("td")

        if len(colunas) > 0:
            dados.append({
                "ticker": colunas[0].text.strip(),
                "tipo": colunas[1].text.strip(),
                "strike": float(colunas[2].text.strip().replace(",", ".")),
                "preco": float(colunas[3].text.strip().replace(",", ".")),
                "delta": float(colunas[7].text.strip().replace(",", ".")),
                "gamma": float(colunas[8].text.strip().replace(",", ".")),
                "vega": float(colunas[9].text.strip().replace(",", ".")),
                "theta": float(colunas[10].text.strip().replace(",", ".")),
                "iv": float(colunas[11].text.strip().replace(",", ".")),
            })

    df = pd.DataFrame(dados)
    return df
 