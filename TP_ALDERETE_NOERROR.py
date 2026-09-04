nombre_usuario = input("¿Cual es su nombre?: ")
while not nombre_usuario.isalpha():
    nombre_usuario = input("Por favor coloque un nombre valido: ")

cant_productos = input("¿Cuantos productos estas comprando?: ")
while not cant_productos.isdigit():
    cant_productos = input("Por favor coloque un numero valido: ")
cant_productos = int(cant_productos)
while cant_productos <= 0:
    cant_productos = input("Por favor coloque un numero mayor a 0: ")
    while not cant_productos.isdigit():
        cant_productos = input("Por favor coloque un numero mayor a 0: ")
    cant_productos = int(cant_productos)


total_sin_descuentos = 0
total_con_descuentos = 0
ahorro_total = 0


print("----------------------------")
print(f"Cliente: {nombre_usuario}")
print(f"Cantidad de productos: {cant_productos}")

for i in range(1, cant_productos + 1):
    precio = input(f"Producto {i} - Precio: ")
    while not precio.isdigit():
        precio = input("Por favor coloque un precio valido: ")
    precio = int(precio)
    total_sin_descuentos = total_sin_descuentos + precio

    descuento = input("Descuento (S/N): ")

    while descuento.lower() != "s" and descuento.lower() != "n":
        descuento = input("Por favor coloque S o N: ")
    if descuento.lower() == "s":
        precio_con_descuento = precio * 0.90
    else:
        precio_con_descuento = precio

    total_con_descuentos = total_con_descuentos + precio_con_descuento

    print(f"Producto {i} - Precio: {precio} Descuento (S/N): {descuento}")

ahorro_total = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cant_productos
print("----------------------------")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
print("----------------------------")

print("EJERCICIO N2")

usuario_correcto="alumno"
clave_correcta="python123"
usuario_intento=" "
clave_intento=" "
nueva_clave=" "
confirmacion_clave=" "

print("Bienvenido al campus UTN")

usuario_intento=input("Por favor coloque su usuario: ")
clave_intento=input("Por favor coloque su clave: ")

for i in range(3):
    if usuario_correcto==usuario_intento and clave_correcta==clave_intento:
        print("ACCESO PERMITIDO")
        break
    print("Credenciales incorrectas")
    if i<2:
        usuario_intento=input("Coloque su usuario: ")
        clave_intento=input("Coloque su clave: ")
else:
    print("USUARIO BLOQUEADO")

if usuario_correcto==usuario_intento and clave_correcta==clave_intento:
    eleccion_usuario=" "
    while eleccion_usuario!=4:
        print("Menu interactivo, escoja su opcion")
        print("1. Ver estado inscripcion  2. Cambiar clave  3. Mostrar mensaje motivacional  4. Salir")
        eleccion_usuario=input("Escriba su eleccion: ")

        while not eleccion_usuario.isdigit():
            print("Error: ingrese un número válido.")
            eleccion_usuario=input("Escriba su eleccion: ")

        eleccion_usuario=int(eleccion_usuario)

        while eleccion_usuario<1 or eleccion_usuario>4:
            print("Error: opción fuera de rango.")
            eleccion_usuario=input("Escriba su eleccion: ")

            while not eleccion_usuario.isdigit():
                print("Error: ingrese un número válido.")
                eleccion_usuario=input("Escriba su eleccion: ")
            eleccion_usuario=int(eleccion_usuario)
        if eleccion_usuario==1:
            print("INSCRIPTO")
        elif eleccion_usuario==2:
            print("Cambio de contraseña")
            nueva_clave=input("Escriba su nueva clave: ")
            while len(nueva_clave)<6:
                print("Error: mínimo 6 caracteres.")
                nueva_clave=input("Escriba su nueva clave: ")
            confirmacion_clave=input("Confirme su clave: ")
            if nueva_clave!=confirmacion_clave:
                print("Sus claves no coinciden")
            else:
                print("Contraseña cambiada con éxito")
                clave_correcta=nueva_clave
        elif eleccion_usuario==3:
            print("EL ESFUERZO DE HOY ES EL EXITO DE MAÑANA")
        elif eleccion_usuario==4:
            print("Sesion cerrada")

