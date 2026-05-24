class fallas:
    def failed_file_es(self):
        while True:
            es()
            p('>> Hola Usuari@')
            es()
            p('○ Actualmente estas en le menu de error')
            es()
            p('1* Error actual y posibles causas')
            p('2* como solucionar este error')
            es()
            while True:
                try:
                    menu_error_es = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if menu_error_es == 1:
                while True:
                    p('◉ Tipo de error')
                    es()
                    p('* El error actual es "101" ModuleNotFoundError')
                    es()
                    p('◉ Causas de el error')
                    es()
                    p('Las causas mas comunes')
                    p('son:')
                    es()
                    p('1: El interprete de python no encuentra alguno de los 3 archivo')
                    p('necesarios, por que se esta ejecutando el programa dentro de la carpeta incorrecta.')
                    es()
                    p('2: No descargaste todos los archivos')
                    es()
                    es()
                    saliendo = salir_s()
                    es()
                    while saliendo != 's':
                        saliendo = salir_s()
                        es()
                    break

            elif menu_error_es == 2:
                while True:
                    p('◉ Maneras de solucionar el error')
                    es()
                    p('1: Abre la carpeta de siste4ma escolar v2026.x.x,')
                    p(' y desde ahi abres abres el archivo .py')
                    es()
                    p('2: Descarga el archivo de mi perfil de github:')
                    p('aunque seria mejor que descargues toda la carpeta de la version')
                    es()
                    saliendo_s = salir_s()
                    es()
                    while saliendo_s != 's':
                        saliendo_s = salir_s()
                        es()
                    break

while True:
    try:
        from configuracion import es, p, error, entrada_us, salir_s
        break

    except ModuleNotFoundError:
        p('No se encuentra un archivo')