# Funciones sistema escolar
def pause():
    es()
    input('Presiona enter para salir <')
    es()

def es():
    print('    ')

import turtle
def cuadrado():
    pantalla = turtle.Turtle()
    pantalla.begin_fill()
    for i in range(4):
        pantalla.forward(50)
        pantalla.left(90)
    pantalla.end_fill()
    print(i)

def menu_docente():
    es()
    linea_menu()
    p('              Bienvenido profe                  ')
    linea_menu()
    es()
    linea_menu2()
    p('          MENU DE OPCIONES DOCENTE')
    linea_menu2()
    es()
    p('□ opciones □')
    es()
    p('[1] Ver areas   | [4] Estudiantes        | [7] <<<< salir')
    p('[2] Eventos     | [5] Añadir estudiante')
    p('[3] Directivos  | [6] Notas estudiante')
    es()

def login_docente():
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

def temas_1():
    p('➤ Temas ciencias naturales')
    p('• Animales        | • Quimica')
    p('• Celulas         | • Laboratorio')
    p('• Medio ambiente')
    pause()

def temas_2():
    p('➤ Temas fisica materia')
    es()
    p('• Mru        |• Unidades de medida')
    p('• Factores de conversion')
    pause()

def temas_3():
    p('➤ Temas sociales')
    es()
    p('• Imperialismo')
    p('• Socialismo')
    p('• Comunismo')
    p('• Nacionalismos')
    pause()

def temas_4():
    p('➤ Temas filosofia')
    es()
    p('• Inicios de la filosofia')
    p('• Principales pensadores de la edad media')
    pause()

def temas_5():
    p('➤ Temas ingles')
    es()
    p('• Verb to be')
    p('• Lisenig')
    p('• Read')
    pause()

def temas_6():
    p('➤ Temas edu. fisica')
    es()
    p('• Juegos tradicionales')
    p('• Historia de el basquetball')
    p('• Historia de el fottball')
    pause()

def temas_7():
    p('➤ Temas religion')
    es()    
    p('• Sin sentidos')
    p('• Sentidos')
    p('• Yo pertenezco a jesus')
    pause()

def temas_8():
    p('➤ Temas etica')
    es()
    p('• Sentimientos')
    p('• Perdon')
    p('• Valores')
    pause()

def temas_9():
    p('➤ Temas  castellano')
    es()
    p('• La vida feliz')
    p('• La metarmofosis')
    p('• Noches blancas')
    pause()

def temas_10():
    p('➤ Temas tecnologia')
    es()
    p('• Diagrama de flujo')
    p('• Makecode')
    p('• Python')
    pause()

def temas_11():
    p('➤ Temas ciencias economicas y politicas')
    es()
    p('• Pensadores')
    p('• Origen')
    p('• Importancia')
    pause()

def temas_12():
    p('➤ Temas matematicas')
    es()
    p('• Seno')
    p('• Coseno')
    p('• Tangente')
    pause()

temas_area_lista = [temas_1, temas_2, temas_3, temas_4, temas_5, temas_6, temas_7, temas_8, temas_9, temas_10, temas_11, temas_12]             
def submenu_areas_():
    linea_submenu()
    p('           Areas                ')
    linea_submenu()
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

def submenu_docentes_area_():
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

def submenu_eventos_():
    linea_submenu()
    p('           Eventos             ')
    p('       Institucionales        ')
    linea_submenu()
    es()
    p('[1] Dia cultura')
    p('[2] Feria de la ciencia')
    p('[3] Izada de bandera')
    p('[4] Dia de la independencia')
    p('[5] Reunion de padres de familia')
    p('[6] << Volver')
    es()

def cultura_1():
    while True:
        p('► Dia a desarrollar')
        es()
        p('El dia a desarrollar este evento es el 1 de abril')
        es()
        odecs1 = salir_s()
        while odecs1 != 's':
            odecs1 = salir_s()
        break

def cultura_2():
    while True:
        p('Evento donde los estudiantes presentan bailes, obras de teatro')
        p('musica y expociciones. objetivgo mostrar los talentos')
        p('artisticos')
        es()
        odecs2 = salir_s()
        while odecs2 != 's':
            odecs2 = salir_s()
        break

def feria_1():
    while True:
        p('► Dia a desarrollar')
        p('El dia a desarrollar este evento es el 20 de agosto')
        es()
        odefs1 = salir_s()
        while odefs1 != 's':
            odefs1 = salir_s()                
        break

def feria_2():
    while True:
        p('Actividad academica donde los estudiantes presentan')
        p('experimentos cientificos, sirve para desarrollar la curiosidad,')
        p('la ivestigacion y el pensamiento critico')
        es()
        odefs2 = salir_s()
        while odefs2 != 's':
            odefs2 = salir_s()
        break  

def izada_1():
    while True:
        p('► Dia a desarrollar')
        p('Esta actividad se desarrolla cada final de periodo,')
        p('es decir. abril 15, agosto 21, noviembre 21')
        es()
        odeis1 = salir_s()
        while odeis1 != 's':
            odeis1 = salir_s()
        break

def izada_2():
    while True:
        p('Acto civico donde donde se rinden honores ala bandera,')
        p('y se reconocen estudiantes destacados')
        es()
        odeis2 = salir_s()
        while odeis2 != 's':
            odeis2 = salir_s()
        break  

def independencia_1():
    while True:
        p('► Dia a desarrollar')
        p('El dia de el desarrollo de el evento es')
        p('20 de agosto')
        es()
        odeins1 = salir_s()
        while odeins1 != 's':
            odeins1 = salir_s()
        break

def independencia_2():
    while True:
        p('Es una actividad donde el colegio conmemora')
        p('la historia de el pais, con actos civicos')
        p('memorias culturales')
        es()
        odeins2 = salir_s()
        while odeins2 != 's':
            odeins2 = salir_s()
        break

def reunion_1():
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

def reunion_2():
    while True:
        p('Reuniones organizadas por el colegio')
        p('para orientar a los acudientes sobre la educacion,')
        p('convivencia y desarrollo de los estudiantes')
        es()
        oders2 = salir_s()
        while oders2 != 's':
            oders2 = salir_s()
        break    

eventos_lista = [cultura_1, cultura_2, feria_1, feria_2, izada_1, izada_2, independencia_1, independencia_2, reunion_1, reunion_2]    

