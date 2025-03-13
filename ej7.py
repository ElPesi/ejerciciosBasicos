def ingresoDatos():
    
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    ciudad = input("Ingresa tu ciudad de residencia: ")

    año_actual = 2025  
    cumpleaños = año_actual - edad
    print(f"Hola, {nombre}! Aquí está tu información:")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")
    print(f"Año de nacimiento: {cumpleaños}")

    if edad > 18:
        print("Eres mayor de 18 años.")
    else:
        print("Eres menor de 18 años.")
    
    
    if edad % 5 == 0:
        print("Tu edad es un múltiplo de 5.")
    else:
        print("Tu edad no es un múltiplo de 5.")


ingresoDatos()
