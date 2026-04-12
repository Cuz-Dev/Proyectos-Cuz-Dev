
#estudiantes sistema escolar

def calculadora():
    while True:
        #Calculadora basica
        #🚀desarrollador Cuz-Dev🚀
        def p(mensaje):
            print(mensaje)
        def es():
            p('   ')    
        s = "s"    
    
        p('════════════════════════════════════════════════')
        p('                  Calculadora                   ')
        p('════════════════════════════════════════════════')
        p('[1] Sumar')
        p('[2] Restar')
        p('[3] Multiplicar')
        p('[4] Dividir')
        p('[5] Info')
        p('[6] <<<< Salir')
        try:
            cal = int(input('escribe numero de opcion!¡:'))
            if cal == 1:
                while True:
                    es()
                    try:
                        p('➤ Suma')
                        es()
                        s1 = int(input('Escribe el primer a sumar:'))
                        s2 = int(input('Escribe el segundo a sumar:'))
                        rs = s1 + s2
                        print("Resultado suma:", rs)
                        es()
                        ss = str(input('➤ Escribe s para salir:')).lower()
                        while ss != s:
                            ss = str(input('➤ ¡!Escribe s para salir!¡:')).lower()
                        break

                    except ValueError:
                        es()
                        p('[ERROR] Debes escribir un numero no una letra:')
                        es()      

            elif cal == 2:
                while True:
                    es()
                    try:
                        p('➤ Resta')
                        es()
                        r1 = int(input('Escribe el primer a restar:'))
                        r2 = int(input('Escribe el segundo a restar:'))
                        rr =  r1 - r2
                        print('Resultado resta:', rr)
                        es()
                        sr = str(input('➤ Escribe s para salir:')).lower()
                        while sr != s:
                            sr = str(input('➤ ¡!Escribe s para salir!¡:')).lower()
                        break

                    except ValueError:
                        es()
                        p('[ERROR] Debes escribir un numero no una letra:')
                        es()      

            elif cal == 3:
                while True:
                    es()
                    try:
                        p('➤ Multiplicacion')
                        es()
                        m1 = int(input('Escribe el primer numero a multiplicar:'))
                        m2 = int(input('Escribe el segundo numero a multiplicar:'))
                        rm = m1 * m2
                        print('Resultado multiplicacion:', rm)
                        es()
                        sm = str(input('➤ Escribe s para salir:')).lower()
                        while sm != s:
                            sm = str(input('➤ ¡!Escribe s para salir:')).lower()
                        break

                    except ValueError:
                        es()
                        p('[ERROR] Debes escribir un numero no una letra:')
                        es()      

            elif cal == 4:
                while True:
                    es()
                    try:
                        p('➤ Division')
                        d1 = int(input('Escribe el primer numero a dividir:'))
                        d2 = int(input('Escribe el segundo numero a dividir:'))
                        rd = d1 / d2
                        print('Resultado division:', rd)
                        es()
                        sd = str(input('➤ Escribe s para salir')).lower()
                        while sd != s:
                            sd = str(input('➤ ¡!Escribe s para salir!¡')).lower()
                        break

                    except ValueError:
                        es()
                        p('[ERROR] Debes escribir un numero no una letra:')
                        es()          

            elif cal == 5:
                while True:
                    p('info')
                    es()
                    p('Calculadora basica v2')
                    p('Desarrollador cuz-dev')
                    es()
                    p('novedades:')
                    p('* Manejo de errores')
                    p('* interfaz mejorada')
                    es()
                    p('¡!Gracias por ejecutar mi programa¡!')
                    es()       
                    si = str(input('➤ Escribe s para salir:')).lower()
                    while si != s:
                        si = str(input('➤ ¡!Escribe s para salir')).lower()
                    break               

            elif cal == 6:
                p('Saliendo*.*')
                es()
                break
            

        except ValueError:
            es()
            p('[ERROR] Debes escribir un numero no una letra:')
            es()      

