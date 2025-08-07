# eco_soluciones_optimo.py

def mostrar_lineas_ing():

    numero1al4 = {"1","2","3","4"}

    valor = input(
        "Te ofrecemos diferentes recomendaciones según lo que desees hacer:\n"
        "1️⃣  Si desea conocer sobre Herramientas\n"
        "2️⃣  Si desea conocer sobre Métodos\n"
        "3️⃣  Si desea conocer sobre Estándares\n"
        "4️⃣  Si desea conocer sobre Patrones\n"
        "Ingrese una opción (1-4): "
    )

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
                print(linea[i], end='')

    except FileNotFoundError:
        print("El archivo no fue encontrado.")

def mostrar_menu_principal():
    print("\n" + "="*40)
    print("      🌿 Bienvenido a EcoSoluciones 🌿")
    print("="*40)
    print(r"""
 _____                    _            _                       
|  ___|                  | |          (_)                      
| |__  ___ ___  ___  ___ | |_   _  ___ _  ___  _ __   ___  ___ 
|  __|/ __/ _ \/ __|/ _ \| | | | |/ __| |/ _ \| '_ \ / _ \/ __|
| |__| (_| (_) \__ \ (_) | | |_| | (__| | (_) | | | |  __/\__ \
\____/\___\___/|___/\___/|_|\__,_|\___|_|\___/|_| |_|\___||___/
    """)
    print("1️⃣  Soy Ingeniero")
    print("2️⃣  Soy Desarrollador")
    print("3️⃣  Salir")
    print("="*40)

def obtener_problema():
    return input("\nDescribe brevemente tu problema técnico: ").lower()

def cargar_consejos(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"⚠️ No se encontró el archivo {archivo}.")
        return []

import string

def limpiar_texto(texto):
    return texto.translate(str.maketrans('', '', string.punctuation)).lower()

def encontrar_mejor_consejo(problema, consejos):
    problema = limpiar_texto(problema)
    palabras_problema = problema.split()

    mejor_consejo = ""
    max_coincidencias = 0

    for consejo in consejos:
        consejo_limpio = limpiar_texto(consejo)
        palabras_consejo = consejo_limpio.split()

        coincidencias = sum(
            1 for palabra in palabras_consejo
            if palabra in palabras_problema or any(p in palabra for p in palabras_problema)
        )

        if coincidencias > max_coincidencias:
            max_coincidencias = coincidencias
            mejor_consejo = consejo

    return mejor_consejo if mejor_consejo else "No se encontró una solución específica, intenta reformular el problema."

def guardar_opinion(opinion):
    with open("RETROALIMENTACIÓN.txt", "a", encoding="utf-8") as f:
        f.write(opinion + "\n")
    input("✅ ¡Gracias por tu opinión!")

#lo que se ejecuta primero
def ejecutar_aplicacion():
    while True:
        mostrar_menu_principal()
        opcion = input("Selecciona una de las opciones: ")

        if opcion == "1":
            profesion = "Ingeniero"

            mostrar_lineas_ing()
            opinion = input("\n¿Te pareció útil la solución? Deja tu opinión.\nSi no quieres dejar una escribe 'no'\n")
            
            if opinion != "no":
                guardar_opinion(f"{profesion} - Opinión: {opinion}")
            else:
                input("✅ Tu opinion no se guardo")

        elif opcion == "2":
            profesion = "Desarrollador"
            archivo = "DESARROLLADOR.txt"

            problema = obtener_problema()
            consejos = cargar_consejos(archivo)
            mejor_consejo = encontrar_mejor_consejo(problema, consejos)

            print(f"\n✅ Solución recomendada:\n{mejor_consejo}")
            opinion = input("\n¿Te pareció útil la solución? Deja tu opinión.\nSi no quieres dejar una escribe 'no'\n")

            if opinion != "no":
                guardar_opinion(f"{profesion} - {problema} - Consejo: {mejor_consejo} - Opinión: {opinion}")
            else:
                input("✅ Tu opinion no se guardo")

        elif opcion == "3":
            despedida()
            break
        else:
            print("❌ Opción inválida. Intenta nuevamente.")
            continue

def despedida():
    print("\n" + "*"*45)
    print("🌟 Gracias por usar EcoSoluciones 🌟")
    print("*"*45)
    print(r"""

  ***     ***
*******  *******
*****************
*****************
 ***************
  *************
    *********
      *****
       ***
        *

    """)
    print("👋 ¡Hasta la próxima! Que tengas un gran día.")
    print("*"*45 + "\n")

if __name__ == "__main__":
    ejecutar_aplicacion()