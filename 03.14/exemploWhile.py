alunos = []
continua = "s"
while continua == "s" or continua == "S":
    alunos.append(input("Nome do aluno:"))
    continua = input("Deseja continuar? [s/n]")

for aluno in alunos:
    print(aluno)

print("Tchau!")
