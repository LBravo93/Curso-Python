n = input('Digite algo: ')
print('O tipo primitivo desse valor é: ',type(n))
print('É numérico? ', n.isnumeric())
print('Só tem espaços? ', n.isspace())
print('Está em letros maiúsculas? ', n.isupper())
print('É alfabético? ', n.isalpha())
print('Só tem letras minúsculas? ', n.islower())
print('Tem letras maiúsculas e minúsculas misturadas? ', n.istitle())