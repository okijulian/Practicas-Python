miLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Encontrar = 5 # elemento a encontrar
Encontrado = False

for i in range(len(miLista)): #busca en la lista desde  la posicion  0 hasta la ultima posicion definida por len
    Encontrado = miLista[i] == Encontrar  # define una nueva variable  que  cuando el for  encuentra el elemento en que posicion se encuenta  lo guarda 
    if Encontrado:
        break

if Encontrado:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")
