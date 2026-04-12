#🧮Sistema escolar dev-v2026.0.6
#🚀desarrollador Cuz-Dev🚀
#🌪️Si lo puedes imaginar lo puedes programar🌪️

def v():
    es()
    print('V2026.0.6')

def p(mensaje):
        print(mensaje)  

import estudiantes
from estudiantes import calculadora
from estudiantes import Number_hunter
from estudiantes import Piedra_papel_tijera

def es():
    print('     ')

def pause():
    input('Presiona enter para salir <')

def error():
    es()
    p('[ERROR] Debes escribir un numero no una letra')
    es()

def volver():
    p('<<<<')
    es()

def salir():
    p('Saliendo*.*')
    es()

def menu_docente():
    while True:
        try:
            es()
            cd = int(input('!Hola profe¡, porfavor escribe tu clave:'))
            while cd != 202614:
                es()
                cd = int(input('[ERROR]!Clave incorrecta¡:'))
                es()
            break

        except ValueError:
            es()
            error()
            es()
    while True:
        es()
        p('────────────────────────────────────────────────')           
        p('              Bienvenido profe                  ')
        p('────────────────────────────────────────────────')
        es()
        ('------------------------------------------------')
        p('          MENU DE OPCIONES DOCENTE')
        p('------------------------------------------------')
        p('□ opciones □')
        p('[1] Ver areas')
        p('[2] Eventos')
        p('[3] Directivos')
        p('[4] << Salir')
        p('=*=*^=*=*=^=*=*=^')
        es()
        while True:
            try:
                od = int(input('!Porfavor dijite numero de opcion¡:'))
                es()
                break

            except ValueError:
                error()

        if od == 1:
            submenu_areas()

        elif od == 2:
            submenu_eventos()

        elif od == 3:
            submenu_directivos()

        elif od == 4:
            salir()
            break

def submenu_areas():
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
        p('□ Info □')
        es()
        p('(13) □□□□□□ Ver docente de cada area □□□□□□□')
        p('(14) <<<< Volver')
        es()
        while True:
            try:
                odp = int(input('!¡Porfavor dijite numero de  opcion¡!:'))
                es()
                break

            except ValueError:
                error()

        if odp == 1:
            submenu_temas1()

        elif odp == 2:
            submenu_temas2()

        elif odp == 3:
            submenu_temas3()

        elif odp == 4:
            submenu_temas4()

        elif odp == 5:
            submenu_temas5()

        elif odp == 6:
            submenu_temas6()

        elif odp == 7:
            submenu_temas7()

        elif odp == 8:
            submenu_temas8()

        elif odp == 9:
            submenu_temas9()

        elif odp == 10:
            submenu_temas10()
        
        elif odp == 11:
            submenu_temas11()

        elif odp == 12:
            submenu_temas12()

        elif odp == 13:
            submenu_docentes_area()

        elif odp == 14:
            volver()
            break

def submenu_temas1():
        p('➤ Temas ciencias naturales')
        p('• Animales')
        p('• Celulas')
        p('• Medio ambiente')
        p('• Quimica')
        p('• Laboratorio')
        pause()

def submenu_temas2():
    p('➤ Temas fisica materia')
    es()
    p('• Mru')
    p('• Factores de conversion')
    p('• Unidades de medida')
    pause()

def submenu_temas3():
    p('➤ Temas sociales')
    es()
    p('• Imperialismo')
    p('• Socialismo')
    p('• Comunismo')
    p('• Nacionalismo')
    pause()

def submenu_temas4():
    p('➤ Temas filosofia')
    es()
    p('• Inicios de la filosofia')
    p('• Principales pensadores de la edad media')
    pause()
            
def submenu_temas5():
    p('➤ Temas ingles')
    es()
    p('• Verb to be')
    p('• Lisenig')
    p('• Read')
    pause()

def submenu_temas6():
    p('➤ Temas edu. fisica')
    es()
    p('• Juegos tradicionales')
    p('• Historia de el basquetball')
    p('• Historia de el fottball')
    pause()
            
def submenu_temas7():
    p('➤ Temas religion')
    es()    
    p('• Sin sentidos')
    p('• Sentidos')
    p('• Yo pertenezco a jesus')
    pause()

