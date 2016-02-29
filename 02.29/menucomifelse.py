
print("**************************")
print("   [1] Calc Media  ")
print("   [2] Cad Aluno  ")
print("   [3] Sair  ")
opcao = input("Digite sua opcao")

if opcao == "1":
    print("Nota1:")
    nota1 = float(input(">"))
    print("Nota2:")
    nota2 = float(input(">"))
    print("Nota3:")
    nota3 = float(input(">"))
    media = (nota1+nota2+nota3) / 3  
    print(" A media do aluno e:",media)
