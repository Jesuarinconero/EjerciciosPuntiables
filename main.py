print("\t\t\t\033[4;1m"+"PROGRAMA TELEGRAMA\n"+"\033[0;m")
frase = input("Teclea el mensaje: ")
print("Cadena tecleada: " + frase)
print("Mensaje a enviar: ")
if frase[-1] != ".":
    frase = frase + "."
fraseStop = frase.replace(".", " STOP") + "STOP"
print(fraseStop)

frase = frase.replace(".", "")
print(frase)
frase = frase.split(" ")
for i in frase:
    long_frase = (len(frase))
    if long_frase>5:
        larga=+1
    else:
        corto=+1
print(frase)
