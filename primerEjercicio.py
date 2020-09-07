respuesta = 1

def Suma(numero1,numero2=0):
    if numero2!=0:
        resultado = numero1 + numero2
        numero1=float(input('Ingrese numero a sumar: '))
        return numero1 + Suma(resultado)
    elif numero2==0:
        return numero1
    else:
        numero2=float(input('Ingrese numero a sumar: '))
        return numero1 + Suma(numero2)

def  Potencia(numero1,numero2=0):
    if numero2!=0:
        resultado = numero1 * numero2
        numero1=float(input('Ingrese numero a sumar: '))
        return numero1 * Potencia(resultado)
    elif numero2==0:
        return numero1
    else:
        numero2=float(input('Ingrese numero a sumar: '))
        return numero1 + Potencia(numero2)

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

def ParOImpar():
    pass

while respuesta != 0:
    print('1.- Suma el numero de datos que el usuario indique')
    print('2.- Potencia de un numero que el usuario indique')
    print('3.- Numero de caracteres')
    print('4.- Contador Vocales y Consonantes')
    print('5.- ')
    print('6.- ')
    print('0.- Salir')
    respuesta=int(input('Respuesta= '))
    if respuesta != 0:
        if respuesta == 1:
            numero1 = float(input('Ingrese el numero uno a sumar: '))
            numero2 = float(input('Ingrese el siguiente numero a sumar: '))
            resultadoSuma=Suma(numero1,numero2)
            print('El resultado de su suma es: ',resultadoSuma)

        if respuesta == 2:
            numero1 = float(input('Ingrese el numero a Potenciar: '))
            numero2 = float(input('Ingrese la Potencia: '))
            resultodoSuma=Suma(numero1,numero2)
            print('El resultado de su Potencia es: ',resultodoSuma)

        if respuesta == 3:
            frase = list(input('Ingrese la frase: '))
            resultadoFrase=NumCaracteres(frase)
            print('La frase tiene tanto caracteres: ',resultadoFrase)

        if respuesta == 4:
            frase = list(input('Ingrese la frase: '))
            VocalesConsonantes(frase)

    else:
        print('Gracias por utilizar nuestro programa')