#Calculadora basica
#🚀desarrollador Cuz-Dev🚀

def p(mensaje):
    print(mensaje)

def es():
    p('   ')    

s = "s"    
while True:
    p('════════════════════════════════════════════════')
    p('                  Calculadora                   ')
    p('════════════════════════════════════════════════')
    p('[1] Sumar')
    p('[2] Restar')
    p('[3] Multiplicar')
    p('[4] Dividir')
    p('[5] Info')
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
                es()
                with open("info-c.txt", "r") as archivo:
                    for leer in archivo:
                        p(leer)
                es()        
                si = str(input('➤ Escribe s para salir:')).lower()
                while si != s:
                    si = str(input('➤ ¡!Escribe s para salir!¡:')).lower()
                break               

    except ValueError:
        es()
        p('[ERROR] Debes escribir un numero no una letra:')
        es()      