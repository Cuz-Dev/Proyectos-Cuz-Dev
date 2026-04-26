#🧮Sistema escolar dev-v2026.0.8
#🚀desarrollador Cuz-Dev🚀
#🌪️Si lo puedes imaginar lo puedes programar🌪️        
def p(mensaje):
        print(mensaje)

def v():
    es()
    p('v2026.0.8')

def es():
    print('     ')

def pause():
    es()
    input('Presiona enter para salir <')
    es()

def error():
    es()
    p('[ERROR 505] Debes escribir un numero no una letra')
    es()

def volver():
    p('<<<<')
    es()

def salir():
    p('Saliendo*.*')
    es()

def Eof():
    p('[ERROR 404] Existe un error con tu compilador:') 

def salir_s():
    return str(input('Escribe s para salir:')).lower().strip()

def entrada_us():
    return int(input('dijita numero de opcion:'))

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
    import estudiantes
    from estudiantes import calculadora
    from estudiantes import Number_hunter
    from estudiantes import Piedra_papel_tijera
    from estudiantes import generador_contraseñas_seguras
        

except ModuleNotFoundError:
    obj = fallas()
    obj.failed_file_es()

class Sistema_escolar:
    def __init__(self):
        self.pantalla = pantalla_principal(self)
        self.docente = MenuDocente()
        self.coordinador = MenuCoordinador()
        self.acudiente = Acudiente()
        self.estudiante = Menu_Estudiante()
        self.herramientas = Menu_herramientas()
        self.menu_fallos_es = fallas()
        self.info = MenuInfo()
        self.RECTOR = MenuRector()

    def iniciar(self):
        self.pantalla.menu_principal()

class MenuDocente:
    def __init__(self,):
        self.areas = SubmenuAreas()
        self.eventos = SubmenuEventos()
        self.directivos = SubmenuDirectivos()
        self.estudiantes_grado = grado()

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
            es()
            p('────────────────────────────────────────────────')           
            p('              Bienvenido profe                  ')
            p('────────────────────────────────────────────────')
            es()
            p('------------------------------------------------')
            p('          MENU DE OPCIONES DOCENTE')
            p('------------------------------------------------')
            p('□ opciones □')
            p('[1] Ver areas')
            p('[2] Eventos')
            p('[3] Directivos')
            p('[4] Estudiantes')
            p('[5] << Salir')
            p('=*=*^=*=*=^=*=*=^')
            es()
            while True:
                try:
                    opcion_docente = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if opcion_docente == 1:
                self.areas.submenu_areas()

            elif opcion_docente == 2:
                self.eventos.submenu_eventos()

            elif opcion_docente == 3:
                self.directivos.submenu_directivos()

            elif opcion_docente == 4:
                self.estudiantes_grado.grados()

            elif opcion_docente == 5:
                salir()
                break
    
class SubmenuAreas:
    def submenu_areas(self):
        while True:           
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            p('           Areas                ')
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            es()
            p('□ temas de cada area □')
            es()
            p('(1) Naturales')
            p('(2) Fisica')
            p('(3) Sociales')
            p('(4) Filosofia')
            p('(5) Ingles')
            p('(6) Edu Fisica')
            p('(7) Religion')
            p('(8) Etica')
            p('(9) Castellano')
            p('(10) Tecnologia')
            p('(11) Economia y politica')
            p('(12) Matematicas')
            es()
            p('(13) <<<< Volver')
            es()
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
            p('□ Docentes de area □')
            es()
            p('[1] Naturales')
            p('[2] Fisica')
            p('[3] Sociales')
            p('[4] Filosofia')
            p('[5] Ingles')
            p('[6] Edu Fisica')
            p('[7] Religion')
            p('[8] Etica')
            p('[9] Castellano')
            p('[10] Tecnologia')
            p('[11] Economia politica')
            p('[12] Matematicas')
            p('[13] <<<< Volver')
            es()
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
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            p('           Eventos             ')
            p('       Institucionales        ')
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            es()
            p('[1] Dia cultura')
            p('[2] Feria de la ciencia')
            p('[3] Izada de bandera')
            p('[4] Dia de la independencia')
            p('[5] Reunion de padres de familia')
            p('[6] << Volver')
            es()
            while True:
                try:
                    eventos = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if eventos == 1:
                self.eventos_1.submenu_eventos1()

            elif eventos == 2:
                self.eventos_2.submenu_eventos2()

            elif eventos == 3:
                self.eventos_3.submenu_eventos3()

            elif eventos == 4:
                self.eventos_4.submenu_eventos4()

            elif eventos == 5:
                self.eventos_5.submenu_eventos5()

            elif eventos == 6:
                volver()
                break

