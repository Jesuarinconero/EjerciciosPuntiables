print("\t\t\t\033[4;1m"+"PROGRAMA TELEGRAMA\n"+"\033[0;m")
frase = input("Teclea el mensaje: ")
print("Cadena tecleada: " + frase)
print("Mensaje a enviar: ")
if frase[-1] != ".":
    frase = frase + "."
fraseStop = frase.replace(".", " STOP") + "STOP"
print(fraseStop)
print(frase)
