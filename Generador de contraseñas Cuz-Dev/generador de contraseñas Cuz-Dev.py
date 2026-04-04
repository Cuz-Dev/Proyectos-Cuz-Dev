#✍️Generador de contraseñas
#🚀desarrollador Cuz-Dev🚀
import random

def p(mensaje):
    print(mensaje)
def es():
    p('  ')

def error():
    es()
    p('[ERROR] Debes escribir un numero no una letra')
    es()

def entrada_us():
    return int(input('¡!Por favor escribe numero de opcion!¡:'))

def volver():
    p('<<<<')
    es()
    
def numero_random():
    return str(random.randint(0,9))

def submenu_invertir():
    es()
    p('[1] invertir contraseña')
    p('[2] Guardar contraseña')
    p('[3] <<<< Volver')
    es()

def salir_s():
    return str(input('Escribe s para salir:')).lower()

def mostrar_generar():
    es()
    p('[1] Empezar a generar 🔥')
    p('[2] <<<< Volver')
    es()

def generando():
    es()
    p('Generando □ ■ ▫ ▪')

def guardando():
    es()
    p('Guardando □ ■ ▫ ▪')
    es()

def guardado_exito():
    es()
    p('Guardado con exito ¡! s' \
    'sEn save password.txt')
    es()

def finalized():
    p('Contraseña finalizada Con exito: ')

simbolos = (
    '#',
    '!',
    '@',
    '$',
    '%',
    '&',
    '¿',
    '?',
    '.',
    ',',
    ':',
    '*'
)

