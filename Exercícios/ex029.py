velocidade = float(input('Digite a velocidade atual do carro: '))
limite = 80
if velocidade <limite:
    print('Você está abaixo do limite de velocidade, continue assim!')

if velocidade == limite:
    print('Você está no LIMITE, não aumente a velocidade ou será multado!')

if velocidade > limite:
    multa = (velocidade - limite) * 7
    print('Você está acima da velocidade, e terá que pagar uma multa de {:.2f} Reais.'.format(multa))


print('---'*7)
print('Fim do Programa.')
print('---'*7)