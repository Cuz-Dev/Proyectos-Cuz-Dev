# Interfaz de terminal de Sistema
def error_():
    print('[Errror critico] No se encuentran los demas archivos:')

while True:
    try:
        from configuracion import es, p, linea_menu, linea_menu2, linea_submenu, salir_s
        break

    except ModuleNotFoundError:
        error_()

def menu_docente():
    es()
    p('     ║╔══════════════════════════════════════════╗')
    p('  ║ ════                 Menu Docente                ║')
    p('╚═══════════════════════════════════════════════ ╝ ╦═════════╗')
    p('                                                  ║         ')
    p('╔                                                            ╗')
    p(' [1] Ver areas   | [4] Estudiantes       | [7] <<<< salir')
    p(' [2] Eventos     | [5] Contraseña        ')
    p(' [3] Directivos  | [6] Acudientes         ')
    p('╚                                                            ╝')
    es()

def menu_coordinador_():
    p('  ║  ╔══════════════════════════════════════════╗══')
    p(' ║                  Menu Coordinador            ║')
    p('╚═══════════════════════════════════════════════ ╝ ╦═════════════════╗')
    p('                                                  ║                 ══')
    p('╔                                                                  ╗')
    p(' [1] Compromisos        |[5] Contraseña')
    p(' [2] Reuniones          |[6] Acudientes')
    p(' [3] Docentes           |[7] <<<< salir')
    p(' [4] Estudiantes       ')
    p('╚                                                                  ╝')
    es()
    es()

def menu_acudiente_():
    p('  ║  ╔══════════════════════════════════════════╗')
    p(' ║              Menu Acudiente                  ║')
    p('╚════════════════════════════════════════════════╝')
    es()
    p('╔                                                ╗')
    p(' [1] Estudiantes')
    p(' [2] Docentes')
    p(' [3] Directivos')
    p(' [4] Eventos')
    p(' [5] Anotaciones')
    p(' [6] <<<< salir')
    p('╚                                                ╝')
    es()

def menu_es():
    p('║  ╔══════════════════════════════════════════╗')
    p('  ║         Menu estudiante                           ║')
    p('╚════════════════════════════════════════════════╝')
    es()
    p('╔                                                ╗')
    p(' [1] Temas')
    p(' [2] Directivos')
    p(' [3] Grados')
    p(' [4] Anotaciones')
    p(' [5] <<<< Salir')
    p('╚                                                ╝')
    es()

def menu_herramientas_():
    p('║  ╔══════════════════════════════════════════╗')
    p('  ║             Menu herramientas         ║       ')
    p('╚════════════════════════════════════════════════╝')
    es()
    p('╔                                       ╗')
    p(' [1] Calculadora')
    p(' [2] Generador de contraseñas seguras')
    p(' [3] Juegos')
    p(' [4] <<<< Salir')
    p('╚                                        ╝')
    es()

def menu_rector_():
    es()
    p('║  ╔══════════════════════════════════════════╗')
    p('  ║                  Menu Rector                ║')
    p('╚═══════════════════════════════════════════════ ╝ ╦═════════╗')
    p('                                                  ║         ')
    p('╔                                                           ╗')
    p(' [1] Areas     | [5] Estudiantes')
    p(' [2] Docentes  | [6] Contraseña')
    p(' [3] Eventos   | [7] Acudientes ')
    p(' [4] Directivos| [8] <<<< Salir')
    p('╚                                                           ╝')
    es()

def menu_secretario_():
    es()
    p('║  ╔══════════════════════════════════════════╗')
    p('  ║  Menu secretaria institucional             ║')
    p('╚════════════════════════════════════════════════╝')
    es()
    p('╔                                                ╗')
    p(' [1] Matricular estudiante   |  [3] Directivos')
    p(' [2] Ver estudiante          |  [4] <<<< Salir')
    p('╚                                                ╝')
    es()


