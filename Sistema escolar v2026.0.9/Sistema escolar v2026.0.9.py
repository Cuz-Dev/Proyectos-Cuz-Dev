#🧮Sistema escolar dev-v2026.0.9
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
    from funciones import submenu_juegos_2
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

    def menu_docente(self):
        while True:
            try:
                es()
                contraseña_docente = int(input('!Hola profe¡, porfavor escribe tu clave:'))
                while contraseña_docente != 202614:
                    es()
                    contraseña_docente = int(input('[ERROR]!Clave incorrecta¡:'))
                    es()
                break

            except ValueError:
                error()

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
                5: self.guardado.menu.menu_guardado
            }

            if opcion_docente in opciones_docente:
                opciones_docente[opcion_docente]()

            elif opcion_docente == 6:
                salir()
                break
    
class SubmenuAreas:
    def submenu_areas(self):
        while True:           
            submenu_areas_()
            while True:
                try:
                    opcion_areas = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if opcion_areas == 1:
                p('➤ Temas ciencias naturales')
                p('• Animales')
                p('• Celulas')
                p('• Medio ambiente')
                p('• Quimica')
                p('• Laboratorio')
                pause()

            elif opcion_areas == 2:
                p('➤ Temas fisica materia')
                es()
                p('• Mru')
                p('• Factores de conversion')
                p('• Unidades de medida')
                pause()

            elif opcion_areas == 3:
                p('➤ Temas sociales')
                es()
                p('• Imperialismo')
                p('• Socialismo')
                p('• Comunismo')
                p('• Nacionalismo')
                pause()

            elif opcion_areas == 4:
                p('➤ Temas filosofia')
                es()
                p('• Inicios de la filosofia')
                p('• Principales pensadores de la edad media')
                pause()
                

            elif opcion_areas == 5:
                p('➤ Temas ingles')
                es()
                p('• Verb to be')
                p('• Lisenig')
                p('• Read')
                pause()

            elif opcion_areas == 6:
                p('➤ Temas edu. fisica')
                es()
                p('• Juegos tradicionales')
                p('• Historia de el basquetball')
                p('• Historia de el fottball')
                pause()
            
            elif opcion_areas == 7:
                p('➤ Temas religion')
                es()    
                p('• Sin sentidos')
                p('• Sentidos')
                p('• Yo pertenezco a jesus')
                pause()

            elif opcion_areas == 8:
                p('➤ Temas etica')
                es()
                p('• Sentimientos')
                p('• Perdon')
                p('• Valores')
                pause()
                
            elif opcion_areas == 9:
                p('➤ Temas  castellano')
                es()
                p('• La vida feliz')
                p('• La metarmofosis')
                p('• Noches blancas')
                pause()            

            elif opcion_areas == 10:
                p('➤ Temas tecnologia')
                es()
                p('• Diagrama de flujo')
                p('• Makecode')
                p('• Python')
                pause()
        
            elif opcion_areas == 11:
                p('➤ Temas ciencias economicas y politicas')
                es()
                p('• Pensadores')
                p('• Origen')
                p('• Importancia')
                pause()

            elif opcion_areas == 12:
                p('➤ Temas matematicas')
                es()
                p('• Seno')
                p('• Coseno')
                p('• Tangente')
                pause()
                
            elif opcion_areas == 13:
                volver()
                break

class Docente_por_area:
    def submenu_docentes_area(self): 
        while True:
            submenu_docentes_area_()
            while True:
                try:      
                    docente_area = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if docente_area == 1:
                p('➤ Ciencias naturales ')
                es()
                p('• dora')
                p('• jhon')
                p('• angelica')
                pause()

            elif docente_area == 2:
                p('➤ Fisica')
                es()
                p('• angela')
                p('• alex')    
                p('• angel')
                pause()
                
            elif docente_area == 3:
                p('➤ Sociales')
                es()
                p('• magdalena')
                p('• mario')
                p('• capera')
                pause()
                
            elif docente_area == 4:
                p('➤ Filosofia')
                es()
                p('• capera')
                p('• elsa')
                pause()

            elif docente_area == 5:
                p('➤ Ingles')
                es()
                p('• carlos')
                p('• sara')
                pause()

            elif docente_area == 6:
                p('➤ Edu fisica')
                es()
                p('• sebastian')
                pause()

            elif docente_area == 7:
                p('➤ Religion')
                es()
                p('• luz')
                pause()

            elif docente_area == 8:
                p('➤ Etica')
                es()
                p('• luz')
                pause()

            elif docente_area == 9:
                p('➤ Castellano')
                es()
                p('• magdalena')
                p('• sofia')
                pause() 

            elif docente_area == 10:
                p('➤ Tecnologia')
                es()
                p('• geovanny')
                pause()

            elif docente_area == 11:
                p('➤ Economia y Politica')
                es()
                p('• capera')
                pause()

            elif docente_area == 12:
                p('➤ Matematica')
                es()  
                p('• ruben')
                p('• angela')
                pause()   

            elif docente_area == 13:
                volver()
                break 

