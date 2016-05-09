arq = open("correntistas.rra","r")
for linha in arq.readlines():
    print(linha, end="")
arq.close()
