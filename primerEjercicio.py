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

while respuesta != 0:
    print('1.- Suma el numero de datos que el usuario indique')
    print('2.- Potencia de un numero que el usuario indique')
    print('3.- ')
    print('4.- ')
    print('5.- ')
    print('6.- ')
    print('0.- ')
    respuesta=int(input('Respuesta= '))
    if respuesta != 0:
        if respuesta == 1:
            numero1 = float(input('Ingrese el numero uno a sumar: '))
            numero2 = float(input('Ingrese el siguiente numero a sumar: '))
            resultodoSuma=Suma(numero1,numero2)
            print('El resultado de su suma es: ',resultodoSuma)

        if respuesta == 0:
            numero1 = float(input('Ingrese el numero a Potenciar: '))
            numero2 = float(input('Ingrese la Potencia: '))
            resultodoSuma=Suma(numero1,numero2)
            print('El resultado de su Potencia es: ',resultodoSuma)
    else:
        print('Gracias por utilizar nuestro programa')