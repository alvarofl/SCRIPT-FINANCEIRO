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
        else:
            print("Opção inválida")


def input_float(msg):
    while True:
        try:
            return float(input(msg))
        except:
            print("Valor inválido")


def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except:
            print("Valor inválido")


def print_dados(dados):
    print(f"\nPETR4: {dados['petr4']:.2f}")
    print(f"Petróleo: {dados['petroleo']:.2f}")
    print(f"USD/BRL: {dados['usd']:.2f}")
    print(f"Dividendos: {dados['dividendos']}")


def print_resultados(resultados):
    print("\n===== MELHORES OPORTUNIDADES =====")

    for item in resultados[:5]:
        print(f"""
Strike: {item['strike']}
Score: {item['score']}
Sinal: {item['sinal']}
Delta: {item['delta']:.2f}
IV: {item['iv']:.2f}
Theta: {item['theta']:.4f}
---------------------------
""")


def main():
    print("Buscando dados de mercado...")
    dados = get_dados()

    if not dados:
        print("Erro ao buscar dados")
        return

    print_dados(dados)

    S = dados["petr4"]
    petroleo = dados["petroleo"]
    usd = dados["usd"]
    dividendos = dados["dividendos"]

    tipo = escolher_tipo()

    dias = input_int("Dias até vencimento: ")
    preco_opcao = input_float("Preço médio das opções: ")

    taxa_juros = 0.13
    t = dias / 365

    print("\nEscaneando opções...")
    resultados = scanner_opcoes(
        tipo,
        S,
        taxa_juros,
        t,
        preco_opcao,
        petroleo,
        usd,
        dividendos
    )

    if not resultados:
        print("Nenhuma oportunidade encontrada")
        return

    resultados.sort(key=lambda x: x["score"], reverse=True)

    print_resultados(resultados)


if __name__ == "__main__":
    main()