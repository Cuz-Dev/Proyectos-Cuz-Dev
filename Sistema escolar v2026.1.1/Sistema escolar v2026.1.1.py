#🧮Sistema escolar dev-v2026.1.1
#🚀desarrollador Cuz-Dev🚀
#🌪️Si lo puedes imaginar lo puedes programar🌪️
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

try:
    from funciones import calculadora
    from funciones import Number_hunter
    from funciones import Piedra_papel_tijera
    from funciones import generador_contraseñas_seguras
    from funciones import linea_menu
    from funciones import linea_menu2
    from funciones import linea_submenu
    from funciones import opcion_grado
    from funciones import error_usuario
    from funciones import grado_ejemplo
    from funciones import curso_ejemplo
    from funciones import menu_docente
    from funciones import submenu_areas_    
    from funciones import submenu_docentes_area_
    from funciones import submenu_eventos_
    from funciones import submenu_eventos_1
    from funciones import submenu_eventos_2
    from funciones import submenu_eventos_3
    from funciones import submenu_eventos_4
    from funciones import submenu_eventos_5
    from funciones import submenu_directivos_
    from funciones import submenu_directivos_1
    from funciones import submenu_directivos_2
    from funciones import submenu_directivos_3
    from funciones import submenu_directivos_4
    from funciones import menu_coordinador_
    from funciones import submenu_compromisos_
    from funciones import compromisos_1
    from funciones import compromisos_2
    from funciones import compromisos_3
    from funciones import compromisos_4
    from funciones import compromisos_5
    from funciones import submenu_reuniones
    from funciones import reuniones_1
    from funciones import reuniones_2
    from funciones import reuniones_3
    from funciones import reuniones_4
    from funciones import reuniones_5
    from funciones import menu_acudiente_
    from funciones import submenu_añadir_es
    from funciones import menu_es
    from funciones import menu_herramientas_
    from funciones import submenu_calculadora_
    from funciones import submenu_generador
    from funciones import submenu_juegos_
    from funciones import submenu_juegos_1
    from funciones import menu_rector_
    from funciones import menu_principal_
    from funciones import p
    from funciones import v
    from funciones import es
    from funciones import pause
    from funciones import error
    from funciones import volver
    from funciones import salir
    from funciones import Eof
    from funciones import salir_s
    from funciones import entrada_us
    from funciones import submenu_juegos_2
    from funciones import temas_area_lista
    from funciones import docentes_area
    from funciones import menu_secretario_
    from funciones import submenu_notas
    from funciones import grado_es
    from funciones import curso_es
    from funciones import curso_inesistente
    from funciones import grado_inesistente
    from funciones import limpiar_pantalla
    from funciones import eventos_lista
    from funciones import directivos_lista
    from funciones import login_docente
    from funciones import login_coordinador
    from funciones import login_rector
    from funciones import login_menu_principal
    import json
        

except ModuleNotFoundError:
    obj = fallas()
    obj.failed_file_es()


class Sistema_escolar:
    def __init__(self):
        self.pantalla = pantalla_principal(self)
        self.docente = MenuDocente()
        self.coordinador = MenuCoordinador()
        self.acudiente = Acudiente()
        self.herramientas = Menu_herramientas()
        self.menu_fallos_es = fallas()
        self.info = MenuInfo()
        self.RECTOR = MenuRector()
        self.estudiante = Menu_Estudiante()
        self.guardado = estudiantes_sistema()
        self.ver = mostrar_estudiantes()
        self.secretario = secretario_virtual()
        self.añadir_nota = menu_añadir_nota()
        self.ver_nota = notas_estudiante()

    def iniciar(self):
        self.pantalla.menu_principal()

