
def menu():
    print("*** MENU ***")
    print("[1] Cadastrar disciplina")
    print("[2] Cadastrar aluno")
    print("[3] Matricular aluno")
    print("[x] Sair")


disciplinas = []
opcao = 0
while opcao != "x":
    menu()
    opcao = input("Digite a opção:")
    if opcao == "1":
        cadastrarDisciplina()
