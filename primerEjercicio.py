respuesta = 1

def Suma(numero1):
    if numero1 != 0:
        numeroTemp=float(input('Ingrese un numero para sumar o "0" para salir: '))
        return numero1 + Suma(numeroTemp)
    else:
        return numero1

def  Potencia(numero1,numero2):
    exponente=numero1
    for i in range(numero2-1):
        numero1*=exponente
    return numero1

def NumCaracteres(frase):
    contador = 0
    for i in range(len(frase)):
        letra = frase.pop()
        if letra != " ":
            contador+=1
        else:
            pass
    return contador

def VocalesConsonantes(frase):
    vocales=0
    consonantes=0
    for i in range(len(frase)):
        letra = frase.pop()
        if letra != " ":
            if letra == 'a' or letra == 'A':
                vocales+=1
            elif letra == 'e' or letra == 'E':
                vocales+=1
            elif letra == 'o' or letra == 'O':
                vocales+=1
            elif letra == 'i' or letra == 'I':
                vocales+=1
            elif letra == 'u' or letra == 'U':
                vocales+=1
            else:
                consonantes+=1
        else:
            pass
    print('Las consonantes que tiene son: ',consonantes)
    print('Las vocales que tiene son: ',vocales)

def ParOImpar(numero):
    residuo = numero % 2
    if residuo == 0:
        print('El numero es par')

    else:
        print('El numero es impar')

def Apuntadores():
    x = 2015
    y = x
    x = 2016

    print(x)
    print(y)

    v = [1]
    w = v
    v.append(2)

    print(v)
    print(w)

while respuesta != 0:
    print('1.- Suma el numero de datos que el usuario indique')
    print('2.- Potencia de un numero que el usuario indique')
    print('3.- Numero de caracteres')
    print('4.- Contador Vocales y Consonantes')
    print('5.- Par o Impar')
    print('6.- Ejemplo Apuntadores')
    print('0.- Salir')
    respuesta=int(input('Respuesta= '))
    if respuesta != 0:
        if respuesta == 1:
            numero1 = float(input('Ingrese el numero uno a sumar: '))
            resultadoSuma=Suma(numero1)
            print('El resultado de su suma es: ',resultadoSuma)

        if respuesta == 2:
            numero1 = int(input('Ingrese el numero a Potenciar: '))
            numero2 = int(input('Ingrese la Potencia: '))
            resultodoPotencia=Potencia(numero1,numero2)
            print('El resultado de su Potencia es: ',resultodoPotencia)

        if respuesta == 3:
            frase = list(input('Ingrese la frase: '))
            resultadoFrase=NumCaracteres(frase)
            print('La frase tiene tanto caracteres: ',resultadoFrase)

        if respuesta == 4:
            frase = list(input('Ingrese la frase: '))
            VocalesConsonantes(frase)

        if respuesta == 5:
            numero = int(input('Ingrese el numero entero: '))
            ParOImpar(numero)

        if respuesta == 6:
            Apuntadores()

    else:
        print('Gracias por utilizar nuestro programa')