class MenuDocente:
    def __init__(self,):
        self.areas = SubmenuAreas()
        self.eventos = SubmenuEventos()
        self.directivos = SubmenuDirectivos()
        self.estudiantes_grado = mostrar_estudiantes()
        self.guardado = estudiantes_sistema()
        self.ver = mostrar_estudiantes()
        self.añadir_nota = menu_añadir_nota()

    def menu_docente(self):
        limpiar_pantalla()
        login_docente()
        limpiar_pantalla()
        while True:
            menu_docente()
            while True:
                try:
                    opcion_docente = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            opciones_docente = {

                1: self.areas.submenu_areas,
                2: self.eventos.submenu_eventos,
                3: self.directivos.submenu_directivos,
                4: self.ver.ver_estudiante,
                5: self.guardado.menu.menu_guardado,
                6: self.añadir_nota.Menu_añadir
            }

            if opcion_docente in opciones_docente:
                opciones_docente[opcion_docente]()

            elif opcion_docente == 7:
                salir()
                limpiar_pantalla()
                break
    
class SubmenuAreas:
    def submenu_areas(self):
        limpiar_pantalla()
        while True:      
            submenu_areas_()
            while True:
                try:
                    opcion_areas = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            opciones_area = {

                1: temas_area_lista[0],
                2: temas_area_lista[1],
                3: temas_area_lista[2],
                4: temas_area_lista[3],
                5: temas_area_lista[4],
                6: temas_area_lista[5],
                7: temas_area_lista[6],
                8: temas_area_lista[7],
                9: temas_area_lista[8],
                10: temas_area_lista[9],
                11: temas_area_lista[10],
                12: temas_area_lista[11]

            }

            if opcion_areas in opciones_area:
                opciones_area[opcion_areas]()
    
            elif opcion_areas == 13:
                volver()
                limpiar_pantalla()
                break

class Docente_por_area:
    def submenu_docentes_area(self):
        limpiar_pantalla()
        while True:
            submenu_docentes_area_()
            while True:
                try:      
                    docente_area = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            opcion_docente_area = {

                1: docentes_area[0],
                2: docentes_area[1],
                3: docentes_area[2],
                4: docentes_area[3],
                5: docentes_area[4],
                6: docentes_area[5],
                7: docentes_area[6],
                8: docentes_area[7],
                9: docentes_area[8],
                10: docentes_area[9],
                11: docentes_area[10],
                12: docentes_area[11]

            }

            if docente_area in opcion_docente_area:
                opcion_docente_area[docente_area]()
                
                
            elif docente_area == 13:
                volver()
                limpiar_pantalla()
                break 

class SubmenuEventos:
    def __init__(self):
        self.eventos_1 = Eventos1()
        self.eventos_2 = Eventos2()
        self.eventos_3 = Eventos3()
        self.eventos_4 = Eventos4()
        self.eventos_5 = Eventos5()

    def submenu_eventos(self):
        limpiar_pantalla()
        while True:
            submenu_eventos_()
            while True:
                try:
                    eventos = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            opciones_area = {
                1: self.eventos_1.submenu_eventos1,
                2: self.eventos_2.submenu_eventos2,
                3: self.eventos_3.submenu_eventos3,
                4: self.eventos_4.submenu_eventos4,
                5: self.eventos_5.submenu_eventos5
            }
            if eventos in opciones_area:
                opciones_area[eventos]()

            elif eventos == 6:
                volver()
                limpiar_pantalla()
                break

class Eventos1:
    def submenu_eventos1(self):
        while True:
            limpiar_pantalla()
            submenu_eventos_1()
            while True:
                try:
                    cultura = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            opciones_cultura = {
                1: eventos_lista[0],
                2: eventos_lista[1]
            }
                
            if cultura in opciones_cultura:
                opciones_cultura[cultura]()

            elif cultura == 3:
                volver()
                limpiar_pantalla()
                break    
class Eventos2:
    def submenu_eventos2(self):
        limpiar_pantalla()
        while True:
            submenu_eventos_2()
            while True:
                try:
                    feria = entrada_us()
                    es()
                    break

                except ValueError:
                    error()
                    
            opciones_feria = {
                1: eventos_lista[2],
                2: eventos_lista[3]
            }

            if feria in opciones_feria:
                opciones_feria[feria]()

            elif feria == 3:
                volver()
                limpiar_pantalla()
                break    

