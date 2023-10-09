#puntuable 3 ...en proceso
#UIT-6.1

print(f"\t\t\t\033[4;1m" + "PROGRAMA OPTIMIZACIÓN TELEGRAMA\n" + "\033[0;m")


# print("Cadena recibida: " + args[0])
def menu_op():
    print("Menu de opciones")
    print("================")

    opciones = {
           '1': ('Opción 1', normal),
           '2': ('Opción 2', pre_redu),
           '3': ('Opción 3', morse),
           '4': ('Salir', salir)
       }
def normal():
    print("precio normal")
def pre_redu():
    print("precio reducido")
def morse():
    print("codigo morse")
def salir():
    print('Saliendo')

print(menu_op)
