
# 🕹️ Number Hunter
#🚀Desarrollador Cuz-dev🚀

import random

def p(message):
    print(message)

def es():
    print('   ')    

s = "s"
c = "c" 

while True:
    es()
    p('🎮 Bienvenido a Number Hunter 🎮')
    p('1* Jugar🕹️')
    p('2* info📝')
    es()
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
                    p('Puntaje: 10')
                    es()
                    p('Nivel dos👾👾')     
                    p('Numero al azar de el 1 al 20')
                    r2 = random.randint(1, 20)
                    n2 = int(input('Dijita el numero que creas que salga:'))
                    es()

                    if n2 == r2:
                        es()
                        p('✔️Correcto')   
                        p('Puntaje: 20')
                        es()
                        p('Nivel tres👾👾👾')
                        p('Numero al azar de el 1 al 30')
                        r3 = random.randint(1, 30)
                        n3 = int(input('Escribe el numero que creas que salga:'))
                        es()

                        if n3 == r3:
                            es()
                            p('✔️Correcto')   
                            p('Puntaje: 30')
                            es()
                            p('Nivel cuatro👾👾👾👾')
                            p('Numero al azar de el 1 al 40:')
                            r4 = random.randint(1, 40)
                            n4 = int(input('Escribe el numero que creas que salga:'))

                            if n4 == r4:
                                es()
                                p('✔️Correcto')   
                                p('Puntaje: 40')
                                es()
                                p('Nivel cinco👾👾👾👾👾')
                                p('Numero al azar de el 1 al 50:')
                                r5 = random.randint(1, 50)
                                n5 = int(input('Escribe el numero que creas que salga:'))

                                if n5 == r5:
                                    es()
                                    p('✔️Correcto')   
                                    p('Puntaje: 50')
                                    es()
                                    p('Nivel seis👾👾👾👾👾👾')
                                    p('Numero al azar de el 1 al 60:')
                                    r6 = random.randint(1, 60)
                                    n6 = int(input('Escribe el numero que creas que salga:'))

                                    if n6 == r6:
                                        es()
                                        p('✔️Correcto')   
                                        p('Puntaje: 60')
                                        es()
                                        p('Nivel siete👾👾👾👾👾👾👾')
                                        p('Numero al azar de el 1 al 70:')
                                        r7 = random.randint(1, 70)
                                        n7 = int(input('Escriba el numero que creas que salga:'))

                                        if n7 == r7:
                                            es()
                                            p('✔️Correcto')   
                                            p('Puntaje: 70')
                                            es()
                                            p('Nivel ocho👾👾👾👾👾👾👾👾')
                                            p('Numero al azar de el 1 al 80:')
                                            r8 = random.randint(1, 80)
                                            n8 = int(input('Escribe el numero que creas que salga:'))

                                            if n8 == r8:
                                                es()
                                                p('✔️Correcto')   
                                                p('Puntaje: 80')
                                                es()
                                                p('Nivel nueve👾👾👾👾👾👾👾👾👾')
                                                p('Numero al azar de el 1 al 90:')
                                                r9 = random.randint(1, 90)
                                                n9 = int(input('Escribe el numero que creas que salga:'))

                                                if n9 == r9:
                                                    es()
                                                    p('✔️Correcto')   
                                                    p('Puntaje: 90')
                                                    es()
                                                    p('Nivel diez👾👾👾👾👾👾👾👾👾👾')
                                                    p('Numero al azar de el 1 al 100:')
                                                    r10 = random.randint(1, 100)
                                                    n10 = int(input('Escribe el numero que creas que salga:'))

                                                    if n10 == r10:
                                                        es()
                                                        p('✔️Correcto')   
                                                        p('Puntaje: 100')
                                                        p('Felicidades te has pasado el juego')

                                                    else:
                                                        p('Game over💥:')
                                                        print('❌Fallaste es:', r10)
                                                        p('Puntaje: 90😀')
                                                        p('Tan cerca pero a la ves tan lejos.....')
                                                        es()
                                                        break        

                                                else:
                                                    p('Game over💥:')
                                                    print('❌Fallaste es:', r9)
                                                    p('Puntaje: 80😀')
                                                    es()
                                                    break     


                                            else:
                                                p('Game over💥:')
                                                print('❌Fallaste es:', r8)
                                                p('Puntaje: 70😀')
                                                es()
                                                break     



                                        else:
                                            p('Game over💥:')
                                            print('❌Fallaste es:', r7)
                                            p('Puntaje: 60😀')
                                            es()
                                            break     

                                    
                                    else: 
                                        p('Game over💥:')
                                        print('❌Fallaste es:', r6)
                                        p('Puntaje: 50😀')
                                        es()
                                        break  

                                else:
                                    p('Game over💥:')
                                    print('❌Fallaste es:', r5)
                                    p('Puntaje: 40😀')
                                    es()
                                    break  



                            else:
                                p('Game over💥:')
                                print('❌Fallaste es:', r4)
                                p('Puntaje: 30😀')
                                es()
                                break  
                        
                        else:
                            p('Game over💥:')
                            print('❌Fallaste es:', r3)
                            p('Puntaje: 20😀')
                            es()
                            break  
                            

                    else:                       
                        p('Game over💥:')
                        print('❌Fallaste es:', r2)
                        p('Puntaje: 10😀')
                        es()
                        break

                    
                
                else:
                    p('Game over💥:')
                    print('❌Fallaste es:', r1)
                    p('Puntaje: 0😫')
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
            