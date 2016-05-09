
correntistas = []
continua = "s"
while continua != "n":
    cpf = input("CPF:")
    nome = input("Nome:")
    correntistas.append([cpf,nome])
    continua = input("Continua[s/n]?")

arq = open("correntistas.rra","a")
for correntista in correntistas:
    arq.write("%s\n" % correntista[0])
    arq.write("%s\n" % correntista[1])
arq.close()
