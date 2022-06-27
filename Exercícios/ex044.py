preco = float(input('Digite o preço das compras: R$').strip())
opcao = int(input(''''ESCOLHA UMA DAS FORMAS DE PAGAMENTO ABAIXO:
    [ 1 ] À vista dinheiro/cheque
    [ 2 ] À vista cartão
    [ 3 ] 2x no cartão
    [ 4 ] 3x ou mais no cartão
Digite o número da sua opçao: '''))
if opcao == 1:
    desconto = (preco / 100) * 10
    precofinal = preco - desconto
    print(f'Sua compra À vista de R${preco:.2f}, terá um desconto de R${desconto:.2f}, ficando por apenas R${precofinal:.2f}.')
elif opcao == 2:
    desconto = (preco / 100) * 5
    precofinal = preco - desconto
    print(f'Sua compra À Vista no cartão de R${preco:.2f}, terá um desconto de R${desconto:.2f}, ficando por apenas R${precofinal:.2f}.')
elif opcao == 3:
    precofinal = preco / 2
    print(f'Sua compra é de R${preco:.2f}. Pagamento em 2x de R${precofinal:.2f}.')
elif opcao == 4:
    quantparcelas = int(input('''Em quantas parcelas deseja pagar?
Digite um número entre 3 e 10: '''))
    if 3 < quantparcelas > 10:
        print('Você digitou um número inválido.')
    else:
            juros = (preco / 100) * 20
            precofinal = preco + juros
            valorparcelas = precofinal / quantparcelas
            print(f'Sua compra de R${preco:.2f}, com pagamento em {quantparcelas} vezes de R${valorparcelas:.2f} com juros. ficando um total de R${precofinal:.2f}.')
else:
    print('Você digitou um número inválido. Escolha uma opção de 1 a 4')