class Eventos1:
    def submenu_eventos1(self):
        while True:
            p('➤ Dia de la cultura')
            es()
            p('[1] Ver dia')
            p('[2] Explicacion')
            p('[3] << Volver')
            es()
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
            p('➤ Feria de la ciencia')
            es()
            p('[1] Ver dia')
            p('[2] Explicacion')
            p('[3] << Volver')
            es()
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
            p('➤ Izada de bandera')
            es()
            p('[1] Ver dias')
            p('[2] Explicacion')
            p('[3] << Volver')
            es()
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
            p('➤ Dia de la independencia')
            es()
            p('[1] Ver dias')
            p('[2] Explicacion')
            p('[3] << Volver')
            es()
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
            p('➤ Reunion de acudientes')
            es()
            p('[1] Ver dias')
            p('[2] Explicacion')
            p('[3] << Volver')
            es()
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
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~') 
            p('         Directivos            ')
            p('       institucionales         ')
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            es()
            p('[1] Rector')
            p('[2] Cordinador')
            p('[3] Psicologa')
            p('[4] Secretario academico')
            p('[5] << Volver')
            es()
            while True:
                try:
                    directivos = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if directivos == 1:
                self.directivo_1.submenu_directivos1()

            elif directivos == 2:
                self.directivo_2.submenu_directivos2()

            elif directivos == 3:
                self.directivo_3.submenu_directivos3()

            elif directivos == 4:
                self.dorectivo_4.submenu_directivos4()

            elif directivos == 5:
                volver()
                break

class directivo1:   
    def submenu_directivos1(self):
        while True:          
            p('➤ RECTOR ')
            es()
            p('[1] Persona acargo')
            p('[2] Funcion')
            p('[3] << Volver')
            es()
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
            p('➤ CORDINADOR')
            es()
            p('[1] Persona acargo')
            p('[2] Funcion')
            p('[3] <<<< Volver')
            es()
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
            p('➤ PSICOLOGA')
            es()
            p('[1] Persona acargo')
            p('[2] Funcion')
            p('[3] <<<< Volver')
            es()
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
            p('➤ SECRETARIO ACADEMICO')
            es()
            p('[1] Persona acargo')
            p('[2] Funcion')
            p('[3] <<<< Volver')
            es()
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
        self.estudiantes_grado = grado()

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
            p('────────────────────────────────────────────────')
            p('               Bienvenido cordinador            ')
            p('────────────────────────────────────────────────')
            p('------------------------------------------------')
            p('                 Menu cordinador                ')
            p('------------------------------------------------')
            p('[1] Compromisos')
            p('[2] Reuniones')
            p('[3] Docentes disponibles en plantel por area')
            p('[4] Estudiantes')
            p('[5] <<<< Salir')
            p('=*=*^=*=*=^=*=*=^')
            es()
            while True:
                try:
                    opcion_coordinador = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if opcion_coordinador == 1:
                self.Sub_menu_compromisos.compromisos()

            elif opcion_coordinador == 2:
                self.Sub_menu_reuniones.reuniones()

            elif opcion_coordinador == 3:
                self.docentes_disponibles.submenu_docentes_area()

            elif opcion_coordinador == 4:
                self.estudiantes_grado.grados()

            elif opcion_coordinador == 5:
                salir()
                break

