import json

# Lista global con 2 gameplays de ejemplo (diccionarios en una sola línea)
lista_gameplays = [{"titulo": "Speedrun Minecraft", "creador": "Dream", "precio": 10.50}, {"titulo": "Top 10 Jugadas", "creador": "GamerPro", "precio": 5.00}]

# Función para agregar un gameplay
def agregar_gameplay(titulo, creador, precio):
    # Se crea el diccionario en una sola línea
    nuevo_gameplay = {"titulo": titulo, "creador": creador, "precio": precio}
    # Se agrega a la lista global
    lista_gameplays.append(nuevo_gameplay)
    print("¡Gameplay agregado con éxito!")

# Función para mostrar todos los gameplays
def ver_gameplays():
    print("\n--- TIENDA DE GAMEPLAYS ---")
    # Condicional para verificar si está vacía
    if len(lista_gameplays) == 0:
        print("No hay gameplays disponibles.")
    else:
        # Ciclo para recorrer la lista
        for i in range(len(lista_gameplays)):
            print(f"{i + 1}. {lista_gameplays[i]['titulo']} | Creador: {lista_gameplays[i]['creador']} | Precio: ${lista_gameplays[i]['precio']:.2f}")

# Función para eliminar un gameplay
def eliminar_gameplay(indice):
    # Condicional para verificar que el índice exista
    if indice >= 0 and indice < len(lista_gameplays):
        # Se elimina usando pop()
        lista_gameplays.pop(indice)
        print("¡Gameplay eliminado con éxito!")
    else:
        print("Número inválido.")

# Función para buscar un gameplay por título
def buscar_gameplay(titulo_buscar):
    print("\n--- RESULTADO DE BÚSQUEDA ---")
    encontrado = 0
    # Ciclo para buscar
    for gp in lista_gameplays:
        # Condicional comparando en minúsculas
        if gp["titulo"].lower() == titulo_buscar.lower():
            print(f"Encontrado: {gp['titulo']} - {gp['creador']} (${gp['precio']})")
            encontrado = 1
            
    # Condicional si no se encontró
    if encontrado == 0:
        print("Gameplay no encontrado.")

# Función para guardar los datos en el archivo JSON
def guardar_json():
    datos_guardar = {}
    # Ciclo para armar el diccionario usando el título como clave
    for gp in lista_gameplays:
        datos_guardar[gp["titulo"]] = gp["precio"]
        
    # Se abre el archivo y se guarda con json.dump
    with open("gameplays.json", "w") as f:
        json.dump(datos_guardar, f)
    print("Datos guardados en 'gameplays.json'.")