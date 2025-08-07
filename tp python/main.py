# eco_soluciones_optimo.py

def mostrar_lineas_ing(valor):

    numero1al4 = {"1","2","3","4"}
    valor = input("te ofrecemos diferentes recomendaciones según lo que desees hacer:\n1 Si desea conocer sobre Herramientas\n2 si desea conocer sobre metodos\n3 si desea conocer sobre estandares\n4 si desea conocer sobre patrones" )
    while valor not in numero1al4:
        valor = input("Por favor ingrese un número válido del 1 al 4: ")

    #Esta vaina muestra un segmento de líneas de un archivo .txt según el valor asignado del 1 al 4.
    if valor == "1":
        inicio, fin = 0, 9
    elif valor == "2":
        inicio, fin = 13, 19
    elif valor == "3":
        inicio, fin = 23, 29
    elif valor == "4":
        inicio, fin = 33, 39  

    try:
        with open("INGENIERO.txt", 'r', encoding ='utf-8') as archivo:
            linea = archivo.readlines()
        
            fin = min(fin, len(linea)) # Asegura que no se pase del tamaño real del archivo osea la lineas

            for i in range(inicio, fin + 1):
                print(f"{linea[i]}")

    except FileNotFoundError:
        print("El archivo no fue encontrado.")

def mostrar_menu_principal():
    print("\n--- EcoSoluciones ---")
    print("1. Soy Ingeniero")
    print("2. Soy Desarrollador")
    print("3. Salir")

def obtener_problema():
    return input("\nDescribe brevemente tu problema técnico: ").lower()

def cargar_consejos(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"⚠️ No se encontró el archivo {archivo}.")
        return []

def encontrar_mejor_consejo(problema, consejos):
    mejor_consejo = ""
    max_coincidencias = 0

    for consejo in consejos:
        palabras_consejo = consejo.lower().split()
        coincidencias = sum(1 for palabra in palabras_consejo if palabra in problema)

        if coincidencias > max_coincidencias:
            max_coincidencias = coincidencias
            mejor_consejo = consejo

    return mejor_consejo if mejor_consejo else "No se encontró una solución específica, intenta reformular el problema."

def guardar_opinion(opinion):
    with open("RETROALIMENTACIÓN.txt", "a", encoding="utf-8") as f:
        f.write(opinion + "\n")
    print("✅ ¡Gracias por tu opinión!")

def ejecutar_aplicacion():
    while True:
        mostrar_menu_principal()
        opcion = input("Selecciona una de las opciones: ")

        if opcion == "1":
            profesion = "Ingeniero"
            archivo = "INGENIERO.txt"
        elif opcion == "2":
            profesion = "Desarrollador"
            archivo = "DESARROLLADOR.txt"
        elif opcion == "3":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intenta nuevamente.")
            continue

        problema = obtener_problema()
        consejos = cargar_consejos(archivo)
        mejor_consejo = encontrar_mejor_consejo(problema, consejos)

        print(f"\n✅ Solución recomendada:\n{mejor_consejo}")
        opinion = input("\n¿Te pareció útil la solución? Deja tu opinión: ")
        guardar_opinion(f"{profesion} - {problema} - Consejo: {mejor_consejo} - Opinión: {opinion}")

if __name__ == "__main__":

    ejecutar_aplicacion()
