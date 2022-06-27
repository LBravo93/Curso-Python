produtos = ('Heineken', 3.89 ,
'Pizza', 10, 
'Mouse', 30 ,
'Ovo de Chocolate' , 80 , 
'Copos de vidro' , 15.50 , 
'Smarth Phone' , 1533.50, 
'Ventilador' , 45.99)
for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
        print(f'{produtos[posicao]:.<30}',end='')
    else:
        print(f'R${produtos[posicao]:.>.2f}')