def menu_principal_():
    p('╔══════════════════════════════════════════╗')
    p('  ║             SISTEMA ESCOLAR               ║')
    p('  ╚════════════════════════════════════════════════╝ ')
    p("    ║                 v1.4                    ║")
    es()
    p('╔ ◉ Coordinador | ◉ Estudiante    | ◉ secretaria ╗')
    p('  ◉ Rector      | ◉ Acudiente     | ◉ info ')
    p('╚ ◉ Docente     | ◉ herramientas                 ╝')
    es()

def submenu_generador_4():
    p('================================================')
    p('         Contraseña de 4 dijitos               ')
    p('================================================')
    es()
    p('[1] Contraseña de 4 dijitos, Numeros')
    p('[2] Contraseña Mixta')
    p('[3] <<<< Volver')
    es()

def menu_generador():
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

def menu_calculadora():
    p('════════════════════════════════════════════════')
    p('                  Calculadora                   ')
    p('════════════════════════════════════════════════')
    p('[1] Sumar')
    p('[2] Restar')
    p('[3] Multiplicar')
    p('[4] Dividir')
    p('[5] Info')
    p('[6] <<<< Salir')

def menu_number_hunter():
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

def menu_piedra_papel_tijera():
    p('════════════════════════════════════════════════')
    p('         ✊Piedra  ✋papel o ✌️tijera            ')
    p('════════════════════════════════════════════════')
    es()
    p('[1] Jugar🎮')
    p('[2] Puntaje⚡')
    p('[3] Info📃 y reglas')
    p('[4] <<<< Volver')
    es()

# submenus

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

submenu_eventos_lista = [submenu_eventos_1, submenu_eventos_2, submenu_eventos_3, submenu_eventos_4,submenu_eventos_5]
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

def submenu_notas():
    linea_menu2()
    p('Notas estudiante')
    linea_menu2()
    es()
    p('[1] Añadir nota estudiante')
    p('[2] Ver nota estudiante')
    p('[3] <<<< Volver')

def submenu_añadir_es():
    linea_submenu()
    p('Sub menu añadir estudiante')
    linea_submenu()
    es()
    p('[1] Añadir estudiante')
    p('[3] <<<< volver')
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

def submenu_invertir():
    es()
    p('[1] invertir contraseña')
    p('[2] Guardar contraseña')
    p('[3] <<<< Volver')
    es()

def submenu_contraseña_6():
    p('================================================')
    p('            Contraseña 6 dijitos              ')
    p('================================================')
    es()
    p('[1] Contraseña de 6 dijitos numeros')
    p('[2] Contraseña mixta')
    p('[3] <<<< Volver')
    es()

def submenu_contraseña_8():
    p('================================================')
    p('              Contraseña 8 dijitos                ')
    p('================================================')
    es()
    p('[1] Contraseña 8 dijitos numeros')
    p('[2] Mixta')
    p('[3] <<<< Volver')
    es()

def opcion_grado():
    p('[1] Ver estudiantes')
    p('[2] <<<< Volver')
    es()

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

def submenu_anotacion():
    p('➤ Anotaciones ')
    es()
    p('[1] Añadir anotacion')
    p('[2] Ver anotacion')
    p('[3] <<<< Volver')
    es()

def submenu_anotacion_2():
    p('➤ Anotaciones ')
    es()
    p('[1] Ver anotacion')
    p('[2] <<<< Volver')
    es()

def submenu_quitar_estudiante():
    p('➤ Eliminar estudiante')
    es()
    p('[1] Quitar estudiante')
    p('[2] <<<< Volver')
    es()

def submenu_cambiar_contraseña():
    p('➤ Contraseña')
    es()
    p('[1] Cambiar contraseña')
    p('[2] <<<< Volver')
    es()

def submenu_añadir_acudiente():
    p('➤ Acudiente')
    es()
    p('[1] Añadir acudiente')
    p('[2] Ver acudientes')
    p('[3] <<<< Volver')
    es()

def estudiantes_sistema_menu():
    p('➤ Estudiantes')
    es()
    p('[1] Estudiantes')
    p('[2] Añadir estudiante')
    p('[3] Notas')
    p('[4] Anotaciones')
    p('[5] <<<< Volver')
    es()