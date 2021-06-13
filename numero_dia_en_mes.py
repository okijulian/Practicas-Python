'''Tu tarea es escribir y probar una función que toma dos argumentos 
(un año y un mes) y devuelve el número de días del mes/año dado 
(mientras que solo febrero es sensible al valor year, tu función debería ser universal).'''
#dependiendo de si es un ano bisiesto o no

def añobisiesto(año):
    if año % 4 != 0:
        return False
    elif año % 4 == 0 and año % 100 != 0:
        return True
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
        return False
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
        return True

def daysInMonth(año, meses):

    diasxmes = [31,28,31,30,31,30,31,31,30,31,30,31]
    if añobisiesto(año):
        if diasxmes [meses -1 ] ==28:
            return 29

        else:
            return diasxmes[meses - 1]
    else:
         return diasxmes[meses - 1]
    return None


#verificacion de que se cumpla las condiciones. 
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
