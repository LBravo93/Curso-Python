total = acimamil = menor = contador = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    contador += 1
    total = total + preco
    if preco > 1000:
        acimamil = acimamil + 1
    if contador == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [SN]\n')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'FIM DO PROGRAMA')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {acimamil} produtos acima de R$1000,00')
print(f'O produto mais barato foi {barato.capitalize()} e custou R${menor:.2f}')