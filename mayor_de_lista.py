# utilizando  ciclo for con in para   comparar elementos de la lista suponiendo siempre de izquierda a derecha la comparativa 

#usando len para contar elementos de la lista
miLista = [0, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista[0]

for i in range(1, len(miLista)):
   if miLista [i]> mayor:
        mayor = miLista[i]

print(mayor)


#con rojada en vez de len
miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista [0]

for i in miLista [1:]:
   if i > mayor:
        mayor = i

print(mayor)
