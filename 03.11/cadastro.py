# Faça um programa que cadastra alunos e lista
# os alunos com nota maior que 7
quantidade = int(input("Quantos alunos?"))
nomes = []
notas = []
for i in range(quantidade):
    nomes.append(input("Nome:"))
    notas.append(float(input("Nota:")))

print("Os alunos Aprovados foram:")
for i in range(quantidade):
    if notas[i] >= 7:
        print("Aluno",i+1)
        print("Nome: ",nomes[i])
        print("Nota: ",notas[i])
    else:
        print(nomes[i],"foi REPROVADO!")
