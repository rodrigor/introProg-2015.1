# Exemplo do uso do IF, ELIF e ELSE
print("**************************")
print("   [1] Calc Media")
print("   [2] Cad Aluno")
print("   [3] Sair")
print("**************************")
opcao = input("Digite sua opcao: ")

if opcao == "1":
    print("Nota1:")
    nota1 = float(input(">"))
    print("Nota2:")
    nota2 = float(input(">"))
    print("Nota3:")
    nota3 = float(input(">"))
    media = (nota1+nota2+nota3) / 3
    print(" A media do aluno e:",media)
    if media >= 7:
        print("APROVADO")
    elif media >= 4:
        print("PROVA FINAL")
    else:
        print("REPROVADO")
elif opcao == "2":
    nome = input("digite seu nome:")
    matricula = input("matricula:")
    print("nome:",nome,"matricula:",matricula)
elif opcao == "3":
    print("até mais!")
else:
    print("Opcao invalida: ",opcao)
