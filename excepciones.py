def readint(prompt, min, max):
    try:
        num = int(input(prompt))
        assert num >= min and num <= max
        return num
    except ValueError:
        print("Error: entrada incorrecta")
        return readint(prompt, min, max)
    except AssertionError:
        print("Error: el valor no está dentro del rango permitido (-10..10)")
        return readint(prompt, min, max)


v = readint("Ingresa un numero de -10 a 10: ", -20, 120)

print("El numero es:", v)