class SubmenuEventos:
    def __init__(self):
        self.eventos_1 = Eventos1()
        self.eventos_2 = Eventos2()
        self.eventos_3 = Eventos3()
        self.eventos_4 = Eventos4()
        self.eventos_5 = Eventos5()

    def submenu_eventos(self):
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
                break

class Eventos1:
    def submenu_eventos1(self):
        while True:
            submenu_eventos_1()
            while True:
                try:
                    cultura = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if cultura == 1:
                while True:
                    p('► Dia a desarrollar')
                    es()
                    p('El dia a desarrollar este evento es el 1 de abril')
                    es()
                    odecs1 = salir_s()
                    while odecs1 != 's':
                        odecs1 = salir_s()
                    break     

            elif cultura == 2:
                while True:
                    p('Evento donde los estudiantes presentan bailes, obras de teatro')
                    p('musica y expociciones. objetivgo mostrar los talentos')
                    p('artisticos')
                    es()
                    odecs2 = salir_s()
                    while odecs2 != 's':
                        odecs2 = salir_s()
                    break      


            elif cultura == 3:
                volver()
                break    
class Eventos2:
    def submenu_eventos2(self):
        while True:
            submenu_eventos_2()
            while True:
                try:
                    feria = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if feria == 1:
                while True:
                    p('► Dia a desarrollar')
                    p('El dia a desarrollar este evento es el 20 de agosto')
                    es()
                    odefs1 = salir_s()
                    while odefs1 != 's':
                        odefs1 = salir_s()                
                    break    

            elif feria == 2:
                while True:
                    p('Actividad academica donde los estudiantes presentan')
                    p('experimentos cientificos, sirve para desarrollar la curiosidad,')
                    p('la ivestigacion y el pensamiento critico')
                    es()
                    odefs2 = salir_s()
                    while odefs2 != 's':
                        odefs2 = salir_s()
                    break    

            elif feria == 3:
                volver()
                break    
class Eventos3:
    def submenu_eventos3():
        while True:
            submenu_eventos_3()
            while True:
                try:
                    izada = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if izada == 1:
                while True:
                    p('► Dia a desarrollar')
                    p('Esta actividad se desarrolla cada final de periodo,')
                    p('es decir. abril 15, agosto 21, noviembre 21')
                    es()
                    odeis1 = salir_s()
                    while odeis1 != 's':
                        odeis1 = salir_s()
                    break    

            elif izada == 2:
                while True:
                    p('Acto civico donde donde se rinden honores ala bandera,')
                    p('y se reconocen estudiantes destacados')
                    es()
                    odeis2 = salir_s()
                    while odeis2 != 's':
                        odeis2 = salir_s()
                    break    

            elif izada == 3:
                volver()
                break 

class Eventos4:
    def submenu_eventos4(self):
        while True:
            submenu_eventos_4()
            while True:
                try:
                    independencia = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if independencia == 1:
                while True:
                    p('► Dia a desarrollar')
                    p('El dia de el desarrollo de el evento es')
                    p('20 de agosto')
                    es()
                    odeins1 = salir_s()
                    while odeins1 != 's':
                        odeins1 = salir_s()
                    break

            elif independencia == 2:
                while True:
                    p('Es una actividad donde el colegio conmemora')
                    p('la historia de el pais, con actos civicos')
                    p('memorias culturales')
                    es()
                    odeins2 = salir_s()
                    while odeins2 != 's':
                        odeins2 = salir_s()
                    break    

            elif independencia == 3:
                volver()
                break

