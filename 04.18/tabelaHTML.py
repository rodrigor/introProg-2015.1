'''
Exemplo de uma tabela em HTML:
<table border = 1>
<tr> <th>Nome</th> <th>Nota</th></tr>
<h1>Lista de alunos</h1>
  <tr> <td>José</td> <td>10</td></tr>
  <tr> <td>Felismina</td>  <td>8</td></tr>
  <tr> <td>Zoroastro</td>  <td>5</td></tr>
</table>
'''



def tabelaHtml(alunos,notas,arquivo):
    print("<table border = 1>", file = arquivo)
    print("<tr> <th>Nome</th> <th>Nota</th></tr>", file = arquivo)
    for i in range(len(alunos)):
        print("<tr><td>",alunos[i],"</td><td>",notas[i],"</td></tr>", file = arquivo)
    print("</table>", file = arquivo)


alunos = []
notas = []
continua = True
while continua:
    alunos.append(input("Digite o nome:"))
    notas.append(int(input("Nota:")))
    opcao = input("Continua? [s/n]:")
    if opcao == "n":
        continua = False

arquivo = open("alunos.html","w")
tabelaHtml(alunos,notas,arquivo)
