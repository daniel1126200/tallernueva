agenda = {}

while True:
    print("Opciones:")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Actualizar contacto")
    print("4. Consultar contacto")
    print("0. Salir")
    
    opcion = input("Elija una opción: ")
    
    #agregar contcto
    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")
        agenda[nombre] = telefono
        print(f"Contacto {nombre} agregado a la agenda.")
    
    #eliminar contato
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
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
    
    elif opcion == "0":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")