class Eventos5:
    def submenu_eventos5(self):
        while True:
            submenu_eventos_5()
            while True:
                try:
                    reunion_acu = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if reunion_acu == 1:
                while True:
                    p('► Dia a desarrollar')
                    p('El dia de el desarrollo es dos dias despues')
                    p('de el final de periodo')
                    p('es decir. abril 15, agosto 21, noviembre 21')
                    es()
                    oders1 = salir_s()
                    while oders1 != 's':
                        oders1 = salir_s()
                    break

            elif reunion_acu == 2:
                while True:
                    p('Reuniones organizadas por el colegio')
                    p('para orientar a los acudientes sobre la educacion,')
                    p('convivencia y desarrollo de los estudiantes')
                    es()
                    oders2 = salir_s()
                    while oders2 != 's':
                        oders2 = salir_s()
                    break    

            elif reunion_acu == 3:
                volver()
                break

class SubmenuDirectivos:
    def __init__(self):
        self.directivo_1 = directivo1()
        self.directivo_2 = directivo2()
        self.directivo_3 = directivo3()
        self.dorectivo_4 = directivo4()

    def submenu_directivos(self):
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
                opciones_directivos[directivos] ()

            elif directivos == 5:
                volver()
                break

class directivo1:   
    def submenu_directivos1(self):
        while True:          
            submenu_directivos_1()
            while True:
                try:
                    Rector = entrada_us()
                    es()
                    break

                except ValueError:
                    error()
            
            if Rector == 1:
                while True:
                    p('► Rector institucional ')
                    p('jhon jairo vernal')
                    es()
                    oddrs1 = salir_s()
                    while oddrs1 != 's':
                        oddrs1 = salir_s()
                    break

            elif Rector == 2:
                while True:
                    p('► Funcion rector')
                    p('Es la maxima autoridad de el colegio se encarga')
                    p('de dirigir la institucion, tomar deciciones y supervisar')
                    p('el funcionamiento de el colegio')
                    es()
                    oddrs2 = salir_s()
                    while oddrs2 != 's':
                        oddrs2 = salir_s()
                    break    

            elif Rector == 3:
                volver()
                break

class directivo2:
    def submenu_directivos2(self):
        while True:
            submenu_directivos_2()
            while True:
                try:
                    Coordinador = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if Coordinador == 1:
                while True:
                    p('► Cordinador')
                    p('elder sanchez')
                    es()
                    oddcs1 = salir_s()
                    while oddcs1 != 's':
                        oddcs1 = salir_s()
                    break

            elif Coordinador == 2:
                while True: 
                    p('► Funciones rector')
                    p('se encarga de organizar las clases, horarios')
                    p('materias, y actividades academicas')
                    p('tambien supervisa el trabajo de docente')
                    es()
                    oddcs2 = salir_s()
                    while oddcs2 != 's':
                        oddcs2 = salir_s()
                    break

            elif Coordinador == 3:
                volver()
                break       

class directivo3:
    def submenu_directivos3(self):
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

            if psicologa == 1:
                while True:
                    p('► Psicologa')
                    p('tatiana mendes')
                    es()
                    oddps1 = salir_s()
                    while oddps1 != 's':
                        oddps1 = salir_s()
                    break    

            elif psicologa == 2:
                while True:
                    p('► funciones psicologa')
                    p('Se encarga principalmente de ayudar al bienestar emocional,')
                    p('social y academico de los estudiantes')
                    es()
                    oddps2 = salir_s()
                    while oddps2 != 's':
                        oddps2 = salir_s()
                    break 

            elif psicologa == 3:
                volver()
                break       

class directivo4:
    def submenu_directivos4(self):
        while True:
            submenu_directivos_4()
            while True:
                try:
                    secretario = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if secretario == 1:
                while True:
                    p('► Secretario academico')
                    p('carlos ruben espitia')
                    es()
                    oddss1 = salir_s()
                    while oddss1 != 's':
                        oddss1 = salir_s()
                    break 

            elif secretario == 2:
                while True:
                    p('► funciones secretario academico') 
                    p('Se encarga de las bases de datos,l registrar nuevos estudiantes')
                    es()
                    oddss2 = salir_s()
                    while oddss2 != 's':
                        oddss2 = salir_s()
                    break

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

    def menu_coordinador(self):
        while True:
            try:
                es()
                contraseña_coordinador = int(input('¡!Hola cordinador por favor dijita tu clave!¡:'))
                while contraseña_coordinador != 202601:
                    es()
                    contraseña_coordinador = int(input('?Acaso no eres el cordinador¿'))
                    es()
                break

            except ValueError:
                es()
                error()
                es()

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
                5: self.guardado.menu.menu_guardado
            }

            if opcion_coordinador in opciones_coordinador:
                opciones_coordinador[opcion_coordinador]()

            elif opcion_coordinador == 6:
                salir()
                break