class compromisos_:
    def compromisos(self):
        while True:
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            p('        Compromisos           ')
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            p('[1] Velar por la disciplina')
            p('[2] Apoyar a los docentes')
            p('[3] Supervisar procesos')
            p('[4] Atender a estudiantes y padres')
            p('[5] Cordinar actividades institucionales')
            p('[6] <<<< Volver')
            p('=*=*^=*=*=^=*=*=^')
            while True:
                try:
                    es()
                    Compromisos = entrada_us()
                    es()
                    break

                except ValueError:
                    error()            

            if Compromisos == 1:
                p('➤ Velar por la disciplina')
                p('Garantizar que los estudiantes cumplan con las normas')
                p('manual de convivencia de la institucion.')
                pause()

            elif Compromisos == 2:
                p('➤ Apoyar a los docentes')
                p('Ayudar a los profesores en la organizacion de actividades academicas,')
                p('y resolver situaciones dentro del aula.')
                pause()

            elif Compromisos == 3:
                p('➤ Supervisar procesos academicos')
                p('Revisar que las clases, evaluaciones y actividades educativas')
                p('se desarrollen correctamente.')
                pause()

            elif Compromisos == 4:
                p('➤ Atender a estudiantes y padres de familia')
                p('Escuchar problemas, inquietudes o conflictos de estudiantes ')
                p('y acudientes para buscar soluciones')
                pause()

            elif Compromisos == 5:
                p('➤ Coordinar actividades isntitucionales')
                p('Organizar eventos academicos, reuniones, proyectos educativos')
                p('y actividades escolares')
                pause()

            elif Compromisos == 6:
                volver()
                break

class reuniones_:
    def reuniones(self):
        while True:
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            p('          Reuniones           ')
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            p('[1] Reuniones con docentes')
            p('[2] Reunion con padres de familia')
            p('[3] Reunion de convivencia escolar')
            p('[4] Reunion de seguimiento academico')
            p('[5] Reunion con directivos')
            p('[6] <<<< Volver')
            p('=*=*^=*=*=^=*=*=^')
            es()
            while True:
                try:
                    Reuniones = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if Reuniones == 1:
                p('➤ Reunion con docentes')
                p('• Rendimientos academico de los estudiantes')
                p('• Planificar clases')
                p('• Actividades escolares')
                pause()

            elif Reuniones == 2:
                p('➤ Reunion con padres de familia')
                p('• Imformar sobre el comportamiento de los estudiantes')
                p('• Explicar el progreso academico')
                p('• Resolver inquietudes de los acudientes')
                pause()
                
            elif Reuniones == 3:
                p('➤ Reunion de convivencia escolar')
                p('• Tratar conflictos entre estudiantes')
                p('• Normas del colegio')
                p('• Mejora deel ambiente escolar')
                pause()

            elif Reuniones == 4:
                p('➤ Reunion de seguimiento academico')
                p('• Rendimiento de los estudiantes')
                p('• Dificultades en ciertas materias')
                p('• Estrategias para mejorar el aprendisaje')
                pause()

            elif Reuniones == 5:
                p('➤ Reunion con directivos')
                p('• El cordinador se reune con el rector y otros responsables')
                p('• para planificar actividades y desiciones de el')
                p('• colegio')
                pause()

            elif Reuniones == 6:
                volver()
                break

class Acudiente:
    def __init__(self):
        self.docentes = Docente_por_area()
        self.directivos = SubmenuDirectivos()
        self.eventos = SubmenuEventos()
        self.estudiantes_grado = grado()

    def menu_acudiente(self):        
        while True:
            p('────────────────────────────────────────────────')
            p('           Bienvenido acudiente                 ')
            p('────────────────────────────────────────────────')
            p('------------------------------------------------')
            p('              Menu acudiente                     ')
            p('------------------------------------------------')
            p('[1] Estudiantes')
            p('[2] Docentes')
            p('[3] Directivos')
            p('[4] Eventos')
            p('[5] <<<< salir')
            es()
            while True:
                try:
                    opcion_acudiente = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if opcion_acudiente == 1:
                self.estudiantes_grado.grados()

            elif opcion_acudiente == 2:
                self.docentes.submenu_docentes_area()
                
            elif opcion_acudiente == 3:
                self.directivos.submenu_directivos()

            elif opcion_acudiente == 4:
                self.eventos.submenu_eventos()

            elif opcion_acudiente == 5:
                salir()
                break