abc = ['a', 'b,' 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

def letra_random():
    return str(random.choice(abc))

def simbolo_random():
    return str(random.choice(simbolos))

def contraseña4_dijitos():
    while True:
        p('================================================')
        p('         Contraseña de 4 dijitos               ')
        p('================================================')
        es()
        p('[1] Contraseña de 4 dijitos, Numeros')
        p('[2] Contraseña Mixta')
        p('[3] <<<< Volver')
        es()
        while True:
            try:
                es()
                usuario_menu1 = entrada_us()
                break

            except  ValueError:
                error()

        if usuario_menu1 == 1:
            contraseña4_submenu1()

        elif usuario_menu1 == 2:
            contraseña_mixta4_submenu1()

        elif usuario_menu1 == 3:
            volver()
            break

def contraseña4_submenu1():
    while True:
        p('➤ Contraseña Numeros 4 dijitos')
        mostrar_generar()
        while True:
            try:
                es()
                dijitos_4 = entrada_us()
                break

            except ValueError:
                error()

        if dijitos_4 == 1:
            generar4_dijitos()  

        elif dijitos_4 == 2:
            volver()
            break

def generar4_dijitos():
    while True:
        generando()
        es()
        dijito1 = numero_random()
        dijito2 = numero_random()
        dijito3 = numero_random()
        dijito4 = numero_random()
        contraseñan4 = dijito1 + dijito2 + dijito3 + dijito4
        agrupacion = [dijito1, dijito2, dijito3, dijito4]
        print(finalized(), "\n", contraseñan4)
        es()
        submenu_invertir()
        es()
        while True:
            try:
                es()
                opcion_menu_anidadod4 = entrada_us()
                break

            except ValueError:
                error()

        if opcion_menu_anidadod4 == 1:
            anidado_generar4(agrupacion)

        elif opcion_menu_anidadod4 == 2:
            guardar_dijitos4(contraseñan4)

        elif opcion_menu_anidadod4 == 3:
            volver()
            break

def guardar_dijitos4(contraseñan4):
    while True:
        guardando()
        with open("save password.txt", "a") as password4:
            password4.write(contraseñan4 + "\n")
        guardado_exito()
        salir_guardar_dijitos4 = salir_s()
        while salir_guardar_dijitos4 != 's':
            salir_guardar_dijitos4 = salir_s()
        break      

def anidado_generar4(agrupacion):
    while True:
        generando()
        es()
        def agrupacion1():
            return str(random.choice(agrupacion))
        dijito1e = agrupacion1()
        dijito2e = agrupacion1()
        dijito3e = agrupacion1()
        dijito4e = agrupacion1()
        contraseñan4e = dijito1e + dijito2e + dijito3e + dijito4e
        print(finalized(), "\n", contraseñan4e)
        es()
        p('[1] Guardar')
        p('[2] <<<< Volver')
        es()
        while True:
            try:
                es()
                anidado_generar4e = entrada_us()
                break

            except ValueError:
                error()

        if anidado_generar4e == 1:
            guardar_dijitos4e(contraseñan4e)

        elif anidado_generar4e == 2:
            volver()
            break

def guardar_dijitos4e(contraseñan4e):
    while True:
        guardando()
        with open("save password.txt", "a") as password4e:
            password4e.write(contraseñan4e + "\n")
        guardado_exito()
        salir_guardar_dijitos4e = salir_s()
        while salir_guardar_dijitos4e != 's':
            salir_guardar_dijitos4e = salir_s()
        break

def contraseña_mixta4_submenu1():
    while True:
        p('➤ Contraseña 4 dijitos mixta')
        es()
        mostrar_generar()
        es()
        while True:
            try:
                mixta4_submenu1 = entrada_us()
                es()
                break

            except ValueError:
                error()

        if mixta4_submenu1 == 1:
            generar_contraseña_mixta4()

        elif mixta4_submenu1 == 2:
            volver()
            break

def generar_contraseña_mixta4():
    while True:
        generando()
        caracter1 = letra_random()
        caracter2 = numero_random()
        caracter3 = letra_random()
        caracter4 = simbolo_random()
        contraseñam4 = caracter1 + caracter2 + caracter3 + caracter4
        agrupacionm4 = [caracter1, caracter2, caracter3, caracter4]
        print(finalized(), "\n", contraseñam4)
        submenu_invertir()
        while True:
            try:
                menu_anidadom4 = entrada_us()
                es()
                break

            except ValueError:
                error()

        if menu_anidadom4 == 1:
            anidado_generar_mixta4(agrupacionm4)

        elif menu_anidadom4 == 2:
            guardar_mixta4(contraseñam4)

        elif menu_anidadom4 == 3:
            volver()
            break

def guardar_mixta4(contraseñam4):
    while True:
        with open("save password.txt", "a") as passwordm4:
            passwordm4.write(contraseñam4 + "\n")
        guardado_exito()
        salir_guardar_mixta4 = salir_s()
        while salir_guardar_mixta4 != 's':
            salir_guardar_mixta4 = salir_s()
        break

def anidado_generar_mixta4(agrupacionm4):
    while True:
        generando()
        def agrupacion_mixta4():
            return str(random.choice(agrupacionm4))
        caracter1e = agrupacion_mixta4()
        caracter2e = agrupacion_mixta4()
        caracter3e = agrupacion_mixta4()
        caracter4e = agrupacion_mixta4()
        contraseñam4e = caracter1e + caracter2e + caracter3e + caracter4e
        print(finalized(), "\n", contraseñam4e)
        p('[1] Guardar')
        p('[2] <<<< Volver')
        es()
        while True:
            try:
                anidado_generar_mixta4e = entrada_us()
                es()
                break

            except ValueError:
                error()

        if anidado_generar_mixta4e == 1:
            guardar_mixta4e(contraseñam4e)

        elif anidado_generar_mixta4e == 2:
            volver()
            break
        
def guardar_mixta4e(contraseñam4e):
    while True:
        with open("save password.txt", "a") as paswordm4e:
            paswordm4e.write(contraseñam4e + "\n")
        guardado_exito()
        salir_guardar_mixta4e = salir_s()
        while salir_guardar_mixta4e != 's':
            salir_guardar_mixta4e = salir_s()
        break

def contraseña6_dijitos():
    while True:
        p('================================================')
        p('            Contraseña 6 dijitos              ')
        p('================================================')
        es()
        p('[1] Contraseña de 6 dijitos numeros')
        p('[2] Contraseña mixta')
        p('[3] <<<< Volver')
        es()
        while True:
            try:
                usuario_menu2 = entrada_us()
                es()
                break

            except ValueError:
                error()

        if usuario_menu2 == 1:
            contraseña_dijitos6()

        elif usuario_menu2 == 2:
            contraseña_m6()

        elif usuario_menu2 == 3:
            volver()
            break

def contraseña_dijitos6():
    while True:
        mostrar_generar()
        dijit1 = numero_random()
        dijit2 = numero_random()
        dijit3 = numero_random()
        dijit4 = numero_random()
        dijit5 = numero_random()
        dijit6 = numero_random()
        contraseña6 = dijit1 + dijit2 + dijit3 + dijit4 + dijit5 + dijit6
        agrupacion6 = [dijit1, dijit2, dijit3, dijit4, dijit5, dijit6]
        generando()
        print(finalized(), "\n", contraseña6)
        submenu_invertir()
        while True:
            try:
                contraseña_dijit6 = entrada_us()
                es()
                break

            except ValueError:
                error()
        if contraseña_dijit6 == 1:
            contraseña_dijitos6e(agrupacion6)

        elif contraseña_dijit6 == 2:
            guardar_contraseña6(contraseña6)

        elif contraseña_dijit6 == 3:
            volver()
            break

def guardar_contraseña6(contraseña6):
    while True:
        with open("save password.txt", "a") as password6:
            password6.write(contraseña6 + "\n")
        es()
        guardado_exito()
        salir_guardar_contraseña6 = salir_s()
        while salir_guardar_contraseña6 != 's':
            salir_guardar_contraseña6 = salir_s()
        break

def contraseña_dijitos6e(agrupacion6):
    while True:
        generando()
        def agrupacione_6():
            return str(random.choice(agrupacion6))
        dijit1e = agrupacione_6()
        dijit2e = agrupacione_6()
        dijit3e = agrupacione_6()
        dijit4e = agrupacione_6()
        dijit5e = agrupacione_6()
        dijit6e = agrupacione_6()
        contraseña6e = dijit1e + dijit2e + dijit3e + dijit4e + dijit5e + dijit6e
        print(finalized(), "\n", contraseña6e)
        es()
        p('[1] Guardar')
        p('[2] <<<< Volver')
        es()
        while True:
            try:
                contraseña_dijitom6 = entrada_us()
                es()
                break

            except ValueError:
                error()

        if contraseña_dijitom6 == 1:
            guardar_contraseña6e(contraseña6e)

        elif contraseña_dijitom6 == 2:
            volver()
            break

def guardar_contraseña6e(contraseña6e):
    while True:
        with open("save password.txt", "a") as password6e:
            password6e.write(contraseña6e + "\n")
        es()
        guardado_exito()
        salir_guardar_contraseña_m6 = salir_s()
        while salir_guardar_contraseña_m6 != 's':
            salir_guardar_contraseña_m6 = salir_s()
        break

def contraseña_m6():
    while True:
        mostrar_generar()
        caracter6m1 = simbolo_random()
        caracter6m2 = letra_random()
        caracter6m3 = numero_random()
        caracter6m4 = letra_random()
        caracter6m5 = simbolo_random()
        caracter6m6 = numero_random()
        contraseñam6 = caracter6m1 + caracter6m2 + caracter6m3 + caracter6m4 + caracter6m5 + caracter6m6
        agrupacionm6 = [caracter6m1, caracter6m2, caracter6m3, caracter6m4, caracter6m5, caracter6m6]
        generando()
        print(finalized(), "\n", contraseñam6)
        submenu_invertir()
        while True:
            try:
                contraseña_dijitm6 = entrada_us()
                es()
                break

            except ValueError:
                error()

        if contraseña_dijitm6 == 1:
            contraseña_m6e(agrupacionm6)

        elif contraseña_dijitm6 == 2:
            guardar_contraseñam6(contraseñam6)

        elif contraseña_dijitm6 == 3:
            volver()
            break

def guardar_contraseñam6(contraseñam6):
    while True:
        with open("save password.txt", "a") as passwordm6:
            passwordm6.write(contraseñam6 + "\n")
        es()
        guardado_exito()
        salir_guardar_contraseñam6 = salir_s()
        while salir_guardar_contraseñam6 != 's':
            salir_guardar_contraseñam6 = salir_s()
        break

def contraseña_m6e(agrupacionm6):
    while True:
        generando()
        def generar_mixto6():
            return str(random.choice(agrupacionm6))
        caracterm6e1 = generar_mixto6()
        caracterm6e2 = generar_mixto6()
        caracterm6e3 = generar_mixto6()
        caracterm6e4 = generar_mixto6()
        caracterm6e5 = generar_mixto6()
        caracterm6e6 = generar_mixto6()
        contraseñam6e = caracterm6e1 + caracterm6e2 + caracterm6e3 + caracterm6e4 + caracterm6e5 + caracterm6e6
        print(finalized(), "\n", contraseñam6e)
        p('[1] Guardar')
        p('[2] <<<< Volver')
        es()
        while True:
            try:
                contraseña_mixtam6e = entrada_us()
                es()
                break

            except ValueError:
                error()

        if contraseña_mixtam6e == 1:
            guardar_mixta6e(contraseñam6e)

        elif contraseña_mixtam6e == 2:
            volver()
            break

def guardar_mixta6e(contraseñam6e):
    while True:
        with open("save password.txt", "a") as passwordm6e:
            passwordm6e.write(contraseñam6e + "\n")
        guardado_exito()
        salir_guardar_mixta6e = salir_s()
        while salir_guardar_mixta6e != 's':
            salir_guardar_mixta6e = salir_s()
        break
def contraseña8_dijitos():
    while True:
        p('================================================')
        p('              Contraseña 8 dijitos                ')
        p('================================================')
        es()
        p('[1] Contraseña 8 dijitos numeros')
        p('[2] Mixta')
        p('[3] <<<< Volver')
        es()
        while True:
            try:
                contraseña_8_dijitos = entrada_us()
                es()
                break

            except ValueError:
                error()

        if contraseña_8_dijitos == 1:
            contraseña_dijitos8()

        elif contraseña_8_dijitos == 2:
            generar_m8()

        elif contraseña_8_dijitos == 3:
            volver()
            break

def contraseña_dijitos8():
    while True:
        mostrar_generar()
        di1 = numero_random()
        di2 = numero_random()
        di3 = numero_random()
        di4 = numero_random()
        di5 = numero_random()
        di6 = numero_random()
        di7 = numero_random()
        di8 = numero_random()
        contraseña8 = di1 + di2 + di3 + di4 + di5 + di6 + di7 + di8
        agrupacion8 = [di1, di2, di3, di4, di5, di6, di7, di8]
        print(finalized(), "\n", contraseña8)
        generando()
        submenu_invertir()
        while True:
            try:
                dijitos8 = entrada_us()
                es()
                break

            except ValueError:
                error()

        if dijitos8 == 1:
            contraseña_dijitos8e(agrupacion8)

        elif dijitos8 == 2:
            guardar_dijitos8(contraseña8)

        elif dijitos8 == 3:
            volver()
            break

def guardar_dijitos8(contraseña8):
    while True:
        with open("save password.txt", "a") as password8:
            password8.write(contraseña8 + "\n")
        es()
        guardado_exito()
        salir_guardar_dijitos8 = salir_s()
        while salir_guardar_dijitos8 != 's':
            salir_guardar_dijitos8 = salir_s()
        break

def contraseña_dijitos8e(agrupacion8):
    while True:
        generando()
        def dijit8e():
            return str(random.choice(agrupacion8))
        di1e = dijit8e()
        di2e = dijit8e()
        di3e = dijit8e()
        di4e = dijit8e()
        di5e = dijit8e()
        di6e = dijit8e()
        di7e = dijit8e()
        di8e = dijit8e()
        contraseña8e = di1e + di2e + di3e + di4e + di5e + di6e + di7e + di8e
        print(finalized(), "\n", contraseña8e)
        p('[1] Guardar')
        p('[2] <<<< Volver')
        es()
        while True:
            try:
                dijitos8e = entrada_us()
                es()
                break

            except ValueError:
                error()

        if dijitos8e == 1:
            guardar_dijitos8e(contraseña8e)

        elif dijitos8e == 2:
            volver()
            break

def guardar_dijitos8e(contraseña8e):
    while True:
        with open("save password.txt", "a") as password8e:
            password8e.write(contraseña8e + "\n")
        es()
        guardado_exito
        salir_guardar_dijitos8e = salir_s()
        while salir_guardar_dijitos8e != 's':
            salir_guardar_dijitos8e = salir_s()
        break

def generar_m8():
    while True:
        mostrar_generar()
        caracterm81 = simbolo_random()
        caracterm82 = letra_random()
        caracterm83 = numero_random()
        caracterm84 = simbolo_random()
        caracterm85 = numero_random()
        caracterm86 = numero_random()
        caracterm87 = simbolo_random()
        caracterm88 = simbolo_random()
        contraseñam8 = caracterm81 + caracterm82 + caracterm83 + caracterm84 + caracterm85 + caracterm86 + caracterm87 + caracterm88
        agrupacionm8 = [caracterm81, caracterm82, caracterm83, caracterm84, caracterm85, caracterm85, caracterm86, caracterm87, caracterm88]
        print(finalized(), "\n", contraseñam8)
        submenu_invertir()
        while True:
            try:
                caracter8e = entrada_us()
                es()
                break

            except ValueError:
                error()

        if caracter8e == 1:
            generar_m8e(agrupacionm8)

        elif caracter8e == 2:
            guardar_m8(contraseñam8)

        elif caracter8e == 3:
            volver()
            break

def guardar_m8(contraseñam8):
    while True:
        with open("save password.txt", "a") as passwordm8:
            passwordm8.write(contraseñam8 + "\n")
        guardado_exito()
        salir_guardarm8 = salir_s()
        while salir_guardarm8 != 's':
            salir_guardarm8 = salir_s()
        break

def generar_m8e(agrupacionm8):
    while True:
        generando()
        def m8e():
            return str(random.choice(agrupacionm8))
        c8e1 = m8e()
        c8e2 = m8e()
        c8e3 = m8e()
        c8e4 = m8e()
        c8e5 = m8e()
        c8e6 = m8e()
        c8e7 = m8e()
        c8e8 = m8e()
        contraseñam8e = c8e1 + c8e2 + c8e3 + c8e4 + c8e5 + c8e6 + c8e7 + c8e8
        print(finalized(), "\n", contraseñam8e)
        p('[1] Guardar')
        p('[2] <<<< Volver')
        es()
        while True:
            try:
                caracter8e = entrada_us()
                es()
                break

            except ValueError:
                error()

        if caracter8e == 1:
            guardar_m8e(contraseñam8e)

        elif caracter8e == 2:
            volver()
            break

def guardar_m8e(contraseñam8e):
    while True:
        with open("save password.txt", "a") as passwordm8e:
            passwordm8e.write(contraseñam8e + "\n")
        guardado_exito()
        salir_guardar_m8e = salir_s()
        while salir_guardar_m8e != 's':
            salir_guardar_m8e = salir_s()
        break


while True:
    p('════════════════════════════════════════════════════════════════════════')
    p('               🔑🛡️Generador de contraseñas🛡️🔑                          ')
    p('                    ------------------------                             ')
    p('                     Desarrollador Cuz-Dev                              ')
    p('════════════════════════════════════════════════════════════════════════')
    es()
    p('[1] Contraseña 4 dijitos')
    p('[2] Contraseña 6 dijitos')
    p('[3] Contraseña 8 dijitos()')
    p('[4] Info')
    es()
    while True:
        try:
            usuario = entrada_us()
            es()
            break

        except ValueError:
            error()

    if usuario == 1:
        contraseña4_dijitos()

    elif usuario == 2:
        contraseña6_dijitos()

    elif usuario == 3:
        contraseña8_dijitos()

    elif usuario == 4:
        while True:
            with open("info-g.txt", "r") as info:
                for i in info:
                    p(i.strip())
                    es()
            salir_usuario4 = salir_s()
            while salir_usuario4 != 's':
                salir_usuario4 = salir_s()
            break






