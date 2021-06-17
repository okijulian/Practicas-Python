#funcion para hacer el factorial de los numeros 
def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    producto = 1
    for i in range(2, n + 1):
        producto *= i
    return producto

for n in range(1, 10): # probando
    print(n, factorialFun(n))

    
    
    #metodo corto por recursividad
def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorialFun(n - 1)

for n in range(1, 10): # probando
    print(n, factorialFun(n))
