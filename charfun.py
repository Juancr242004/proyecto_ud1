def esPalindromo(cadena):
    # limpiar la cadena
    cadena = ''.join(c for c in cadena if c.isalnum()).lower()
    # Comprobar si la cadena es plindromo
    if cadena == cadena[::-1]:
        return "La frase SÍ es un palíndromo"
    else:
        return "La frase NO es un palíndromo"
