'''Supongamos que eres un administrador de sistemas y necesitas validar el acceso de los usuarios 
a un sitio web. Crea un script que verifique si el nombre de usuario y la contraseña ingresados son 
correctos y permita el acceso solo si ambos son correctos.'''

# --- Lista de usuarios y claves
nombres_contrasenas = [["juan123", "clave123"], ["ana456", "clave456"], ["pedro789", "clave789"]]

# --- Entrada de usuario y clave
usuario = input("Introduce tu nombre de usuario: ")
clave = input("Introduce tu contraseña: ")

# --- Recorremos la lista de usuarios y claves para verificar si las entradas coinciden con los de la lista
# La variable reiniciar, nos permitirá mantenernos en el bucle, y se reiniciará mientras no se ingrese el usuario y clave del 
# usuario que quiere ingresar. 
no_reiniciar = False
while no_reiniciar == False:
    # Iniciamos el recorrido del bucle pasando por cada usuario y clave
    for i in range(len(nombres_contrasenas)):
        nombre = nombres_contrasenas[i][0]
        password = nombres_contrasenas[i][1]
        # Verificamos que el usuario y la clave sean identicas a alguna de las guardadas en la lista
        if usuario == nombre and clave == password:
            print(f"Acceso permitido.¡Bienvenido {nombre}!")
            no_reiniciar = True # Con esta variable al ser verdad, rompemos la condición del while que nos mantiene en el bucle
        # En caso de no coindicar el usuario y clave con algunas de las guardadas, se vuelve a pedir el ingreso de ellos
        elif i == len(nombres_contrasenas)-1 and (usuario != nombre or clave != password) and no_reiniciar == False:
            print("Usuario o contraseña inválida. Por favor inténtelo nuevamente")
            usuario = input("Introduce tu usuario: ")
            clave = input("Introduce tu contraseña: ")