class Eventos3:
    def submenu_eventos3():
        limpiar_pantalla()
        while True:
            submenu_eventos_3()
            while True:
                try:
                    izada = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            opciones_izada = {
                1: eventos_lista[4],
                2: eventos_lista[5]
            }

            if izada in opciones_izada:
                opciones_izada[izada]()

            elif izada == 3:
                volver()
                limpiar_pantalla()
                break 

class Eventos4:
    def submenu_eventos4(self):
        limpiar_pantalla()
        while True:
            submenu_eventos_4()
            while True:
                try:
                    independencia = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            opciones_independencia = {
                1: eventos_lista[6],
                2: eventos_lista[7]
            }

            if independencia in opciones_independencia:
                opciones_independencia[independencia]()

            elif independencia == 3:
                volver()
                limpiar_pantalla()
                break

class Eventos5:
    def submenu_eventos5(self):
        limpiar_pantalla()
        while True:
            submenu_eventos_5()
            while True:
                try:
                    reunion_acu = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            opciones_reuniones = {
                1: eventos_lista[8],
                2: eventos_lista[9]
            }

            if reunion_acu in opciones_reuniones:
                opciones_reuniones[reunion_acu]()

            elif reunion_acu == 3:
                volver()
                limpiar_pantalla()
                break

class SubmenuDirectivos:
    def __init__(self):
        self.directivo_1 = directivo1()
        self.directivo_2 = directivo2()
        self.directivo_3 = directivo3()
        self.dorectivo_4 = directivo4()

    def submenu_directivos(self):
        limpiar_pantalla()
        while True:
            submenu_directivos_()
            while True:
                try:
                    directivos = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            opciones_directivos = {
                1: self.directivo_1.submenu_directivos1,
                2: self.directivo_2.submenu_directivos2,
                3: self.directivo_3.submenu_directivos3,
                4: self.dorectivo_4.submenu_directivos4
            }

            if directivos in opciones_directivos:
                opciones_directivos[directivos]()

            elif directivos == 5:
                volver()
                limpiar_pantalla()
                break

class directivo1:   
    def submenu_directivos1(self):
        limpiar_pantalla()
        while True:          
            submenu_directivos_1()
            while True:
                try:
                    Rector = entrada_us()
                    es()
                    break

                except ValueError:
                    error()
            
            opciones_rector = {
                1: directivos_lista[0],
                2: directivos_lista[1]
            }

            if Rector in opciones_rector:
                opciones_rector[Rector]()

            elif Rector == 3:
                volver()
                limpiar_pantalla()
                break

class directivo2:
    def submenu_directivos2(self):
        limpiar_pantalla()
        while True:
            submenu_directivos_2()
            while True:
                try:
                    Coordinador = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            opciones_coordinador = {
                1: directivos_lista[2],
                2: directivos_lista[3]
            }

            if Coordinador in opciones_coordinador:
                opciones_coordinador[Coordinador]()

            elif Coordinador == 3:
                volver()
                limpiar_pantalla()
                break       

class directivo3:
    def submenu_directivos3(self):
        limpiar_pantalla()
        while True:
            submenu_directivos_3()
            while True:
                try:
                    es()
                    psicologa = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            opciones_psicologa = {
                1: directivos_lista[4],
                2: directivos_lista[5]
            }

            if psicologa in opciones_psicologa:
                opciones_psicologa[psicologa]()

            elif psicologa == 3:
                volver()
                limpiar_pantalla()
                break       

class directivo4:
    def submenu_directivos4(self):
        limpiar_pantalla()
        while True:
            submenu_directivos_4()
            while True:
                try:
                    secretario = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            opciones_secretario = {
                1: directivos_lista[6],
                2: directivos_lista[7]
            }

            if secretario in opciones_secretario:
                opciones_secretario[secretario]()

            elif secretario == 3:
                volver()
                break