def submenu_temas8():
    p('➤ Temas etica')
    es()
    p('• Sentimientos')
    p('• Perdon')
    p('• Valores')
    pause()

def submenu_temas9():
    p('➤ Temas  castellano')
    es()
    p('• La vida feliz')
    p('• La metarmofosis')
    p('• Noches blancas')
    pause()            

def submenu_temas10():
    p('➤ Temas tecnologia')
    es()
    p('• Diagrama de flujo')
    p('• Makecode')
    p('• Python')
    pause()

def submenu_temas11():
    p('➤ Temas ciencias economicas y politicas')
    es()
    p('• Pensadores')
    p('• Origen')
    p('• Importancia')
    pause()

def submenu_temas12(): 
    p('➤ Temas matematicas')
    es()
    p('• Seno')
    p('• Coseno')
    p('• Tangente')
    pause()

def submenu_docentes_area(): 
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
                odpd = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                es()
                break

            except ValueError:
                error()

        if odpd == 1:
            submenu_docentes1()

        elif odpd == 2:
            submenu_docentes2()

        elif odpd == 3:
            submenu_docentes3()

        elif odpd == 4:
            submenu_docentes4()

        elif odpd == 5:
            submenu_docentes5()

        elif odpd == 6:
            submenu_docentes6()

        elif odpd == 7:
            submenu_docentes7()

        elif odpd == 8:
            submenu_docentes8()

        elif odpd == 9:
            submenu_docentes9()

        elif odpd == 10:
            submenu_docentes10()

        elif odpd == 11:
            submenu_docentes11()

        elif odpd == 12:
            submenu_docentes12()

        elif odpd == 13:
            volver()
            break                    
            
def submenu_docentes1():       
        p('➤ Ciencias naturales ')
        es()
        p('• dora')
        p('• jhon')
        p('• angelica')
        pause()

def submenu_docentes2():
    p('➤ Fisica')
    es()
    p('• angela')
    p('• alex')    
    p('• angel')
    pause()

def submenu_docentes3():
    p('➤ Sociales')
    es()
    p('• magdalena')
    p('• mario')
    p('• capera')
    pause()
            
def submenu_docentes4():
    p('➤ Filosofia')
    es()
    p('• capera')
    p('• elsa')
    pause()

def submenu_docentes5():
    p('➤ Ingles')
    es()
    p('• carlos')
    p('• sara')
    pause()
        
def submenu_docentes6():
    p('➤ Edu fisica')
    es()
    p('• sebastian')
    pause()
            
def submenu_docentes7():
    p('➤ Religion')
    es()
    p('• luz')
    pause()

def submenu_docentes8():
    p('➤ Etica')
    es()
    p('• luz')
    pause()
            
def submenu_docentes9():
    p('➤ Castellano')
    es()
    p('• magdalena')
    p('• sofia')
    pause() 
        
def submenu_docentes10():
    p('➤ Tecnologia')
    es()
    p('• geovanny')
    pause()
                
def submenu_docentes11():
    p('➤ Economia y Politica')
    es()
    p('• capera')
    pause()

def submenu_docentes12():
    p('➤ Matematica')
    es()  
    p('• ruben')
    p('• angela')
    pause()   

def submenu_eventos():
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
                ode = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                es()
                break

            except ValueError:
                error()

        if ode == 1:
            submenu_eventos1()

        elif ode == 2:
            submenu_eventos2()

        elif ode == 3:
            submenu_eventos3()

        elif ode == 4:
            submenu_eventos4()

        elif ode == 5:
            submenu_eventos5()

        elif ode == 6:
            volver()
            break

def submenu_eventos1():
    while True:
        p('➤ Dia de la cultura')
        es()
        p('[1] Ver dia')
        p('[2] Explicacion')
        p('[3] << Volver')
        es()
        while True:
            try:
                odec = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                es()
                break

            except ValueError:
                error()

        if odec == 1:
            while True:
                p('► Dia a desarrollar')
                es()
                p('El dia a desarrollar este evento es el 1 de abril')
                es()
                odecs1 = str(input('Escribe s para salir:')).lower()
                while odecs1 != 's':
                    odecs1 = str(input('¡!Escribe s para salir!¡:')).lower()
                break     

        elif odec == 2:
            while True:
                p('Evento donde los estudiantes presentan bailes, obras de teatro')
                p('musica y expociciones. objetivgo mostrar los talentos')
                p('artisticos')
                es()
                odecs2 = str(input('Escribe s para salir:')).lower()
                while odecs2 != 's':
                    odecs2 = str(input('¡!Escribe s para salir!¡:')).lower()
                break      


        elif odec == 3:
            volver()
            break    

