print(f"\t\t\t\033[4;1m"+"PROGRAMA TELEGRAMA\n"+"\033[0;m")
frase = input("Teclea el mensaje: ")
print("Cadena tecleada: " + frase)
print("Mensaje a enviar: ")
if frase[-1] != ".":
    frase = frase + "."
fraseStop = frase.replace(".", " STOP") + "STOP"
print(fraseStop)

frase = frase.replace(".", "").replace(",", "")
frase = frase.split(" ")
print(frase)
larga = 0
corto = 0
longi_frase = (len(frase))
for palabra in frase:
    if len(palabra) > 5:
        larga =larga + 1
    else:
        corto = corto + 1

To_largo = larga*0.5
To_corto = corto*0.25
Total = To_corto+To_largo
print("La cadena contiene " + str(longi_frase) + " palabras de las cuales " + str(larga) + " tienen más de 5 letras.")
print("Por tanto, al precio de 0.25€/palabra tenemos "+str(corto)+" y a 0.50€/palabra hay otras "+str(larga)+".")
print("Total: "+str(Total)+"€")
