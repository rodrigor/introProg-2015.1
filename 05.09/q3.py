def lerNumero(msg,menor,maior):
    while True:
        numero = float(input(msg))
        if (numero >= menor) and (numero <= maior):
            return numero
        print("Entrada inválida!")

idade = lerNumero("Digite sua idade:",0,120)
print("A idade digitada foi: ",idade)

nota = lerNumero("Digite uma nota:",0,10)
print("A nota digitada foi:", nota)

imc = lerNumero("Digite seu percentual de gordura",0,1)
print("O imc é de:",imc)
