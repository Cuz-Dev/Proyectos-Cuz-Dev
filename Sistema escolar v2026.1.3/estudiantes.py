import json

def error_():
    print('[Errror critico] No se encuentran los demas archivos:')

while True:
    try:
        from configuracion import limpiar_pantalla, s_n, borrado_exitoso
        break

    except ValueError:
        error_()
        
while True:
    try:
        from UI import submenu_añadir_es, submenu_notas, submenu_anotacion, submenu_anotacion_2
        break

    except ModuleNotFoundError:
        error_()

while True:
    try:
        from UI import submenu_quitar_estudiante
        break

    except ModuleNotFoundError:
        error_()

while True:
    try: 
        from configuracion import limpiar_pantalla, error, es, p, entrada_us, grado_ejemplo, curso_ejemplo
        from configuracion import anotacion_
        break

    except ModuleNotFoundError:
        error_()

while True:
    try:
        from configuracion import entrada
        break

    except ModuleNotFoundError:
        error_()

while True:
    try:
        from configuracion import volver, salir, linea_menu, linea_menu2, curso_inesistente, grado_inesistente, grado_es, curso_es
        break

    except ModuleNotFoundError:
        error_()

while True:
    try:
        from utilidades import pedir_apellido
        es()
        break

    except ModuleNotFoundError:
        error_()

class estudiantes_sistema:
    def __init__(self):
        self.guardar = guardar_estudiante()
        self.menu = MenuGuardado()

class MenuGuardado:
    def __init__(self):
        self.guardad = guardar_estudiante()
    def menu_guardado(self):
        while True:
            submenu_añadir_es()
            while True:
                try:
                    guardado = entrada_us()
                    break

                except ValueError:
                    error()


            if guardado == 1:
                self.guardad.datos_es()
                self.guardad.guardado()

            else:
                limpiar_pantalla()
                break

class guardar_estudiante:
    def __init__(self):
        self.estudiante = {}
        self.mostrar = estudiante_ver()

    def datos_es(self):
            self.nombre = str(input('Escribe el nombre de el estudiante: ')).capitalize().strip()
            es()
            self.apellido = str(input('Escribe el apellido: ')).capitalize().strip()
            es()
            grado_ejemplo()
            es()
            self.grado = str(input('Dijita el grado: '))
            es()
            while True:
                if self.grado.isdigit():
                    break
                else:
                    es()
                    p('debes escribir un numero valido:')
            while True:
                curso_ejemplo()
                es()
                self.curso = str(input('Dijita el curso: '))
                es()
                if self.curso.isdigit():
                    break
                else:
                    es()
                    p('debes escribir un numero valido: ')

    def guardado(self):
        nuevo = {

            self.apellido: {
                'Nombre': self.nombre,
                'notas': {},
                'anotaciones': []

            }

        }

        with open("estudiantes.json", "r") as f:
            self.estudiantes = json.load(f)

        self.estudiantes.setdefault(self.grado, {})
        self.estudiantes[self.grado].setdefault(self.curso, {})
        self.estudiantes[self.grado][self.curso] = nuevo

        with open("estudiantes.json", "w") as f:
            json.dump(self.estudiantes, f, indent=4)


    def notas_es(self):
        es()
        materias = [

            "Matematicas",
            "Edu fisica",
            "Catellano",
            "Ingles",
            "Biologia",
            "Filosofia",
            "Tecnologia",
            "Fisica",
            "Sociales",
            "Quimica",
            "Artistica",
        ]

        for i, materia in enumerate(materias):
            print(f"{i + 1}. {materia}")

        while True:
            try:
                seleccion_usuario = entrada_us()
                es()
                break

            except ValueError:
                error()

        self.mostrar.opcion_usuario()
        seleccion_es = pedir_apellido()
        with open("estudiantes.json", "r") as archivo:
            datos = json.load(archivo)

        while True:        
            nota = float(input("Ingrese nota: "))
            es()

            if nota > 0 and nota <= 5:
                materia = materias[seleccion_usuario - 1]
                estudiante_nota = datos[self.mostrar.grado][self.mostrar.curso][seleccion_es]

                if "notas" not in estudiante_nota:
                    estudiante_nota["notas"] = {}

                if materia not in estudiante_nota["notas"]:
                    estudiante_nota["notas"][materia] = []
                estudiante_nota["notas"][materia].append(nota)
                with open("estudiantes.json", "w") as archivo_json:
                    json.dump(datos, archivo_json, indent=4)
                break

            else:
                p('nota ivalida')

class menu_añadir_nota:
    def __init__(self):
        self.añadir = guardar_estudiante()
        self.ver_notas = notas_estudiante()

    def Menu_añadir(self):
        while True:
            submenu_notas()
            while True:
                try:
                    opcion_submenu = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            opciones = {

                1: self.añadir.notas_es,
                2: self.ver_notas.ver_notas
            }

            if opcion_submenu in opciones:
                opciones[opcion_submenu]()

            elif opcion_submenu == 3:
                volver()
                limpiar_pantalla()
                break


