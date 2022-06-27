peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print (f'Seu IMC (Índice de massa corporal) é de {imc:.2f}: Você está abaixo do peso ideal.')
elif imc <= 25:
    print(f'Seu IMC (Índice de massa corporal) é de {imc:.2f}: Você está no peso ideal.')
elif imc <= 30:
    print(f'Seu IMC (Índice de massa corporal) é de {imc:.2f}: com Sobrepeso.')
elif imc <= 40:
    print(f'Seu IMC (Índice de massa corporal) é de {imc:.2f}: Você está na Obesidade.')
else:
    print(f'Seu IMC (Índice de massa corporal) é de {imc:.2f}: Você está na OBESIDADE MÓRBIDA. ')