def rector_1():
    while True:
        p('► Rector institucional ')
        p('jhon jairo vernal')
        es()
        oddrs1 = salir_s()
        while oddrs1 != 's':
            oddrs1 = salir_s()
        break

def rector_2():
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

def coordinador_1():
    while True:
        p('► Cordinador')
        p('elder sanchez')
        es()
        oddcs1 = salir_s()
        while oddcs1 != 's':
            oddcs1 = salir_s()
        break

def coordinador_2():
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

def psicologa_1():
    while True:
        p('► Psicologa')
        p('tatiana mendes')
        es()
        oddps1 = salir_s()
        while oddps1 != 's':
            oddps1 = salir_s()
        break

def psicologa_2():
    while True:
        p('► funciones psicologa')
        p('Se encarga principalmente de ayudar al bienestar emocional,')
        p('social y academico de los estudiantes')
        es()
        oddps2 = salir_s()
        while oddps2 != 's':
            oddps2 = salir_s()
        break   

def secretario_1():
    while True:
        p('► Secretario academico')
        p('carlos ruben espitia')
        es()
        oddss1 = salir_s()
        while oddss1 != 's':
            oddss1 = salir_s()
        break

def secretario_2():
    while True:
        p('► funciones secretario academico') 
        p('Se encarga de las bases de datos,l registrar nuevos estudiantes')
        es()
        oddss2 = salir_s()
        while oddss2 != 's':
            oddss2 = salir_s()
        break

directivos_lista = [rector_1, rector_2, coordinador_1, coordinador_2, psicologa_1, psicologa_2, secretario_1, secretario_2]    


def docente_area_1():
    p('➤ Ciencias naturales ')
    es()
    p('• dora')
    p('• jhon')
    p('• angelica')
    pause()

def docente_area_2():
    p('➤ Fisica')
    es()
    p('• angela')
    p('• alex')    
    p('• angel')
    pause()

def docente_area_3():
    p('➤ Sociales')
    es()
    p('• magdalena')
    p('• mario')
    p('• capera')
    pause()

def docente_area_4():
    p('➤ Filosofia')
    es()
    p('• capera')
    p('• elsa')
    pause()

def docente_area_5():
    p('➤ Ingles')
    es()
    p('• carlos')
    p('• sara')
    pause()

def docente_area_6():
    p('➤ Edu fisica')
    es()
    p('• sebastian')
    pause()

def docente_area_7():
    p('➤ Religion')
    es()
    p('• luz')
    pause()

def docente_area_8():
    p('➤ Etica')
    es()
    p('• luz')
    pause()

def docente_area_9():
    p('➤ Castellano')
    es()
    p('• magdalena')
    p('• sofia')
    pause()

def docente_area_10():
    p('➤ Tecnologia')
    es()
    p('• geovanny')
    pause()

def docente_area_11():
    p('➤ Economia y Politica')
    es()
    p('• capera')
    pause()

def docente_area_12():
    p('➤ Matematica')
    es()  
    p('• ruben')
    p('• angela')
    pause()

docentes_area = [docente_area_1, docente_area_2, docente_area_3, docente_area_4, docente_area_5, docente_area_6, docente_area_7, docente_area_8, docente_area_9, docente_area_10, docente_area_11, docente_area_12]   

def submenu_eventos_1():
    p('➤ Dia de la cultura')
    es()
    p('[1] Ver dia')
    p('[2] Explicacion')
    p('[3] << Volver')
    es()

def submenu_eventos_2():
    p('➤ Feria de la ciencia')
    es()
    p('[1] Ver dia')
    p('[2] Explicacion')
    p('[3] << Volver')
    es()

def submenu_eventos_3():
    p('➤ Izada de bandera')
    es()
    p('[1] Ver dias')
    p('[2] Explicacion')
    p('[3] << Volver')
    es()

def submenu_eventos_4():
    p('➤ Dia de la independencia')
    es()
    p('[1] Ver dias')
    p('[2] Explicacion')
    p('[3] << Volver')
    es()

def submenu_eventos_5():
    p('➤ Reunion de acudientes')
    es()
    p('[1] Ver dias')
    p('[2] Explicacion')
    p('[3] << Volver')
    es()

def submenu_directivos_():
    linea_submenu() 
    p('         Directivos            ')
    p('       institucionales         ')
    linea_submenu()
    es()
    p('[1] Rector')
    p('[2] Cordinador')
    p('[3] Psicologa')
    p('[4] Secretario academico')
    p('[5] << Volver')
    es()

def submenu_directivos_1():
    p('➤ RECTOR ')
    es()
    p('[1] Persona acargo')
    p('[2] Funcion')
    p('[3] << Volver')
    es()

def submenu_directivos_2():
    p('➤ CORDINADOR')
    es()
    p('[1] Persona acargo')
    p('[2] Funcion')
    p('[3] <<<< Volver')
    es()

def submenu_directivos_3():
    p('➤ PSICOLOGA')
    es()
    p('[1] Persona acargo')
    p('[2] Funcion')
    p('[3] <<<< Volver')
    es()

def submenu_directivos_4():
    p('➤ SECRETARIO ACADEMICO')
    es()
    p('[1] Persona acargo')
    p('[2] Funcion')
    p('[3] <<<< Volver')
    es()

def menu_coordinador_():
    linea_menu()
    p('               Bienvenido cordinador            ')
    linea_menu()
    es()
    linea_menu2()
    p('                 Menu cordinador                ')
    linea_menu2()
    es()
    p('[1] Compromisos        | [4] Estudiantes')
    p('[2] Reuniones          | [5] Añadir estudiantes')
    p('[3] Docentes           | [6] Notas estudiantes')
    p('[5] Añadir estudiantes | [7] <<<< Salir')
    es()

def login_coordinador():
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
            error()

logins = [login_docente, login_coordinador,]

def compromisos_1():
    p('➤ Velar por la disciplina')
    p('Garantizar que los estudiantes cumplan con las normas')
    p('manual de convivencia de la institucion.')
    pause()

def compromisos_2():
    p('➤ Apoyar a los docentes')
    p('Ayudar a los profesores en la organizacion de actividades academicas,')
    p('y resolver situaciones dentro del aula.')
    pause()

def compromisos_3():
    p('➤ Supervisar procesos academicos')
    p('Revisar que las clases, evaluaciones y actividades educativas')
    p('se desarrollen correctamente.')
    pause()

