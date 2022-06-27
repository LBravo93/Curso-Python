from time import sleep
numero_1 = int(input('Digite o primeiro número: \n').strip())
numero_2 = int(input('Digite o segundo número: \n').strip())
numero_maior = numero_1
opcoes = str(input('''Digite o número equivalente ao que deseja fazer:
    \033[32m[1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa\033[m\n'''))
while opcoes not in '5':
    if opcoes == '1':
        print(f'A soma de {numero_1} + {numero_2} é {numero_1 + numero_2}\n'+'\033[31m=-=\033[m'*13)
    elif opcoes == '2':
        print(f'O número {numero_1} multiplicado pelo {numero_2} fica {numero_1 * numero_2}.\n'+'\033[31m=-=\033[m'*13)
    elif opcoes == '3':
        if numero_2 > numero_1:
            numero_maior = numero_2
            print(f'O maior digitado foi {numero_maior}.\n'+'\033[31m=-=\033[m'*13)
        else:
            print('Os números digitados são iguais.\n'+'\033[31m=-=\033[m'*13)
    elif opcoes == '4':
        numero_1 = int(input('Digite o primeiro número: \n').strip())
        numero_2 = int(input('Digite o segundo número: \n').strip())
    else:
        print('A opção escolhida não existe. Escolha uma opção válida.\n'+'\033[31m=-=\033[m'*13)
    sleep(2)
    opcoes = str(input('''O que deseja fazer agora?
    \033[32m[1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa\n\033[m'''))
print('\033[31mFIM DO PROGRAMA!!!\033[m')