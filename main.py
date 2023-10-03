print(f"\t\t\t\033[4;1m"+"PROGRAMA TELEGRAMA\n"+"\033[0;m")
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
print(frase)
larga = 0
corto = 0
longi_frase = (len(frase))
for palabra in frase:
    if palabra > 5:
        larga = larga + frase
    else:
        corto = corto + frase
print(frase)
print(longi_frase)
#print("La cadena contiene"+ long_frase + "palabras de las cuales" )#larga +  "tienen más de 5 letras.")
#print("Por tanto, al precio de 0.25€/palabra tenemos "5" y a 0.50€/palabra hay otras 4.")
