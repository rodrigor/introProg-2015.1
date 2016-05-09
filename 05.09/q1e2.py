def somar(lista):
    soma = 0
    for num in lista:
        soma = soma + num
    return soma

def media(lista):
    return somar(lista)/len(lista)

idades = [10,60,90,100]
print(media(idades))
