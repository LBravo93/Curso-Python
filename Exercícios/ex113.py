from modulo_numeros import leiaint, leiafloat
import modulo_cores


            

numint = leiaint(modulo_cores.amarelo('Digite um número: '))
numfloat = leiafloat(modulo_cores.amarelo('Digite um número real: '))
print(modulo_cores.verde(f'O número inteiro digitado foi {numint} e o real foi {numfloat}'))