def factorial (numero):
        if numero == 1 or numero == 0:
            if numero == 0:
                return 1
            else:
                return numero
        else:
            try:
                return numero * factorial(numero-1)
            except RecursionError:
                print('Ingrese un número mayor o igual a 1')
            except TypeError:
                print('Ingrese un número mayor o igual a 1')

numero = input('Ingrese un número: ')
if numero.isnumeric():
        numero=int(numero)
        print('El factorial del numero es: ',factorial(numero))  
else:
    numero=ord(numero)
    if numero>=65 and numero<=90:
        print('El factorial del numero es: ',factorial(numero))
    elif numero>=97 and numero<=122:
        print('El factorial del numero es: ',factorial(numero))
    else:
        print('Ingrese una letra MAYÚSCULA O minuscula')