import random
from time import sleep
escolha = int(input('''QUE OS JOGOS COMECEM
Escolha uma das opções para jogar JOKENPÔ
    [ 1 ] PEDRA
    [ 2 ] PAPEL
    [ 3 ] TESOURA
Qual é a sua jogada?
    ''').strip())

opcoes = ['PEDRA', 'PAPEL' , 'TESOURA']
maquina = (random.choice(opcoes))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('-='*13)
print(f'''A maquina escolheu: {maquina}''')

if escolha == 1:
    escolha = 'PEDRA'
elif escolha == 2:
    escolha = 'PAPEL'
elif escolha == 3:
    escolha = 'TESOURA'
else:
    print('E você quis ser espertinho e quebrar meu código...TENTE NOVAMENTE.')

print(f'Você escolheu: {escolha}')
print('-='*13)

if escolha == 'PEDRA' and maquina == 'PEDRA' or escolha == 'PAPEL' and maquina == 'PAPEL' or escolha == 'TESOURA' and maquina == 'TESOURA':
    print('EMPATE. Vai de novo.')
elif escolha == 'PEDRA' and maquina == 'PAPEL' or escolha == 'PAPEL' and maquina == 'TESOURA' or escolha == 'TESOURA' and maquina == 'PEDRA':
    print('Você PERDEU!!!')
else:
    print('Você GANHOU!!!')