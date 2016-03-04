TAXA_POR_QUILO = 6

peso = float(input("Digite o peso da encomenda (em kg):"))

if peso <= 5:
    print("O valor do frete é R$ 30,00")
elif peso <= 100:
    frete = peso * TAXA_POR_QUILO
    print("O valor do frete é de",frete)
else:
    print("Frete especial. Calculado sob consulta!")

if peso <= 10:
    print("Prazo de entrega: 5 dias úteis")
else:
    print("Prazo de entrega: 15 dias úteis")