def Number_hunter():
    # 🕹️ Number Hunter
    #🚀Desarrollador Cuz-dev🚀
    # Si lo puedes imaginar lo puedes programar
    import random
    def p(message):
        print(message)
    def es():
        print('   ')    
    s = "s"
    c = "c"
    contador_nh = 0
    while True:
        es()
        p('================================================')
        p('         🔥Bienvenido a Number Hunter🔥         ')
        p('             🕹️---------------🕹️               ')
        p('          vdesarrollado por Cuz-Dev🚀           ')
        p('================================================')
        es()
        p('1* Jugar🕹️')
        p('2* info📝y Reglas')
        p('3* Salir🚪')
        es()

        try:
            nh = int(input('Escribe numero de opcion para continuar:'))

            if nh == 1:
                while True:
                    p('👾👽 Number Hunter 👾👽')
                    p('Dijita 1 para Empezar🔥:')
                    p('Dijita 2 para salir:')
                    es()
                    juego1 = int(input('Escribe opcion:'))

                    if juego1 == 1:
                        es()                
                        p('Nivel uno👾')
                        p('Numero al azar de el 1 al 10')
                        r1 = random.randint(1, 10)
                        es()
                        n1 = int(input('Dijita el numero que creas que salga:'))
                
                        if n1 == r1:
                            es()
                            ('✔️Correcto')
                            contador_nh += 10
                            p('Puntaje:', contador_nh)
                            es()
                            p('Nivel dos👾👾')     
                            p('Numero al azar de el 1 al 20')
                            r2 = random.randint(1, 20)
                            n2 = int(input('Dijita el numero que creas que salga:'))
                            es()

                            if n2 == r2:
                                es()
                                p('✔️Correcto')
                                contador_nh += 10   
                                p('Puntaje:', contador_nh)
                                es()
                                p('Nivel tres👾👾👾')
                                p('Numero al azar de el 1 al 30')
                                r3 = random.randint(1, 30)
                                n3 = int(input('Escribe el numero que creas que salga:'))
                                es()

                                if n3 == r3:
                                    es()
                                    p('✔️Correcto')   
                                    contador_nh += 10   
                                    p('Puntaje:', contador_nh)
                                    es()
                                    p('Nivel cuatro👾👾👾👾')
                                    p('Numero al azar de el 1 al 40:')
                                    r4 = random.randint(1, 40)
                                    n4 = int(input('Escribe el numero que creas que salga:'))

                                    if n4 == r4:
                                        es()
                                        p('✔️Correcto')   
                                        contador_nh += 10   
                                        p('Puntaje:', contador_nh)
                                        es()
                                        p('Nivel cinco👾👾👾👾👾')
                                        p('Numero al azar de el 1 al 50:')
                                        r5 = random.randint(1, 50)
                                        n5 = int(input('Escribe el numero que creas que salga:'))

                                        if n5 == r5:
                                            es()
                                            p('✔️Correcto')   
                                            contador_nh += 10   
                                            p('Puntaje:', contador_nh)
                                            es()
                                            p('Nivel seis👾👾👾👾👾👾')
                                            p('Numero al azar de el 1 al 60:')
                                            r6 = random.randint(1, 60)
                                            n6 = int(input('Escribe el numero que creas que salga:'))

                                            if n6 == r6:
                                                es()
                                                p('✔️Correcto')   
                                                contador_nh += 10   
                                                p('Puntaje:', contador_nh)
                                                es()
                                                p('Nivel siete👾👾👾👾👾👾👾')
                                                p('Numero al azar de el 1 al 70:')
                                                r7 = random.randint(1, 70)
                                                n7 = int(input('Escriba el numero que creas que salga:'))

                                                if n7 == r7:
                                                    es()
                                                    p('✔️Correcto')   
                                                    contador_nh += 10   
                                                    p('Puntaje:', contador_nh)
                                                    es()
                                                    p('Nivel ocho👾👾👾👾👾👾👾👾')
                                                    p('Numero al azar de el 1 al 80:')
                                                    r8 = random.randint(1, 80)
                                                    n8 = int(input('Escribe el numero que creas que salga:'))

                                                    if n8 == r8:
                                                        es()
                                                        p('✔️Correcto')   
                                                        contador_nh += 10   
                                                        p('Puntaje:', contador_nh)
                                                        es()
                                                        p('Nivel nueve👾👾👾👾👾👾👾👾👾')
                                                        p('Numero al azar de el 1 al 90:')
                                                        r9 = random.randint(1, 90)
                                                        n9 = int(input('Escribe el numero que creas que salga:'))

                                                        if n9 == r9:
                                                            es()
                                                            p('✔️Correcto')   
                                                            contador_nh += 10   
                                                            p('Puntaje:', contador_nh)
                                                            es()
                                                            p('Nivel diez👾👾👾👾👾👾👾👾👾👾')
                                                            p('Numero al azar de el 1 al 100:')
                                                            r10 = random.randint(1, 100)
                                                            n10 = int(input('Escribe el numero que creas que salga:'))

                                                            if n10 == r10:
                                                                es()
                                                                p('✔️Correcto')   
                                                                contador_nh += 10   
                                                                p('Puntaje:', contador_nh)
                                                                es()
                                                                p('Felicidades te has pasado el juego')

                                                            else:
                                                                p('Game over💥:')
                                                                print('❌Fallaste es:', r10)
                                                                p('Puntaje: 90😀')
                                                                p('Tan cerca pero a la ves tan lejos.....')
                                                                contador_nh = 0
                                                                es()
                                                                break        

                                                        else:
                                                            p('Game over💥:')
                                                            print('❌Fallaste es:', r9)
                                                            p('Puntaje: 80😀')
                                                            contador_nh = 0
                                                            es()
                                                            break     


                                                    else:
                                                        p('Game over💥:')
                                                        print('❌Fallaste es:', r8)
                                                        p('Puntaje: 70😀')
                                                        contador_nh = 0
                                                        es()
                                                        break     

                                                else:
                                                    p('Game over💥:')
                                                    print('❌Fallaste es:', r7)
                                                    p('Puntaje: 60😀')
                                                    contador_nh = 0
                                                    es()
                                                    break     

                                    
                                            else: 
                                                p('Game over💥:')
                                                print('❌Fallaste es:', r6)
                                                p('Puntaje: 50😀')
                                                contador_nh = 0
                                                es()
                                                break  

                                        else:
                                            p('Game over💥:')
                                            print('❌Fallaste es:', r5)
                                            p('Puntaje: 40😀')
                                            contador_nh = 0
                                            es()
                                            break  

                                    else:
                                        p('Game over💥:')
                                        print('❌Fallaste es:', r4)
                                        p('Puntaje: 30😀')
                                        contador_nh = 0
                                        es()
                                        break  
                        
                                else:
                                    p('Game over💥:')
                                    print('❌Fallaste es:', r3)
                                    p('Puntaje: 20😀')
                                    contador_nh = 0
                                    es()
                                    break  
                            

                            else:                       
                                p('Game over💥:')
                                print('❌Fallaste es:', r2)
                                p('Puntaje: 10😀')
                                contador_nh = 0
                                es()
                                break

                    
                
                        else:
                            p('Game over💥:')
                            print('❌Fallaste es:', r1)
                            p('Puntaje: 0😫')
                            contador_nh = 0
                            es()
                            break

                    elif juego1 == 2:
                        p('Saliendo')
                        es()
                        break        

            elif nh == 2:
                while True:
                    p('info📝')
                    p('info  Number Hunter')
                    es()
                    p('novedades')
                    p('* Manejo de errores')
                    p('* Mejora de el contador')
                    es()
                    p('juego desarrollado por Cuz-Dev')
                    p('*cada que el usuario pierda se reiniciara el juego')
                    p('*juego arcade, 10 niveles')
                    es()
                    p('Reglas')
                    p('* No se puede manipular el codigo, es decir no se pude poner una instruccion print')
                    p('que muestre el resultado de el numero random que elige la maquina..')
                    p('* Este juego es de pura posibilidad')
                    es()
                    p('¡! Gracias por ejecutar mi programa !¡')
                    es()
                    p('Recuerda que en mi github hay mas proyectos')
                    es()       
                    salir = str(input('Escribe s para salir')).lower()
                    while salir != s:
                        salir = str(input('!¡Escribe s para salir¡!')).lower()
                    break                  
            
            elif nh == 3:
                p('<<<<')
                es()
                break

        except ValueError:
            es()
            print('[ERROR] Debes escribir un numero no una letra:') 
            es()      

