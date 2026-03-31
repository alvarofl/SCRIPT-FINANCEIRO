from py_vollib.black_scholes.implied_volatility import implied_volatility
from py_vollib.black_scholes.greeks.analytical import delta, gamma, vega, theta, rho


def calcular_iv(tipo, S, K, r, t, preco_opcao):
    try:
        iv = implied_volatility(preco_opcao, S, K, t, r, tipo)
        return iv
    except:
        return None


def calcular_gregas(tipo, S, K, r, t, iv):
    if iv is None:
        return None

    return {
        "delta": delta(tipo, S, K, t, r, iv),
        "gamma": gamma(tipo, S, K, t, r, iv),
        "vega": vega(tipo, S, K, t, r, iv),
        "theta": theta(tipo, S, K, t, r, iv),
        "rho": rho(tipo, S, K, t, r, iv)
    }


def calcular_opcoes(tipo, S, K, r, t, preco_opcao):
    iv = calcular_iv(tipo, S, K, r, t, preco_opcao)

    if iv is None:
        return None

    gregas = calcular_gregas(tipo, S, K, r, t, iv)

    return {
        "iv": iv,
        "delta": gregas["delta"],
        "gamma": gregas["gamma"],
        "vega": gregas["vega"],
        "theta": gregas["theta"],
        "rho": gregas["rho"]
    }