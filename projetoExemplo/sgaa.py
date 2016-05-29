'''
 SGAA - Sistema de Gerência de Atividades Acadêmicas
 Código de exemplo do projeto de Introdução à Programação
 Professor: Rodrigo Rebouças de Almeida

 Usa os módulos:
    arquivos: que gerencia a leitura e escrita em arquivos
    telas: que gerencia a exibição de elementos da tela: menus, títulos, etc.
    entrada: que contém funções para tratar a entrada de dados do usuário
'''

import arquivos as arq
import telas as tela
import entrada as ent


def cad_atividade():
    tela.cls()
    tela.print_titulo("Cadastro de atividades")
    atividade = ent.ler_atividade()
    arq.gravar_atividade(atividade)
    ent.pause()

def listar_atividades():
    atividades = arq.ler_atividades()
    tela.listar_atividades(atividades)
    ent.pause()

def remover_atividade():
    tela.print_titulo("Remover atividade")
    codigo = ent.ler_str("Digite o código da atividade:")
    if not arquivo.existe_codigo(codigo):
        print("Não existe atividade com o código %s" % codigo)
    else:
        atividade = arquivo.ler_atividade(codigo)
        tela.exibir_atividade(atividade)
        opcao = ent.ler_opcao("Tem certeza que quer remover esta atividade? [s/n]",["s","n"])
        if opcao == "s":
            if(arquivo.remover_atividade(codigo)):
                print("Atividade removida com sucesso!")
            else:
                print("ERRO Interno: A atividade não foi removida!")
    ent.pause()



atividades = []
professores = []

opcao = ""

itens_menu = ["Cadastrar atividade",
              "Listar atividades",
              "Remover atividade"]
opcoes_menu = tela.gerar_opcoes_menu(itens_menu)

while opcao != "x":
    tela.menu("SGAA",itens_menu,opcoes_menu)
    opcao = ent.ler_opcao("Opção:",opcoes_menu)
    if opcao == '1':
        cad_atividade()
    elif opcao == "2":
        listar_atividades()
    elif opcao == "3":
        remover_atividade()