def Piedra_papel_tijera():
    #🕹️Piedra papel o tijera ✊✋✌️
    #🚀Desarrollador Cuz-Dev 🚀
    import random
    def p(mensaje):
        print(mensaje)
    def es():
        p('   ')
    def resultado():
        print('  ')
        print('🕹️Resultado🕹️')
        print('      ')
    def pause():
        input('➤ ENTER PARA CONTINUAR')     
    piedra = 'piedra'
    papel = 'papel'
    tijera = 'tijera'
    contador1 = 0
    contador2 = 0
    opciones = ['piedra', 'papel', 'tijera']
    s = 's'

    while True:
        p('════════════════════════════════════════════════')
        p('         ✊Piedra  ✋papel o ✌️tijera            ')
        p('════════════════════════════════════════════════')
        es()
        p('[1] Jugar🎮')
        p('[2] Puntaje⚡')
        p('[3] Info📃 y reglas')
        p('[4] <<<< Volver')
        es()
        try:
            op = int(input('➤ Escribe numero de opcion:'))

            if op == 1:
                while True:    
                    p('[1] Empezar 🔥')
                    p('[2] <<<< Salir')
                    es()
                    juego = int(input('➤ Escribe numero de opcion:'))
    
                    if juego == 1:
                        while True:                   
                            p('========================')
                            p('         Elige          ')
                            p('========================')
                            opm = random.choice(opciones)
                            es()
                            p('[1] ✊ Piedra')
                            p('[2] ✋ Papel')
                            p('[3] ✌️ Tijera')
                            p('[4] Volver')
                            es()
                            v = int(input('➤ Escribe numero de opcion:'))
                
                            if opm == 'piedra':
                                if v == 1:
                                    es()
                                    resultado()
                                    es()
                                    p('empate⚔️')
                                    print('maquina elegio 🤖', ' ', opm)
                                    print('tú elegististe 👤',' ', 'piedra')
                                    pause()
                                    es()
                            
                                elif v == 2:
                                    es()
                                    resultado()
                                    es()
                                    print('Victoria 🏆')
                                    print('maquina elegio 🤖', ' ', opm)
                                    print('tú elegististe 👤',' ', 'papel')
                                    es()
                                    contador1 += 1
                                    print('JUGADOR:', contador1, '/', 'MAQUINA:', contador2)
                                    pause()
                                    es()
                            
                                elif v == 3:
                                    es()
                                    resultado()
                                    es()
                                    p('derrota 😈')
                                    print('maquina elegio 🤖', ' ', opm)
                                    print('tú elegististe 👤',' ', 'tijera')
                                    es()
                                    contador2 += 1
                                    print('JUGADOR:', contador1, '/', 'MAQUINA:', contador2)
                                    pause()
                                    es()
                
                            
                            elif opm == 'papel':
                                if v == 1:
                                    es()
                                    resultado()
                                    es()
                                    print('derrota 😈')
                                    print('maquina elegio 🤖', ' ', opm)
                                    print('tú elegististe 👤',' ', 'piedra')
                                    es()
                                    contador2 += 1
                                    print('JUGADOR:', contador1, '/', 'MAQUINA:', contador2)
                                    pause()
                                    es()

                                elif v == 2:
                                    es()
                                    resultado()
                                    es()
                                    print('empate ⚔️')
                                    print('maquina elegio 🤖', ' ', opm)
                                    print('tú elegististe 👤',' ', 'papel')
                                    pause()
                                    es()
                            
                                elif v == 3:
                                    es()
                                    resultado()
                                    es()
                                    print('Victoria 🏆')
                                    print('maquina elegio 🤖', ' ', opm)
                                    print('tú elegististe 👤',' ', 'tijera')
                                    es()
                                    contador1 += 1
                                    print('JUGADOR:', contador1, '/', 'MAQUINA:', contador2)
                                    pause()
                                    es()
                            
                            elif opm == 'tijera':                     
                                if v == 1:
                                    es()
                                    resultado()
                                    es()
                                    print('Victoria 🏆')
                                    print('maquina elegio 🤖', ' ', opm)
                                    print('tú elegististe 👤',' ', 'piedra')
                                    es()
                                    contador1 += 1
                                    print('JUGADOR:', contador1, '/', 'MAQUINA:', contador2)
                                    pause()
                                    es()
                            
                                elif v == 2:
                                    es()
                                    resultado()
                                    es()
                                    print('derrota 😈')
                                    print('maquina elegio 🤖', ' ', opm)
                                    print('tú elegististe 👤',' ', 'papel')
                                    es()
                                    contador2 += 1
                                    print('JUGADOR:', contador1, '/', 'MAQUINA:', contador2)
                                    pause()
                                    es()

                                elif v == 3:
                                    es()
                                    resultado()
                                    es()
                                    print('empate ⚔️')
                                    print('maquina elegio 🤖', ' ', opm)
                                    print('tú elegististe 👤',' ', 'tijera')
                                    pause()
                                    es()

                                if v == 4:
                                    p('<<<<')
                                    es()
                                    break           


                    elif juego == 2:
                        p('<<<< Saliendo')
                        es()
                        break    


            elif op == 2:
                while True:
                    p('========================')
                    p('        Puntaje          ')
                    p('========================')
                    es()
                    p('[1] puntaje jugador')
                    p('[2] Puntaje maquina')
                    p('[3] Salir')
                    es()
                    puntaje = int(input('➤ Escribe numero de opcion:'))

                    if puntaje == 1:
                        while True:
                            p('👾 Puntaje jugador 👾')
                            p(contador1)
                            es()
                            if contador1 <= contador2:
                                p('le ganaste ala maquina🤯')
                            else:
                                p('Te gano la maquina🤭')
                            es()        
                            salir1 = str(input('Escribe s para salir:')).lower()
                            while salir1 != s:
                                salir1 = str(input('¡!Escribe para salir!¡:')).lower()
                            break

                    elif puntaje == 2:
                        while True:
                            p('🤖 Puntaje Maquina 🤖')
                            p(contador2)
                            salir2 = str(input('Escribe s para salir:')).lower()
                            while salir2 != s:
                                salir2 = str(input('¡!Escribe s salir!¡:'))
                            break

                    elif puntaje == 3:
                        p('<<<<')
                        es()
                        break      
                
            
            elif op == 3:
                while True:
                    p('🕹️Info juego🕹️')
                    es()
                    p('Piedra papel o tijera')
                    p('Desarrollador Cuz-Dev')
                    es()
                    p('*Puntaje usuario, maquina')
                    p('*Retroceso bucle while')
                    p('*si pierdes no se borra tu Puntaje')
                    es()
                    p('reglas')
                    p('* No se puede manipular el codigo, es decir no se puede poner la  funcion print')
                    p('para que muestre la eleccion  de la maquina')
                    es()
                    p('v2 Novedades')
                    p('* manejo de errores')
                    es()
                    p('¡!Gracias por ejecutar mi programa¡!')
                    es()
                    p('Recuerda que en mi github hay mas proyectos')
                    es()
                    salir3 = str(input('Escribe s para salir:')).lower()
                    while salir3 != s:
                        salir3 = str(input('¡!Escribe s para salir!¡:')).lower()
                    break

            elif op == 4:
                p('<<<<')
                es()
                break            

        except ValueError:
            es()
            p('[ERROR] Debes escribir un numero no una letra:')
            es()


