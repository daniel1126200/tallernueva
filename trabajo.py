agenda = {
    
    "contacto":{
    "nombre":"daniel",
    "numero":22333,
    "email":"daniel@.com"
    },
    
    "contacto1":{
        "nombre": "juan",
        "numero": 45678,
        "email": "juan@.com"
    },
    
    "contacto2":{
        "nombre":"felipe",
        "numero": 21379,
        "email":"felipe@.com"
    },
    
    "contacto3":{
        "nombre":"brayan",
        "numero":28383,
        "email":"brayan@.com"
    }
    
}

while True:
    print("Opciones:")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Actualizar contacto")
    print("4. Consultar contacto")
    
    opcion = input("Elija una opción: ")
    
    #agregar contcto
    if opcion == "1":
        nombre = input("daniel: ")
        telefono = input("22333: ")
        email = input("daniel@.com")
        agenda["contacto"] = telefono
        print(f"Contacto {nombre} agregado a la agenda.")
    
    #eliminar contato
    elif opcion == "2":
        nombre = input("contacto: ")
        if nombre in agenda:
            del agenda[nombre]
            print(f"Contacto {nombre} eliminado de la agenda.")
        else:
            print(f"El contacto {nombre} no existe en la agenda.")
    
    #Actualizar contacto
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto cuyo número desea actualizar: ")
        if nombre in agenda:
            telefono = input("Ingrese el nuevo número de teléfono: ")
            agenda[nombre] = telefono
            print(f"Número de {nombre} actualizado en la agenda.")
        else:
            print(f"El contacto {nombre} no existe en la agenda.")
    
    #consultar contato
    elif opcion == "4":
        nombre = input("Ingrese el nombre del contacto a consultar: ")
        if nombre in agenda:
            print(f"Teléfono de {nombre}: {agenda[nombre]}")
        else:
            print(f"El contacto {nombre} no existe en la agenda.")
            break
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")    
    