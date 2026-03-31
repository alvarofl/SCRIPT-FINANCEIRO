from options import calcular_opcoes
from strategy import gerar_sinal


def gerar_strikes(preco):
    strikes = []
    for i in range(-3, 4):
        strikes.append(round(preco + i, 2))
    return strikes


def scanner_opcoes(tipo, S, r, t, preco_opcao, petroleo, usd, dividendos):
    resultados = []

    strikes = gerar_strikes(S)

    for strike in strikes:
        try:
            opcoes = calcular_opcoes(tipo, S, strike, r, t, preco_opcao)

            if opcoes is None:
                continue

            iv = opcoes["iv"]
            delta = opcoes["delta"]
            gamma = opcoes["gamma"]
            vega = opcoes["vega"]
            theta = opcoes["theta"]
            rho = opcoes["rho"]

            sinal, score = gerar_sinal(iv, delta, gamma, vega, theta, rho, petroleo, usd, dividendos)

            resultados.append({
                "strike": strike,
                "iv": iv,
                "delta": delta,
                "gamma": gamma,
                "vega": vega,
                "theta": theta,
                "rho": rho,
                "sinal": sinal,
                "score": score
            })

        except Exception as e:
            print("Erro no strike", strike, e)

    return resultados