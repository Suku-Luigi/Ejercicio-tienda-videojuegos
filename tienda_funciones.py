# funcion para mostrar el catalogo
def mostrar_catalogo(catalogo):
    print("\n--- CATALOGO GAMEZONE ---")
    print("Codigo | Videojuego | Precio | Existencia")
    # ciclo para recorrer el catalogo
    for producto in catalogo:
        print(f"{producto['codigo']} | {producto['nombre']} | ${producto['precio']:.2f} | {producto['existencia']}")

# funcion para buscar un producto por su codigo
def buscar_producto(catalogo, codigo):
    # ciclo para buscar el codigo
    for producto in catalogo:
        if producto['codigo'] == codigo:
            return producto
    # si termina el ciclo y no lo encuentra devuelve 0
    return 0

# funcion para validar si hay existencia
def hay_existencia(existencia, cantidad):
    # valida que la cantidad sea mayor a 0 y menor o igual a la existencia
    if cantidad > 0 and existencia >= cantidad:
        return 1 # devuelve 1
    else:
        return 0 # devuelve 0

# funcion para calcular el importe
def calcular_importe(precio, cantidad):
    return precio * cantidad

# funcion para calcular el total
def calcular_total(subtotal, descuento=0.0, impuesto=0.16):
    # resta el descuento al subtotal
    subtotal_con_descuento = subtotal - (subtotal * descuento)
    # calcula el impuesto y lo suma
    total = subtotal_con_descuento + (subtotal_con_descuento * impuesto)
    # redondea a 2 decimales
    return round(total, 2)

# funcion para actualizar la existencia
def actualizar_existencia(existencia, cantidad):
    return existencia - cantidad
