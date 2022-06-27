from bdb import Breakpoint


def ajuda(com):
    help(com)



comando = ''
while True:
    comando = str(input('       LISTA DE COMANDOS       \nDigite o comando: '))
    if comando.upper() == 'FIM':
        print('     PROGRAMA FINALIZADO     ')
        break
    else:
        ajuda(comando)