def submenu_eventos2():
    while True:
        p('➤ Feria de la ciencia')
        es()
        p('[1] Ver dia')
        p('[2] Explicacion')
        p('[3] << Volver')
        es()
        while True:
            try:
                odef = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                es()
                break

            except ValueError:
                error()

        if odef == 1:
            while True:
                p('► Dia a desarrollar')
                p('El dia a desarrollar este evento es el 20 de agosto')
                es()
                odefs1 = str(input('Escribe s para salir:')).lower()
                while odefs1 != 's':
                    odefs1 = str(input('¡!Escribe s para salir!¡:')).lower()
                break    

        elif odef == 2:
            while True:
                p('Actividad academica donde los estudiantes presentan')
                p('experimentos cientificos, sirve para desarrollar la curiosidad,')
                p('la ivestigacion y el pensamiento critico')
                es()
                odefs2 = str(input('Escribe ese paea salir:')).lower()
                while odefs2 != 's':
                    odefs2 = str(input('¡!Escribe s para salir!¡:')).lower()
                break    

        elif odef == 3:
            volver()
            break    

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
                odei = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                es()
                break

            except ValueError:
                error()

        if odei == 1:
            while True:
                p('► Dia a desarrollar')
                p('Esta actividad se desarrolla cada final de periodo,')
                p('es decir. abril 15, agosto 21, noviembre 21')
                es()
                odeis1 = str(input('Escribe s para salir:')).lower()
                while odeis1 != 's':
                    odeis1 = str(input('¡!Escribe s para salir!¡:')).lower()
                break    

        elif odei == 2:
            while True:
                p('Acto civico donde donde se rinden honores ala bandera,')
                p('y se reconocen estudiantes destacados')
                es()
                odeis2 = str(input('Escribe s para salir:')).lower()
                while odeis2 != 's':
                    odeis2 = str(input('¡!Escribe s para salir!¡:')).lower()
                break    

        elif odei == 3:
            volver()
            break    

def submenu_eventos4():
    while True:
        p('➤ Dia de la independencia')
        es()
        p('[1] Ver dias')
        p('[2] Explicacion')
        p('[3] << Volver')
        es()
        while True:
            try:
                odein = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                es()
                break

            except ValueError:
                error()

        if odein == 1:
            while True:
                p('► Dia a desarrollar')
                p('El dia de el desarrollo de el evento es')
                p('20 de agosto')
                es()
                odeins1 = str(input('Escribe s para salir:')).lower()
                while odeins1 != 's':
                    odeins1 = str(input('¡!Escribe s para salir¡!:')).lower()
                break

        elif odein == 2:
            while True:
                p('Es una actividad donde el colegio conmemora')
                p('la historia de el pais, con actos civicos')
                p('memorias culturales')
                es()
                odeins2 = str(input('Escribe s para salir:')).lower()
                while odeins2 != 's':
                    odeins2 = str(input('¡!Escribe s para salir!¡:')).lower()
                break    

        elif odein == 3:
            volver()
            break

def submenu_eventos5():
    while True:
        p('➤ Reunion de acudientes')
        es()
        p('[1] Ver dias')
        p('[2] Explicacion')
        p('[3] << Volver')
        es()
        while True:
            try:
                oder = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                es()
                break

            except ValueError:
                error()

        if oder == 1:
            while True:
                p('► Dia a desarrollar')
                p('El dia de el desarrollo es dos dias despues')
                p('de el final de periodo')
                p('es decir. abril 15, agosto 21, noviembre 21')
                es()
                oders1 = str(input('Escribe s para salir:')).lower()
                while oders1 != 's':
                    oders1 = str(input('¡!Escribe s para salir!¡:')).lower()
                break

        elif oder == 2:
            while True:
                p('Reuniones organizadas por el colegio')
                p('para orientar a los acudientes sobre la educacion,')
                p('convivencia y desarrollo de los estudiantes')
                es()
                oders2 = str(input('Escribe s para salir:')).lower()
                while oders2 != 's':
                    oders2 = str(input('¡!Escribe s para salir!¡:')).lower()
                break    

        elif oder == 3:
            volver()
            break