gd61 = [ 
    "Estudiantes grado 6:1"
    "1* Elnora Padilla",
    "2* Rodney Tran",
    "3* Callie Gray",
    "4* Jean Simpson",
    "5* Lloyd Johnston",
    "6* Harry Wright",
    "7* Elmer McLaughlin",
    "8* Harold Fields",
    "9* Lelia Sparks",
    "10* Beulah Flowers",
    "11* Christopher Rodriquez",
    "12* Mayme Armstrong",
    "13* Gavin Mathis",
    "14* Clara Payne",
    "15* Bessie KimBertha Reynolds",
    "16* Ricky Myers",
    "17* Jackson Torres",
    "18* Mike Cooper",
    "19* Hilda Pittman",
    "20* Olive Howard",
    "21* Mollie Berry"
]

gd62 = [
    "Estudiantes grado 6:2",
    "1* Cynthia Tyler",
    "2* Gertrude Fletcher",
    "3* Timothy Alvarado",
    "4* Lillian Lawrence",
    "5* Leon Butler",
    "6* Hester Gregory",
    "7* Clyde Wong",
    "8* Lucille Luna",
    "9* Jeremiah Craig",
    "10* Louis McCoy",
    "11* Nannie Dennis",
    "12* Lottie Huff",
    "13* Erik Murray",
    "14* Shawn Osborne",
    "14* Lena Houston",
    "15* Myrtle Wolfe",
    "16* Raymond Dennis",
    "17* Larry Harper",
    "18* Johanna Lewis",
    "19* Rosalie Becker",
    "20* Dennis Cole",
]    