class MenuCoordinador:
    def __init__(self):
        self.docentes_disponibles = Docente_por_area()
        self.Sub_menu_compromisos = compromisos_()
        self.Sub_menu_reuniones = reuniones_()
        self.estudiantes_grado = mostrar_estudiantes()
        self.guardado = estudiantes_sistema()
        self.ver = mostrar_estudiantes()
        self.notas_estudiantes = notas_estudiante()

    def menu_coordinador(self):
        limpiar_pantalla()
        login_coordinador()
        limpiar_pantalla()
        while True:
            menu_coordinador_()
            while True:
                try:
                    opcion_coordinador = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            opciones_coordinador = {
                1: self.Sub_menu_compromisos.compromisos,
                2: self.Sub_menu_reuniones.reuniones,
                3: self.docentes_disponibles.submenu_docentes_area,
                4: self.ver.ver_estudiante,
                5: self.guardado.menu.menu_guardado,
                6: self.notas_estudiantes.ver_notas
            }

            if opcion_coordinador in opciones_coordinador:
                opciones_coordinador[opcion_coordinador]()

            elif opcion_coordinador == 7:
                salir()
                limpiar_pantalla()
                break

class compromisos_:
    def compromisos(self):
        limpiar_pantalla()
        while True:
            submenu_compromisos_()
            while True:
                try:
                    es()
                    Compromiso_s = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            compromisos_opcion = {

                1: compromisos_1,
                2: compromisos_2,
                3: compromisos_3,
                4: compromisos_4,
                5: compromisos_5

            }        
            
            if Compromiso_s in compromisos_opcion:
                compromisos_opcion[Compromiso_s]()

            elif Compromiso_s == 6:
                volver()
                limpiar_pantalla()
                break

class reuniones_:
    def reuniones(self):
        limpiar_pantalla()
        while True:
            submenu_reuniones()
            while True:
                try:
                    Reuniones = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            reuniones_opcion = {

                1: reuniones_1,
                2: reuniones_2,
                3: reuniones_3,
                4: reuniones_4,
                5: reuniones_5

            }

            if Reuniones in reuniones_opcion:
                reuniones_opcion[Reuniones]()

            elif Reuniones == 6:
                volver()
                limpiar_pantalla()
                break

class Acudiente:
    def __init__(self):
        self.docentes = Docente_por_area()
        self.directivos = SubmenuDirectivos()
        self.eventos = SubmenuEventos()
        self.estudiantes_grado = mostrar_estudiantes()
        self.ver = mostrar_estudiantes()

    def menu_acudiente(self):
        limpiar_pantalla()        
        while True:
            menu_acudiente_()
            while True:
                try:
                    opcion_acudiente = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            opciones_acudiente = {
                1: self.ver.ver_estudiante,
                2: self.docentes.submenu_docentes_area,
                3: self.directivos.submenu_directivos,
                4: self.eventos.submenu_eventos
            }

            if opcion_acudiente in opciones_acudiente:
                opciones_acudiente[opcion_acudiente]()

            elif opcion_acudiente == 5:
                salir()
                limpiar_pantalla()
                break

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

            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "notas": {}

        }

        with open("estudiantes.json", "r") as f:
            self.estudiantes = json.load(f)

        self.estudiantes.setdefault(self.grado, {})
        self.estudiantes[self.grado].setdefault(self.curso, [])
        self.estudiantes[self.grado][self.curso].append(nuevo)

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
        es()
        p('dijita el numero de el estudiante:')
        es()
        while True:
            try:
                seleccion_es = entrada_us()
                es()
                break

            except ValueError:
                error()

        with open("estudiantes.json", "r") as archivo:
            datos = json.load(archivo)

        while True:        
            nota = float(input("Ingrese nota: "))
            es()

            if nota > 0 and nota <= 5:
                materia = materias[seleccion_usuario - 1]
                estudiante_nota = datos[self.mostrar.grado][self.mostrar.curso][seleccion_es - 1]

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

    def ver_estudiante(self):
        while True:
            linea_menu2()
            p('Estudiantes')
            linea_menu2()
            es()
            p('[1] Ver estudiante')
            p('[2] <<<< Volver')
            es()
            while True:
                try:
                    opcion_mostrar_estudiante = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if opcion_mostrar_estudiante == 1:
                self.estudiante.opcion_usuario()

            elif opcion_mostrar_estudiante == 2:
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
                    for i ,self.estudiante in enumerate(lista, start=1):
                        es()
                        print(f"{i}: {self.estudiante["Nombre"]}{self.estudiante["Apellido"]}")
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
                for i,self.estudiante in enumerate(list, start=1):
                    es()
                    print(f"{i}: {self.estudiante["Nombre"]}{self.estudiante["Apellido"]}")
                    if "notas" in self.estudiante:
                        for materia, notas in self.estudiante["notas"].items():
                            es()
                            print(f"{materia}: {notas}")

                    else:
                        p('Este, estudiante no tinen notas')

            else:
                curso_inesistente()

        else:
            grado_inesistente()


