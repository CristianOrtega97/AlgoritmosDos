def MayorDivisor(numero1,numero2):
    if numero1 == numero2:
        return numero1
    elif numero1>numero2:
        return MayorDivisor(numero1-numero2,numero2)
    else:
        return MayorDivisor(numero1,numero2-numero1)
        
respuesta = 1
print('Tarea en equipo')
print('EQUIPO:')
print('Emanuel Camarena')
print('Andoni Ibarra')
print('Jorge Vazquez')
print('')
print('')
print('')
while respuesta != 0:
    print('Ingrese la opción deseada: ')
    print('1.- Par e Impar')
    print('2.- Ordenar por Recursividad')
    print('3.- Mayor Divisor')
    print('0.- Salir')
    print('')
    try:
        respuesta = int(input('Respuesta: '))
        if respuesta == 1:
            #Código de Andoni
            pass
        elif respuesta == 2:
            #Código de Jorge
            pass
        elif respuesta == 3:
            #Código Emanuel
            try:
                numero1 = int(input('Ingrese el primer número: '))
                numero2 = int(input('Ingrese el segundo número: '))
                resultado = MayorDivisor(numero1,numero2)
                print('El resultado es: ',resultado)
            except ValueError:
                print('Ingrese un número entero o caracter válido')
        elif respuesta == 0:
            print('Saliendo del Sistema')
        else:
            print('Ingrese un número válido')
    except ValueError:
        print('No se ingresó una entrada válida, intente de nuevo')