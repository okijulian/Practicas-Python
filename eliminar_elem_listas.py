#este prograba busca elementos repetidos en una lista los borra y los almacena en una nueva lista. 

miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]#lista de ejemplo

nuevalista= []# crea una nueva lista vacia para  pasar los elemento 
for i in miLista: # verifica elementos de la lista
    if i not in nuevalista: 
        nuevalista.append(i)

print("La lista solo con elementos únicos:")
print(nuevalista)


