cadena = "Ana lana ana "
#elimino espacios en blanco y pongo
cadena_sin_espacios = cadena.replace(' ', '').lower()
#acá podemos hacer un print si queremos chequear cómo quedó con print(cadena_sin_espacios)
if cadena_sin_espacios == cadena_sin_espacios[::-1]:
    print(f'La frase ingresada: "{cadena}", es un palíndromo')
else:
    print(f'La frase ingresada: "{cadena}", no es un palíndromo')
