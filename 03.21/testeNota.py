nota_invalida = True
while nota_invalida:
    nota = float(input("Digite a nota:"))
    nota_invalida = nota < 0 or nota > 10
    if nota_invalida:        
        print("Nota inválida!")
