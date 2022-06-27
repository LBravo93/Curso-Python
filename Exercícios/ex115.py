import modulo_cores
from modulo_arquivo import *
from modulo_menu import *
from modulo_numeros import leiaint
from modulo_strings import *

sistemaTXT = ("ex115.txt")

cabeçalho('Sistema arquivo v1.0')

verificExisteArquivo(sistemaTXT)
if not verificExisteArquivo(sistemaTXT):
    criartxt(sistemaTXT)
else:
    print(f'{"Arquivo de registro encontrado!":^42}')

while True:
    opc = menu(['Ver pessoas cadastradas',
               'Cadastrar pessoas', 'Finalizar programa'])
    res = leiaint("Digite sua opção: ")
    if res == 1:
        cabeçalho(modulo_cores.amarelo('Ver Pessoas Cadastradas'))
        mostrartxt(sistemaTXT)

    elif res == 2:
        cabeçalho(modulo_cores.amarelo('Cadastrar Pessoas'))
        n = leiastr('Digite o Nome: ').strip()
        i = leiaint('Digite a Idade: ')

        adicionartxt(sistemaTXT, n, i, )
        continue

    elif res == 3:
        cabeçalho(modulo_cores.vermelho('Programa finalizado'))
        break

    elif res > 3:
        print()
        print(modulo_cores.vermelho(f'A opção "{res}" não existe.'))