def submenu_directivos():
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
                odd = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                es()
                break

            except ValueError:
                error()

        if odd == 1:
            submenu_directivos1()

        elif odd == 2:
            submenu_directivos2()

        elif odd == 3:
            submenu_directivos3()

        elif odd == 4:
            submenu_directivos4()

        elif odd == 5:
            volver()
            break


def submenu_directivos1():
    while True:          
        p('➤ RECTOR ')
        es()
        p('[1] Persona acargo')
        p('[2] Funcion')
        p('[3] << Volver')
        es()
        while True:
            try:
                oddr = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                es()
                break

            except ValueError:
                error()
            
        if oddr == 1:
            while True:
                p('► Rector institucional ')
                p('jhon jairo vernal')
                es()
                oddrs1 = str(input('Escribe s para salir:')).lower()
                while oddrs1 != 's':
                    oddrs1 = str(input('¡!Escribe s para salir!¡:')).lower()
                break

        elif oddr == 2:
            while True:
                p('► Funcion rector')
                p('Es la maxima autoridad de el colegio se encarga')
                p('de dirigir la institucion, tomar deciciones y supervisar')
                p('el funcionamiento de el colegio')
                es()
                oddrs2 = str(input('Escribe s para salir:')).lower()
                while oddrs2 != 's':
                    oddrs = str(input('¡!Escribe s para salir¡!:')).lower()
                break    

        elif oddr == 3:
            volver()
            break

def submenu_directivos2():
    while True:
        p('➤ CORDINADOR')
        es()
        p('[1] Persona acargo')
        p('[2] Funcion')
        p('[3] <<<< Volver')
        es()
        while True:
            try:
                oddc = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                es()
                break

            except ValueError:
                error()

        if oddc == 1:
            while True:
                p('► Cordinador')
                p('elder sanchez')
                es()
                oddcs1 = str(input('Escribe s para salir:')).lower()
                while oddcs1 != 's':
                    oddcs1 = str(input('¡!Escribe s para salir!¡:')).lower()
                break

        elif oddc == 2:
            while True: 
                p('► Funciones rector')
                p('se encarga de organizar las clases, horarios')
                p('materias, y actividades academicas')
                p('tambien supervisa el trabajo de docente')
                es()
                oddcs2 = str(input('Escribe s para salir:')).lower()
                while oddcs2 != 's':
                    oddcs2 = str(input('¡!Escribe s para continuar!¡:')).lower()
                break

        elif oddc == 3:
            volver()
            break       

def submenu_directivos3():
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
                oddp = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                es()
                break

            except ValueError:
                error()

        if oddp == 1:
            while True:
                p('► Psicologa')
                p('tatiana mendes')
                es()
                oddps1 = str(input('Escribe s para salir:')).lower()
                while oddps1 != 's':
                    oddps1 = str(input('¡!Escribe s para salir!¡:')).lower()
                break    

        elif oddp == 2:
            while True:
                p('► funciones psicologa')
                p('Se encarga principalmente de ayudar al bienestar emocional,')
                p('social y academico de los estudiantes')
                es()
                oddps2 = str(input('Escribe s para salir:')).lower()
                while oddps2 != 's':
                    oddps2 = str(input('¡!Escribe s para salir!¡')).lower()
                break 

        elif oddp == 3:
            volver()
            break       

def submenu_directivos4():
    while True:
        p('➤ SECRETARIO ACADEMICO')
        es()
        p('[1] Persona acargo')
        p('[2] Funcion')
        p('[3] <<<< Volver')
        es()
        while True:
            try:
                odds = int(input('!¡ Porfavor dijita numero de opcion¡!:'))
                es()
                break

            except ValueError:
                error()

        if odds == 1:
            while True:
                p('► Secretario academico')
                p('carlos ruben espitia')
                es()
                oddss1 = str(input('Escribe s para salir:')).lower()
                while oddss1 != 's':
                    oddss1 = str(input('¡!Escribe s para salir¡!:')).lower()
                break 

        elif odds == 2:
            while True:
                p('► funciones secretario academico') 
                p('Se encarga de las bases de datos,l registrar nuevos estudiantes')
                es()
                oddss2 = str(input('Escribe s para salir:')).lower()
                while oddss2 != 's':
                    oddss2 = str(input('¡!Escribe s para salir¡!:')).lower()
                break

        elif odds == 3:
            volver()
            break

