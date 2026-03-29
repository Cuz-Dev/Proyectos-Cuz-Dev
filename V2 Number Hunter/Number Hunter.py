
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

        if nh == 2:
            while True:
                p('info📝')
                with open("infoh.txt", "r") as archivo:
                    for linea in archivo:
                        p(linea)
                es()        
                salir = str(input('Escribe s para salir')).lower()
                while salir != s:
                    salir = str(input('!¡Escribe s para salir¡!')).lower()
                break                  
            

    except ValueError:
        es()
        print('[ERROR] Debes escribir un numero no una letra:') 
        es()      