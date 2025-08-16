import random

def dividir_amostras(amostras, num_grupos):
    random.shuffle(amostras)
    grupos = [sorted(amostras[i::num_grupos]) for i in range(num_grupos)]
    return grupos

def redistribuir_grupos(grupos, nome_var1, nome_var2):
    novos_grupos = []
    for nome, grupo in grupos:
        subgrupos = dividir_amostras(grupo, 2)
        novos_grupos.append((f"{nome} - {nome_var1}", subgrupos[0]))
        novos_grupos.append((f"{nome} - {nome_var2}", subgrupos[1]))
    return novos_grupos

def main():
    amostras = list(range(1, int(input("Digite o número total de amostras: ")) + 1))
    num_grupos = int(input("Digite o número de grupos: "))
    nomes_grupos = [input(f"Digite o nome do grupo {i + 1}: ") for i in range(num_grupos)]

    grupos = [(nome, sorted(amostras[i::num_grupos])) for i, nome in enumerate(nomes_grupos)]

    etapa = 1
    while etapa <= 4:
        print(f"\nEtapa {etapa} concluída. Grupos:")
        for nome, grupo in grupos:
            print(f"{nome}: {grupo}")

        if input("\nDeseja distribuir as amostras novamente? (S/N): ").strip().lower() != 's':
            break

        nome_var1 = input(f"Digite o nome da variável 1 para a etapa {etapa + 1}: ")
        nome_var2 = input(f"Digite o nome da variável 2 para a etapa {etapa + 1}: ")

        grupos = redistribuir_grupos(grupos, nome_var1, nome_var2)
        etapa += 1

    print("\nDistribuição final das amostras:")
    for nome, grupo in grupos:
        print(f"{nome}: {grupo}")

if _name_ == "__main__":
    main()
