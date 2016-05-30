import os

arquivo_atividade = "atividades.txt"

def gravar_atividade(atividade):
    arq = open(arquivo_atividade,"a")
    arq.write("%s;%s;%s\n" % (atividade[0],atividade[1],atividade[2]))
    arq.close()

def atualizar_atividades(atividades):
    arq = open(arquivo_atividade,"w")
    for atividade in atividades:
        arq.write("%s;%s;%s\n" % (atividade[0],atividade[1],atividade[2]))
    arq.close()

def ler_atividades():
    atividades = []
    if not os.path.exists(arquivo_atividade):
        return atividades
    
    arq = open(arquivo_atividade,"r")
    linhas = arq.read().splitlines()
    for linha in linhas:
        atividade_str = linha.split(";")
        codigo = atividade_str[0]
        tipo = atividade_str[1]
        nome = atividade_str[2]
        atividades.append([codigo,tipo,nome])
    return atividades

def ler_codigos_atividades():
    atividades = ler_atividades()
    codigos = []
    for atividade in atividades:
        codigos.append(atividade[0])
    return codigos

def existe_codigo(codigo):
    return codigo in ler_codigos_atividades()

def alterar_atividade(codigo,novaAtividade):
    remover_atividade(codigo)
    gravar_atividade(novaAtividade)

def remover_atividade(codigo):
    atividades = ler_atividades()
    for i,atividade in enumerate(atividades):
        if atividade[0] == codigo:
            atividades.pop(i)
            atualizar_atividades(atividades)
            return True
    return False

def ler_atividade(codigo):
    atividades = ler_atividades()
    for atividade in atividades:
        if atividade[0] == codigo:
            return atividade
    return False
