
def somar(a,b):
    return a + b


n1 = int(input("Numero1:"))
n2 = int(input("Numero2:"))
arquivo = open("exemploAula.html","w")
print("<b><i>",somar(n1,n2),"</i></b>", file = arquivo)