def menu_coordinador():
    while True:
        try:
            es()
            code = int(input('¡!Hola cordinador por favor dijita tu clave!¡:'))
            while code != 202601:
                es()
                code = int(input('?Acaso no eres el cordinador¿'))
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
        p('[4] <<<< Salir')
        p('=*=*^=*=*=^=*=*=^')
        es()
        while True:
            try:
                opc = int(input('!¡ Porfavor dijita  numero de opcion ¡!:'))
                es()
                break

            except ValueError:
                error()

        if opc == 1:
            compromisos()

        elif opc == 2:
            reuniones()

        elif opc == 3:
            submenu_docentes_area()

        elif opc == 4:
            salir()
            break

def compromisos():
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
                opcc = int(input('!¡ Porfavor dijita numero de opcion¡!:'))
                es()
                break

            except ValueError:
                error()            

        if opcc == 1:
            compromisos_1()

        elif opcc == 2:
            compromisos_2()

        elif opcc == 3:
            compromisos_3()

        elif opcc == 4:
            compromisos_4()

        elif opcc == 5:
            compromisos_5()

        elif opcc == 6:
            volver()
            break


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

def reuniones():
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
                opcr = int(input('!¡Porfavor dijita tu numero de opcion¡!:'))
                es()
                break

            except ValueError:
                error()

        if opcr == 1:
            reuniones_1()

        elif opcr == 2:
            reuniones_2()

        elif opcr == 3:
            reuniones_3()

        elif opcr == 4:
            reuniones_4()

        elif opcr == 5:
            reuniones_5()

        elif opcr == 6:
            volver()
            break

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

def menu_acudiente():        
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
                oac = int(input('¡!Por favor dijita numero de opcion!¡:'))
                es()
                break

            except ValueError:
                error()

        if oac == 1:
            grados()

        elif oac == 2:
            submenu_docentes_area()
            
        elif oac == 3:
            submenu_directivos()

        elif oac == 4:
            submenu_eventos()

        elif oac == 5:
            salir()
            break

def grados():        
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
                oace = int(input('!¡Por favor dijita numero de opcion¡!:'))
                es()
                break

            except ValueError:
                error()

        if oace == 1:
            estudiantes_1()

        elif oace == 2:
            estudiantes_2()

        elif oace == 3:
            estudiantes_3()

        elif oace == 4:
            estudiantes_4()

        elif oace == 5:
            estudiantes_5()

        elif oace == 6:
            estudiantes_6

        elif oace == 7:
            volver()
            break

def estudiantes_1():
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
                oaces = int(input('!¡Por favor dijita numero de opcion¡!:'))
                es()
                break

            except  ValueError:
                error()

        if oaces == 1:
            while  True:
                p('[1] Ver estudiantes')
                p('[2] <<<< Volver')
                es()
                while True:
                    try:
                        oaces1 = int(input('!¡Por favor escribe numero de opcion¡!:'))
                        es()
                        break

                    except ValueError:
                        error()

                if oaces1 == 1:
                    while True:
                        for eg61 in estudiantes.gd61:
                            p(eg61)
                            es()
                        eg61s = str(input('Escribe s para salir:')).lower()
                        while eg61s != 's':
                            eg61s = str(input('¡!Escribe s paea salir¡!:')).lower()
                        break

                elif oaces1 == 2:
                    volver()
                    break

                elif oaces == 2:
                    while True:
                        p('[1] Ver estudiantes')
                        p('[2] <<<< Volver')
                        es()
                        while True:
                            try:
                                oaces2 = int(input('!¡Por favor dijita numero de opcion¡!:'))
                                es()
                                break

                            except ValueError:
                                error()
                                    
                        if oaces2 == 1:
                            while True:
                                for eg62 in estudiantes.gd62:
                                    p(eg62)
                                    es()
                                eg62s = str(input('Escribe s para salir:')).lower()
                                while eg62s != 's':
                                    eg62s = str(input('¡!Escribe s para salir!¡:')).lower()    
                                break
                                    
                        elif oaces2 == 2:
                            volver()
                            break
                                        

                elif oaces == 3:
                    while True:
                        p('[1] Ver estudiantes')
                        p('[2] <<<< Volver')
                        es()
                        while True:
                            try:
                                oaces3 = int(input('¡!Por favor dijita numero de opcion¡!:'))
                                es()
                                break

                            except ValueError:
                                error()

                        if oaces3 == 1:
                            while True:
                                for eg63 in estudiantes.gd63:
                                    p(eg63)
                                    es()
                                eg63s = str(input('Escribe s para salir:')).lower
                                while eg63s != 's':
                                    eg63s = str(input('¡!Escribe s para salir!¡:'))
                                break    


                        elif oaces3 == 2:
                            volver()
                            break
                                
                elif oaces == 4:
                    volver()
                    break

