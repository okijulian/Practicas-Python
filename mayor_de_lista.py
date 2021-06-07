# utilizando  ciclo for con in para   comparar elementos de la lista suponiendo siempre de izquierda a derecha la comparativa 
miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista [0]

for i in miLista [1:]:
   if i > mayor:
        mayor = i

print(mayor)

