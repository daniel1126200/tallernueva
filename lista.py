# Inicializa una lista vacía para representar la agenda
estudiante = [
    "danuel"
]

while True:
    print("Opciones:")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Actualizar contacto")
    print("4. Consultar contacto")
    
    opcion = input("Elija una opción para continuar: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")
        contacto = {"nombre": nombre, "telefono": telefono}
        estudiante.append(contacto)
        print(f"Contacto {nombre} agregado a la agenda.")
    
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        encontrado = False
        for contacto in estudiante:
            if contacto["nombre"] == nombre:
                estudiante.remove(contacto)
                encontrado = True
                print(f"Contacto {nombre} eliminado de la agenda.")
                break
        if not encontrado:
            print(f"El contacto {nombre} no existe en la agenda.")
    
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto cuyo número desea actualizar: ")
        encontrado = False
        for contacto in estudiante:
            if contacto["nombre"] == nombre:
                telefono = input("Ingrese el nuevo número de teléfono: ")
                contacto["telefono"] = telefono
                encontrado = True
                print(f"Número de {nombre} actualizado en la agenda.")
                break
        if not encontrado:
            print(f"El contacto {nombre} no existe en la agenda.")
    
    elif opcion == "4":
        nombre = input("Ingrese el nombre del contacto a consultar: ")
        encontrado = False
        for contacto in estudiante:
            if contacto["nombre"] == nombre:
                print(f"Teléfono de {nombre}: {contacto['telefono']}")
                encontrado = True
                break
        if not encontrado:
            print(f"El contacto {nombre} no existe en la agenda.")
        break
    
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")