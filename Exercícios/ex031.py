viagem = float(input('Digite a kilometragem da viagem que você deseja: '))
if viagem <= 200:
    print('Sua viagem tem {:.0f} kilômetros de distância. Nesse caso custará R${:.2f}.'.format(viagem, viagem * 0.50))
else:
    print('Sua viagem tem {:.0f} kilômetros de distância, sendo assim, custará R${:.2f}.'.format(viagem, viagem * 0.45))