class grado:
    def __init__(self):
        self.sexto = grado_sexto()
        self.septimo = grado_septimo()
        self.octavo = grado_octavo()
        self.noveno = grado_noveno()
        self.decimo = grado_decimo()
        self.undecimo = grado_undecimo()

    def grados(self):        
        while True:
            p('[1] Grado sexto')
            p('[2] Grado septimo')   
            p('[3] Grado octavo')
            p('[4] Grado noveno')
            p('[5] Grado decimo')
            p('[6] Grado once')
            p('[7] <<<< Volver')
            es()
            while True:
                try:
                    opcion_grado = entrada_us()
                    es()
                    break

                except ValueError:
                    error()
            if opcion_grado == 1:
                self.sexto.estudiantes_1()

            elif opcion_grado == 2:
                self.septimo.estudiantes_2()

            elif opcion_grado == 3:
                self.octavo.estudiantes_3()

            elif opcion_grado == 4:
                self.noveno.estudiantes_4()

            elif opcion_grado == 5:
                self.decimo.estudiantes_5()

            elif opcion_grado == 6:
                self.undecimo.estudiantes_6()

            elif opcion_grado == 7:
                volver()
                break
            
class grado_sexto:
    def estudiantes_1(self):
        def __init__(self):
            self.fallo_es = fallas()
        while True:
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            p('           Sexto              ')
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            p('[1] Sexto 1')
            p('[2] Sexto 2')
            p('[3] Sexto 3')
            p('[4] <<<< Volver')
            es()
            while True:
                try:
                    opcion_sexto = entrada_us()
                    es()
                    break

                except  ValueError:
                    error()

            if opcion_sexto == 1:
                while  True:
                    p('[1] Ver estudiantes')
                    p('[2] <<<< Volver')
                    es()
                    while True:
                        try:
                            opcion_s1 = entrada_us()
                            es()
                            break

                        except ValueError:
                            error()

                    if opcion_s1 == 1:
                        while True:
                            try:
                                for eg61 in estudiantes.gd61:
                                    p(eg61)
                                    es()
                                eg61s = salir_s()
                                while eg61s != 's':
                                    eg61s = salir_s()
                                break

                            except ModuleNotFoundError:
                                self.fallo_es.failed_file_es()

                    elif opcion_s1 == 2:
                        volver()
                        break

            elif opcion_sexto == 2:
                while True:
                    p('[1] Ver estudiantes')
                    p('[2] <<<< Volver')
                    es()
                    while True:
                        try:
                            opcion_s2 = entrada_us()
                            es()
                            break

                        except ValueError:
                            error()
                                    
                    if opcion_s2 == 1:
                        while True:
                            try:
                                for eg62 in estudiantes.gd62:
                                    p(eg62)
                                    es()
                                eg62s = salir_s()
                                while eg62s != 's':
                                    eg62s = salir_s()    
                                break

                            except ModuleNotFoundError:
                                self.fallo_es.failed_file_es()
                                    
                    elif opcion_s2 == 2:
                        volver()
                        break
                                        

            elif opcion_sexto == 3:
                while True:
                    p('[1] Ver estudiantes')
                    p('[2] <<<< Volver')
                    es()
                    while True:
                        try:
                            opcion_s3 = entrada_us()
                            es()
                            break

                        except ValueError:
                            error()

                    if opcion_s3 == 1:
                        while True:
                            try:
                                for eg63 in estudiantes.gd63:
                                    p(eg63)
                                    es()
                                eg63s = salir_s()
                                while eg63s != 's':
                                    eg63s = salir_s()
                                break    

                            except ModuleNotFoundError:
                                self.fallo_es.failed.file_es()

                    elif opcion_s3 == 2:
                        volver()
                        break
                                
            elif opcion_sexto == 4:
                volver()
                break

