def es_par(numero):
    return numero % 2 == 0

def solicitar_numero():
    return int(input('Ingrese un numero:'))

def main():
    numero = solicitar_numero()

    if (es_par(numero)):
        print('es par')
    else:
        print('es impar')

main()
