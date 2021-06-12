#funciones con listas.

#ejemplo1
def sumaDeLista(lst):
    sum = 0

    for elem in lst:
        sum += elem

    return sum

print(sumaDeLista([5, 4, 3]))  # se invoca de esta manera

#ejemplo 2
def strangeListFunction(n):
    strangeList = []

    for i in range(0, n):
        strangeList.insert(0, i)

    return strangeList


print(strangeListFunction(5)) # devuelve una lista de 5 elementos de mayor a menor. 
