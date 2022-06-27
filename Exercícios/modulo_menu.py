from modulo_numeros import leiaint
from time import sleep
import modulo_cores
from modulo_arquivo import *



def linha(tam=42):
    return '-' * tam

def cabeçalho(msg):
    print(linha())
    print(f'{msg:^45}')
    print(linha())


def menu(a):
    cabeçalho(modulo_cores.amarelo('CADASTRO'))
    c = 1
    for item in a:#Para mostrar o menu. as Opções do menu devem estar em forma de lista
        print(modulo_cores.amarelo(c),modulo_cores.amarelo('-'),modulo_cores.azul(item))
        c = c + 1

    print(linha())
