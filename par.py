
def es_par(numero):
    return numero % 2 == 0

numero = int(input('Ingrese un numero:'))

if (es_par(numero)):
    print('es par')
else:
    print('es impar')