print("EJERCICIO N3")

lunes1=""
lunes2=""
lunes3=""
lunes4=""
martes1=""
martes2=""
martes3=""

nombre_operador=input("¿Cual es el nombre del operador?: ")
while not nombre_operador.isalpha():
    nombre_operador=input("Por favor coloque un nombre valido: ")

eleccion_usuario=0

while eleccion_usuario!=5:
    print("----------------------------")
    print("MENU")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del dia")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    eleccion_usuario=input("Escoja una opcion: ")

    while not eleccion_usuario.isdigit():
        eleccion_usuario=input("Por favor coloque un numero valido: ")

    eleccion_usuario=int(eleccion_usuario)

    while eleccion_usuario<1 or eleccion_usuario>5:
        eleccion_usuario=input("Por favor coloque una opcion entre 1 y 5: ")

        while not eleccion_usuario.isdigit():
            eleccion_usuario=input("Por favor coloque un numero valido: ")

        eleccion_usuario=int(eleccion_usuario)

    if eleccion_usuario==1:
        dia=input("Elija el dia: 1=Lunes 2=Martes: ")

        while not dia.isdigit():
            dia=input("Por favor coloque 1 o 2: ")

        dia=int(dia)

        while dia<1 or dia>2:
            dia=input("Por favor coloque 1 o 2: ")

            while not dia.isdigit():
                dia=input("Por favor coloque 1 o 2: ")

            dia=int(dia)

        nombre_paciente=input("¿Cual es el nombre del paciente?: ")

        while not nombre_paciente.isalpha():
            nombre_paciente=input("Por favor coloque un nombre valido: ")

        if dia==1:
            if nombre_paciente==lunes1 or nombre_paciente==lunes2 or nombre_paciente==lunes3 or nombre_paciente==lunes4:
                print("El paciente ya tiene un turno ese dia")
            elif lunes1=="":
                lunes1=nombre_paciente
                print("Turno reservado")
            elif lunes2=="":
                lunes2=nombre_paciente
                print("Turno reservado")
            elif lunes3=="":
                lunes3=nombre_paciente
                print("Turno reservado")
            elif lunes4=="":
                lunes4=nombre_paciente
                print("Turno reservado")
            else:
                print("No hay turnos disponibles")

        else:
            if nombre_paciente==martes1 or nombre_paciente==martes2 or nombre_paciente==martes3:
                print("El paciente ya tiene un turno ese dia")
            elif martes1=="":
                martes1=nombre_paciente
                print("Turno reservado")
            elif martes2=="":
                martes2=nombre_paciente
                print("Turno reservado")
            elif martes3=="":
                martes3=nombre_paciente
                print("Turno reservado")
            else:
                print("No hay turnos disponibles")

    elif eleccion_usuario==2:
        dia=input("Elija el dia: 1=Lunes 2=Martes: ")

        while not dia.isdigit():
            dia=input("Por favor coloque 1 o 2: ")

        dia=int(dia)

        while dia<1 or dia>2:
            dia=input("Por favor coloque 1 o 2: ")

            while not dia.isdigit():
                dia=input("Por favor coloque 1 o 2: ")

            dia=int(dia)

        nombre_paciente=input("¿Cual es el nombre del paciente?: ")

        while not nombre_paciente.isalpha():
            nombre_paciente=input("Por favor coloque un nombre valido: ")

        if dia==1:
            if lunes1==nombre_paciente:
                lunes1=""
                print("Turno cancelado")
            elif lunes2==nombre_paciente:
                lunes2=""
                print("Turno cancelado")
            elif lunes3==nombre_paciente:
                lunes3=""
                print("Turno cancelado")
            elif lunes4==nombre_paciente:
                lunes4=""
                print("Turno cancelado")
            else:
                print("No se encontro el turno")
        else:
            if martes1==nombre_paciente:
                martes1=""
                print("Turno cancelado")
            elif martes2==nombre_paciente:
                martes2=""
                print("Turno cancelado")
            elif martes3==nombre_paciente:
                martes3=""
                print("Turno cancelado")
            else:
                print("No se encontro el turno")

    elif eleccion_usuario==3:
        dia=input("Elija el dia: 1=Lunes 2=Martes: ")

        while not dia.isdigit():
            dia=input("Por favor coloque 1 o 2: ")

        dia=int(dia)

        while dia<1 or dia>2:
            dia=input("Por favor coloque 1 o 2: ")

            while not dia.isdigit():
                dia=input("Por favor coloque 1 o 2: ")

            dia=int(dia)

        if dia==1:
            print("Lunes")
            print("Turno 1:",lunes1 if lunes1!="" else "(libre)")
            print("Turno 2:",lunes2 if lunes2!="" else "(libre)")
            print("Turno 3:",lunes3 if lunes3!="" else "(libre)")
            print("Turno 4:",lunes4 if lunes4!="" else "(libre)")
        else:
            print("Martes")
            print("Turno 1:",martes1 if martes1!="" else "(libre)")
            print("Turno 2:",martes2 if martes2!="" else "(libre)")
            print("Turno 3:",martes3 if martes3!="" else "(libre)")

    elif eleccion_usuario==4:
        ocupados_lunes=0
        ocupados_martes=0

        if lunes1!="":
            ocupados_lunes=ocupados_lunes+1
        if lunes2!="":
            ocupados_lunes=ocupados_lunes+1
        if lunes3!="":
            ocupados_lunes=ocupados_lunes+1
        if lunes4!="":
            ocupados_lunes=ocupados_lunes+1

        if martes1!="":
            ocupados_martes=ocupados_martes+1
        if martes2!="":
            ocupados_martes=ocupados_martes+1
        if martes3!="":
            ocupados_martes=ocupados_martes+1

        print("Lunes: ",ocupados_lunes,"ocupados y",4-ocupados_lunes,"disponibles")
        print("Martes: ",ocupados_martes,"ocupados y",3-ocupados_martes,"disponibles")

        if ocupados_lunes>ocupados_martes:
            print("El dia con mas turnos es Lunes")
        elif ocupados_martes>ocupados_lunes:
            print("El dia con mas turnos es Martes")
        else:
            print("Hay empate entre Lunes y Martes")