class Menu_Estudiante:
    def __init__(self):
        self.areas_temas = SubmenuAreas()
        self.directivos = SubmenuDirectivos()
        self.estudiantes_grado = mostrar_estudiantes()
        self.ver = mostrar_estudiantes()

    def menu_estudiante(self):
        limpiar_pantalla()
        while True:
            menu_es()
            while True:
                try:
                    opcion_estudiante = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            estudiante_opcion = {

                1: self.areas_temas.submenu_areas,
                2: self.directivos.submenu_directivos,
                3: self.ver.ver_estudiante
            }

            if opcion_estudiante in estudiante_opcion:
                estudiante_opcion[opcion_estudiante]()
                
            elif opcion_estudiante == 4:
                salir()
                limpiar_pantalla()
                break

class Menu_herramientas:
    def __init__(self):
        self.fallo_es = fallas()
    def menu_herramientas(self):
        limpiar_pantalla()
        while True:
            menu_herramientas_()
            while True:
                try:
                    opcion_herramientas = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if opcion_herramientas == 1:
                while True:
                    submenu_calculadora_()
                    while True:
                        try:
                            opcion_calculadora = entrada_us()
                            es()
                            break

                        except ValueError:
                            error()

                    if opcion_calculadora == 1:
                        while True:
                            try:
                                calculadora()
                                break

                            except ModuleNotFoundError:
                                self.fallo_es.failed_file_es()

                    elif opcion_calculadora == 2:
                        volver()
                        limpiar_pantalla()
                        break

            elif opcion_herramientas == 2:
                while True:
                    submenu_generador()
                    while True:
                        try:
                            herramientas_generador = entrada_us()
                            es()
                            break

                        except ValueError:
                            error()
                
                    if herramientas_generador == 1:
                        while True:
                            try:
                                generador_contraseñas_seguras()
                                break

                            except ModuleNotFoundError:
                                self.fallo_es.failed_file_es()

                    elif herramientas_generador == 2:
                        volver()
                        limpiar_pantalla()
                        break
                
            elif opcion_herramientas == 3:
                while True:
                    submenu_juegos_()
                    while True:
                        try:
                            opcion_juegos = entrada_us()
                            es()
                            break

                        except ValueError:
                            error()

                    if opcion_juegos == 1:
                        while True:
                            submenu_juegos_1()
                            while True:
                                try:
                                    opcion_number_hunter = entrada_us()
                                    es()
                                    break

                                except ValueError:
                                    error()

                            if opcion_number_hunter == 1:
                                while True:
                                    try:
                                        Number_hunter()
                                        es()
                                        break

                                    except ModuleNotFoundError:
                                        self.fallo_es.failed_file_es()

                            elif opcion_number_hunter == 2:
                                volver()
                                limpiar_pantalla()
                                break    

                    elif opcion_juegos == 2:
                        while True:
                            submenu_juegos_2()
                            while True:
                                try:
                                    opcion_piedra_papel = entrada_us()
                                    es()
                                    break

                                except ValueError:
                                    error()

                            if opcion_piedra_papel == 1:
                                while True:
                                    try:
                                        Piedra_papel_tijera()
                                        break

                                    except ModuleNotFoundError:
                                        self.fallo_es.failed_file_es()

                            elif opcion_piedra_papel == 2:
                                volver()
                                limpiar_pantalla()
                                break

                    elif opcion_juegos == 3:
                        volver()
                        limpiar_pantalla()
                        break

            elif opcion_herramientas == 4:
                salir()
                limpiar_pantalla()
                break

