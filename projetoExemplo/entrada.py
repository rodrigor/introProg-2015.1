

def ler_opcao(msg = "Digite a opção:",opcoes = ["x"]):
    while True:
        opcao = input(msg)
        if opcao in opcoes:
            return opcao
        print("Opção inválida (%s)" % opcao)

def ler_str(msg, min = -1, max = -1):
    while True:
        entrada = input(msg)
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

def ler_atividade():
    codigo_atividade = ler_str("Código da atividade:",5,5)
    tipo = ler_opcao("Tipo da atividade [pesquisa, extensão, ensino, admin]:",["pesquisa","ensino","extensão","admin"])
    atividade = ler_str("Atividade:",5,200)
    return [codigo_atividade,tipo,atividade]
