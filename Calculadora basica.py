
def p(mensaje):
    print(mensaje)

def es():
    p('   ')    

s = "s"    
while True:
    p('======= Calculadora =======')
    p('1*Sumar')
    p('2*Restar')
    p('3*Multiplicar')
    p('4*Dividir')
    p('5*Info')
    cal = int(input('escribe numero de opcion!¡:'))

    if cal == 1:
        while True:
            es()
            s1 = int(input('Escribe el primer a sumar:'))
            s2 = int(input('Escribe el segundo a sumar:'))
            rs = s1 + s2
            print("Resultado suma:", rs)
            ss = str(input('Escribe s para salir')).lower()
            while ss != s:
                ss = str(input('¡!Escribe s para salir!¡')).lower()
            break

    elif cal == 2:
        while True:
            es()
            r1 = int(input('Escribe el primer a restar:'))
            r2 = int(input('Escribe el segundo a restar:'))
            rr =  r1 - r2
            print('Resultado resta:', rr)
            sr = str(input('Escribe s para salir:')).lower()
            while sr != s:
                sr = str(input('¡!Escribe s para salir!¡:')).lower()
            break

    elif cal == 3:
        while True:
            es()
            m1 = int(input('Escribe el primer numero a multiplicar:'))
            m2 = int(input('Escribe el segundo numero a multiplicar:'))
            rm = m1 * m2
            print('Resultado multiplicacion:', rm)
            sm = str(input('Escribe s para salir:')).lower()
            while sm != s:
                sm = str(input('¡!Escribe s para salir:')).lower()
            break

    elif cal == 4:
        while True:
            es()
            d1 = int(input('Escribe el primer numero a dividir:'))
            d2 = int(input('Escribe el segundo numero a dividir:'))
            rd = d1 / d2
            print('Resultado division:', rd)
            sd = str(input('Escribe s para salir')).lower()
            while sd != s:
                sd = str(input('¡!Escribe s para salir!¡')).lower()
            break    
  
    elif cal == 5:
        while True:
            es()
            with open("info-c.txt", "r") as archivo:
                for leer in archivo:
                    p(leer)
            es()        
            si = str(input('Escribe s para salir:')).lower()
            while si != s:
                si = str(input('¡!Escribe s para salir!¡:')).lower()
            break               