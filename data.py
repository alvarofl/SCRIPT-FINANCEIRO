import yfinance as yf
from datetime import datetime


def get_petroleo():
    brent = yf.Ticker("BZ=F")
    hist = brent.history(period="1d")
    return float(hist["Close"].iloc[-1])


def get_usdbrl():
    usd = yf.Ticker("BRL=X")
    hist = usd.history(period="1d")
    return float(hist["Close"].iloc[-1])


def get_petr4():
    petr4 = yf.Ticker("PETR4.SA")
    hist = petr4.history(period="1d")
    return float(hist["Close"].iloc[-1])


def get_dividendos():
    import yfinance as yf
    from datetime import datetime

    petr4 = yf.Ticker("PETR4.SA")
    div = petr4.dividends

    if len(div) == 0:
        return False

    ultimo_dividendo = div.index[-1]

    # Remover timezone para evitar erro
    ultimo_dividendo = ultimo_dividendo.tz_localize(None)

    hoje = datetime.now()

    dias = (hoje - ultimo_dividendo).days

    # Se teve dividendo nos últimos 90 dias
    if dias < 90:
        return True
    else:
        return False
 


def get_dados():
    dados = {
        "petroleo": get_petroleo(),
        "usd": get_usdbrl(),
        "petr4": get_petr4(),
        "dividendos": get_dividendos()
    }

    return dados