from data import get_dados
from scanner import scanner_opcoes


def escolher_tipo():
    while True:
        print("\nTipo de operação:")
        print("1 - CALL")
        print("2 - PUT")

        op = input("Escolha: ")

        if op == "1":
            return "c"
        elif op == "2":
            return "p"


def main():
    print("Buscando dados de mercado...")
    dados = get_dados()

    S = dados["petr4"]
    petroleo = dados["petroleo"]
    usd = dados["usd"]
    dividendos = dados["dividendos"]

    print(f"\nPETR4: {S:.2f}")
    print(f"Petroleo: {petroleo:.2f}")
    print(f"USD/BRL: {usd:.2f}")
    print(f"Dividendos: {dividendos}")

    tipo = escolher_tipo()

    dias = int(input("Dias até vencimento: "))
    preco_opcao = float(input("Preço médio das opções: "))

    r = 0.13
    t = dias / 365

    print("\nEscaneando opções...")
    resultados = scanner_opcoes(tipo, S, r, t, preco_opcao, petroleo, usd, dividendos)

    # Ordenar por score
    resultados.sort(key=lambda x: x["score"], reverse=True)

    print("\n===== MELHORES OPORTUNIDADES =====")

    for r in resultados[:5]:
        print(f"""
Strike: {r['strike']}
Score: {r['score']}
Sinal: {r['sinal']}
Delta: {r['delta']:.2f}
IV: {r['iv']:.2f}
Theta: {r['theta']:.4f}
---------------------------
""")

if __name__ == "__main__":
    main()