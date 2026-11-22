import tienda_funciones

def main():
    # catalogo inicial con los juegos solicitados, maximo 9 unidades
    catalogo = [
        {
            "codigo": "G001",
            "nombre": "God of War Ragnarok",
            "precio": 1299.00,
            "existencia": 5
        },
        {
            "codigo": "G002",
            "nombre": "God of War (2018)",
            "precio": 599.00,
            "existencia": 8
        },
        {
            "codigo": "G003",
            "nombre": "Resident Evil 4 Remake",
            "precio": 899.00,
            "existencia": 7
        },
        {
            "codigo": "G004",
            "nombre": "Devil May Cry 5",
            "precio": 499.00,
            "existencia": 9
        },
        {
            "codigo": "G005",
            "nombre": "Mario Bros Yoshi's Island",
            "precio": 799.00,
            "existencia": 6
        },
        {
            "codigo": "G006",
            "nombre": "Poppy Playtime 5",
            "precio": 199.00,
            "existencia": 9
        }
    ]
    
    # variables locales para el carrito y el total
    carrito = []
    subtotal = 0.0
    
    # variable de control 1 para continuar
    comprando = 1
    
    print("Bienvenido a GameZone!")
    
    # ciclo principal
    while comprando == 1:
        tienda_funciones.mostrar_catalogo(catalogo)
        codigo = input("\nIngrese el codigo del videojuego (o escriba SALIR para terminar): ")
        
        # validacion de salida
        if codigo == "SALIR" or codigo == "salir":
            comprando = 0
        else:
            # busca el producto
            producto = tienda_funciones.buscar_producto(catalogo, codigo)
            
            # validacion si el producto no existe
            if producto == 0:
                print("Error: El codigo ingresado no existe. Intente de nuevo.")
            else:
                cantidad = int(input("Ingrese la cantidad a comprar: "))
                
                # valida la existencia
                if tienda_funciones.hay_existencia(producto['existencia'], cantidad) == 1:
                    # calcula el importe
                    importe = tienda_funciones.calcular_importe(producto['precio'], cantidad)
                    
                    # agrega al carrito
                    linea_carrito = {"nombre": producto['nombre'], "cantidad": cantidad, "importe": importe}
                    carrito.append(linea_carrito)
                    
                    # actualiza el inventario
                    producto['existencia'] = tienda_funciones.actualizar_existencia(producto['existencia'], cantidad)
                    
                    # acumula el subtotal
                    subtotal = subtotal + importe
                    print(f"Agregado! {cantidad} x {producto['nombre']} = ${importe:.2f}")
                else:
                    print(f"Error: No hay existencia suficiente o cantidad invalida. Disponibles: {producto['existencia']}")

    # fin de la compra
    print("\n--- RESUMEN DE COMPRA ---")
    if len(carrito) == 0:
        print("No se agregaron productos al carrito.")
    else:
        # ciclo para mostrar el carrito
        for item in carrito:
            print(f"{item['cantidad']} x {item['nombre']} | Importe: ${item['importe']:.2f}")
            
        print(f"\nSubtotal: ${subtotal:.2f}")
        
        # variable descuento
        descuento_aplicar = 0.0
        
        # aplica el 10 por ciento si el subtotal es mayor o igual a 1000
        if subtotal >= 1000.00:
            descuento_aplicar = 0.10
            print(f"Descuento aplicado (10%): -${subtotal * 0.10:.2f}")
        else:
            print("Descuento aplicado (0%): $0.00")
            
        # Calculamos el subtotal con el descuento del 10% ya aplicado
        subtotal_desc = subtotal - (subtotal * descuento_aplicar)
        
        # --- RETO EXTRA: CUPON GAME50 ---
        print(f"\nSubtotal a pagar antes de impuestos: ${subtotal_desc:.2f}")
        tiene_cupon = input("Tienes un cupon de descuento GAME50? (S/N): ")
        
        if tiene_cupon == "S" or tiene_cupon == "s":
            codigo_cupon = input("Ingresa el codigo del cupon: ")
            if codigo_cupon == "GAME50":
                subtotal_desc = subtotal_desc - 50.00
                print("Cupon GAME50 aplicado! Se descontaron $50.00")
            else:
                print("Cupon invalido. No se aplico descuento.")
        # -------------------------------
        
        # Llamada a la funcion usando argumentos con nombre
        total_final = tienda_funciones.calcular_total(subtotal_desc, descuento=0.0)
        
        # calculo del impuesto para mostrarlo
        impuesto_calculado = subtotal_desc * 0.16
        print(f"IVA (16%): ${impuesto_calculado:.2f}")
        print(f"TOTAL A PAGAR: ${total_final:.2f}")
        
    # muestra inventario final
    print("\n--- INVENTARIO RESTANTE ---")
    for producto in catalogo:
        print(f"{producto['nombre']}: {producto['existencia']} unidades")

# llama a la funcion principal
main()