class grado_septimo:
    def estudiantes_2(self):
        def __init__(self):
            self.fallo_es = fallas()
        while True:
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            p('         Septimo              ')
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            p('[1] Septimo 1')
            p('[2] Septimo 2')
            p('[3] Septimo 3')
            p('[4] <<<< Volver')
            es()
            while True:
                try:
                    opcion_septimo = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if opcion_septimo == 1:
                while True:
                    p('[1] Ver estudiantes')
                    p('[2] <<<< Volver')
                    es()
                    while True:
                        try:
                            opcion_sp1 = entrada_us()
                            es()
                            break

                        except ValueError:
                            es()
                            error()                        
                            es()

                    if opcion_sp1 == 1:
                        while True:
                            try:
                                for eg71 in estudiantes.gd71:
                                    p(eg71)
                                es()
                                eg71s = salir_s()
                                while eg71s != 's':
                                    eg71s = salir_s()
                                break

                            except  ModuleNotFoundError:
                                self.fallo_es.failed_file_es()

                    elif opcion_sp1 == 2:
                        volver()
                        break     

            elif opcion_septimo == 2:
                while True:
                    p('[1] Ver estudiantes')
                    p('[2] <<<< Volver')
                    es()
                    while True:
                        try:
                            opcion_sp2 = entrada_us()
                            es()
                            break

                        except ValueError:
                            error() 

                    if opcion_sp2 == 1:
                        while True:
                            try:
                                for eg72 in estudiantes.gd72:
                                    p(eg72)
                                    es()
                                eg72s = salir_s()
                                while eg72s != 's':
                                    eg72s = salir_s()
                                break

                            except ModuleNotFoundError:
                                self.fallo_es.failed_file_es()


                    elif opcion_sp2 == 2:
                        volver()
                        break
                                
            elif opcion_septimo == 3:
                while True:
                    p('[1] Ver estudiantes')
                    p('[2] <<<< Volver')
                    es()
                    while True:
                        try:
                            opcion_sp3 = entrada_us()
                            es()
                            break

                        except ValueError:
                            error()

                    if opcion_sp3 == 1:
                        while True:
                            try:
                                for eg73 in estudiantes.gd73:
                                    p(eg73)
                                    es()
                                eg73s = salir_s()
                                while eg73s != 's':
                                    eg73s = salir_s()
                                break

                            except ModuleNotFoundError:
                                self.fallo_es.failed_file_es()

                    elif opcion_sp3 == 2:
                        volver()
                        break
                                        
            elif opcion_septimo == 4:
                volver()
                break

class grado_octavo:
    def estudiantes_3(self):
        def __init__(self):
            self.fallo_es = fallas()
        while True:
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            p('          Octavo               ')
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            p('[1] Octavo 1')
            p('[2] Octavo 2')
            p('[3] <<<< Volver')
            while True:
                try:
                    opcion_octavo = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if opcion_octavo == 1:
                while True:
                    p('[1] Ver estudiantes')
                    p('[2] <<<< volver')
                    es()
                    while True:
                        try:
                            opcion_o1 = entrada_us()
                            es()
                            break

                        except ValueError:
                            error()

                    if opcion_o1 == 1:
                        while True:
                            try:
                                for eg81 in estudiantes.gd81:
                                    p(eg81)
                                    es()
                                eg81s = salir_s()
                                while eg81s != 's':
                                    eg81s = salir_s()
                                break

                            except ModuleNotFoundError:
                                self.fallos_es.failed_file_es()    

                    elif opcion_o1 == 2:
                        volver()
                        break
                            
            elif opcion_octavo == 2:
                while True:
                    p('[1] Ver estudiantes')
                    p('[2] <<<< Volver')
                    es()
                    while True:
                        try:
                            opcion_o2 = entrada_us()
                            es()
                            break

                        except ValueError:
                            error()

                    if opcion_o2 == 1:
                        while True:
                            try:
                                for eg82 in estudiantes.gd82:
                                    p(eg82)
                                    es()
                                eg82s = salir_s()
                                while eg82s != 's':
                                    eg82s = salir_s()
                                break

                            except ModuleNotFoundError:
                                self.fallo_es.failed_file_es()         

                    elif opcion_o2 == 2:
                        volver()
                        break


            elif opcion_octavo == 3:
                volver()
                break

class grado_noveno:
    def estudiantes_4(self):
        def __init__(self):
            self.fallo_es = fallas()                 
        while True:
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            p('           Noveno             ')
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            p('[1] Noveno 1')
            p('[2] Noveno 2')
            p('[3] <<<< Volver')
            es()
            while True:
                try:
                    opcion_noveno = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if opcion_noveno == 1:
                while True:
                    p('[1] Ver estudiantes')
                    p('[2] <<<< Volver')
                    es()
                    while True:
                        try:
                            opcion_n1 = entrada_us()
                            es()
                            break

                        except ValueError:
                            error()

                    if opcion_n1 == 1:
                        while True:
                            try:
                                for eg91 in estudiantes.gd91:
                                    p(eg91)
                                    es()
                                eg91s = salir_s()
                                while eg91s != 's':
                                    eg91s = salir_s()
                                break

                            except ModuleNotFoundError:
                                self.fallos_es.failed_file_es()

                    elif opcion_n1 == 2:
                        volver()
                        break

            elif opcion_noveno == 2:
                while True:
                    p('[1] Ver estudiantes')
                    p('[2] <<<< Volver')
                    es()
                    while True:
                        try:
                            opcion_n2 = entrada_us()
                            es()
                            break

                        except ValueError:
                            error()

                    if opcion_n2 == 1:
                        while True:
                            try:
                                for eg92 in estudiantes.gd92:
                                    p(eg92)
                                    es()
                                eg92s = salir_s()
                                while eg92s != 's':
                                    eg92s = salir_s()
                                break

                            except ModuleNotFoundError:
                                self.fallo_es.failed_file_es()

                    elif opcion_n2 == 2:
                        volver()
                        break                                 

            elif opcion_noveno == 3:
                volver()
                break

