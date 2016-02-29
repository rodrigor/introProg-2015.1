
cabecalho = "Menu"

tam_linha = 45
linha = "_" * tam_linha
tam_cabecalho = len(cabecalho)
tam_margem = (tam_linha - tam_cabecalho) / 2
margem = " " * int(tam_margem)

titulo = margem + cabecalho + margem

print(linha)
print(titulo)
print("  [1] Cadastrar Aluno  ")
print("  [2] Sair       ")
print(linha)

