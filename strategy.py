def gerar_sinal(iv, delta, gamma, vega, theta, petroleo, usd, dividendos):
    
    score = 0

    # IV
    if iv > 0.35:
        score += 2
    elif iv < 0.20:
        score -= 1

    # Petróleo
    if petroleo > 85:
        score += 1
    else:
        score -= 1

    # Dólar
    if usd > 5.0:
        score += 1

    # Dividendos
    if dividendos:
        score += 2

    # Delta
    if delta > 0.5:
        score += 1
    elif delta < -0.5:
        score -= 1

    # Theta (evitar theta muito negativo)
    if theta < -0.05:
        score -= 1

    # Definir sinal
    if score >= 3:
        sinal = "CALL"
    elif score <= -2:
        sinal = "PUT"
    else:
        sinal = "NAO OPERAR"

    return sinal, score