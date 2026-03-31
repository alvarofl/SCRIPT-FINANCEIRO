#cálcular GREGAS E DELTA 

# options.py

from py_vollib.black_scholes.implied_volatility import implied_volatility
from py_vollib.black_scholes.greeks.analytical import delta
from py_vollib.black_scholes.greeks.analytical import gamma
from py_vollib.black_scholes.greeks.analytical import vega
from py_vollib.black_scholes.greeks.analytical import theta


def calcular_iv(tipo, S, K, r, t, preco_opcao):
    """
    tipo: 'c' para call, 'p' para put
    S: preço da ação
    K: strike
    r: taxa de juros (ex: 0.13)
    t: tempo até vencimento em anos
    preco_opcao: preço da opção no mercado
    """
    iv = implied_volatility(preco_opcao, S, K, t, r, tipo)
    return iv


def calcular_gregas(tipo, S, K, r, t, iv):
    d = delta(tipo, S, K, t, r, iv)
    g = gamma(tipo, S, K, t, r, iv)
    v = vega(tipo, S, K, t, r, iv)
    th = theta(tipo, S, K, t, r, iv)

    return {
        "delta": d,
        "gamma": g,
        "vega": v,
        "theta": th
    }


def calcular_opcoes(tipo, S, K, r, t, preco_opcao):
    iv = calcular_iv(tipo, S, K, r, t, preco_opcao)
    gregas = calcular_gregas(tipo, S, K, r, t, iv)

    return {
        "iv": iv,
        "delta": gregas["delta"],
        "gamma": gregas["gamma"],
        "vega": gregas["vega"],
        "theta": gregas["theta"]
    }