class MenuInfo:
    def __init__(self):
        self.fallo_es = fallas()       
    def menu_info(self):
        limpiar_pantalla()
        while True:
            try:
                es()
                with open("info.txt", "r") as archivo:
                    for linea in archivo:
                        p(linea.strip())
                while True:
                    try:
                        sa = int(input('Escribe 1* para salir:'))
                        while sa != 1:
                            sa = int(input('!¡Escribe 1 para salir¡!:'))
                        break

                    except ValueError:
                        error()
                break

            except ModuleNotFoundError:
                self.fallo_es.failed_file_es()

class MenuRector:
    def __init__(self):
        self.areas_Temas = SubmenuAreas()
        self.docentes_Area = Docente_por_area()
        self.eventos_I = SubmenuEventos()
        self.directivos_I = SubmenuDirectivos()
        self.guardar = estudiantes_sistema()
        self.ver = mostrar_estudiantes()
        self.notas_estudiante = notas_estudiante()

    def Menu_rector(self):
        limpiar_pantalla()
        login_rector()
        limpiar_pantalla()
        while True:
            menu_rector_()
            while True:
                try:
                    opcion_rector = entrada_us()
                    es()
                    break

                except ValueError:
                    error()
            rector = {

                1: self.areas_Temas.submenu_areas,
                2: self.docentes_Area.submenu_docentes_area,
                3: self.eventos_I.submenu_eventos,
                4: self.directivos_I.submenu_directivos,
                5: self.guardar.menu.menu_guardado,
                6: self.ver.ver_estudiante,
                7: self.notas_estudiante.ver_notas

            }

            if opcion_rector in rector:
                rector[opcion_rector]()
                
            elif opcion_rector == 8:
                salir()
                limpiar_pantalla()
                break

class secretario_virtual:
    def __init__(self):
        self.directivos = SubmenuDirectivos()
        self.guardar = estudiantes_sistema()
        self.visualizar = mostrar_estudiantes()

    def menu_secretario(self):
        limpiar_pantalla()
        while True:
            menu_secretario_()
            while True:
                try:
                    opcion_secretaria = entrada_us()
                    es()
                    break

                except ValueError:
                    error()
            
            opciones_secretaria = {
                1: self.guardar.menu.menu_guardado,
                2: self.visualizar.ver_estudiante,
                3: self.directivos.submenu_directivos
            }

            if opcion_secretaria in opciones_secretaria:
                opciones_secretaria[opcion_secretaria]()

            elif opcion_secretaria == 4:
                salir()
                limpiar_pantalla()
                break

class pantalla_principal:
    def __init__(self, sistema):
        self.sistema = sistema

    def menu_principal(self):
        login_menu_principal()
        while True:
            limpiar_pantalla()
            menu_principal_()
            persona = str(input('¡!Escribe el nombre de el menu al que quieres entrar!¡:')).lower().strip()

            if persona == 'docente':
                self.sistema.docente.menu_docente()

            elif persona == 'rector':
                self.sistema.RECTOR.Menu_rector()

            elif persona == 'coordinador':
                self.sistema.coordinador.menu_coordinador()

            elif persona == 'acudiente':
                self.sistema.acudiente.menu_acudiente()

            elif persona == 'estudiante':
                self.sistema.estudiante.menu_estudiante()            

            elif persona == 'herramientas':
                self.sistema.herramientas.menu_herramientas()

            elif persona == 'info':
                self.sistema.info.menu_info()

            elif persona == 'secretaria':
                self.sistema.secretario.menu_secretario()

            else:
                error_usuario()

empezar = Sistema_escolar()
empezar.iniciar()