class grado_decimo:
    def estudiantes_5(self):
        def __init__(self):
            self.fallo_es = fallas()
        while True:
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            p('           Decimo              ')
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            p('[1] Decimo 1')
            p('[2] Decimo 2')
            p('[3] <<<< Volver')
            es()
            while True:
                try:
                    opcion_decimo = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if opcion_decimo == 1:
                while True:
                    p('[1] Ver estudiantes')
                    p('[2] <<<< Volver')
                    es()
                    while True:
                        try:
                            opcion_d1 = entrada_us()
                            es()
                            break

                        except ValueError:
                            error()

                    if opcion_d1 == 1:
                        while True:
                            try:
                                for eg101 in estudiantes.gd101:
                                    p(eg101)
                                    es()
                                eg101s = salir_s()
                                while eg101s != 's':
                                    eg101s = salir_s()
                                break

                            except ModuleNotFoundError:
                                self.fallo_es.failed_file_es()
                                    
                    elif opcion_d1 == 2:
                        volver()
                        break

            elif opcion_decimo == 2:
                while True:
                    p('[1] Ver estudiantes')
                    p('[2] <<<< Volver')
                    es()
                    while True:
                        try:
                            opcion_d2 = entrada_us()
                            es()
                            break

                        except ValueError:
                            error()

                    if opcion_d2 == 1:
                        while True:
                            try:
                                for eg102 in estudiantes.gd102:
                                    p(eg102)
                                    es()
                                eg102s = salir_s()
                                while eg102s != 's':
                                    eg102s = salir_s()
                                break

                            except ModuleNotFoundError:
                                self.fallo_es.failed_file_es()

                    elif opcion_d2 == 2:
                        volver()
                        break

            elif opcion_decimo == 3:
                volver()
                break

class grado_undecimo:
    def estudiantes_6(self):
        def __init__(self):
            self.fallo_es = fallas()
        while True:
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            p('           Undecimo           ')
            p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            p('[1] Undecimo 1')
            p('[2] Undecimo 2')
            p('[3] <<<< Volver')
            es()
            while True:
                try:
                    opcion_undecimo = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if opcion_undecimo == 1:
                while True:
                    p('[1] Ver estudiantes')
                    p('[2] <<<< Volver')
                    es()
                    while True:
                        try:
                            opcion_u1 = entrada_us()
                            es()
                            break

                        except ValueError:
                            error()

                    if opcion_u1 == 1:
                        while True:
                            try:
                                for eg111 in estudiantes.gd111:
                                    p(eg111)
                                    es()
                                eg111s = salir_s()
                                while eg111s != 's':
                                    eg111s = salir_s()
                                break

                            except ModuleNotFoundError:
                                self.fallo_es.failed_file_es()

                    elif opcion_u1 == 2:
                        volver()
                        break

            elif opcion_undecimo == 2:
                p('[1] Ver estudiantes')
                p('[2] <<<< Volver')
                es()
                while True:
                    try:
                        opcion_u2 = entrada_us()
                        es()
                        break

                    except ValueError:
                        error()
                    
                if opcion_u2 == 1:
                    while True:
                        try:
                            for eg112 in estudiantes.gd112:
                                p(eg112)
                                es()
                            eg112s = salir_s()
                            while eg112s != 's':
                                eg112s = salir_s()
                            break

                        except ModuleNotFoundError:
                            self.fallo_es.failed_file_es()       

                elif opcion_u2 == 2:
                    volver()
                    break    

            elif opcion_undecimo == 3:
                volver()
                break

