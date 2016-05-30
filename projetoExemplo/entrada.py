

def selecionar_item(msg = "Digite a opção:",itens = ["Sair"],opcoes = []):
    if not opcoes:
        for i in range(len(itens)):
            opcoes.append(str(i+1))
    print(msg)
    for i in range(len(itens)):
        print("[%s] %s" % (opcoes[i],itens[i]))
    while True:
        opcao = input("> ")
        if opcao in opcoes:
            return itens[int(opcao)-1]
        print("Opção inválida (%s)" % opcao)

def ler_opcao(msg = "Digite a opção:",opcoes = ["x"]):
    while True:
        opcao = input(msg)
        if opcao in opcoes:
            return opcao
        print("Opção inválida (%s)" % opcao)

def ler_str(msg, min = -1, max = -1):
    while True:
        print(msg)
        entrada = input(">")
        if max == -1 and min == -1:
            return entrada
        tam = len(entrada)
        if tam > max:
            print("[ERRO] O tamanho máximo da entrada é %d" % max)
        elif tam < min:
            print("[ERRO] O tamanho mínimo da enrtada é %d" % min)
        else:
            return entrada



def pause():
    print()
    input("[Pressione qualquer tecla para continuar]")

def ler_atividade(atividade = ["","",""]):
    if atividade[0] == "":
        atividade[0] = ler_str("Código da atividade:",3,5)
    atividade[1] = selecionar_item("Tipo da atividade (%s):" % atividade[1],["Pesquisa","Ensino","Extensão","Administração"])
    atividade[2] = ler_str("Atividade (%s):" % atividade[2],0,200)
    return atividade
