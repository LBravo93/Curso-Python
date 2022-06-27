def maior(*num):
    cont = total = 0
    print('~~'*30)
    print('    Analisando números informados: ',end='')
    for valor in num:
        print(f'{valor}, ',end='')
        if cont == 0:
            total = valor
        else:
            if valor > total:
                total = valor
        cont = cont + 1
    print(f'\n    Ao todo foram informados {cont} valores.\n    E o maior valor foi {total}')
    print('~~'*30)


maior(5,7,9,3,1,5,15,45,35,65,85,45,7,225)
maior(4,7,2,9,7)
maior()