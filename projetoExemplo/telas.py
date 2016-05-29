
def cls():
    for i in range(100):
        print()


def print_linha(tam):
    print("─" * tam)

def centralizar(txt,tam):
    diferenca_margem = ""
    if len(txt) % 2 != 0:
        diferenca_margem = " "
    tam_margem = int((tam - len(txt)) / 2)
    margem = " " * tam_margem
    return margem + txt + margem + diferenca_margem

def esquerda(txt,tam):
    tam_margem = tam - len(txt)
    return txt + (" "*tam_margem)


def maior(lista_txt):
    maior = 0
    for txt in lista_txt:
        tam = len(txt)
        if tam > maior:
            maior = tam
    return maior

def gerar_opcoes_menu(itens):
    opcoes = []
    for i in range(len(itens)):
        opcoes.append(str(i+1))
    opcoes.append("x")
    return opcoes

def print_titulo(msg):
    print_linha(len(msg)+2)
    print(" "+msg+" ")
    print_linha(len(msg)+2)

def menu(titulo,itens, opcoes = []):
    if len(opcoes) == 0:
        opcoes = gerar_opcoes_menu(itens)

    tamanho = maior(itens) + len(" [?]  ")

    if len(titulo) > tamanho:
        tamanho = len(titulo)
    cls()
    print_linha(tamanho)
    print(centralizar(titulo,tamanho))
    for i in range(len(itens)):
        print(" [{0}] {1}".format(opcoes[i],itens[i]))
    print(" [x] Sair")
    print_linha(tamanho)

def listar_atividades(atividades):
    TAM_COD = 8
    TAM_TIPO = 10
    TAM_ATIV = 30
    cls()
    print_titulo("Listar atividades")
    print()
    head = "| %s | %s | %s |" % (centralizar("Codigo",TAM_COD),centralizar("Tipo",TAM_TIPO),esquerda("Atividade",TAM_ATIV))
    print_linha(len(head))
    print(head)
    print_linha(len(head))
    for atividade in atividades:
        print("| %s | %s | %s |" % (centralizar(atividade[0],TAM_COD),centralizar(atividade[1],TAM_TIPO),esquerda(atividade[2],TAM_ATIV)))
    print_linha(len(head))

def exibir_atividade(atividade):
    if len(atividade) != 3:
        print("[ERRO!] ATIVIDADE INVÁLIDA! %s" % atividade)
        return

    print("Codigo: %s | Tipo: %s" % (atividade[0],atividade[1]))
    print("Nome:   %s" % atividade[2])
