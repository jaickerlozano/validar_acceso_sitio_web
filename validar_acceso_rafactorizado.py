'''Supongamos que eres un administrador de sistemas y necesitas validar el acceso de los usuarios 
a un sitio web. Crea un script que verifique si el nombre de usuario y la contraseña ingresados son 
correctos y permita el acceso solo si ambos son correctos.'''

import json

def comprobar_nombre_contrasena(user_name, password, lista_usuarios_contrasenas):
    '''Esta función comprueba si el nombre de usuario y la contraseña son
    correctos y devuelve un valor boolean'''

    try:
        for user, key in lista_usuarios_contrasenas.items():
            if user == user_name and key == password:
                return True
        return False
    
    # En caso que no exista diccionarios en la lista
    except AttributeError:
        print("Falla de conexión con servidores. Intente más tarde.")
        return False


def cargar_nombres_contrasenas():
    '''Esta función carga los nombres y contraseñas guardados
    en un archivo .json'''
    
    try:
        with open('nombres_contrasenas.json', 'r') as file:
            nombres_contrasenas = json.load(file)
        # En caso que quiera una tuplas de tuplas ejecuto este código y quito el diccionario
        #nombres_contrasenas = tuple([tuple(nombres_contrasenas[i]) for i in range(len(nombres_contrasenas))])

        return dict(nombres_contrasenas)
    
    # En caso que no se encuentre el archivo 
    except FileNotFoundError:
        print(f"Error: El archivo 'nombres_contrasenas.json' no se encuentra.")

    # En caso que exista un error en la entrada del archivo
    except IOError:
        print("Error: Problema de entrada/salida al intentar leer el archivo.")

def pedir_datos_para_ingreso():
    '''Esta función pide el nombre de usuario y la contraseña del usuario'''
    
    while True:

        nombre = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        
        # Valida si el nombreo no está vacío
        if not nombre:
            print("Campo vacío. Intente nuevamente.")
        
        # Valida si el password no está vacío
        elif not password:
            print("Campo vacío. Intente nuevamente.")

        else:
            return nombre, password


# Ejemplo de uso

nombre_usuario, contrasena = pedir_datos_para_ingreso()

lista_usuarios_contrasenas = cargar_nombres_contrasenas()

if not lista_usuarios_contrasenas:
    print("No se puede proceder sin datos de usuario")

else:
    check_value = comprobar_nombre_contrasena(nombre_usuario, contrasena, lista_usuarios_contrasenas)
    if check_value:
        print(f"Acceso permitido. !Bienvenido {nombre_usuario}¡")
    else:
        print("Nombre de usuario y contraseña incorrectos.")
