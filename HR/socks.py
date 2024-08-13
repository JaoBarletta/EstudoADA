

def sockMerchant(n,ar):
    # Criamos um dicionário que irá armazenar como (chave , valor) o (cor , quantidade)
    # dessa maneira conseguimos contar a quantidade de cada cor
    cores = {}
    # Percorresmos o dicionário
    for meia_cor in ar:
        # Se a cor ja existir, adicionamos +1 ao valor
        if meia_cor in cores:
            cores[meia_cor] += 1
        else:
            cores[meia_cor] = 1
        

    # depois só fazemos uma somatória com base nos valores do dicionário
    pares = 0
    for contagem in cores.values():
        pares += contagem // 2

    return pares



if __name__ == "__main__":
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)