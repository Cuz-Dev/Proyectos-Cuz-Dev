
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
                                p('<<<< Saliendo')
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
                    p('<<<< Saliendo')
                    es()
                    break      
                
            
        elif op == 3:
            while True:
                p('🕹️Info juego🕹️')
                es()
                with open("infop.txt", "r") as archivo:
                    for leer in archivo:
                        p(leer)
                es()
                salir3 = str(input('Escribe s para salir:')).lower()
                while salir3 != s:
                    salir3 = str(input('¡!Escribe s para salir!¡:')).lower()
                break            

    except ValueError:
        es()
        p('[ERROR] Debes escribir un numero no una letra:')
        es()