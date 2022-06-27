from math import hypot
oposto = float(input("Digite o comprimento do cateto oposto:"))
adjacente = float(input("Digite o comprimento do cateto adjacente: "))
print("A hipotenusa vai medir: {:.2f}".format(hypot(oposto, adjacente)))