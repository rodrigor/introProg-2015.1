

# TAREFA:
# Altere a função "menu()" para que ela
# receba uma lista de opções. A função
# deve exibir o menu com as opções contidas
# na lista


def menu(titulo,tamanho,itens):
    topo = "┏"+("─" * tamanho) + "┓"
    tam_margem = int((tamanho - len(titulo)) / 2)
    margemesq = "│"+ " " * tam_margem
    margemdir = (" " * tam_margem) + "│"
    print(topo)
    print(margemesq,titulo,margemdir)
    for i in range(len(itens)):
        print("│ [",i+1,"] ",itens[i],"│")
    print("[ x ] Sair")


opcoes = ["Cadastrar produto",
          "Listar produtos",
          "Procurar produto"]
menu("Cadastro produtos",50,opcoes)