class Menu_Estudiante:
    def __init__(self):
        self.areas_temas = SubmenuAreas()
        self.directivos = SubmenuDirectivos()
        self.estudiantes_grado = grado()
    def menu_estudiante(self):
        while True:
            p('────────────────────────────────────────────────')
            p('            Bienvenido estudiante             ')
            p('────────────────────────────────────────────────')
            p('------------------------------------------------')
            p('              Menu estudiantes                  ')
            p('------------------------------------------------')
            p('[1] Temas')
            p('[2] Directivos')
            p('[3] Grados')
            p('[4] <<<< Salir')
            es()
            while True:
                try:
                    opcion_estudiante = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if opcion_estudiante == 1:
                self.areas_temas.submenu_areas()

            elif opcion_estudiante == 2:
                self.directivos.submenu_directivos()
                
            elif opcion_estudiante == 3:
                self.grado_grados()
                
            elif opcion_estudiante == 4:
                salir()
                break

class Menu_herramientas:
    def __init__(self):
        self.fallo_es = fallas()
    def menu_herramientas(self):
        while True:
            p('────────────────────────────────────────────────')
            p('                Herramientas                    ')
            p('────────────────────────────────────────────────')
            es()
            p('[1] Calculadora')
            p('[2] Generador de contraseñas seguras')
            p('[3] Juegos')
            p('[4] <<<< Salir')
            es()
            while True:
                try:
                    opcion_herramientas = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if opcion_herramientas == 1:
                while True:
                    p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    p('        Calculadora')
                    p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    es()
                    p('[1] iniciar calculadora')
                    p('[2] <<<< Volver')
                    es()
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
                    p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    p('         Generador de contraseñas segurastas                ')
                    p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    es()
                    p('[1] Empezar')
                    p('[2] <<<< Volver')
                    es()
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
                    p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    p('             Juegos           ')
                    p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    es()
                    p('[1] Number Hunter')
                    p('[2] Piedra papel o tijera')
                    p('[3] <<<< Volver')
                    es()
                    while True:
                        try:
                            opcion_juegos = entrada_us()
                            es()
                            break

                        except ValueError:
                            error()

                        if opcion_juegos == 1:
                            while True:
                                p('➤ Number hunter')
                                es()
                                p('[1] Iniciar juego')
                                p('[2] <<<< Volver')
                                es()
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
                                            break

                                        except ModuleNotFoundError:
                                            self.fallo_es.failed_file_es()

                                elif opcion_number_hunter == 2:
                                    volver()
                                    break    

                        elif opcion_juegos == 2:
                            Piedra_papel_tijera()

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
        self.estudiantes_por_grado = grado()

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
            es()
            p('────────────────────────────────────────────────')
            p('            Bienvenido rector                 ')
            p('────────────────────────────────────────────────') 
            es()
            p('------------------------------------------------')
            p('           MENU DE OPCIONES RECTOR              ')
            p('------------------------------------------------')
            p('□ opciones □')
            p('[1] Areas')
            p('[2] Docentes disponibles')
            p('[3] Eventos')
            p('[4] Directivos')
            p('[5] Estudiantes')
            p('[6] <<<< Salir')
            es()
            while True:
                try:
                    opcion_rector = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            if opcion_rector == 1:
                self.areas_Temas.submenu_areas()

            elif opcion_rector == 2:
                self.docentes_Area.submenu_docentes_area()

            elif opcion_rector == 3:
                self.eventos_I.submenu_eventos()

            elif opcion_rector == 4:
                self.directivos_I.submenu_directivos()

            elif opcion_rector == 5:
                self.estudiantes_por_grado.grados()

            elif opcion_rector == 6:
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
            p('════════════════════════════════════════════════')
            p('         SISTEMA ESCOLAR V2026.0.8')
            p('════════════════════════════════════════════════')
            es()
            p('=============================================')
            p("        Bienvenido al sistema                ")
            p('=============================================')
            es()
            p('◉ Coordinador')
            p('◉ Rector')
            p('◉ Docente')
            p('◉ Estudiante')
            p('◉ Acudiente')
            p('◉ herramientas')
            p('◉ info')
            es()
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

empezar = Sistema_escolar()
empezar.iniciar()

