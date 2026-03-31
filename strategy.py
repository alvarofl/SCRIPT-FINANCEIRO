def gerar_sinal(iv, delta, gamma, vega, theta, rho, petroleo, usd, dividendos):

    score = 0

    if iv is not None:
        if iv > 0.35:
            score += 1
        elif iv < 0.20:
            score += 2

    if delta > 0.5:
        score += 2
    elif delta < -0.5:
        score -= 2

    if gamma > 0.05:
        score += 1

    if vega > 0.10:
        score += 1

    if theta < -0.05:
        score -= 1

    if rho > 0.05:
        score += 1

    if petroleo > 85:
        score += 1
    else:
        score -= 1

    if usd > 5.0:
        score += 1

    if dividendos:
        score += 2

    if score >= 5:
        sinal = "CALL"
    elif score <= -3:
        sinal = "PUT"
    else:
        sinal = "NAO OPERAR"

    return sinal, score