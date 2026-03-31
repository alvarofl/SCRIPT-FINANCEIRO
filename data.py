import yfinance as yf
from datetime import datetime


def get_price(ticker):
    try:
        ativo = yf.Ticker(ticker)
        hist = ativo.history(period="1d")
        return float(hist["Close"].iloc[-1])
    except Exception as e:
        print(f"Erro ao buscar {ticker}: {e}")
        return None


def get_dividendos():
    try:
        petr4 = yf.Ticker("PETR4.SA")
        div = petr4.dividends

        if len(div) == 0:
            return {
                "teve_dividendo_recente": False,
                "ultimo_dividendo": None
            }

        ultimo_dividendo = div.index[-1].tz_localize(None)
        hoje = datetime.utcnow()
        dias = (hoje - ultimo_dividendo).days

        return {
            "teve_dividendo_recente": dias < 90,
            "ultimo_dividendo": ultimo_dividendo,
            "dias_desde_dividendo": dias
        }

    except Exception as e:
        print(f"Erro ao buscar dividendos: {e}")
        return None


def get_dados():
    dados = {
        "petroleo": get_price("BZ=F"),
        "usd": get_price("BRL=X"),
        "petr4": get_price("PETR4.SA"),
        "dividendos": get_dividendos()
    }

    return dados