def estudiantes_2():
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
                oacesp = int(input('¡!Por favor dijita numero de opcion¡!:'))
                es()
                break

            except ValueError:
                error()

        if oacesp == 1:
            while True:
                p('[1] Ver estudiantes')
                p('[2] <<<< Volver')
                es()
                while True:
                    try:
                        oacesp1 = int(input('¡!Por favor dijita numero de opcion!¡:'))
                        es()
                        break

                    except ValueError:
                        es()
                        error()                        
                        es()

                if oacesp1 == 1:
                    while True:
                        for eg71 in estudiantes.gd71:
                            p(eg71)
                            es()
                        eg71s = str(input('Escribe s para salir')).lower()
                        while eg71s != 's':
                            eg71s = str(input('¡!Escribe s para salir!¡'))
                        break

                elif oacesp1 == 2:
                    volver()
                    break     

        elif oacesp == 2:
            while True:
                p('[1] Ver estudiantes')
                p('[2] <<<< Volver')
                es()
                while True:
                    try:
                        oacesp2 = int(input('¡!Por favor dijita numero de opcion!¡:'))
                        es()
                        break

                    except ValueError:
                        error() 

                if oacesp2 == 1:
                        while True:
                            for eg72 in estudiantes.gd72:
                                p(eg72)
                                es()
                            eg72s = str(input('Escribe s para continuar:')).lower()
                            while eg72s != 's':
                                eg72s = str(input('¡!Escribe s para continuar:')).lower()
                            break


                elif oacesp2 == 2:
                    volver()
                    break
                                
        elif oacesp == 3:
            while True:
                p('[1] Ver estudiantes')
                p('[2] <<<< Volver')
                es()
                while True:
                    try:
                        oacesp3 = int(input('¡!Por favor dijita numero de opcion!¡'))
                        es()
                        break

                    except ValueError:
                        error()

                if oacesp3 == 1:
                    while True:
                        for eg73 in estudiantes.gd73:
                            p(eg73)
                            es()
                        eg73s = str(input('Escribe s para salir')).lower()
                        while eg73s != 's':
                            eg73s = str(input('¡!Escribe s para salir!¡')).lower()
                        break

                elif oacesp3 == 2:
                    volver()
                    break
                                        
        elif oacesp == 4:
            volver()
            break

def estudiantes_3():
    while True:
        p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        p('          Octavo               ')
        p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        p('[1] Octavo 1')
        p('[2] Octavo 2')
        p('[3] <<<< Volver')
        while True:
            try:
                oaceo = int(input('¡!Por favor dijita numero de opcion¡!'))
                es()
                break

            except ValueError:
                error()

        if oaceo == 1:
            while True:
                p('[1] Ver estudiantes')
                p('[2] <<<< volver')
                es()
                while True:
                    try:
                        oaceo1 = int(input('¡!Por favor escribe numero de opcion!¡'))
                        es()
                        break

                    except ValueError:
                        error()

                if oaceo1 == 1:
                    while True:
                        for eg81 in estudiantes.gd81:
                            p(eg81)
                            es()
                        eg81s = str(input('Escribe s para salir')).lower()
                        while eg81s != 's':
                            eg81s = str(input('¡!Escribe s para salir!¡')).lower()
                        break    

                elif oaceo1 == 2:
                    volver()
                    break
                            
        elif oaceo == 2:
            while True:
                p('[1] Ver estudiantes')
                p('[2] <<<< Volver')
                es()
                while True:
                    try:
                        oaceo2 = int(input('¡!Por favor dijita numero de opcion'))
                        es()
                        break

                    except ValueError:
                        error()

                if oaceo2 == 1:
                    while True:
                        for eg82 in estudiantes.gd82:
                            p(eg82)
                            es()
                        eg82s = str(input('Escribe s para salir:')).lower()
                        while eg82s != 's':
                            eg82s = str(input('¡!Escribe s para salir!¡:')).lower()
                        break         

                elif oaceo2 == 2:
                    volver()
                    break


        elif oaceo == 3:
            volver()
            break

