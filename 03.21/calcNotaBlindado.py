# Faça um programa que cadastra notas e calcula média
# Exemplo do menu:
#  ---------------------
# |         MENU        |
# | [1] Cadastrar notas |
# | [2] Calcular média  |
# | [3] Situação        |
# | [x] Sair            |
#  ---------------------
# 1) No cadastro de notas, receber 3 notas.
# 2) Calcular a média das 3 notas
# 3) Informar se o aluno está aprovado, reprovado
#    ou na Final.

opcao = ""
notas = []
while opcao != "x":
    print(" --------------------- ")
    print("|         MENU        |")
    print("| [1] Cadastrar notas |")
    print("| [2] Calcular média  |")
    print("| [3] Situação        |")
    print("| [x] Sair            |")
    print(" --------------------- ")
    opcao = input("Opção:")
    if opcao == "1":
        notas = []
        notas.append(float(input("Nota 1:")))
        notas.append(float(input("Nota 2:")))
        notas.append(float(input("Nota 3:")))
        # print("RR:",notas)
    elif opcao == "2":
        if len(notas) == 0:
            print("Por favor, cadastre as notas!")
        else:
            media = (notas[0] + notas [1] + notas[2]) / 3
            print("A média do aluno é: %.1f"%(media))
    elif opcao == "3":
        if len(notas) == 0:
            print("Por favor, cadastre as notas!")
        else:
            media = (notas[0] + notas [1] + notas[2]) / 3
            if media >= 7:
                print("APROVADO")
            elif media >= 4:
                print("FINAL")
            else:
                print("REPROVADO")
    elif opcao == "x":
        print("Saindo do sistema...")
    else:
        print("Opção inválida!")
print("Volte sempre!")
