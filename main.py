#puntuable 3 ...en proceso
#UIT-6.1

import sys

print(f"\t\t\t\033[4;1m" + "PROGRAMA OPTIMIZACIÓN TELEGRAMA\n" + "\033[0;m")

arg = sys.argv[1:]
arg = " ".join(arg)

print(f"Cadena recibida: {arg}")

def normal(arg):
    # Asignación de variables a 0 para que no coga unos valores erróneos residuales, variables que nos harán falta más adelante.
    larga = 0
    corto = 0

    frase = ""

    # Especificaremos que si el usuario no introduce ningún punto final lo pondrá el programa solo.
    if frase[-1] != ".":
        frase = frase + "."

    # Ahora indicamos que nos reemplace todos los puntos de la frase por STOPS.
    fraseStop = frase.replace(".", " STOP") + "STOP"
    print(fraseStop)

    # Ahora indicamos que nos quite todos los puntos, y por si el usuario pone comas también para que nos lo quite  en la frase anteriormente introducida.
    frase = frase.replace(".", "").replace(",", "")

    # Lo convertimos en una lista.
    frase = frase.split(" ")
    # Variable para saber cuantos elementos tiene la lista.
    lon_frase = (len(frase))

    """Bucle for para que nos baya recocrriendo en la lista frase los elementos que sean mayor a 5 caracteres,
    y nos lo asignen a la variable larga, si no por lo tanto sera menor a 5 caracteres y sera asignada a la variable corto.
    """
    for palabra in frase:
        if len(palabra) > 5:
            larga += 1
        else:
            corto += 1

    # Operaciones aritméticas para darnos el resultado de lo que costara enviar las palabras escritas.
    To_largo = larga * 0.5
    To_corto = corto * 0.25
    Total = To_corto + To_largo

    # Salida por pantalla de los resultados obtenidos, usando los f-Strings para un formateo sencillo de la cadena.
    print(f"\nLa cadena contiene  {lon_frase}  palabras de las cuales {larga} tienen más de 5 letras.")
    print(f"Por tanto, al precio de 0.25€/palabra tenemos {corto} y a 0.50€/palabra hay otras {larga}.")
    print(f"Total: {Total}€\n")

    print("Mensaje enviado: ")
    print(frase)
    print()
def pre_redu():
    frase = sys.argv[0]
    lon_frase = (len(frase))
    larga = 0
    corto = 0
    for palabra in frase:
        if len(palabra) > 5:
            larga += 1
        else:
            corto += 1
    print(f"\nLa cadena contiene  {lon_frase}  palabras de las cuales {larga} tienen más de 5 letras  pero se han recortado.")
def morse():
    print("codigo morse")


salir = False
opcion = 0
while not salir:
    print("\t\t\t\tMenú de Opciones")
    print("\t\t\t\t================")
    print("1) Envío con precio normal")
    print("2) Envío con precio reducido")
    print("3) Envío barato en código Morse")
    print("4) Salir")
    opcion = int(input("\t\tOpción: "))
    if opcion == 1:
        normal(arg)
    elif opcion == 2:
        pre_redu()
    elif opcion == 3:
        morse()
    elif opcion == 4:
        print("Saliendo del programa....")
        salir = True

    else:
        print("Introduce un número entre 1 y 4")