print("Sistema cerrado")

print("EJERCICIO N4")

energia=100
tiempo=12
cerraduras_abiertas=0
alarma=False
codigo_parcial=""

nombre_agente=input("¿Cual es el nombre del agente?: ")

while not nombre_agente.isalpha():
    nombre_agente=input("Por favor coloque un nombre valido: ")

racha_forzar=0

while energia>0 and tiempo>0 and cerraduras_abiertas<3 and alarma==False:
    print("----------------------------")
    print("Agente:",nombre_agente)
    print("Energia:",energia)
    print("Tiempo:",tiempo)
    print("Cerraduras abiertas:",cerraduras_abiertas)
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion=input("Escoja una opcion: ")

    while not opcion.isdigit():
        opcion=input("Por favor coloque un numero valido: ")

    opcion=int(opcion)

    while opcion<1 or opcion>3:
        opcion=input("Por favor coloque una opcion entre 1 y 3: ")

        while not opcion.isdigit():
            opcion=input("Por favor coloque un numero valido: ")

        opcion=int(opcion)

    if opcion==1:
        energia=energia-20
        tiempo=tiempo-2
        racha_forzar=racha_forzar+1

        if racha_forzar==3:
            print("La cerradura se trabo")
            alarma=True
        elif energia<40:
            riesgo=input("Riesgo de alarma. Elija un numero del 1 al 3: ")

            while not riesgo.isdigit():
                riesgo=input("Por favor coloque un numero del 1 al 3: ")

            riesgo=int(riesgo)

            while riesgo<1 or riesgo>3:
                riesgo=input("Por favor coloque un numero del 1 al 3: ")

                while not riesgo.isdigit():
                    riesgo=input("Por favor coloque un numero del 1 al 3: ")

                riesgo=int(riesgo)

            if riesgo==3:
                alarma=True
                print("Se activo la alarma")
            else:
                cerraduras_abiertas=cerraduras_abiertas+1
        else:
            cerraduras_abiertas=cerraduras_abiertas+1

    elif opcion==2:
        energia=energia-10
        tiempo=tiempo-3
        racha_forzar=0

        print("Hackeando panel...")

        for i in range(4):
            codigo_parcial=codigo_parcial+"A"
            print("Progreso:",codigo_parcial)

        if len(codigo_parcial)>=8 and cerraduras_abiertas<3:
            cerraduras_abiertas=cerraduras_abiertas+1
            print("Se abrio una cerradura")

    elif opcion==3:
        energia=energia+15

        if energia>100:
            energia=100

        tiempo=tiempo-1
        racha_forzar=0

        if alarma==True:
            energia=energia-10

    if alarma==True and tiempo<=3 and cerraduras_abiertas<3:
        print("La alarma bloqueo el sistema")
        break