gd63 = [
    "Estudiantes de grado 6:3"
    "1* Tyler James",
    "2* Marie Gonzales",
    "3* Lina Porter",
    "4* Isabel Potter",
    "5* Callie Perry",
    "6* Rosetta McKinney",
    "7* Verna Rice",
    "8* Todd Diaz",
    "9* Inez George",
    "10* Helena Santiago",
    "11* Christopher Evans",
    "12* Madge Schultz",
    "13* Ray Hill",
    "14* Sally Obrien",
    "15* Myra Joseph",
    "16* Lida Carpenter",
    "17* Ethan Park",
    "18* Bryan Elliott",
    "20* Myra Cox",
    "21* Augusta Erickson",
    "22* Vera Welch",
    "23* Jeffrey Simpson",
    "24* Carolyn Vargas"
]  


gd71 = [
    "Estudiantes de grado 7:1"
    "1* Fannie Roberson",
    "2* Elsie Walters",
    "3* Joe Castillo",
    "4* Myrtle Strickland",
    "5* Elsie Coleman",
    "6* Devin Roberson",
    "7* Floyd Perry",
    "8* Anthony Gardner",
    "9* Jayden Lopez",
    "10* Ora Cannon",
    "11* Wesley Gray",
    "12* Adele Austin",
    "13* Susan Mathis",
    "14* Clyde Garcia",
    "15* Josephine Harvey",
    "16* Brent Stokes",
    "17* Frances Lyons",
    "18* Jim McBride",
    "19* Ryan Huff",
    "20* Tommy Woods",
    "21* Hallie Gardner",
    "22* Louis Love",
]

