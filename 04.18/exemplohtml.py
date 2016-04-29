
def somar(a,b):
    return a + b


n1 = int(input("Numero1:"))
n2 = int(input("Numero2:"))
arquivo = open("exemploAula.html","w")
print("<b>",somar(n1,n2),"</b>", file = arquivo)
print("<i>",somar(n1,n2),"</i>", file = arquivo)
arquivo.close()