if cerraduras_abiertas==3:
    print("VICTORIA")
elif energia<=0 or tiempo<=0:
    print("DERROTA")
elif alarma==True:
    print("DERROTA (bloqueo)")

print("EJERCICIO N5")
print("--- BIENVENIDO A LA ARENA ---")

nombre_jugador=input("Nombre del Gladiador: ")

while not nombre_jugador.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_jugador=input("Nombre del Gladiador: ")

vida_jugador=100
vida_enemigo=100
pociones=3
ataque_pesado=15
daño_enemigo=12
turno_gladiador=True

print("=== INICIO DEL COMBATE ===")

while vida_jugador>0 and vida_enemigo>0:

    print("----------------------------")
    print(nombre_jugador,"(HP:",vida_jugador,") vs Enemigo (HP:",vida_enemigo,") | Pociones:",pociones)
    print("Elige accion:")
    print("1. Ataque Pesado")
    print("2. Rafaga Veloz")
    print("3. Curar")

    opcion=input("Opcion: ")

    while not opcion.isdigit():
        print("Error: Ingrese un numero valido.")
        opcion=input("Opcion: ")

    opcion=int(opcion)

    while opcion<1 or opcion>3:
        print("Error: opcion fuera de rango.")
        opcion=input("Opcion: ")

        while not opcion.isdigit():
            print("Error: Ingrese un numero valido.")
            opcion=input("Opcion: ")

        opcion=int(opcion)

    if opcion==1:

        if vida_enemigo<20:
            daño=ataque_pesado*1.5
            print("¡Golpe critico!")
        else:
            daño=ataque_pesado

        vida_enemigo=vida_enemigo-daño

        print("¡Atacaste al enemigo por",daño,"puntos de daño!")

    elif opcion==2:

        print(">> ¡Inicias una rafaga de golpes!")

        for i in range(3):
            vida_enemigo=vida_enemigo-5
            print("> Golpe conectado por 5 de daño")

    elif opcion==3:

        if pociones>0:
            vida_jugador=vida_jugador+30
            pociones=pociones-1
            print("¡Te curaste 30 puntos!")
        else:
            print("¡No quedan pociones!")

    if vida_enemigo>0:

        vida_jugador=vida_jugador-daño_enemigo

        print("¡El enemigo te ataco por 12 puntos de daño!")


if vida_jugador>0:
    print("¡VICTORIA!",nombre_jugador,"ha ganado la batalla.")
else:
    print("DERROTA. Has caido en combate.")