gd72 = [
    "Estudiantes de grado 7:2"
    "1* Jennie Beck",
    "2* Claudia Morrison",
    "3* Jason Hunter",
    "4* Harriet Elliott",
    "5* Tillie Dunn",
    "6* Isaiah Griffin",
    "7* Mable Vargas",
    "8* Ada Mack",
    "9* Allie Simmons",
    "10* Georgie Fowler",
    "11* Hannah Stanley",
    "12* Miguel Cortez",
    "13* Glenn Burgess",
    "14* Austin Bates",
    "15* Celia Brady",
    "16* Warren Barrett",
    "17* Verna Moran",
    "18* Rachel Stone",
    "19* Josephine Walters",
] 

gd73 = [
    "Esctudiantes grado 7:3"
    "1* Harry Singleton",
    "2* Mathilda Stone",
    "3* Alan Frazier",
    "4* Alfred Jackson",
    "5* Josephine Armstrong",
    "6* Lela Brewer",
    "7* Louis Hansen",
    "8* Jeffery Owens",
    "9* Landon Cannon",
    "10* Christine Marshall",
    "11* Tillie Cunningham",
    "12* Daniel Webster",
    "13* Jennie Evans",
    "14* Mamie Rodriquez",
    "15* Ruth Perkins",
    "16* Jordan Nash",
    "17* Derek Perez",
    "18* Julia Holmes",
    "19* Gavin Brown",
    "20* Nina Soto",
    "21* Katie Tucker",
]

gd81 = [
    "Estudiantes grado 8:1"
    "1* Alberta Kelley",
    "2* Carrie Cox",
    "3* Edna Bailey",
    "4* Hannah Cummings",
    "5* Randy Watkins",
    "6* Lydia Burton",
    "7* Pauline Jones",
    "8* Catherine Tucker",
    "9* Louise Reynolds",
    "10* Estelle Simmons",
    "11* Lucas Andrews",
    "12* Don Joseph",
    "13* Howard Tyler",
    "14* Caleb Norton",
    "15* Roxie Jefferson",
    "16* Ian Fleming",
    "17* Thomas Tate",
    "18* Willie Gordon",
    "19* Hester Waters",
    "20* Andrew Cole",
    "21* Isabel Hart",
    "22* Donald Black",

]    

gd82 = [
    "Estidantes de grado 8:2"
    "1* Elsie Peterson",
    "2* James Nichols",
    "3* Clarence Grant",
    "4* Noah Mendoza",
    "5* Evan Thornton",
    "6* Cordelia Mack",
    "7* Tommy Pope",
    "8* Clara Cook",
    "9* Victor Dennis",
    "10* Leila Russell",
    "11* Lela Smith",
    "12* Jacob Harmon",
    "13* Caroline Parks",
    "14* Ryan Mason",
    "15* Dale Lewis",
    "16* Curtis Gonzales",
    "17* Kenneth Schneider",
    "18* Minnie Graham",
    "19* Nicholas Simpson",

]

