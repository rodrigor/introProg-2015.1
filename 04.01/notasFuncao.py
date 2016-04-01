def menu():
    print(" --------------------- ")
    print("|         MENU        |")
    print("| [1] Cadastrar notas |")
    print("| [2] Calcular média  |")
    print("| [3] Situação        |")
    print("| [x] Sair            |")
    print(" --------------------- ")

def cadNotas():
    minhasNotas = []
    minhasNotas.append(float(input("Nota 1:")))
    minhasNotas.append(float(input("Nota 2:")))
    minhasNotas.append(float(input("Nota 3:")))
    return minhasNotas

def calcMedia(valores):
    soma = 0.0
    for valor in valores:
        soma = soma + valor
    return soma / len(valores)

def situacao(valor):
    if valor >= 7:
        return "APROVADO"
    elif valor >= 4:
        return "FINAL"
    else:
        return "REPROVADO"



opcao = ""
notas = []
while opcao != "x":
    menu()
    opcao = input("Opção:")
    if opcao == "1":
        notas = cadNotas()
    elif opcao == "2":
        print("A média do aluno é: %.1f"%(calcMedia(notas)))
    elif opcao == "3":
        print(situacao(calcMedia(notas)))
    elif opcao == "x":
        print("Saindo do sistema...")
    else:
        print("Opção inválida!")
print("Volte sempre!")
