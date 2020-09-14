def Fibonacci(numero):
    if numero == 0:
        return numero
    elif numero == 1:
        return numero
    else:
        return Fibonacci(numero -1) + Fibonacci(numero-2)

def ProductoSuma(numero):
    if numero == 1:
            return numero
    else:
        try:
            return numero + ProductoSuma(numero-1)
        except RecursionError:
            print('Ingrese un número mayor o igual a 1')

def ProductoMult(numero):
    if numero == 1:
            return numero
    else:
        try:
            return numero * ProductoMult(numero-1)
        except RecursionError:
            print('Ingrese un número mayor o igual a 1')

def Palindromo(frase,primera_pos,ultima_pos):
    if primera_pos == ultima_pos:
        return True
    elif primera_pos == ultima_pos+1:
        return True
    else: 
        aux1 = frase[primera_pos]
        aux2 = frase[ultima_pos]
        frase[primera_pos] = aux2
        frase[ultima_pos] = aux1
        return Palindromo(frase, primera_pos + 1,ultima_pos-1)

respuesta = 1

while respuesta != 0:
    print('1.- Fibonacci')
    print('2.- Producto y Suma de 1 a N')
    print('3.- Palíndromo')
    print('0.- Salir')
    respuesta=int(input('Respuesta= '))
    if respuesta != 0:
        if respuesta == 1:
            numero = input('Ingrese un número: ')
            if numero.isnumeric():
                numero=int(numero)
                print('El Fibonacci del numero es: ',Fibonacci(numero))  
            else:
                numero=ord(numero)
                if numero>=65 and numero<=90:
                    print('El Fibonacci del numero es: ',Fibonacci(numero))
                elif numero>=97 and numero<=122:
                    print('El Fibonacci del numero es: ',Fibonacci(numero))
                else:
                    print('Ingrese una letra MAYÚSCULA O minuscula')
        if respuesta == 2:
            print('1.- Suma')
            print('2.- Producto')
            print('0.- Salir')
            opcion=int(input('Seleccione la opción deseada: '))
            
            if opcion != 0:
                if opcion == 1:
                    numero = int(input('Ingrese un número: '))
                    print('La respuesta es: ',ProductoSuma(numero))
                elif opcion == 2:
                    numero = int(input('Ingrese un número: '))
                    print('La respuesta es: ',ProductoMult(numero))
                else:
                    print('Ingrese una opción valida')
                    print('Volviendo al menú principal')
            else:
                print('Volviendo al menú principal')

        if respuesta == 3:
            frase = str(input('Ingrese la frase palíndroma: ')).lower()
            fraseoriginal = frase.replace(" ","")
            frase = frase.replace(" ","")
            frase = list(frase)
            fraseoriginal = list(fraseoriginal)
            ultima_pos = len(frase)-1  #Ultima posición
            primera_pos = 0   #Primer posicion
            Palindromo(frase,primera_pos,ultima_pos)
            if (frase == fraseoriginal):
                print('La frase es Palindromo')
            else:
                print('La frase no es Palindromo')

    else:
        print('Gracias por utilizar nuestro programa')