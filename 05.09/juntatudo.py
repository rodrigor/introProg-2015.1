def somar(lista):
    soma = 0
    for num in lista:
        soma = soma + num
    return soma

def media(lista):
    return somar(lista)/len(lista)

opcao =  "s"
idades = []
while opcao == "s":
    idade = int(input("Digite a idade:"))
    idades.append(idade)
    opcao = input("Continua?[s/n]:")

print("A média das idades é %.2f" % media(idades))
