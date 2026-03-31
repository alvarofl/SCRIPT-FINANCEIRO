import requests
import pandas as pd
from bs4 import BeautifulSoup


def to_float(valor):
    try:
        return float(valor.replace(",", "."))
    except:
        return None


def get_opcoes_statusinvest():
    url = "https://statusinvest.com.br/opcoes/petr4"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print("Erro ao acessar StatusInvest:", e)
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    tabela = soup.find("table")

    if tabela is None:
        print("Tabela não encontrada")
        return None

    linhas = tabela.find_all("tr")

    dados = []

    for linha in linhas[1:]:
        colunas = linha.find_all("td")

        if len(colunas) < 12:
            continue

        try:
            dados.append({
                "ticker": colunas[0].text.strip(),
                "tipo": colunas[1].text.strip(),
                "strike": to_float(colunas[2].text.strip()),
                "preco": to_float(colunas[3].text.strip()),
                "delta": to_float(colunas[7].text.strip()),
                "gamma": to_float(colunas[8].text.strip()),
                "vega": to_float(colunas[9].text.strip()),
                "theta": to_float(colunas[10].text.strip()),
                "iv": to_float(colunas[11].text.strip()),
            })
        except Exception as e:
            print("Erro ao processar linha:", e)

    df = pd.DataFrame(dados)

    return df