class compromisos_:
    def compromisos(self):
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
                break

class reuniones_:
    def reuniones(self):
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
                break

class Acudiente:
    def __init__(self):
        self.docentes = Docente_por_area()
        self.directivos = SubmenuDirectivos()
        self.eventos = SubmenuEventos()
        self.estudiantes_grado = mostrar_estudiantes()
        self.ver = mostrar_estudiantes()

    def menu_acudiente(self):        
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
                break

class guardar_estudiante:
    def __init__(self):
        self.estudiante = {}

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
            "Apellido": self.apellido

        }

        
        with open("estudiantes.json", "r") as f:
            self.estudiantes = json.load(f)

        self.estudiantes.setdefault(self.grado, {})
        self.estudiantes[self.grado].setdefault(self.curso, [])
        self.estudiantes[self.grado][self.curso].append(nuevo)

        with open("estudiantes.json", "w") as f:
            json.dump(self.estudiantes, f, indent=4)


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
                break

class estudiante_ver:
    def opcion_usuario(self):
        while True:
            grado_usuario = str(input('Dijita el grado: ')).strip()
            es()
            curso_usuario = str(input('Dijita el curso: ')).strip()
            with open("estudiantes.json", "r") as f:
                archivo = json.load(f)

            if grado_usuario in archivo:
                if curso_usuario in archivo[grado_usuario]:
                    lista = archivo[grado_usuario][curso_usuario]
                    for i ,estudiante in enumerate(lista, start=1):
                        es()
                        p(f"Grado:{grado_usuario}")
                        p(f"    Curso: {curso_usuario}")
                        es()
                        print(f"{i}: {estudiante["Nombre"]}{estudiante["Apellido"]}")
                else:
                    p('[ERROR] Ese curso no existe: ')
            else:
                p('[ERROR] Ese grado no existe: ')
            pause()
            break
   
class Menu_Estudiante:
    def __init__(self):
        self.areas_temas = SubmenuAreas()
        self.directivos = SubmenuDirectivos()
        self.estudiantes_grado = mostrar_estudiantes()
        self.ver = mostrar_estudiantes()

    def menu_estudiante(self):
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
                break

class Menu_herramientas:
    def __init__(self):
        self.fallo_es = fallas()
    def menu_herramientas(self):
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
                                break

                    elif opcion_juegos == 3:
                        volver()
                        break

            elif opcion_herramientas == 4:
                salir()
                break

class MenuInfo:
    def __init__(self):
        self.fallo_es = fallas()       
    def menu_info(self):
        while True:
            try:
                es()
                with open("info.txt", "r") as archivo:
                    for linea in archivo:
                        p(linea.strip())
                sa = int(input('Escribe 1* para salir:'))
                while sa != 1:
                    sa = int(input('!¡Escribe 1 para salir¡!:'))
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

    def Menu_rector(self):
        while True:
            try:
                es()
                contraseña_rector = int(input('¡!Hola rector!¡, Por favor dijita la clave:'))
                while contraseña_rector != 202600:
                    es()
                    contraseña_rector = int(input('[ERROR]!Clave incorrecta¡:'))
                    es()
                break

            except ValueError:
                error()

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
                6: self.ver.ver_estudiante

            }

            if opcion_rector in rector:
                rector[opcion_rector]()
                
            elif opcion_rector == 7:
                salir()
                break

class pantalla_principal:
    def __init__(self, sistema):
        self.sistema = sistema

    def menu_principal(self):
        while True:
            try:
                v()
                colegio = str(input('Por favor escribe colegio python para continuar:')).lower()
                break

            except EOFError:
                Eof()             

        while colegio != 'colegio python':
            es()
            colegio = str(input('[ERROR] colegio incorrecto:')).lower()
            es()

        while True:
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

            else:
                error_usuario()

empezar = Sistema_escolar()
empezar.iniciar()


