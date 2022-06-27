import random

primeiro_aluno = input('Digite o nome do primeiro aluno: ')
segundo_aluno = input('Digite o nome do segundo aluno: ')
terceiro_aluno = input("Digite o nome do terceiro aluno: ")
quarto_aluno = input("Digite o nome do quarto aluno: ")
alunos_apresentacao = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
random.shuffle(alunos_apresentacao)
print('A ordem da apresentação será: {}'.format(alunos_apresentacao))