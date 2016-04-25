import time
import os
def cls():
    os.system("cls")


def carregando_sistema():
    print("''''''''''''''''''''''''''''''''AAAAAA'''''''''''''''''''''''AA'''''''''''''''''''''''''''''''''''''")
    print("'''''''''''''''''''''''''''''AAAAAAAAAAAA'''''''''''''''''''AAAAAA''''''''''''''''''''''''''''''''''")
    print("''''''''''''''''''''''''''AAAAAAAAAAAAAAAAAA*'''''''''''''''AAAAAAAAAA''''''''''''''''''''''''''''''")
    print("'''''''''''''''''''''''AAAAAAAAAAAAAAAAAAAAAAAAA''''''''''''AAAAAAAAAAAAA'''''''''''''''''''''''''''")
    print("'''''''''''''''''''CAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'''''''''AAAAAAAAAAAAAAA'''''''''''''''''''''''''")
    print("'''''''''''''''''CCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA''''''''AAAAAAAAAAAAAAAAA'''''''''''''''''''''''")
    print("'''''''''''''''''CCCCAAAAAAAAAAAAAAAAAAAAAAAAAAAAA''''''''''AAAAAAAAAAAAAAAAAA''''''''''''''''''''''")
    print("'''''''''''''''''CCCCCCAAAAAAAAAAAAAAAAAAAAAAAA'''''''''''''AAAAAAAAAAAAAAAAAA''''''''''''''''''''''")
    print("'''''''''''''''''CCCCCCCCCCAAAAAAAAAAAAAAAAC''''''''''''''''AAAAAAAAAAAAAAAAAA*'''''''''''''''''''''")
    print("'''''''''''''''''CCCCCCCCCCCCCAAAAAAAAAA''''''''''''''''''''AAAAAAAAAAAAAAAAAA*'''''''''''''''''''''")
    print("'''''''''''''''''CCCCCCCCCCCCCCCCAAAA'''''''''''''''''''''''CAAAAAAAAAAAAAAAAA*'''''''''''''''''''''")
    print("'''''''''''''''''CCCCCCCCCCCCCCCCCCCA'''''''''''''''''''''''CCAAAAAAAAAAAAAAAA*'''''''''''''''''''''")
    print("'''''''''''''''''CCCCCCCCCCCCCCCCCCCCCC'''''''''''''''''''''CCCCAAAAAAAAAAAAAA*'''''''''''''''''''''")
    print("'''''''''''''''''CCCCCCCCCCCCCCCCCCCCCCCCC('''''''''''''''''CCCCCCCAAAAAAAAAAA*'''''''''''''''''''''")
    print("'''''''''''''''''CCCCCCCCCCCCCCCCCCCCCCCCCCCCC''''''''''''''CCCCCCCCCCAAAAAAAA*'''''''''''''''''''''")
    print("'''''''''''''''''CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC'''''''''''CCCCCCCCCCCCCCAAAA*'''''''''''''''''''''")
    print("'''''''''''''''''CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC''''''''CCCCCCCCCCCCCCCCCA*'''''''''''''''''''''")
    print("''''''''''''''''''CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC'''''''CCCCCCCCCCCCCCCCCC*'''''''''''''''''''''")
    print("'''''''''''''''''''''CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC,''''''CCCCCCCCCCCCCCCCCC*'''''''''''''''''''''")
    print("''''''''''''''''''''''''CCCCCCCCCCCCCCCCCCCCCCCCCCCCC,''''''CCCCCCCCCCCCCCCCCC*'''''''''''''''''''''")
    print("''''''''''''''''''''''''''''CCCCCCCCCCCCCCCCCCCCCCCCC,''''''CCCCCCCCCCCCCCCCCC*'''''''''''''''''''''")
    print("'''''''''''''''''''''''''''''''CCCCCCCCCCCCCCCCCCCCCC,''''''CCCCCCCCCCCCCCCCCC*'''''''''''''''''''''")
    print("'''''''''''''''''''''''''''''''''ACCCCCCCCCCCCCCCCCCC,''''''CCCCCCCCCCCCCCCCCC*'''''''''''''''''''''")
    print("'''''''''''''''''''''''''''''''''AAAACCCCCCCCCCCCCCCC,''''''CCCCCCCCCCCCCCCCCC*'''''''''''''''''''''")
    print("''''''''''''''''''''''''''''''AAAAAAAAAACCCCCCCCCCCCC,''''''CCCCCCCCCCCCCCCCCC*'''''''''''''''''''''")
    print("'''''''''''''''''''''''''''AAAAAAAAAAAAAAAACCCCCCCCCC,''''''CCCCCCCCCCCCCCCCCC*'''''''''''''''''''''")
    print("'''''''''''''''''''''''AAAAAAAAAAAAAAAAAAAAAAAACCCCCC,''''''CCCCCCCCCCCCCCCCCC*'''''''''''''''''''''")
    print("''''''''''''''''''''AAAAAAAAAAAAAAAAAAAAAAAAAAAAACCCC,''''''CCCCCCCCCCCCCCCCCC*'''''''''''''''''''''")
    print("''''''''''''''''''AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC'''''''CCCCCCCCCCCCCCCCCC*'''''''''''''''''''''")
    print("'''''''''''''''''''CAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC''''''''''CCCCCCCCCCCCCCCCC*'''''''''''''''''''''")
    print("'''''''''''''''''''''''AAAAAAAAAAAAAAAAAAAAAAAAA''''''''''''''''CCCCCCCCCCCCCC*'''''''''''''''''''''")
    print("''''''''''''''''''''''''''AAAAAAAAAAAAAAAAAAA''''''''''''''''''''''(CCCCCCCCCC*'''''''''''''''''''''")
    print("'''''''''''''''''''''''''''''AAAAAAAAAAAA''''''''''''''''''''''''''''''CCCCCCC*'''''''''''''''''''''")
    print("''''''''''''''''''''''''''''''''AAAAAA''''''''''''''''''''''''''''''''''''CCCC''''''''''''''''''''''")
    print("             .########..########.##.....##....##.....##.####.##....##.########...#######.")
    print("             .##.....##.##.......###...###....##.....##..##..###...##.##.....##.##.....##")
    print("             .##.....##.##.......####.####....##.....##..##..####..##.##.....##.##.....##")
    print("             .########..######...##.###.##....##.....##..##..##.##.##.##.....##.##.....##")
    print("             .##.....##.##.......##.....##.....##...##...##..##..####.##.....##.##.....##")
    print("             .##.....##.##.......##.....##......##.##....##..##...###.##.....##.##.....##")
    print("             .########..########.##.....##.......###....####.##....##.########...#######.")
    print("\n\nPor favor aguarde, dentro de alguns instantes o sistema iniciará...")
    print ("Carregando...")

    for i in range (80):
        print ("▓", end="")
        time.sleep(0.1)
    print ("\nSistema Carregado com sucesso!")
    time.sleep(1)
    cls()

def menu(lista_menu,tamanho,titulo):
    cont=0
    tam_margem = int((tamanho-len(titulo))/2)
    margem = "_" * tam_margem
    print(margem,titulo,margem)
    for i in lista_menu:
            print ("            [",cont+1,"]",i)
            cont=cont+1
    print ("_"*52)

carregando_sistema()
lista_menu=[]
preencher_menu=True
print ("CRIANDO O MENU:")
print ("A qualquer momento você poderá digitar sair, isso irá finalizar a criação do menu.")
while preencher_menu:
    temp=input("Digite as opções desejadas para seu menu: ")
    lista_menu.append(temp)
    if temp == "Sair" or temp == "sair":
        preencher_menu=False
        cls()
menu (lista_menu, 50,"MENU")
