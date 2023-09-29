print("\t\t\tPROGRAMA TELEGRAMA\n")
frase = input("Teclea el mensaje: ")
print("Cadena tecleada: " + frase)
print("Mensaje a enviar: ")
fraseStop = frase.replace("."," STOP")+ "STOP"
print(fraseStop)