
def solicitar_numero():
    return int(input('Ingrese un numero:'))

def main():
    numero = solicitar_numero()

    if (numero % 2 == 0):
        print('es par')
    else:
        print('es impar')

main()