

disciplinas = []

opcao = "s"
while opcao == "s":
    codigo = input("codigo da disciplina:")
    nome = input("digite o nome da disciplina:")
    disciplinas.append([codigo,nome])
    opcao = input("Continua?[s/n]")

for disc in disciplinas:
    print(disc[0],"-",disc[1])
