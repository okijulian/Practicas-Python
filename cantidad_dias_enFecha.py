def isYearLeap(year):
    return (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)


def daysInMonth(year, month):
    diasPorMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if isYearLeap(year):
        if diasPorMes[month - 1] == 28:
            return (29)
        else:
            return (diasPorMes[month - 1])
    else:
        return (diasPorMes[month - 1])

    return (None)


def dayOfYear(year, month, day):
    if year < 1582 or month > 12 or month < 1:
        return (None)

    if day > daysInMonth(year, month) or day < 1:
        return (None)

    totalDias = day
    month = month - 1
    while month > 0:
        totalDias += daysInMonth(year, month)
        month -= 1

    return (totalDias)








testYears = [2021, 2000, 2016, 1987]
testMonths = [1, 12, 1, 11]
testDias= [1,31,2,7]
testResults = [1,366,1,1]

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