def estudiantes_4():                    
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
                oacen = int(input('¡!Por favor dijita numero de opcion!¡'))
                es()
                break

            except ValueError:
                error()

        if oacen == 1:
            while True:
                p('[1] Ver estudiantes')
                p('[2] <<<< Volver')
                es()
                while True:
                    try:
                        oacen1 = int(input('¡!Por favor dijita numero de opcion!¡'))
                        es()
                        break

                    except ValueError:
                        error()

                if oacen1 == 1:
                    while True:
                        for eg91 in estudiantes.gd91:
                            p(eg91)
                            es()
                        eg91s = str(input('Escribe s para salir:')).lower()
                        while eg91s != 's':
                            eg91s = str(input('¡!Escribe s para salir!¡:')).lower()
                        break

                elif oacen1 == 2:
                    volver()
                    break

        elif oacen == 2:
            while True:
                p('[1] Ver estudiantes')
                p('[2] <<<< Volver')
                es()
                while True:
                    try:
                        oacen2 = int(input('¡!Por favor dijita numero opcion!¡:'))
                        es()
                        break

                    except ValueError:
                        error()

                if oacen2 == 1:
                    while True:
                        for eg92 in estudiantes.gd92:
                            p(eg92)
                            es()
                        eg92s = str(input('Escribe s para salir:')).lower()
                        while eg92s != 's':
                            eg92s = str(input('¡!Escribe s para salir!¡:')).lower()
                        break

                elif oacen2 == 2:
                    volver()
                    break                                 

        elif oacen == 3:
            volver()
            break                   

def estudiantes_5():
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
                oaced = int(input('¡!Por favor dijita numero de opcion!¡:'))
                es()
                break

            except ValueError:
                error()

        if oaced == 1:
            while True:
                p('[1] Ver estudiantes')
                p('[2] <<<< Volver')
                es()
                while True:
                    try:
                        oaced1 = int(input('¡!Por favor dijita numero de opcion!¡:'))
                        es()
                        break

                    except ValueError:
                        error()

                if oaced1 == 1:
                    while True:
                        for eg101 in estudiantes.gd101:
                            p(eg101)
                            es()
                        eg101s = str(input('Escribe s para salir:')).lower()
                        while eg101s != 's':
                            eg101s = str(input('¡!Escribe s para salir!¡:')).lower()
                        break
                                    
                elif oaced1 == 2:
                    volver()
                    break

        elif oaced == 2:
            while True:
                p('[1] Ver estudiantes')
                p('[2] <<<< Volver')
                es()
                while True:
                    try:
                        oaced2 = int(input('¡!Por favor dijita numero de opcion!¡:'))
                        es()
                        break

                    except ValueError:
                        error()

                if oaced2 == 1:
                    while True:
                        for eg102 in estudiantes.gd102:
                            p(eg102)
                            es()
                        eg102s = str(input('Escribe s para salir:')).lower()
                        while eg102s != 's':
                            eg102s = str(input('¡!Escribe s para salir!¡:')).lower()
                        break

                elif oaced2 == 2:
                    volver()
                    break


        elif oaced == 3:
            volver()
            break

def estudiantes_6():
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
                oaceu = int(input('¡!Por favor dijita numero de opcion!¡:'))
                es()
                break

            except ValueError:
                error()

        if oaceu == 1:
            while True:
                p('[1] Ver estudiantes')
                p('[2] <<<< Volver')
                es()
                while True:
                    try:
                        oaceu1 = int(input('¡!Por favor dijita numero de opcion!¡:'))
                        es()
                        break

                    except ValueError:
                        error()

                if oaceu1 == 1:
                    while True:
                        for eg111 in estudiantes.gd111:
                            p(eg111)
                            es()
                        eg111s = str(input('Escribe s para salir:')).lower()
                        while eg111s != 's':
                            eg111s = str(input('¡!Escribe s para salir¡!:')).lower()
                        break

                elif oaceu1 == 2:
                    while True:
                        for eg112 in estudiantes.gd112:
                            p(eg112)
                            es()
                        eg112s = str(input('Escribe s para salir')).lower()
                        while eg112s != 's':
                            eg112s = str(input('¡!Escribe s para salir¡!:')).lower()
                        break       

                elif oaceu1 == 3:
                    volver()
                    break                         

