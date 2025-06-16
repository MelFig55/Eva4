ListaReservas= {}

codigofr = "EstoyEnListaDeReserva"
stock = 20
def reservar_zapatillas():
    while True:
        nombre = input("Ingrese el nombre de la reserva: ")
        if not nombre:
            print("El nombre no puede estar vacio")
            continue
        break

    if nombre not in ListaReservas:
        codigo = input("Introduce el codigo sereto: ")
        if codigo == codigofr:
            ListaReservas[nombre] = 1
            global stock
            stock -= 1
            print(f"Reserva realizada a nombre de {nombre} !")
            return
        else:
            print("Contraseña incorrecta!")
    else:
        print("Usuario ya ha hecho una reserva, solo una reserva por usuario!")
    

def buscar_reserva():
    while True:
        nombre = input("Ingrese el nombre a buscar: ")
        if not nombre:
            print("El nombre no puede estar vacio")
            continue
        break
    if nombre in ListaReservas:
        if ListaReservas[nombre] == 1:
            print(f"Reserva a nombre de {nombre} encontrada!\nDesea pagar un adicional por la reserva VIP? esta permite tener una reserva de 2 pares de zapatillas.")
            while True:
                try:
                    yn = input("Y/N").capitalize()
                    if yn in ["Y", "N"]:
                        break
                    else:
                        print("Ingresa una opcion valida!")
                except:
                    print("Hubo un error...")
            if yn == "Y":
                print(f"Reserva VIP realizada al usuario {nombre} !")
                ListaReservas[nombre] = 2
                global stock 
                stock -= 1
        else:
            print(f"Reserva a nombre de  usuario VIP: {nombre} encontrada!")
    else:
        print("Nombre no encontrado!")

def salir():
    print("Saliendo...")

def cancelar_reserva():
    while True:
        nombre = input("Nombre a cancelar: ")
        if not nombre:
            print("El nombre no puede estar vacio")
            continue
        break
    if nombre in ListaReservas:
        global stock
        stock += ListaReservas[nombre] 
        del ListaReservas[nombre]
        print(f"Reserva a nombre de {nombre} realizada.")
    else:
        print("Nombre no encontrado.")

def menu():
    opcion = 0
    while opcion != 4:
        print("TOTEM AUTOATENCION RESERVA STRIKE\n1.Reservar zapatillas.\n2.Buscar zapatillas reservadas.\n3.Cancelar reserva de zapatillas.\n4.Salir.")
        while True:
            try:
                opcion = int(input(""))
                if opcion >= 1 and opcion <= 4:
                    break
                else:
                    print("Introduce una opcion valida")
            except:
                print("Hubo un error, intentalo denuevo.")
    
        if opcion == 1:
         reservar_zapatillas()
        elif opcion == 2:
         buscar_reserva()
        elif opcion == 3:
         cancelar_reserva()
        elif opcion == 4:
            salir()

menu()
