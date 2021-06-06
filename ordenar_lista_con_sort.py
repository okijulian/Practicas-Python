miLista = []
swapped = True
num = int (input("¿Cuántos elementos deseas ordenar?:")) #pide al usuario que ingrese la cantidad de nuevos elementos en la lista 

for i in range(num):
    val = float(input("Introduce un elemento de la lista:"))
    miLista.append(val)

    miLista.sort()

print("\nOrdenado:")
print(miLista)
