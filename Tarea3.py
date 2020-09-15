# Torres de Hanoi
def Hanoi(n,inicio,final,medio):
        if n == 1:
            print("Mover %i de la torre %s a la torre %s" %(n,inicio,final))
        else:
            Hanoi(n-1,inicio,medio,final)
            print("Mover %i de la torre %s a la torre %s" %(n,inicio,final))
            Hanoi(n-1,medio,final,inicio)

n = int(input('Ingrese el numero de aros: '))
inicio = input('¿De que torre parte? ')
final = input('¿A que torre va? ')
medio = input('¿Cual sobra? ')
Hanoi(n,inicio,final,medio)