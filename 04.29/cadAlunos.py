'''
Faça um programa que cadastra alunos.
Cada aluno possui as seguintes informações:
- Matricula
- Nome
- CPF
- Genero
- Data de Nascimento

Após o cadastro, o sistema deve listar os
alunos cadastrados.
'''
MAT = 0
NOME = 1
CPF = 2
GENERO = 3
NASC = 4

def lerAluno():
    mat = input("Matrícula:")
    nome = input("Nome completo:")
    cpf = input("CPF:")
    genero = input("Genero:")
    nasc = input("Nascimento:")
    return [mat,nome,cpf,genero,nasc]

def alinha(texto, tam):
    if texto > tam:
        print("Erro! o texto é maior que o tamanho")
    else:
        margem = tam - texto
        return texto + (" "*margem)

def tabela(cabecalho,tamanhos,elementos):
    colunas = len(elementos)
    
    print("╔═══════════════════╗")
    print("║      M E N U      ║")
    print("╠═══╦═══════════════╣")
    print("║ 1 ║               ║")
    print("╠═══╬═══════════════╣")
    print("║ 2 ║               ║")
    print("╠═══╬═══════════════╣")
    print("║ 1 ║               ║")
    print("╠═══╬═══════════════╣")
    print("║ 4 ║ Sair          ║")
    print("╚═══╩═══════════════╝")


alunos = []
opcao = "s"
while opcao == "s":
    alunos.append(lerAluno())
    opcao = input("Continua?[s/n]")

print("_________________________________")
print("| Mat | Nome | CPF | Genero | Nasc")
for aluno in alunos:
    print(aluno[MAT],"|",aluno[NOME],"|",aluno[CPF],"|"
          aluno[GENERO],"|",aluno[NASC])