def menu_estudiante():
    while True:
        p('────────────────────────────────────────────────')
        p('            Bienvenido estudiante             ')
        p('────────────────────────────────────────────────')
        p('------------------------------------------------')
        p('              Menu estudiantes                  ')
        p('------------------------------------------------')
        p('[1] Temas')
        p('[2] Docentes')
        p('[3] Directivos')
        p('[4] Grados')
        p('[5] <<<< Salir')
        es()
        while True:
            try:
                oe = int(input('¡!Por favor dijita numero de opcion!¡:'))
                es()
                break

            except ValueError:
                error()
        if oe == 1:
            submenu_areas()

        elif oe == 2:
            submenu_docentes_area()
                
        elif oe == 3:
            submenu_directivos()
                
        elif oe == 4:
            grados()

        elif oe == 5:
            salir()
            break

def menu_herramientas():
    while True:
        p('────────────────────────────────────────────────')
        p('                Herramientas                    ')
        p('────────────────────────────────────────────────')
        es()
        p('[1] Calculadora')
        p('[2] Juegos')
        p('[3] <<<< Salir')
        es()
        while True:
            try:
                h = int(input('¡!Por favor dijita numero de opcion!¡:'))
                es()
                break

            except ValueError:
                error()

        if h == 1:
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
                        hc = int(input('¡!Por favor dijita numero de opcion!¡:'))
                        es()
                        break

                    except ValueError:
                        error()

                if hc == 1:
                    calculadora()

                elif hc == 2:
                    volver()
                    break

        elif h == 2:
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
                        hg = int(input('¡!Por favor dijita numero de opcion!¡:'))
                        es()
                        break

                    except ValueError:
                        error()

                if hg == 1:
                    while True:
                        p('➤ Number hunter')
                        es()
                        p('[1] Iniciar juego')
                        p('[2] <<<< Volver')
                        es()
                        while True:
                            try:
                                hgn = int(input('¡!Por favor dijita numero de opcion!¡:'))
                                es()
                                break

                            except ValueError:
                                error()

                        if hgn == 1:
                            Number_hunter()

                        elif hgn == 2:
                            volver()
                            break    

                elif hg == 2:
                    Piedra_papel_tijera()

                elif hg == 3:
                    volver()
                    break
                        
                    
        elif h == 3:
            salir()
            break
            
def menu_info():
    while True:
        es()
        with open("info.txt", "r") as archivo:
            for linea in archivo:
                p(linea.strip())
            sa = int(input('Escribe 1* para salir:'))
            while sa != 1:
                sa = int(input('!¡Escribe 1 para salir¡!:'))
            break

v()
colegio = str(input('Por favor escribe colegio python para continuar:')).lower()

while colegio != 'colegio python':
    es()
    colegio = str(input('[ERROR] colegio incorrecto:')).lower()
es()

while True:
    p('════════════════════════════════════════════════')
    p('         SISTEMA ESCOLAR V2026.0.6')
    p('════════════════════════════════════════════════')
    es()
    p('=============================================')
    p("        Bienvenido al sistema                ")
    p('=============================================')
    es()
    p('◉ Coordinador')
    p('◉ Docente')
    p('◉ Estudiante')
    p('◉ Acudiente')
    p('◉ herramientas')
    p('◉ info')
    es()
    persona = str(input('¡!Escribe el nombre de el menu al que quieres entrar!¡:')).lower()

    if persona == 'docente':
        menu_docente()

    elif persona == 'coordinador':
        menu_coordinador()

    elif persona == 'acudiente':
        menu_acudiente()


    elif persona == 'estudiante':
        menu_estudiante()               

    elif persona == 'herramientas':
        menu_herramientas()

    elif persona == 'info':
        menu_info()
