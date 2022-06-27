import modulo_cores
def leiastr(msg):
    while True:
        try:
            a = str(input(msg).strip().capitalize())
            if a.isnumeric():
                print(modulo_cores.vermelho('Digite apenas Letras!'))
            else:
                return a

        except(KeyboardInterrupt):
            print(modulo_cores.vermelho('\nO usuário interrompeu o programa. \nTente Novamente!!'))


