numero = ('Zero' , 'Um' , 'Dois' , 'Três' , 'Quatro' , 'Cinco' ,
'Seis' , 'Sete' , 'Oito' , 'Nove' , 'Dez' ,
'Onze' , 'Doze' , 'Treze' , 'Quatorze' , 'Quinze' ,
'Dezesseis' , 'Dezessete' , 'Dezoito' , 'Dezenove' , 'Vinte')
while True:
    numuser = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numuser <=20:
        break
    print('Tente novamente.')
print(f'Você digitou o número {numero[numuser]}')
