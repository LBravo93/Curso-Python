import math

angulo = float(input("Digite o ângulo que você quer calcular: "))
seno = math.sin(math.radians(angulo))
print("O ângulo de {} tem o SENO de {:.2f}.".format(angulo, seno))