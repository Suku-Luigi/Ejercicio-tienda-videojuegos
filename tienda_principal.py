import tienda_funciones

print("¡Bienvenido a la Tienda de Gameplays!\n")

# Variable de control
opcion = ""

# Ciclo del menú
while opcion != "5":
    print("\n--- MENÚ TIENDA ---")
    print("1. Agregar gameplay")
    print("2. Ver gameplays")
    print("3. Eliminar gameplay")
    print("4. Buscar gameplay")
    print("5. Salir")
    
    opcion = input("Elige una opción (1-5): ")
    
    if opcion == "1":
        titulo = input("Título del gameplay: ")
        creador = input("Nombre del creador: ")
        precio = float(input("Precio: "))
        # Llamada a la función del módulo
        tienda_funciones.agregar_gameplay(titulo, creador, precio)
        
    elif opcion == "2":
        # Llamada a la función del módulo
        tienda_funciones.ver_gameplays()
        
    elif opcion == "3":
        tienda_funciones.ver_gameplays()
        numero = int(input("Número de gameplay a eliminar: "))
        # Se resta 1 para ajustar al índice de la lista
        tienda_funciones.eliminar_gameplay(numero - 1)
        
    elif opcion == "4":
        titulo_buscar = input("Ingresa el título a buscar: ")
        # Llamada a la función del módulo
        tienda_funciones.buscar_gameplay(titulo_buscar)
        
    elif opcion == "5":
        print("Saliendo de la tienda...")
        
    else:
        print("Opción inválida. Intenta de nuevo.")

# Al salir del ciclo, se llama a la función para guardar el JSON
tienda_funciones.guardar_json()

print("Gracias por visitar la tienda.")