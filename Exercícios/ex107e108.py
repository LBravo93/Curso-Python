from funcoes import moeda, dobro, centomais, centomenos ,metade, resumonum

preco = float(input('Digite o preço: R$'))
print(f'A metade de R${moeda(preco)} é R$'+f'{metade(preco,cash=True)}')
print(f'O dobro de R${moeda(preco)} é R$'+f'{dobro(preco,cash=True)}')
print(f'Se aumentarmos 10%, temos R$'+f'{centomais(preco, 10,cash=True)}')
print(f'Se diminuirmos 25%, temos R${centomenos(preco, 25, True)}')
resumonum(preco)