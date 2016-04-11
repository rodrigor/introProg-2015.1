def media(listaNumeros):
    soma = 0
    for numero in listaNumeros:
        soma = soma + numero
    return soma / len(listaNumeros)

numeros = []
continua = True
while continua:
    numeros.append(float(input("Numero?")))
    opcao = input("continua?[s/n]")
    if(opcao == "n"):
        continua = False
print("A média é: ",media(numeros))
