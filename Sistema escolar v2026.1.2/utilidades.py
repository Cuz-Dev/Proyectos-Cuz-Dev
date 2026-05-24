def error_():
    print('[Errror critico] No se encuentran los demas archivos:')

while True:
    try:
        from configuracion import es, p, pause, salir_s
        break

    except ModuleNotFoundError:
        error_()

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

