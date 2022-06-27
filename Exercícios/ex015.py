dias = int(input("Digite os dias alugados? (apenas números) "))
km = float(input("Qauntos Kilômetros rodados? (apenas números)"))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))