def compromisos_4():
    p('➤ Atender a estudiantes y padres de familia')
    p('Escuchar problemas, inquietudes o conflictos de estudiantes ')
    p('y acudientes para buscar soluciones')
    pause()

def compromisos_5():
    p('➤ Coordinar actividades isntitucionales')
    p('Organizar eventos academicos, reuniones, proyectos educativos')
    p('y actividades escolares')
    pause()

def submenu_compromisos_():
    linea_submenu()
    p('        Compromisos           ')
    linea_submenu()
    p('[1] Velar por la disciplina')
    p('[2] Apoyar a los docentes')
    p('[3] Supervisar procesos')
    p('[4] Atender a estudiantes y padres')
    p('[5] Cordinar actividades institucionales')
    p('[6] <<<< Volver')
    p('=*=*^=*=*=^=*=*=^')

def submenu_reuniones():
    linea_submenu()
    p('          Reuniones           ')
    linea_submenu()
    es()
    p('[1] Reuniones con docentes')
    p('[2] Reunion con padres de familia')
    p('[3] Reunion de convivencia escolar')
    p('[4] Reunion de seguimiento academico')
    p('[5] Reunion con directivos')
    p('[6] <<<< Volver')
    p('=*=*^=*=*=^=*=*=^')
    es()

def reuniones_1():
    p('➤ Reunion con docentes')
    p('• Rendimientos academico de los estudiantes')
    p('• Planificar clases')
    p('• Actividades escolares')
    pause()

def reuniones_2():
    p('➤ Reunion con padres de familia')
    p('• Imformar sobre el comportamiento de los estudiantes')
    p('• Explicar el progreso academico')
    p('• Resolver inquietudes de los acudientes')
    pause()

def submenu_notas():
    linea_menu2()
    p('Notas estudiante')
    linea_menu2()
    es()
    p('[1] Añadir nota estudiante')
    p('[2] Ver nota estudiante')
    p('[3] <<<< Volver')

def reuniones_3():
    p('➤ Reunion de convivencia escolar')
    p('• Tratar conflictos entre estudiantes')
    p('• Normas del colegio')
    p('• Mejora deel ambiente escolar')
    pause()

def reuniones_4():
    p('➤ Reunion de seguimiento academico')
    p('• Rendimiento de los estudiantes')
    p('• Dificultades en ciertas materias')
    p('• Estrategias para mejorar el aprendisaje')
    pause()

def reuniones_5():
    p('➤ Reunion con directivos')
    p('• El cordinador se reune con el rector y otros responsables')
    p('• para planificar actividades y desiciones de el')
    p('• colegio')
    pause()

def menu_acudiente_():
    linea_menu()
    p('           Bienvenido acudiente                 ')
    linea_menu()
    es()
    linea_menu2()
    p('              Menu acudiente                     ')
    linea_menu2()
    es()
    p('[1] Estudiantes')
    p('[2] Docentes')
    p('[3] Directivos')
    p('[4] Eventos')
    p('[5] <<<< salir')
    es()

def submenu_añadir_es():
    linea_submenu()
    p('Sub menu añadir estudiante')
    linea_submenu()
    es()
    p('[1] Añadir estudiante')
    p('[2] <<<< volver')
    es()


def menu_es():
    linea_menu()
    p('            Bienvenido estudiante             ')
    linea_menu()
    es()
    linea_menu2()
    p('              Menu estudiantes                  ')
    linea_menu2()
    es()
    p('[1] Temas')
    p('[2] Directivos')
    p('[3] Grados')
    p('[4] <<<< Salir')
    es()

def menu_herramientas_():
    linea_menu()
    p('                Herramientas                    ')
    linea_menu()
    es()
    p('[1] Calculadora')
    p('[2] Generador de contraseñas seguras')
    p('[3] Juegos')
    p('[4] <<<< Salir')
    es()

def submenu_calculadora_():
    linea_submenu()
    p('        Calculadora')
    linea_submenu()
    es()
    p('[1] iniciar calculadora')
    p('[2] <<<< Volver')
    es()

def submenu_generador():
    linea_submenu()
    p('         Generador de contraseñas segurastas                ')
    linea_submenu()
    es()
    p('[1] Empezar')
    p('[2] <<<< Volver')
    es()


def submenu_juegos_():
    linea_submenu()
    p('             Juegos           ')
    linea_submenu()
    es()
    p('[1] Number Hunter')
    p('[2] Piedra papel o tijera')
    p('[3] <<<< Volver')
    es()

def submenu_juegos_1():
    p('➤ Number hunter')
    es()
    p('[1] Iniciar juego')
    p('[2] <<<< Volver')
    es()


def submenu_juegos_2():
    p('➤ Piedra papel o tijera')
    es()
    p('[1] Iniciar juego')
    p('[2] <<<< Volver')
    es()

def menu_rector_():
    es()
    linea_menu()
    p('            Bienvenido rector                 ')
    linea_menu() 
    es()
    linea_menu2()
    p('           MENU DE OPCIONES RECTOR              ')
    linea_menu2()
    es()
    p('□ opciones □')
    p('[1] Areas     | [5] Agregar estudiantes')
    p('[2] Docentes  | [6] Estudiantes')
    p('[3] Eventos   | [7] Notas estudiante')
    p('[4] Directivos| [8] <<<< Salir')
    es()

def login_rector():
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

def menu_secretario_():
    es()
    linea_menu()
    p('     Menu secretaria institucional ')
    linea_menu()
    es()
    p('[1] Matricular estudiante   |  [3] Directivos')
    p('[2] Ver estudiante          |  [4] <<<< Salir')
    es()


def menu_principal_():
    p('════════════════════════════════════════════════')
    p('                SISTEMA ESCOLAR')
    p('════════════════════════════════════════════════')
    es()
    p('=============================================')
    p("                     v1.1                    ")
    p('=============================================')
    es()
    p('◉ Coordinador | ◉ Estudiante    | ◉ secretaria')
    p('◉ Rector      | ◉ Acudiente     | ◉ info ')
    p('◉ Docente     | ◉ herramientas')
    es()

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
        colegio = str(input('[ERROR] colegio incorrecto:')).lower()
        es()


def p(mensaje):
    print(mensaje)

def v():
    es()
    p('v2026.1.1')

