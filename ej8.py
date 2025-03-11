n = -2

def comprobar(n):
    if(n > 0):
        return "Es positivo"
    elif (n < 0):
        return "Es negativo"
    elif (n == 0):
        return "Es cero"

print(comprobar(n))

def comprobarPar(n):
    if(n % 2 == 0):
        return "Es par"
    else:
        return "Es impar"
    
print(comprobarPar(n))