class mostrar_estudiantes:
    def __init__(self):
        self.estudiante = estudiante_ver()
        self.quitar = quitar_estudiante()

    def ver_estudiante(self):
        while True:
            linea_menu2()
            p('Estudiantes')
            linea_menu2()
            es()
            p('[1] Ver estudiante')
            p('[2] Borrar estudiante')
            p('[3] <<<< Volver')
            es()
            while True:
                try:
                    opcion_mostrar_estudiante = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            opciones = {
                1: self.estudiante.opcion_usuario,
                2: self.quitar.Quitar_estudiante
            }

            if opcion_mostrar_estudiante in opciones:
                opciones[opcion_mostrar_estudiante]()

            elif opcion_mostrar_estudiante == 3:
                volver()
                limpiar_pantalla()
                break

class estudiante_ver:
    def opcion_usuario(self):
        while True:
            self.grado = grado_es()
            es()
            self.curso = curso_es()
            with open("estudiantes.json", "r") as f:
                archivo = json.load(f)

            if self.grado in archivo:
                if self.curso in archivo[self.grado]:
                    lista = archivo[self.grado][self.curso]
                    p(f"Grado:{self.grado}")
                    p(f"    Curso: {self.curso}")
                    for i, (apellido, datos) in enumerate(lista.items(), start=1):
                        print(f"{i}: {datos['Nombre']} {apellido}")
                    return lista
                else:
                    curso_inesistente()
            else:
                grado_inesistente()
            break

class notas_estudiante:
    def ver_notas(self):
        grado = grado_es()
        es()
        curso = curso_es()
        es()
        with open("estudiantes.json", "r") as read:
            archivo = json.load(read)

        if grado in archivo:
            if curso in archivo[grado]:
                list = archivo[grado][curso]
                p(f"Grado: {grado}")
                p(f"Curso: {curso}")
                for i, (apellido, datos) in enumerate(list.items(), start=1):
                    print(f"{i}: {datos['Nombre']}{apellido}") 
                    print(f"{datos['notas']}")

            else:
                curso_inesistente()

        else:
            grado_inesistente()

class anotacion:
    def __init__(self):
        self.mostrar = estudiante_ver()
        self.g = guardar_estudiante()
        self.estudiante = {}

    def añadir_anotacion(self):
        with open('estudiantes.json', 'r') as d:
            archivo = json.load(d)

        self.mostrar.opcion_usuario()
        selecion_us = pedir_apellido()
        limpiar_pantalla()
        an = anotacion_()
        anotaciones = archivo[self.mostrar.grado][self.mostrar.curso][selecion_us]
        if 'anotaciones' not in anotaciones:
            anotaciones['anotaciones'] = []
        anotaciones['anotaciones'].append(an)
        with open('estudiantes.json', 'w') as j:
            json.dump(archivo, j, indent=4)

    def mostrar_anotacion(self):
        with open('estudiantes.json', 'r') as j:
            leer = json.load(j)
        self.mostrar.opcion_usuario()
        seleccion = entrada_us()
        limpiar_pantalla()
        lista_estudiantes = list(leer[self.mostrar.grado][self.mostrar.curso].keys())
        apellido = lista_estudiantes[seleccion - 1]
        anotaciones = leer[self.mostrar.grado][self.mostrar.curso][apellido]['anotaciones']

        for i, texto in enumerate(anotaciones, start=1):
            print(f"{i}. {texto}")
                    
class submenu_anotaciones:
    def __init__(self):
        self.guardar = anotacion()

    def Sub_Menu_Anotacion(self):
        while True:
            submenu_anotacion()
            opcion = entrada()
            opciones_anotacion = {

                1:self.guardar.añadir_anotacion,
                2: self.guardar.mostrar_anotacion

            }

            if opcion in opciones_anotacion:
                opciones_anotacion[opcion]()

            elif opcion == 3:
                salir()
                limpiar_pantalla()
                break        
        
class submenu_anotaciones_2:
    def __init__(self):
        self.mostrar = anotacion()

    def Sub_Menu_Anotacion_2(self):
        while True:
            submenu_anotacion_2()
            opcion = entrada()

            opciones_anotacion_2 = {

                1:self.mostrar.mostrar_anotacion
            }

            if opcion in opciones_anotacion_2:
                opciones_anotacion_2[opcion]()

            elif opcion == 2:
                salir()
                limpiar_pantalla()
                break

class quitar_estudiante:
    def __init__(self):
        self.mostrar = estudiante_ver()

    def Quitar_estudiante(self):
        with open('estudiantes.json', 'r') as f:
            archivo = json.load(f)
        self.mostrar.opcion_usuario()
        es()
        selecion = pedir_apellido()
        opcion = s_n()

        if opcion == 's':
            if self.mostrar.grado in archivo:
                if self.mostrar.curso in archivo[self.mostrar.grado]:
                    del archivo[self.mostrar.grado][self.mostrar.curso][selecion]
                    with open('estudiantes.json', 'w') as d:
                        json.dump(archivo, d, indent=4)
                    borrado_exitoso()

            else:
                grado_inesistente()

        elif opcion == 'n':
            limpiar_pantalla()

class submenu_quitar():
    def __init__(self):
        self.quitar = quitar_estudiante()

    def Submenu_Quitar(self):
        while True:
            submenu_quitar_estudiante()
            opcion = entrada_us()
            opciones = {
                1: self.quitar.Quitar_estudiante
            }

            if opcion in opciones:
                opciones[opcion]()

            else:
                volver()
                limpiar_pantalla()
                break