gd91 = [
    "Estudiantes grado 9:1"
    "1* Georgia Gordon",
    "2* Darrell Dawson",
    "3* Shane Blair",
    "4* Harriett Gibson",
    "5* Sally Alvarez",
    "6* Travis Crawford",
    "7* Lester Campbell",
    "8* Benjamin Vargas",
    "9* Lulu Smith",
    "10* Nannie Horton",
    "11* Tillie Simpson",
    "12* Marion Howell",
    "13* Shane Robbins",
    "14* Lewis Gomez",
    "15* Willie Reed",
    "16* Noah Cooper",
    "17* Gilbert Perry",
    "18* Rose Moreno",
    "19* Connor Owen",
    "20* Amanda Manning",
    "21* Lola Bryan",
    "22* Paul Rodgers",
    "23* John Lopez",

]    

gd92 = [
    "Estudiantes de grado 9:2"
    "1* Lela King",
    "2* Jennie Lane",
    "3* Sally Rice",
    "4* Minerva Ortiz",
    "5* Harriett Hamilton",
    "6* Juan Maxwell",
    "7* Rachel Atkins",
    "8* Mayme Delgado",
    "9* Pauline Jacobs",
    "10* Louisa Robbins",
    "11* Joel Salazar",
    "12* Mina Brady",
    "13* Phillip Holland",
    "14* Emilie Bell",
    "15* Lou Campbell",
    "16* Blanche Ryan",
    "17* Glenn Strickland",
    "18* Timothy Holland",
    "19* Earl Chandler",

]

gd101 = [
    "Estudiantes grado 10:1"
    "1* Herbert Harvey",
    "2* Ruby McCarthy",
    "3* Alex Barrett",
    "4* Douglas Woods",
    "5* Arthur Fernandez",
    "6* Don Snyder",
    "7* Ann Cross",
    "8* Lillie Rose",
    "9* Blake Lewis",
    "10* Ophelia Gibson",
    "11* Sarah Cross",
    "12* Randy Cain",
    "13* Howard Poole",
    "14* Ricky Richards",
    "15* Esther Cross",
    "16* Dylan Frazier",
    "17* Sam Frazier",
    "18* Isaac Freeman",
    "19* Sally Hale",
    "20* Joseph Cook",
    "21* Jack Craig",
    "22* Blanche Buchanan",
    "23* Mabelle Austin",
    "24* Austin Wallace",

]    

gd102 = [
    "Estudiantes grado 10:2"
    "1* Belle Abbott",
    "2* Alice Miller",
    "3* Cynthia Abbott",
    "4* Alfred Gray",
    "5* Jeffery Pearson",
    "6* Mason Miles",
    "7* Adrian Palmer",
    "8* Emma Lawrence",
    "9* Rose Bailey",
    "10* Myrtie Collins",
    "11* Cory Powell",
    "12* Cameron Knight",
    "13* Devin Woods",
    "14* Mary Benson",
    "15* Minerva Townsend",
    "16* Daisy Norton",
    "17* Charlie Mullins",
    "18* Carrie Phillips",
    "19* Allie Jennings",
    "20* Sophie Mendez ",
    "21* Roy Allen",
    "22* Marc Fletcher",
    
]

gd111 = [
    "Estudiantes grado 11:1"
    "1* Vincent Freeman",
    "2* Nathan Lucas",
    "3* Gene Rodriquez",
    "4* Kathryn Washington",
    "5* Essie Hamilton",
    "6* Stephen Oliver",
    "7* Roger Gross",
    "8* Danny Norris",
    "9* Tony Quinn",
    "10* Randy Ruiz",
    "11* Ophelia Bishop",
    "12* Blanche Brock",
    "13* Elizabeth Cortez",
    "14* Rodney Ruiz",
    "15* Daisy Douglas",
    "16* Francisco Grant",
    "17* Ruby Curtis",
    "18* Lora Banks",
    "19* Emma Colon",
    "20* Blake Flores",
    "21* Warren Francis",

]    

gd112 = [
    "Estudiantes grado 11:2"
    "1* Abbie Cross",
    "2* Michael Martin",
    "3* Ora Martin",
    "4* Gilbert Wilkins",
    "5* Anthony Martin",
    "6* Irene Klein",
    "7* Mayme Curry",
    "8* Marcus Christensen",
    "9* Luke Underwood",
    "10* Lloyd Rice",
    "11* Todd Francis",
    "12* Jared Fowler",
    "13* Brandon Alvarado",
    "14* Josie Soto",
    "15* Devin Crawford",
    "16* Bill Jensen",
    "17* Kenneth Elliott",
    "18* Phoebe Roberts",
    "19* Eula Tate",
    "20* Sallie Marsh",

]    