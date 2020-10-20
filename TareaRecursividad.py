import random
from random import randint

def MayorDivisor(numero1,numero2):
    if numero1 == numero2:
        return numero1
    elif numero1>numero2:
        return MayorDivisor(numero1-numero2,numero2)
    else:
        return MayorDivisor(numero1,numero2-numero1)

def impar (num):
    if (num == 0):
        return False
    else:
        return par(num-1)

def par (num):
    if (num == 0): 
        return True
    else:
        return impar(num-1)

def sort_quick (lista):
    if len(lista) <= 1:
        return lista     
    elemento_igual,elemento_mayor,elemento_menor = [],[],[]
    pivote = lista[randint(0,len(lista)-1)]
    for elemento in lista:
        if elemento < pivote:
            elemento_menor.append(elemento)
        elif elemento == pivote:
            elemento_igual.append(elemento)
        else:
            elemento_mayor.append(elemento)
        return sort_quick(elemento_menor) + elemento_igual + sort_quick(elemento_mayor)

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
            numero = int(input('Ingrese el número: '))
            print(par(numero))
        elif respuesta == 2:
            #Código de Jorge
            lista = [random.randrange(1, 100, 1) for i in range(1000)]
            ordenado=sort_quick(lista)
            print(ordenado)
        elif respuesta == 3:
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