def es():
    print('     ')

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

def entrada_us():
    return int(input('dijita numero de opcion:'))
    
def linea_menu():
    p('────────────────────────────────────────────────')


def linea_menu2():
    p('------------------------------------------------')

def linea_submenu():
    p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def opcion_grado():
    p('[1] Ver estudiantes')
    p('[2] <<<< Volver')
    es()

def error_usuario():
    es()
    p('[ERROR] Nombre de usuario invalido: ')
    es()

def grado_ejemplo():
    p('Ejemplo "10" ')

def curso_ejemplo():
    p('Ejemplo "1" ')

def grado_es():
    return str(input('Dijita el grado: ')).strip()

def curso_es():
    return str(input('Dijita el curso: ')).strip()

def curso_inesistente():
    p('[ERROR] Ese curso no existe: ')

def grado_inesistente():
    p('[ERROR] Ese grado no existe: ')

def generador_contraseñas_seguras():
    menu_contraseñas()
import random
def p(mensaje):
    print(mensaje)
def es():
    p('  ')
def error():
    es()
    p('[ERROR] Debes escribir un numero no una letra')
    es()
def entrada_us():
    return int(input('¡!Por favor escribe numero de opcion!¡:'))
def volver():
    p('<<<<')
    es()
def numero_random():
    return str(random.randint(0,9))
def submenu_invertir():
    es()
    p('[1] invertir contraseña')
    p('[2] Guardar contraseña')
    p('[3] <<<< Volver')
    es()
def salir_s():
    return str(input('Escribe s para salir:')).lower()
def mostrar_generar():
    es()
    p('[1] Empezar a generar 🔥')
    p('[2] <<<< Volver')
    es()

def generando():
    es()
    p('Generando □ ■ ▫ ▪')

def guardando():
    es()
    p('Guardando □ ■ ▫ ▪')
    es()

def guardado_exito():
    es()
    p('Guardado con exito ¡! s' \
    'sEn save password.txt')
    es()

def finalized():
    p('Contraseña finalizada Con exito: ')

simbolos = (
    '#',
    '!',
    '@',
    '$',
    '%',
    '&',
    '¿',
    '?',
    '.',
    ',',
    ':',
    '*'
)

