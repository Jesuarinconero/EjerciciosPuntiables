# Asignación de variables a 0 para que no coga unos valores erróneos residuales, variables que nos harán falta más adelante.
larga = 0
corto = 0

print(f"\t\t\t\033[4;1m"+"PROGRAMA TELEGRAMA\n"+"\033[0;m")

# El usuario deberá introducir la frase que desea enviar.
frase = input("Teclea el mensaje: ")
print("Cadena tecleada: " + frase)
print("Mensaje a enviar: ")

# Especificaremos que si el usuario no introduce ningún punto final lo pondrá el programa solo.
if frase[-1] != ".":
    frase = frase + "."
    
# Ahora indicamos que nos reemplace todos los puntos de la frase por STOPS.
fraseStop = frase.replace(".", " STOP") + "STOP"
print(fraseStop)

# Ahora indicamos que nos quite todos los puntos, y por si el usuario pone comas también para que nos lo quite  en la frase anteriormente introducida.
frase = frase.replace(".", "").replace(",", "")

# Lo convertimos en una lista.
frase = frase.split(" ")
# Variable para saber cuantos elementos tiene la la lista.
lon_frase = (len(frase))

"""Bucle for para que nos baya recocrriendo en la lista frase los elementos que sean mayor a 5 caracteres,
y nos lo asignen a la variable larga, si no por lo tanto sera menor a 5 caracteres y sera asignada a la variable corto.
"""
for palabra in frase:
    if len(palabra) > 5:
        larga += 1
    else:
        corto +=  1
        
# Operaciones aritméticas para darnos el resultado de lo que costara enviar las palabras escritas.
To_largo = larga*0.5
To_corto = corto*0.25
Total = To_corto+To_largo
# Salida por pantalla de los resultados obtenidos.
print("La cadena contiene " + str(lon_frase) + " palabras de las cuales " + str(larga) + " tienen más de 5 letras.")
print("Por tanto, al precio de 0.25€/palabra tenemos "+str(corto)+" y a 0.50€/palabra hay otras "+str(larga)+".")
print("Total: "+str(Total)+"€")
