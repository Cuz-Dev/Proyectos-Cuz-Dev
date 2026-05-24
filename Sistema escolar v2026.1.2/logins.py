def error_():
    print('[Errror critico] No se encuentran los demas archivos:')

while True:
    try:
        from configuracion import es, error, v, Eof, limpiar_pantalla
        break

    except ModuleNotFoundError:
        error_()

def login_docente():
    while True:
        try:
            es()
            contraseña_docente = int(input('!Hola profe¡, porfavor escribe tu clave:'))
            while contraseña_docente != 202614:
                es()
                limpiar_pantalla()
                contraseña_docente = int(input('[ERROR]!Clave incorrecta¡:'))
                es()
            break

        except ValueError:
            error()

def login_coordinador():
    while True:
        try:
            es()
            contraseña_coordinador = int(input('¡!Hola cordinador por favor dijita tu clave!¡:'))
            while contraseña_coordinador != 202601:
                es()
                limpiar_pantalla()
                contraseña_coordinador = int(input('?Acaso no eres el cordinador¿'))
                es()
            break

        except ValueError:
            error()


def login_rector():
    while True:
        try:
            es()
            contraseña_rector = int(input('¡!Hola rector!¡, Por favor dijita la clave:'))
            while contraseña_rector != 202600:
                es()
                limpiar_pantalla()
                contraseña_rector = int(input('[ERROR]!Clave incorrecta¡:'))
                es()
            break

        except ValueError:
            error()

def login_menu_principal():
    while True:
        try:
            v()
            colegio = str(input('Por favor escribe colegio python para continuar:')).lower()
            break

        except EOFError:
            Eof()             

    while colegio != 'colegio python':
        es()
        limpiar_pantalla()
        colegio = str(input('[ERROR] colegio incorrecto:')).lower()
        es()