abc = ['a', 'b,' 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
import os

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")

    else:
        os.system("clear")


def letra_random():
    return str(random.choice(abc))

def simbolo_random():
    return str(random.choice(simbolos))

def contraseña4_dijitos():
    while True:
        p('================================================')
        p('         Contraseña de 4 dijitos               ')
        p('================================================')
        es()
        p('[1] Contraseña de 4 dijitos, Numeros')
        p('[2] Contraseña Mixta')
        p('[3] <<<< Volver')
        es()
        while True:
            try:
                es()
                usuario_menu1 = entrada_us()
                break

            except  ValueError:
                error()

        if usuario_menu1 == 1:
            contraseña4_submenu1()

        elif usuario_menu1 == 2:
            contraseña_mixta4_submenu1()

        elif usuario_menu1 == 3:
            volver()
            break

def error_es():
    p('[ERROR 101] No se encuentra el archivo save password.txt')
    p('!¡Sin ese archivo no se puede guardar las contraseñas que crees¡!')

def contraseña4_submenu1():
    while True:
        p('➤ Contraseña Numeros 4 dijitos')
        mostrar_generar()
        while True:
            try:
                es()
                dijitos_4 = entrada_us()
                break

            except ValueError:
                error()

        if dijitos_4 == 1:
            generar4_dijitos()  

        elif dijitos_4 == 2:
            volver()
            break

def generar4_dijitos():
    while True:
        generando()
        es()
        dijito1 = numero_random()
        dijito2 = numero_random()
        dijito3 = numero_random()
        dijito4 = numero_random()
        contraseñan4 = dijito1 + dijito2 + dijito3 + dijito4
        agrupacion = [dijito1, dijito2, dijito3, dijito4]
        print(finalized(), "\n", contraseñan4)
        es()
        submenu_invertir()
        es()
        while True:
            try:
                es()
                opcion_menu_anidadod4 = entrada_us()
                break

            except ValueError:
                error()

        if opcion_menu_anidadod4 == 1:
            anidado_generar4(agrupacion)

        elif opcion_menu_anidadod4 == 2:
            guardar_dijitos4(contraseñan4)

        elif opcion_menu_anidadod4 == 3:
            volver()
            break

def guardar_dijitos4(contraseñan4):
    while True:
        guardando()
        try:
            with open("save password.txt", "a") as password4:
                password4.write(contraseñan4 + "\n")
            guardado_exito()
            salir_guardar_dijitos4 = salir_s()
            while salir_guardar_dijitos4 != 's':
                salir_guardar_dijitos4 = salir_s()
            break

        except ModuleNotFoundError:
            error_es()

def anidado_generar4(agrupacion):
    while True:
        generando()
        es()
        def agrupacion1():
            return str(random.choice(agrupacion))
        dijito1e = agrupacion1()
        dijito2e = agrupacion1()
        dijito3e = agrupacion1()
        dijito4e = agrupacion1()
        contraseñan4e = dijito1e + dijito2e + dijito3e + dijito4e
        print(finalized(), "\n", contraseñan4e)
        es()
        p('[1] Guardar')
        p('[2] <<<< Volver')
        es()
        while True:
            try:
                es()
                anidado_generar4e = entrada_us()
                break

            except ValueError:
                error()

        if anidado_generar4e == 1:
            guardar_dijitos4e(contraseñan4e)

        elif anidado_generar4e == 2:
            volver()
            break

def guardar_dijitos4e(contraseñan4e):
    while True:
        guardando()
        try:
            with open("save password.txt", "a") as password4e:
                password4e.write(contraseñan4e + "\n")
            guardado_exito()
            salir_guardar_dijitos4e = salir_s()
            while salir_guardar_dijitos4e != 's':
                salir_guardar_dijitos4e = salir_s()
            break

        except ModuleNotFoundError:
            error_es()

def contraseña_mixta4_submenu1():
    while True:
        p('➤ Contraseña 4 dijitos mixta')
        es()
        mostrar_generar()
        es()
        while True:
            try:
                mixta4_submenu1 = entrada_us()
                es()
                break

            except ValueError:
                error()

        if mixta4_submenu1 == 1:
            generar_contraseña_mixta4()

        elif mixta4_submenu1 == 2:
            volver()
            break

def generar_contraseña_mixta4():
    while True:
        generando()
        caracter1 = letra_random()
        caracter2 = numero_random()
        caracter3 = letra_random()
        caracter4 = simbolo_random()
        contraseñam4 = caracter1 + caracter2 + caracter3 + caracter4
        agrupacionm4 = [caracter1, caracter2, caracter3, caracter4]
        print(finalized(), "\n", contraseñam4)
        submenu_invertir()
        while True:
            try:
                menu_anidadom4 = entrada_us()
                es()
                break

            except ValueError:
                error()

        if menu_anidadom4 == 1:
            anidado_generar_mixta4(agrupacionm4)

        elif menu_anidadom4 == 2:
            guardar_mixta4(contraseñam4)

        elif menu_anidadom4 == 3:
            volver()
            break

def guardar_mixta4(contraseñam4):
    while True:
        with open("save password.txt", "a") as passwordm4:
            passwordm4.write(contraseñam4 + "\n")
        guardado_exito()
        salir_guardar_mixta4 = salir_s()
        while salir_guardar_mixta4 != 's':
            salir_guardar_mixta4 = salir_s()
        break

def anidado_generar_mixta4(agrupacionm4):
    while True:
        generando()
        def agrupacion_mixta4():
            return str(random.choice(agrupacionm4))
        caracter1e = agrupacion_mixta4()
        caracter2e = agrupacion_mixta4()
        caracter3e = agrupacion_mixta4()
        caracter4e = agrupacion_mixta4()
        contraseñam4e = caracter1e + caracter2e + caracter3e + caracter4e
        print(finalized(), "\n", contraseñam4e)
        p('[1] Guardar')
        p('[2] <<<< Volver')
        es()
        while True:
            try:
                anidado_generar_mixta4e = entrada_us()
                es()
                break

            except ValueError:
                error()

        if anidado_generar_mixta4e == 1:
            guardar_mixta4e(contraseñam4e)

        elif anidado_generar_mixta4e == 2:
            volver()
            break
        
def guardar_mixta4e(contraseñam4e):
    while True:
        with open("save password.txt", "a") as paswordm4e:
            paswordm4e.write(contraseñam4e + "\n")
        guardado_exito()
        salir_guardar_mixta4e = salir_s()
        while salir_guardar_mixta4e != 's':
            salir_guardar_mixta4e = salir_s()
        break

def contraseña6_dijitos():
    while True:
        p('================================================')
        p('            Contraseña 6 dijitos              ')
        p('================================================')
        es()
        p('[1] Contraseña de 6 dijitos numeros')
        p('[2] Contraseña mixta')
        p('[3] <<<< Volver')
        es()
        while True:
            try:
                usuario_menu2 = entrada_us()
                es()
                break

            except ValueError:
                error()

        if usuario_menu2 == 1:
            contraseña_dijitos6()

        elif usuario_menu2 == 2:
            contraseña_m6()

        elif usuario_menu2 == 3:
            volver()
            break

def contraseña_dijitos6():
    while True:
        mostrar_generar()
        dijit1 = numero_random()
        dijit2 = numero_random()
        dijit3 = numero_random()
        dijit4 = numero_random()
        dijit5 = numero_random()
        dijit6 = numero_random()
        contraseña6 = dijit1 + dijit2 + dijit3 + dijit4 + dijit5 + dijit6
        agrupacion6 = [dijit1, dijit2, dijit3, dijit4, dijit5, dijit6]
        generando()
        print(finalized(), "\n", contraseña6)
        submenu_invertir()
        while True:
            try:
                contraseña_dijit6 = entrada_us()
                es()
                break

            except ValueError:
                error()
        if contraseña_dijit6 == 1:
            contraseña_dijitos6e(agrupacion6)

        elif contraseña_dijit6 == 2:
            guardar_contraseña6(contraseña6)

        elif contraseña_dijit6 == 3:
            volver()
            break

def guardar_contraseña6(contraseña6):
    while True:
        with open("save password.txt", "a") as password6:
            password6.write(contraseña6 + "\n")
        es()
        guardado_exito()
        salir_guardar_contraseña6 = salir_s()
        while salir_guardar_contraseña6 != 's':
            salir_guardar_contraseña6 = salir_s()
        break

def contraseña_dijitos6e(agrupacion6):
    while True:
        generando()
        def agrupacione_6():
            return str(random.choice(agrupacion6))
        dijit1e = agrupacione_6()
        dijit2e = agrupacione_6()
        dijit3e = agrupacione_6()
        dijit4e = agrupacione_6()
        dijit5e = agrupacione_6()
        dijit6e = agrupacione_6()
        contraseña6e = dijit1e + dijit2e + dijit3e + dijit4e + dijit5e + dijit6e
        print(finalized(), "\n", contraseña6e)
        es()
        p('[1] Guardar')
        p('[2] <<<< Volver')
        es()
        while True:
            try:
                contraseña_dijitom6 = entrada_us()
                es()
                break

            except ValueError:
                error()

        if contraseña_dijitom6 == 1:
            guardar_contraseña6e(contraseña6e)

        elif contraseña_dijitom6 == 2:
            volver()
            break

def guardar_contraseña6e(contraseña6e):
    while True:
        with open("save password.txt", "a") as password6e:
            password6e.write(contraseña6e + "\n")
        es()
        guardado_exito()
        salir_guardar_contraseña_m6 = salir_s()
        while salir_guardar_contraseña_m6 != 's':
            salir_guardar_contraseña_m6 = salir_s()
        break

def contraseña_m6():
    while True:
        mostrar_generar()
        caracter6m1 = simbolo_random()
        caracter6m2 = letra_random()
        caracter6m3 = numero_random()
        caracter6m4 = letra_random()
        caracter6m5 = simbolo_random()
        caracter6m6 = numero_random()
        contraseñam6 = caracter6m1 + caracter6m2 + caracter6m3 + caracter6m4 + caracter6m5 + caracter6m6
        agrupacionm6 = [caracter6m1, caracter6m2, caracter6m3, caracter6m4, caracter6m5, caracter6m6]
        generando()
        print(finalized(), "\n", contraseñam6)
        submenu_invertir()
        while True:
            try:
                contraseña_dijitm6 = entrada_us()
                es()
                break

            except ValueError:
                error()

        if contraseña_dijitm6 == 1:
            contraseña_m6e(agrupacionm6)

        elif contraseña_dijitm6 == 2:
            guardar_contraseñam6(contraseñam6)

        elif contraseña_dijitm6 == 3:
            volver()
            break

def guardar_contraseñam6(contraseñam6):
    while True:
        with open("save password.txt", "a") as passwordm6:
            passwordm6.write(contraseñam6 + "\n")
        es()
        guardado_exito()
        salir_guardar_contraseñam6 = salir_s()
        while salir_guardar_contraseñam6 != 's':
            salir_guardar_contraseñam6 = salir_s()
        break

def contraseña_m6e(agrupacionm6):
    while True:
        generando()
        def generar_mixto6():
            return str(random.choice(agrupacionm6))
        caracterm6e1 = generar_mixto6()
        caracterm6e2 = generar_mixto6()
        caracterm6e3 = generar_mixto6()
        caracterm6e4 = generar_mixto6()
        caracterm6e5 = generar_mixto6()
        caracterm6e6 = generar_mixto6()
        contraseñam6e = caracterm6e1 + caracterm6e2 + caracterm6e3 + caracterm6e4 + caracterm6e5 + caracterm6e6
        print(finalized(), "\n", contraseñam6e)
        p('[1] Guardar')
        p('[2] <<<< Volver')
        es()
        while True:
            try:
                contraseña_mixtam6e = entrada_us()
                es()
                break

            except ValueError:
                error()

        if contraseña_mixtam6e == 1:
            guardar_mixta6e(contraseñam6e)

        elif contraseña_mixtam6e == 2:
            volver()
            break

def guardar_mixta6e(contraseñam6e):
    while True:
        with open("save password.txt", "a") as passwordm6e:
            passwordm6e.write(contraseñam6e + "\n")
        guardado_exito()
        salir_guardar_mixta6e = salir_s()
        while salir_guardar_mixta6e != 's':
            salir_guardar_mixta6e = salir_s()
        break
def contraseña8_dijitos():
    while True:
        p('================================================')
        p('              Contraseña 8 dijitos                ')
        p('================================================')
        es()
        p('[1] Contraseña 8 dijitos numeros')
        p('[2] Mixta')
        p('[3] <<<< Volver')
        es()
        while True:
            try:
                contraseña_8_dijitos = entrada_us()
                es()
                break

            except ValueError:
                error()

        if contraseña_8_dijitos == 1:
            contraseña_dijitos8()

        elif contraseña_8_dijitos == 2:
            generar_m8()

        elif contraseña_8_dijitos == 3:
            volver()
            break

def contraseña_dijitos8():
    while True:
        mostrar_generar()
        di1 = numero_random()
        di2 = numero_random()
        di3 = numero_random()
        di4 = numero_random()
        di5 = numero_random()
        di6 = numero_random()
        di7 = numero_random()
        di8 = numero_random()
        contraseña8 = di1 + di2 + di3 + di4 + di5 + di6 + di7 + di8
        agrupacion8 = [di1, di2, di3, di4, di5, di6, di7, di8]
        print(finalized(), "\n", contraseña8)
        generando()
        submenu_invertir()
        while True:
            try:
                dijitos8 = entrada_us()
                es()
                break

            except ValueError:
                error()

        if dijitos8 == 1:
            contraseña_dijitos8e(agrupacion8)

        elif dijitos8 == 2:
            guardar_dijitos8(contraseña8)

        elif dijitos8 == 3:
            volver()
            break

def guardar_dijitos8(contraseña8):
    while True:
        with open("save password.txt", "a") as password8:
            password8.write(contraseña8 + "\n")
        es()
        guardado_exito()
        salir_guardar_dijitos8 = salir_s()
        while salir_guardar_dijitos8 != 's':
            salir_guardar_dijitos8 = salir_s()
        break

def contraseña_dijitos8e(agrupacion8):
    while True:
        generando()
        def dijit8e():
            return str(random.choice(agrupacion8))
        di1e = dijit8e()
        di2e = dijit8e()
        di3e = dijit8e()
        di4e = dijit8e()
        di5e = dijit8e()
        di6e = dijit8e()
        di7e = dijit8e()
        di8e = dijit8e()
        contraseña8e = di1e + di2e + di3e + di4e + di5e + di6e + di7e + di8e
        print(finalized(), "\n", contraseña8e)
        p('[1] Guardar')
        p('[2] <<<< Volver')
        es()
        while True:
            try:
                dijitos8e = entrada_us()
                es()
                break

            except ValueError:
                error()

        if dijitos8e == 1:
            guardar_dijitos8e(contraseña8e)

        elif dijitos8e == 2:
            volver()
            break

def guardar_dijitos8e(contraseña8e):
    while True:
        with open("save password.txt", "a") as password8e:
            password8e.write(contraseña8e + "\n")
        es()
        guardado_exito
        salir_guardar_dijitos8e = salir_s()
        while salir_guardar_dijitos8e != 's':
            salir_guardar_dijitos8e = salir_s()
        break

def generar_m8():
    while True:
        mostrar_generar()
        caracterm81 = simbolo_random()
        caracterm82 = letra_random()
        caracterm83 = numero_random()
        caracterm84 = simbolo_random()
        caracterm85 = numero_random()
        caracterm86 = numero_random()
        caracterm87 = simbolo_random()
        caracterm88 = simbolo_random()
        contraseñam8 = caracterm81 + caracterm82 + caracterm83 + caracterm84 + caracterm85 + caracterm86 + caracterm87 + caracterm88
        agrupacionm8 = [caracterm81, caracterm82, caracterm83, caracterm84, caracterm85, caracterm85, caracterm86, caracterm87, caracterm88]
        print(finalized(), "\n", contraseñam8)
        submenu_invertir()
        while True:
            try:
                caracter8e = entrada_us()
                es()
                break

            except ValueError:
                error()

        if caracter8e == 1:
            generar_m8e(agrupacionm8)

        elif caracter8e == 2:
            guardar_m8(contraseñam8)

        elif caracter8e == 3:
            volver()
            break

def guardar_m8(contraseñam8):
    while True:
        with open("save password.txt", "a") as passwordm8:
            passwordm8.write(contraseñam8 + "\n")
        guardado_exito()
        salir_guardarm8 = salir_s()
        while salir_guardarm8 != 's':
            salir_guardarm8 = salir_s()
        break

def generar_m8e(agrupacionm8):
    while True:
        generando()
        def m8e():
            return str(random.choice(agrupacionm8))
        c8e1 = m8e()
        c8e2 = m8e()
        c8e3 = m8e()
        c8e4 = m8e()
        c8e5 = m8e()
        c8e6 = m8e()
        c8e7 = m8e()
        c8e8 = m8e()
        contraseñam8e = c8e1 + c8e2 + c8e3 + c8e4 + c8e5 + c8e6 + c8e7 + c8e8
        print(finalized(), "\n", contraseñam8e)
        p('[1] Guardar')
        p('[2] <<<< Volver')
        es()
        while True:
            try:
                caracter8e = entrada_us()
                es()
                break

            except ValueError:
                error()

        if caracter8e == 1:
            guardar_m8e(contraseñam8e)

        elif caracter8e == 2:
            volver()
            break

def guardar_m8e(contraseñam8e):
    while True:
        with open("save password.txt", "a") as passwordm8e:
            passwordm8e.write(contraseñam8e + "\n")
        guardado_exito()
        salir_guardar_m8e = salir_s()
        while salir_guardar_m8e != 's':
            salir_guardar_m8e = salir_s()
        break

def menu_contraseñas():
    while True:
        p('════════════════════════════════════════════════════════════════════════')
        p('               🔑🛡️Generador de contraseñas🛡️🔑                          ')
        p('                    ------------------------                             ')
        p('                     Desarrollador Cuz-Dev                              ')
        p('════════════════════════════════════════════════════════════════════════')
        es()
        p('[1] Contraseña 4 dijitos')
        p('[2] Contraseña 6 dijitos')
        p('[3] Contraseña 8 dijitos()')
        p('[4] Info')
        p('[5] <<<< Salir')
        es()
        while True:
            try:
                usuario = entrada_us()
                es()
                break

            except ValueError:
                error()

        if usuario == 1:
            contraseña4_dijitos()

        elif usuario == 2:
            contraseña6_dijitos()

        elif usuario == 3:
            contraseña8_dijitos()

        elif usuario == 4:
            while True:
                es()
                p('info Generador de contraseñas')
                p('Desarrollador Cuz-Dev')
                es()
                p('* crea contraseñas de 4 6, 8 dijitos')
                p('combinando numeros, simbolos, letras')
                p('* Genera contraseñas random dijitos y letras,')
                p('simbolos, totalmete elegidos. por la maquina')
                p('* Guarda contraseñas en el archivo')
                p('save password.txt')
                es()
                p('Recuerda que en mi github hay mas proyectos')
                es()
                while salir_usuario4 != 's':
                    salir_usuario4 = salir_s()
                break

        elif usuario == 5:
            p('Saliendo*.*')
            es()
            break


def calculadora():
    while True:
        #Calculadora basica
        #🚀desarrollador Cuz-Dev🚀
        def p(mensaje):
            print(mensaje)
        def es():
            p('   ')    
        s = "s"    
    
        p('════════════════════════════════════════════════')
        p('                  Calculadora                   ')
        p('════════════════════════════════════════════════')
        p('[1] Sumar')
        p('[2] Restar')
        p('[3] Multiplicar')
        p('[4] Dividir')
        p('[5] Info')
        p('[6] <<<< Salir')
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
                    p('info')
                    es()
                    p('Calculadora basica v2')
                    p('Desarrollador cuz-dev')
                    es()
                    p('novedades:')
                    p('* Manejo de errores')
                    p('* interfaz mejorada')
                    es()
                    p('¡!Gracias por ejecutar mi programa¡!')
                    es()       
                    si = str(input('➤ Escribe s para salir:')).lower()
                    while si != s:
                        si = str(input('➤ ¡!Escribe s para salir')).lower()
                    break               

            elif cal == 6:
                p('Saliendo*.*')
                es()
                break
            

        except ValueError:
            es()
            p('[ERROR] Debes escribir un numero no una letra:')
            es()      

def Number_hunter():
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
        p('3* Salir🚪')
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

            elif nh == 2:
                while True:
                    p('info📝')
                    p('info  Number Hunter')
                    es()
                    p('novedades')
                    p('* Manejo de errores')
                    p('* Mejora de el contador')
                    es()
                    p('juego desarrollado por Cuz-Dev')
                    p('*cada que el usuario pierda se reiniciara el juego')
                    p('*juego arcade, 10 niveles')
                    es()
                    p('Reglas')
                    p('* No se puede manipular el codigo, es decir no se pude poner una instruccion print')
                    p('que muestre el resultado de el numero random que elige la maquina..')
                    p('* Este juego es de pura posibilidad')
                    es()
                    p('¡! Gracias por ejecutar mi programa !¡')
                    es()
                    p('Recuerda que en mi github hay mas proyectos')
                    es()       
                    salir = str(input('Escribe s para salir')).lower()
                    while salir != s:
                        salir = str(input('!¡Escribe s para salir¡!')).lower()
                    break                  
            
            elif nh == 3:
                p('<<<<')
                es()
                break

        except ValueError:
            es()
            print('[ERROR] Debes escribir un numero no una letra:') 
            es()      

def Piedra_papel_tijera():
    #🕹️Piedra papel o tijera ✊✋✌️
    #🚀Desarrollador Cuz-Dev 🚀
    import random
    def p(mensaje):
        print(mensaje)
    def es():
        p('   ')
    def resultado():
        print('  ')
        print('🕹️Resultado🕹️')
        print('      ')
    def pause():
        input('➤ ENTER PARA CONTINUAR')     
    piedra = 'piedra'
    papel = 'papel'
    tijera = 'tijera'
    contador1 = 0
    contador2 = 0
    opciones = ['piedra', 'papel', 'tijera']
    s = 's'

    while True:
        p('════════════════════════════════════════════════')
        p('         ✊Piedra  ✋papel o ✌️tijera            ')
        p('════════════════════════════════════════════════')
        es()
        p('[1] Jugar🎮')
        p('[2] Puntaje⚡')
        p('[3] Info📃 y reglas')
        p('[4] <<<< Volver')
        es()
        try:
            op = int(input('➤ Escribe numero de opcion:'))

            if op == 1:
                while True:    
                    p('[1] Empezar 🔥')
                    p('[2] <<<< Salir')
                    es()
                    juego = int(input('➤ Escribe numero de opcion:'))
    
                    if juego == 1:
                        while True:                   
                            p('========================')
                            p('         Elige          ')
                            p('========================')
                            opm = random.choice(opciones)
                            es()
                            p('[1] ✊ Piedra')
                            p('[2] ✋ Papel')
                            p('[3] ✌️ Tijera')
                            p('[4] Volver')
                            es()
                            v = int(input('➤ Escribe numero de opcion:'))
                
                            if opm == 'piedra':
                                if v == 1:
                                    es()
                                    resultado()
                                    es()
                                    p('empate⚔️')
                                    print('maquina elegio 🤖', ' ', opm)
                                    print('tú elegististe 👤',' ', 'piedra')
                                    pause()
                                    es()
                            
                                elif v == 2:
                                    es()
                                    resultado()
                                    es()
                                    print('Victoria 🏆')
                                    print('maquina elegio 🤖', ' ', opm)
                                    print('tú elegististe 👤',' ', 'papel')
                                    es()
                                    contador1 += 1
                                    print('JUGADOR:', contador1, '/', 'MAQUINA:', contador2)
                                    pause()
                                    es()
                            
                                elif v == 3:
                                    es()
                                    resultado()
                                    es()
                                    p('derrota 😈')
                                    print('maquina elegio 🤖', ' ', opm)
                                    print('tú elegististe 👤',' ', 'tijera')
                                    es()
                                    contador2 += 1
                                    print('JUGADOR:', contador1, '/', 'MAQUINA:', contador2)
                                    pause()
                                    es()
                
                            
                            elif opm == 'papel':
                                if v == 1:
                                    es()
                                    resultado()
                                    es()
                                    print('derrota 😈')
                                    print('maquina elegio 🤖', ' ', opm)
                                    print('tú elegististe 👤',' ', 'piedra')
                                    es()
                                    contador2 += 1
                                    print('JUGADOR:', contador1, '/', 'MAQUINA:', contador2)
                                    pause()
                                    es()

                                elif v == 2:
                                    es()
                                    resultado()
                                    es()
                                    print('empate ⚔️')
                                    print('maquina elegio 🤖', ' ', opm)
                                    print('tú elegististe 👤',' ', 'papel')
                                    pause()
                                    es()
                            
                                elif v == 3:
                                    es()
                                    resultado()
                                    es()
                                    print('Victoria 🏆')
                                    print('maquina elegio 🤖', ' ', opm)
                                    print('tú elegististe 👤',' ', 'tijera')
                                    es()
                                    contador1 += 1
                                    print('JUGADOR:', contador1, '/', 'MAQUINA:', contador2)
                                    pause()
                                    es()
                            
                            elif opm == 'tijera':                     
                                if v == 1:
                                    es()
                                    resultado()
                                    es()
                                    print('Victoria 🏆')
                                    print('maquina elegio 🤖', ' ', opm)
                                    print('tú elegististe 👤',' ', 'piedra')
                                    es()
                                    contador1 += 1
                                    print('JUGADOR:', contador1, '/', 'MAQUINA:', contador2)
                                    pause()
                                    es()
                            
                                elif v == 2:
                                    es()
                                    resultado()
                                    es()
                                    print('derrota 😈')
                                    print('maquina elegio 🤖', ' ', opm)
                                    print('tú elegististe 👤',' ', 'papel')
                                    es()
                                    contador2 += 1
                                    print('JUGADOR:', contador1, '/', 'MAQUINA:', contador2)
                                    pause()
                                    es()

                                elif v == 3:
                                    es()
                                    resultado()
                                    es()
                                    print('empate ⚔️')
                                    print('maquina elegio 🤖', ' ', opm)
                                    print('tú elegististe 👤',' ', 'tijera')
                                    pause()
                                    es()

                                if v == 4:
                                    p('<<<<')
                                    es()
                                    break           


                    elif juego == 2:
                        p('<<<< Saliendo')
                        es()
                        break    


            elif op == 2:
                while True:
                    p('========================')
                    p('        Puntaje          ')
                    p('========================')
                    es()
                    p('[1] puntaje jugador')
                    p('[2] Puntaje maquina')
                    p('[3] Salir')
                    es()
                    puntaje = int(input('➤ Escribe numero de opcion:'))

                    if puntaje == 1:
                        while True:
                            p('👾 Puntaje jugador 👾')
                            p(contador1)
                            es()
                            if contador1 <= contador2:
                                p('le ganaste ala maquina🤯')
                            else:
                                p('Te gano la maquina🤭')
                            es()        
                            salir1 = str(input('Escribe s para salir:')).lower()
                            while salir1 != s:
                                salir1 = str(input('¡!Escribe para salir!¡:')).lower()
                            break

                    elif puntaje == 2:
                        while True:
                            p('🤖 Puntaje Maquina 🤖')
                            p(contador2)
                            salir2 = str(input('Escribe s para salir:')).lower()
                            while salir2 != s:
                                salir2 = str(input('¡!Escribe s salir!¡:'))
                            break

                    elif puntaje == 3:
                        p('<<<<')
                        es()
                        break      
                
            
            elif op == 3:
                while True:
                    p('🕹️Info juego🕹️')
                    es()
                    p('Piedra papel o tijera')
                    p('Desarrollador Cuz-Dev')
                    es()
                    p('*Puntaje usuario, maquina')
                    p('*Retroceso bucle while')
                    p('*si pierdes no se borra tu Puntaje')
                    es()
                    p('reglas')
                    p('* No se puede manipular el codigo, es decir no se puede poner la  funcion print')
                    p('para que muestre la eleccion  de la maquina')
                    es()
                    p('v2 Novedades')
                    p('* manejo de errores')
                    es()
                    p('¡!Gracias por ejecutar mi programa¡!')
                    es()
                    p('Recuerda que en mi github hay mas proyectos')
                    es()
                    salir3 = str(input('Escribe s para salir:')).lower()
                    while salir3 != s:
                        salir3 = str(input('¡!Escribe s para salir!¡:')).lower()
                    break

            elif op == 4:
                p('<<<<')
                es()
                break            

        except ValueError:
            es()
            p('[ERROR] Debes escribir un numero no una letra:')
            es()
