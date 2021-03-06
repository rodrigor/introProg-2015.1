'''
 SGAA - Sistema de Gerência de Atividades Acadêmicas
 Código de exemplo do projeto de Introdução à Programação
 Professor: Rodrigo Rebouças de Almeida

 Usa os módulos:
    arq_atividade: que gerencia a leitura e escrita das atividades nos arquivos
    telas: que gerencia a exibição de elementos da tela: menus, títulos, etc.
    entrada: que contém funções para tratar a entrada de dados do usuário
'''

import arq_atividade as ativ
import telas as tela
import entrada as ent


def cad_atividade():
    tela.cls()
    tela.print_titulo("Cadastro de atividades")
    atividade = ent.ler_atividade()
    if ativ.existe_codigo(atividade[0]):
        print("[ERRO] Já existe uma atividade com o código '%s'" % atividade[0])
    else:
        ativ.gravar_atividade(atividade)
    ent.pause()

def listar_atividades():
    atividades = ativ.ler_atividades()
    tela.listar_atividades(atividades)
    ent.pause()

def remover_atividade():
    tela.print_titulo("Remover atividade")
    codigo = ent.ler_str("Digite o código da atividade:")
    if not ativ.existe_codigo(codigo):
        print("Não existe atividade com o código %s" % codigo)
    else:
        atividade = ativ.ler_atividade(codigo)
        tela.exibir_atividade(atividade)
        opcao = ent.ler_opcao("Tem certeza que quer remover esta atividade?",["Sim","Não"],["s","n"])
        if opcao == "s":
            if(ativ.remover_atividade(codigo)):
                print("Atividade removida com sucesso!")
            else:
                print("ERRO Interno: A atividade não foi removida!")
    ent.pause()

def alterar_atividade():
    tela.print_titulo("Alterar atividade")
    codigo = ent.ler_str("Código da atividade:")
    if not ativ.existe_codigo(codigo):
        print("ERRO: Não existe atividade com o código '%s'" % codigo)
    else:
        atividade = ativ.ler_atividade(codigo)
        tela.exibir_atividade(atividade)
        novaAtividade = ent.ler_atividade(atividade)
        ativ.alterar_atividade(codigo,novaAtividade)
        print("Atividade alterada com sucesso!")
    ent.pause()


atividades = []
professores = []

itens_menu = ["Cadastrar atividade",
              "Listar atividades",
              "Remover atividade",
              "Alterar atividade"]
opcoes_menu = tela.gerar_opcoes_menu(itens_menu)

opcao = ""
while opcao != "x":
    tela.menu("SGAA",itens_menu,opcoes_menu)
    opcao = ent.ler_opcao("Opção:",opcoes_menu)
    if opcao == '1':
        cad_atividade()
    elif opcao == "2":
        listar_atividades()
    elif opcao == "3":
        remover_atividade()
    elif opcao == "4":
        alterar_atividade()
