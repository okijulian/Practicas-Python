def añobisiesto(año):
    if año % 4 != 0:

        return False

    elif año % 4 == 0 and año % 100 != 0:

        return True
    

    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:

        return False

    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:

        return True
#un verificador para ver si la operacion es correcta  mostrando en ambas listas si es correcta o da un error en la operacion para cada caso
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = añobisiesto(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
