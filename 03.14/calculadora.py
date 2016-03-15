# Faça uma calculadora.
# A calculadora Soma e Subtrai
# Se o usuário escolher a opção 1:
#    o programa deve ler dois valores e exibir sua soma
# Se o usuário escolher a opção 2:
#    o programa deve ler dois valores e exibir a subtração
# Se o usuário escolher a opção x:
#    sair do programa
opcao = ""
while opcao != "x":
    print("[1] Somar")
    print("[2] Subtrair")
    print("[x] Sair")
    opcao = input("Digite a opção:")
    if opcao == "1":
        print("SOMAR")
        n1 = float(input("Digite o primeiro numero:"))
        n2 = float(input("Digite o segundo numero:"))
        print(n1,"+",n2,":",n1+n2)
    elif opcao == "2":
        print("SUBTRAIR")
        n1 = float(input("Digite o primeiro numero:"))
        n2 = float(input("Digite o segundo numero:"))
        print(n1,"-",n2,":",n1-n2)
print("Obrigado por usar a Calculadora! Até mais!")
