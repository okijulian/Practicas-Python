
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

def dayOfYear(año , meses , dia):

    cantDias = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

    if daysInMonth(año, meses):
            if  cantDias [dia -1 ]== 28:
                return 2
            else:
                return cantDias [dia -1]
        else:
            return cantDias [dia -1]
    else:
        return cantDias [dia-1]

    return None

testYears = [2021, 2000, 2016, 1987]
testMonths = [6, 2, 1, 11]
testDias= [13,20,2,7]
testResults = [lunes,martes,jueves,viernes]

for i in range (len(testYears)):
    yr =testYears[i]
    mo =testMonths[i]
    di = testDias[i]
    print(yr,mo,di,"->", end=" ")
    result = dayOfYear(yr,mo,di)
    if result == testResults[i]:
        print ('OK')
    else:
        print("Error")
