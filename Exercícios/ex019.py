import random
aluno_1 = input('Primeiro aluno: ')
aluno_2 = input('Segundo aluno: ')
aluno_3 = input('Terceiro aluno: ')
aluno_4 = input('Quarto aluno: ')
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
sorteio = random.choice(lista)
print("O grande vencedor é: {}".format(sorteio))