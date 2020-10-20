#Shell
def ordenamientoDeShell(unaLista):
    contadorSublistas = len(unaLista)//2
    while contadorSublistas > 0:

      for posicionInicio in range(contadorSublistas):
        brechaOrdenamientoPorInsercion(unaLista,posicionInicio,contadorSublistas)

      print("Después de los incrementos de tamaño",contadorSublistas,
                                   "La lista es",unaLista)

      contadorSublistas = contadorSublistas // 2

def brechaOrdenamientoPorInsercion(unaLista,inicio,brecha):
    for i in range(inicio+brecha,len(unaLista),brecha):

        valorActual = unaLista[i]
        posicion = i

        while posicion>=brecha and unaLista[posicion-brecha]>valorActual:
            unaLista[posicion]=unaLista[posicion-brecha]
            posicion = posicion-brecha

        unaLista[posicion]=valorActual

#Insercion
def ordenamientoPorInsercion(unaLista):
   for indice in range(1,len(unaLista)):

     valorActual = unaLista[indice]
     posicion = indice

     while posicion>0 and unaLista[posicion-1]>valorActual:
         unaLista[posicion]=unaLista[posicion-1]
         posicion = posicion-1

     unaLista[posicion]=valorActual

#quicksort
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 
 
# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),

#Merge Sort
def merge_sort(values): 
  
    if len(values)>1: 
        m = len(values)//2
        left = values[:m] 
        right = values[m:] 
        left = merge_sort(left) 
        right = merge_sort(right) 
  
        values =[] 
  
        while len(left)>0 and len(right)>0: 
            if left[0]<right[0]: 
                values.append(left[0]) 
                left.pop(0) 
            else: 
                values.append(right[0]) 
                right.pop(0) 
  
        for i in left: 
            values.append(i) 
        for i in right: 
            values.append(i) 
                  
    return values 
  
# Input list 
a = [12, 11, 13, 5, 6, 7] 
print("Given array is") 
print(*a) 
  
a = merge_sort(a) 
  
# Print output 
print("Sorted array is : ") 
print(*a) 
