#Sistema escolar v2026.0.3
#desarrollador Cuz-Dev
#Si lo puedes imaginar lo puedes programar

def v():
    print('V2026.0.3')

def p(mensaje):
        print(mensaje)  


import estudiantes

v()

def es():
    print('     ')

def pause():
    input('Presiona enter para volver al menu')        

d = 'docente'
e = 'estudiante'
co = 'coordinador'
c = 202614
cod = 202601
ac = 'acudiente'
es()
s = 's'
i = 'info'



colegio = str(input('!¡Por favor escribe el nombre de este colegio para continuar:')).lower()

col = 'colegio python'


while col != colegio:
    es()
    colegio = str(input('!colegio incorrecto!:')).lower()
es()    

p('========== !¡Hola este es al menu¡! ==========')
p('********** ¡!sede bachiller¡! ************')

while True:
    es()
    p('******** !¡Bienvenido al sistema!¡ ********')
    es()
    p('*Coordinador')
    p('*Docente')
    p('*Estudiante')
    p('*Acudiente')
    p('*info')
    es()
    persona = str(input('¡!Escribe el mombre de le menu al que quieres entrar!¡:')).lower()
    if persona == d:
        cd = int(input('!Hola profe¡, porfavor escribe tu clave:'))
        while cd != c:
            es()
            cd = int(input('!Clave incorrecta¡, ?acaso no eres docente¿:'))
            
     
        while True:
            es()           
            p('!¡Bienvenido profe¡!')
            es()
            p('============== MENU DE OPCIONES DOCENTE ===============')
            p(' ========== opciones ==========')
            p('1* Ver areas')
            p('2* Eventos')
            p('3* Directivos')
            p('4* salir')
            p('=*=*^=*=*=^=*=*=^') 
            od = int(input('!Porfavor dijite numero de opcion¡:'))
            es()
            
            if od == 1:
                while True:           
                    p('*********** Areas ***********')
                    es()
                    p('/////////// temas de cada area /////////////')
                    es()
                    p('1* Naturales')
                    p('2* Fisica')
                    p('3* Sociales')
                    p('4* Filosofia')
                    p('5* Ingles')
                    p('6* Edu Fisica')
                    p('7* Religion')
                    p('8* Etica')
                    p('9* Castellano')
                    p('10* Tecnologia')
                    p('11* Economia politica')
                    p('12* Matematicas')
                    es()
                    p('^^^^^^ Info ^^^^^')
                    es()
                    p('13* *=*=*=*= Ver docente de cada area *=*=*=*=')
                    p('14* salir')


                    odp = int(input('!¡Porfavor dijite numero de  opcion¡!:'))
                    es()

                    if odp == 1:
                        p('*Temas ciencias naturales *')
                        p('*Animales')
                        p('*Celulas')
                        p('*Medio ambiente')
                        p('*Quimica')
                        p('*Laboratorio')
                        pause()

                    elif odp == 2:
                        p('** Temas fisica materia **')
                        es()
                        p('*Mru')
                        p('*Factores de conversion')
                        p('*Unidades de medida')
                        pause()

                    elif odp ==3:
                        p('**** Temas sociales ****')
                        es()
                        p('*Imperialismo')
                        p('*Socialismo')
                        p('*Comunismo')
                        p('*Nacionalismo')
                        pause()

                    elif odp == 4:
                        p('***** Temas filosofia *****')
                        es()
                        p('*Inicios de la filosofia')
                        p('*Principales pensadores de la edad media')
                        pause()
            
                    elif odp == 5:
                        p('******* Temas ingles ******')
                        es()
                        p('*Verb to be')
                        p('*Lisenig')
                        p('*Read')
                        pause()

                    elif odp == 6:
                        p('******* Temas edu. fisica ******')
                        es()
                        p('*Juegos tradicionales')
                        p('*Historia de el basquetball')
                        p('*Historia de el fottball')
                        pause()
            
                    elif odp == 7:
                        p('******** Temas religion ********')
                        es()    
                        p('*Sin sentidos')
                        p('*Sentidos')
                        p('*Yo pertenezco a jesus')
                        pause()

                    elif odp == 8:
                        p('********* Temas etica *********')
                        es()
                        p('*Sentimientos')
                        p('*Perdon')
                        p('*Valores')
                        pause()

                    elif odp == 9:
                        p('********** Temas  castellano **********')
                        es()
                        p('*La vida feliz')
                        p('*La metarmofosis')
                        p('*Noches blancas')
                        pause()            

                    elif odp == 10:
                        p('*********** Temas tecnologia ***********')
                        es()
                        p('*Diagrama de flujo')
                        p('*Makecode')
                        p('*Python')
                        pause()

                    elif odp == 11:
                        p('************ Temas ciencias economicas y politicas ************')
                        es()
                        p('*Pensadores')
                        p('*Origen')
                        p('*Importancia')
                        pause()

                    elif odp == 12:
                        p('************* Temas matematicas *************')
                        es()
                        p('*Seno')
                        p('*Coseno')
                        p('*Tangente')
                        pause()

                    elif odp == 13:
                        while True:
                            p('=^=^=^=^=^ Docentes de area =^=^=^=^=^')
                            es()
                            p('1* Naturales')
                            p('2* Fisica')
                            p('3* Sociales')
                            p('4* Filosofia')
                            p('5* Ingles')
                            p('6* Edu Fisica')
                            p('7* Religion')
                            p('8* Etica')
                            p('9* Castellano')
                            p('10* Tecnologia')
                            p('11* Economia politica')
                            p('12 *Matematicas')
                            p('13* salir')
                            es()      
                            odpd = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                            es()
            
                            if odpd == 1:
                                p('= Ciencias naturales =')
                                es()
                                p('1* dora')
                                p('2* jhon')
                                p('3* angelica')
                                pause()
    
                            elif odpd == 2:
                                p('== Fisica ==')
                                es()
                                p('1* angela')
                                p('2* alex')
                                p('3* angel')
                                pause()
                            elif odpd == 3:
                                p('=== Sociales ===')
                                es()
                                p('1* magdalena')
                                p('2* mario')
                                p('2* capera')
                                pause()
            
                            elif odpd == 4:
                                p('==== Filosofia ====')
                                es()
                                p('1* capera')
                                p('2* elsa')
                                pause()

                            elif odpd == 5:
                                p('===== Ingles =====')
                                es()
                                p('carlos')
                                p('sara')
                                pause()
        
                            elif odpd == 6:
                                p('====== Edu fisica =====')
                                es()
                                p('sebastian')
                                pause()
            
                            elif odpd == 7:
                                p('======= Religion =======')
                                es()
                                p('luz')
                                pause()
             
                            elif odpd == 8:
                                p('======= Etica ========')
                                es()
                                p('luz')
                                pause()
            
                            elif odpd == 9:
                                p('========= Castellano =========')
                                es()
                                p('1* magdalena')
                                p('2* sofia')
                                pause() 
        
            
                            elif odpd == 10:
                                p('========== Tecnologia ==========')
                                es()
                                p('geovanny')
                                pause()
                
                            elif odpd == 11:
                                p('=========== Economia y Politica ===========')
                                es()
                                p('capera')
                                pause()


                            elif odpd == 12:
                                p('=========== Matematicas ============')
                                es()  
                                p('1* ruben')
                                p('2* angela')
                                pause()

                            elif odpd == 13:
                                p('Saliendo*.*')
                                es()
                                break   

                    elif odp == 14:
                        p('Saliendo*.*')
                        es()
                        break                 
        

            elif od == 2:
                while True:
                    p('********** Eventos **********')
                    p('****** Institucionales *****')
                    es()
                    p('1* Dia cultura')
                    p('2* Feria de la ciencia')
                    p('3* Izada de bandera')
                    p('4* Dia de la independencia')
                    p('5* Reunion de padres de familia')
                    p('6* salir')
                    es()
                    ode = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                    es()

                    if ode == 1:
                        while True:
                            p('*=*=*=*= Dia de la cultura *=*=*=*=')
                            es()
                            p('1* Ver dia')
                            p('2* Explicacion')
                            p('3* salir')
                            es()
                            odec = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                            es()

                            if odec == 1:
                                while True:
                                    p('* Dia a desarrollar *')
                                    es()
                                    p('El dia a desarrollar este evento es el 1 de abril')
                                    es()
                                    odecs1 = str(input('Escribe s para salir:')).lower()
                                    while odecs1 != s:
                                        odecs1 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break     

                            elif odec == 2:
                                while True:
                                    p('Evento donde los estudiantes presentan bailes, obras de teatro')
                                    p('musica y expociciones. objetivgo mostrar los talentos')
                                    p('artisticos')
                                    es()
                                    odecs2 = str(input('Escribe s para salir:')).lower()
                                    while odecs2 != s:
                                        odecs2 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break      


                            elif odec == 3:
                                p('Saliendo*.*')
                                es()
                                break    

                    elif ode == 2:
                        while True:
                            p('*=*=*=*= Feria de la ciencia *=*=*=*=')
                            es()
                            p('1* Ver dia')
                            p('2* Explicacion')
                            p('3* salir')
                            es()
                            odef = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                            es()

                            if odef == 1:
                                while True:
                                    p('El dia a desarrollar este evento es el 20 de agosto')
                                    es()
                                    odefs1 = str(input('Escribe s para salir:')).lower()
                                    while odefs1 != s:
                                        odefs1 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break    

                            elif odef == 2:
                                while True:
                                    p('Actividad academica donde los estudiantes presentan')
                                    p('experimentos cientificos, sirve para desarrollar la curiosidad,')
                                    p('la ivestigacion y el pensamiento critico')
                                    es()
                                    odefs2 = str(input('Escribe ese paea salir:')).lower()
                                    while odefs2 != s:
                                        odefs2 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break    

                            elif odef == 3:
                                p('Saliendo*.*')
                                es()
                                break    

                    elif ode == 3:
                        while True:
                            p('*=*=*=*= Izada de bandera *=*=*=*=')
                            es()
                            p('1* Ver dias')
                            p('2* Explicacion')
                            p('3* salir')
                            es()
                            odei = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                            es()

                            if odei == 1:
                                while True:
                                    p('Esta actividad se desarrolla cada final de periodo,')
                                    p('es decir. abril 15, agosto 21, noviembre 21')
                                    es()
                                    odeis1 = str(input('Escribe s para salir:')).lower()
                                    while odeis1 != s:
                                        odeis1 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break    

                            elif odei == 2:
                                while True:
                                    p('Acto civico donde donde se rinden honores ala bandera,')
                                    p('y se reconocen estudiantes destacados')
                                    es()
                                    odeis2 = str(input('Escribe s para salir:')).lower()
                                    while odeis2 != s:
                                        odeis2 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break    

                            elif odei == 3:
                                p('Saliendo*.*')
                                es()
                                break    

                    elif ode == 4:
                        while True:
                            p('*=*=*=*= Dia de la independencia *=*=*=*=')
                            es()
                            p('1* Ver dias')
                            p('2* Explicacion')
                            p('3* salir')
                            es()
                            odein = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                            es()

                            if odein == 1:
                                while True:
                                    p('El dia de el desarrollo de el evento es')
                                    p('20 de agosto')
                                    es()
                                    odeins1 = str(input('Escribe s para salir:')).lower()
                                    while odeins1 != s:
                                        odeins1 = str(input('¡!Escribe s para salir¡!:')).lower()
                                    break

                            elif odein == 2:
                                while True:
                                    p('Es una actividad donde el colegio conmemora')
                                    p('la historia de el pais, con actos civicos')
                                    p('memorias culturales')
                                    es()
                                    odeins2 = str(input('Escribe s para salir:')).lower()
                                    while odeins2 != s:
                                        odeins2 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break    

                            elif odein == 3:
                                p('Saliendo*.*')
                                es()
                                break


                    elif ode == 5:
                        while True:
                            p('*=*=*=*= Reunion de acudientes *=*=*=*=')
                            es()
                            p('1* Ver dias')
                            p('2* Explicacion')
                            p('3* salir')
                            es()
                            oder = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                            es()

                            if oder == 1:
                                while True:
                                    p('El dia de el desarrollo es dos dias despues')
                                    p('de el final de periodo')
                                    p('es decir. abril 15, agosto 21, noviembre 21')
                                    es()
                                    oders1 = str(input('Escribe s para salir:')).lower()
                                    while oders1 != s:
                                        oders1 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break

                            elif oder == 2:
                                while True:
                                    p('Reuniones organizadas por el colegio')
                                    p('para orientar a los acudientes sobre la educacion,')
                                    p('convivencia y desarrollo de los estudiantes')
                                    es()
                                    oders2 = str(input('Escribe s para salir:')).lower()
                                    while oders2 != s:
                                        oders2 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break    

                            elif oder == 3:
                                p('Saliendo*.*')
                                es()
                                break


                    elif ode == 6:
                        p('Saliendo*.*')
                        es()
                        break   


            elif od == 3:
                while True:  
                    p('********* Directivos *********')
                    p('******** institucionales ********')
                    es()
                    p('1* Rector')
                    p('2* Cordinador')
                    p('3* Psicologa')
                    p('4* Secretario academico')
                    p('5* salir')
                    es()

                    odd = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                    if odd == 1:
                        while True:
                            p('RECTOR')
                            es()
                            p('1* Persona acargo')
                            p('2* Funcion')
                            p('3* salir')
                            es()
                            oddr = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                            es()
            
                            if oddr == 1:
                                while True:
                                    p('== Rector institucional ==')
                                    p('jhon jairo vernal')
                                    es()
                                    oddrs1 = str(input('Escribe s para salir:')).lower()
                                    while oddrs1 != s:
                                        oddrs1 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break

                            elif oddr == 2:
                                while True:
                                    p('** Funcion rector **')
                                    p('Es la maxima autoridad de el colegio se encarga')
                                    p('de dirigir la institucion, tomar deciciones y supervisar')
                                    p('el funcionamiento de el colegio')
                                    es()
                                    oddrs2 = str(input('Escribe s para salir:')).lower()
                                    while oddrs2 != s:
                                        oddrs = str(input('¡!Escribe s para salir¡!:')).lower()
                                    break    

                            elif oddr == 3:
                                p('Saliendo*.*')
                                es()
                                break    


                    elif odd == 2:
                        while True:
                            p('CORDINADOR')
                            es()
                            p('1* Persona acargo')
                            p('2* Funcion')
                            p('3* salir')
                            es()
                            oddc = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                            es()

                            if oddc == 1:
                                while True:
                                    p('==== Cordinador ====')
                                    p('elder sanchez')
                                    es()
                                    oddcs1 = str(input('Escribe s para salir:')).lower()
                                    while oddcs1 != s:
                                        oddcs1 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break

                            elif oddc == 2:
                                while True: 
                                    p('**** Funciones rector ****')
                                    p('se encarga de organizar las clases, horarios')
                                    p('materias, y actividades academicas')
                                    p('tambien supervisa el trabajo de docente')
                                    es()
                                    oddcs2 = str(input('Escribe s para salir:')).lower()
                                    while oddcs2 != s:
                                        oddcs2 = str(input('¡!Escribe s para continuar!¡:')).lower()
                                    break

                            elif oddc == 3:
                                p('Saliendo*.*')
                                es()
                                break        

                    elif odd == 3:
                        while True:
                            p('PSICOLOGA')
                            es()
                            p('1* Persona acargo')
                            p('2* Funcion')
                            p('3* salir')
                            es()
                            oddp = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                            es()

                            if oddp == 1:
                                while True:
                                    p('====== Psicologa ======')
                                    p('tatiana mendes')
                                    es()
                                    oddps1 = str(input('Escribe s para salir:')).lower()
                                    while oddps1 != s:
                                        oddps1 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break    

                            elif oddp == 2:
                                while True:
                                    p('******* funciones psicologa ********')
                                    p('Se encarga principalmente de ayudar al bienestar emocional,')
                                    p('social y academico de los estudiantes')
                                    es()
                                    oddps2 = str(input('Escribe s para salir:')).lower()
                                    while oddps2 != s:
                                        oddps2 = str(input('¡!Escribe s para salir!¡')).lower()
                                    break 

                            elif oddp == 3:
                                p('Saliendo*.*')
                                es()
                                break       

                    elif odd == 4:
                        while True:
                            p('SECRETARIO ACADEMICO')
                            es()
                            p('1* Persona acargo')
                            p('2* Funcion')
                            p('3* salir')
                            es()
                            odds = int(input('!¡ Porfavor dijita numero de opcion¡!:'))
                            es()

                            if odds == 1:
                                while True:
                                    p('======== Secretario academico ========')
                                    p('carlos ruben espitia')
                                    es()
                                    oddss1 = str(input('Escribe s para salir:')).lower()
                                    while oddss1 != s:
                                        oddss1 = str(input('¡!Escribe s para salir¡!:')).lower()
                                    break 

                            elif odds == 2:
                                while True:
                                    p('********** funciones secretario academico **********') 
                                    p('Se encarga de las bases de datos,l registrar nuevos estudiantes')
                                    es()
                                    oddss2 = str(input('Escribe s para salir:')).lower()
                                    while oddss2 != s:
                                        oddss2 = str(input('¡!Escribe s para salir¡!:')).lower()
                                    break

                            elif odds == 3:
                                p('Saliendo*.*')
                                es()
                                break          

                    elif odd == 5:
                        p('Saliendo*.*')
                        es()
                        break



            elif od == 4:
                p('Saliendo*.*')
                es() 
                break            

    elif persona == co:
        code = int(input('¡!Hola cordinador por favor dijita tu clave!¡:'))
        while code != cod:
            code = int(input('?Acaso no eres el cordinador¿'))
        es()    
        while True:
            p('!¡Bienvenido cordinador¡!')
            p('=============== Menu cordinador ===============')
            p('1* Compromisos')
            p('2* Reuniones')
            p('3* Docentes disponibles en plantel por area')
            p('4* salir')
            p('=*=*^=*=*=^=*=*=^')
            opc = int(input('!¡ Porfavor dijita  numero de opcion ¡!:'))
            es()

            if opc == 1:
                while True:
                    p('******* Compromisos *******')
                    p('1* Velar por la disciplina')
                    p('2* Apoyar a los docentes')
                    p('3* Supervisar procesos')
                    p('4* Atender a estudiantes y padres')
                    p('5* Cordinar actividades institucionales')
                    p('6* salir')
                    p('=*=*^=*=*=^=*=*=^')
                    opcc = int(input('!¡ Porfavor dijita numero de opcion¡!:'))
                    es()

                    if opcc == 1:
                        p('=*=*=*= Velar por la disciplina =*=*=*=')
                        p('Garantizar que los estudiantes cumplan con las normas')
                        p('manual de convivencia de la institucion.')
                        pause()

                    elif opcc == 2:
                        p('=*=*=*= Apoyar al0os docentes =*=*=*=')
                        p('Ayudar a los profesores en la organizacion de actividades academicas,')
                        p('y resolver situaciones dentro del aula.')
                        pause()

                    elif opcc == 3:
                        p('=*=*=*= Supervisar procesos academicos =*=*=*=')
                        p('Revisar que las clases, evaluaciones y actividades educativas')
                        p('se desarrollen correctamente.')
                        pause()

                    elif opcc == 4:
                        p('=*=*=*= Atender a estudiantes y padres de familia =*=*=*=')
                        p('Escuchar problemas, inquietudes o conflictos de estudiantes ')
                        p('y acudientes para buscar soluciones')
                        pause()

                    elif opcc == 5:
                        p('=*=*=*= Coordinar actividades isntitucionales =*=*=*=')
                        p('Organizar eventos academicos, reuniones, proyectos educativos')
                        p('y actividades escolares')
                        pause()

                    elif opcc == 6:
                        p('Saliendo*.*')
                        es()
                        break
            elif opc == 2:
                while True:
                    p('******* Reuniones *******')
                    p('1* Reuniones con docentes')
                    p('2* Reunion con padres de familia')
                    p('3* Reunion de convivencia escolar')
                    p('4* Reunion de seguimiento academico')
                    p('5* Reunion con directivos')
                    p('6* salir')
                    p('=*=*^=*=*=^=*=*=^')
        
                    opcr = int(input('!¡Porfavor dijita tu numero de opcion¡!:'))
                    es()

                    if opcr == 1:
                        p('=*=*=*= Reunion con docentes =*=*=*=')
                        p('* Rendimientos academico de los estudiantes')
                        p('* Planificar clases')
                        p('* Actividades escolares')
                        pause()

                    elif opcr == 2:
                        p('=*=*=*= Reunion con padres de familia =*=*=*=')
                        p('* Imformar sobre el comportamiento de los estudiantes')
                        p('* Explicar el progreso academico')
                        p('* Resolver inquietudes de los acudientes')
                        pause()

                    elif opcr == 3:
                        p('=*=*=*= Reunion de convivencia escolar =*=*=*=')
                        p('* Tratar conflictos entre estudiantes')
                        p('* Normas del colegio')
                        p('* Mejora deel ambiente escolar')
                        pause()

                    elif opcr == 4:
                        p('=*=*=*= Reunion de seguimiento academico =*=*=*=')
                        p('* Rendimiento de los estudiantes')
                        p('* Dificultades en ciertas materias')
                        p('* Estrategias para mejorar el aprendisaje')
                        pause()

                    elif  opcr == 5:
                        p('=*=*=*= Reunion con directivos =*=*=*=')
                        p('El cordinador se reune con el rector y otros responsables')
                        p('para planificar actividades y desiciones de el')
                        p('colegio')
                        pause()

                    elif opcr == 6:
                        p('Saliendo*.*')
                        es()
                        break                    





            elif opc == 3:
                while True:
                    p('******* Docentes disponibles en plantel *******')
                    es()
                    p('1* Naturales')
                    p('2* Fisica')
                    p('3* Sociales')
                    p('4* Filosofia')
                    p('5* Ingles')
                    p('6* Edu Fisica')
                    p('7* Religion')
                    p('8* Etica')
                    p('9* Castellano')
                    p('10* Tecnologia')
                    p('11* Economia politica')
                    p('12* Matematicas')
                    p('13* salir')

                    opcd = int(input('!¡Porfavor dijite su opcion¡!:'))
                    es()

                    if opcd == 1:
                        p('= Ciencias naturales =')
                        es()
                        p('1* dora')
                        p('2* jhon')
                        p('3* angelica')
                        pause()

                    elif opcd == 2:
                        p('== Fisica ==')
                        es()
                        p('1* angela')
                        p('2* alex')
                        p('3* angel')
                        pause()

                    elif opcd == 3:
                        p('=== Sociales ===')
                        es()
                        p('1* magdalena')
                        p('2* mario')
                        p('2* capera')
                        pause()

                    elif opcd == 4:
                        p('==== Filosofia ====')
                        es()
                        p('1* capera')
                        p('2* elsa')
                        pause()


                    elif opcd == 5:
                        p('===== Ingles =====')
                        es()
                        p('1* carlos')
                        p('2* bonilla')
                        pause()

                    elif opcd == 6:
                        p('====== Edu fisica')
                        es()
                        p('sebastian')
                        pause()
                    elif opcd == 7:
                        p('======= Religion =======')
                        es()
                        p('luz')
                        pause() 

                    elif opcd == 8:
                        p('======= Etica ========')
                        es()
                        p('luz')
                        pause()

                    elif opcd == 9:
                        p('========= Castellano =========')
                        es()
                        p('1* magdalena')
                        p('2* sofia')
                        pause() 

                    elif opcd == 10:
                        p('========== Tecnologia ==========')
                        es()
                        p('geovanny')
                        pause() 

                    elif opcd == 11:
                        p('=========== Economia y Politica ===========')
                        es()
                        p('capera')
                        pause()

                    elif opcd == 12:
                        p('=========== Matematicas ============')
                        es()  
                        p('1* ruben')
                        p('2* angela')
                        pause()

                    elif opcd == 13:
                        p('saliendo*.*')
                        es()
                        break    

            elif opc == 4:
                p('Saliendo*.*')
                es()
                break         
    
    elif persona == ac:
        while True:
            p('============== Menu acudientes  ============== ')
            p('1* Estudiantes')
            p('2* Docentes')
            p('3* Directivos')
            p('4* Eventos')
            p('5* salir')
            oac = int(input('¡!Por favor dijita numero de opcion!¡:'))

            if oac == 1:
                while True:
                    p('1* Grado sexto')
                    p('2* Grado septimo')   
                    p('3* Grado octavo')
                    p('4* Grado noveno')
                    p('5* Grado decimo')
                    p('6* Grado once')
                    p('7* Salir')
                    es()

                    oace = int(input('!¡Por favor dijita numero de opcion¡!:'))
                    es()

                    if oace == 1:
                        while True:
                            p('1* Sexto 1')
                            p('2* Sexto 2')
                            p('3* Sexto 3')
                            p('4* salir')
                            oaces = int(input('!¡Por favor dijita numero de opcion¡!:'))
                            if oaces == 1:
                                while  True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oaces1 = int(input('!¡Por favor escribe numero de opcion¡!:'))

                                    if oaces1 == 1:
                                        while True:
                                            for eg61 in estudiantes.gd61:
                                                p(eg61)
                                                es()
                                            eg61s = str(input('Escribe s para salir:')).lower()
                                            while eg61s != s:
                                                eg61s = str(input('¡!Escribe s paea salir¡!:')).lower()
                                            break

                                    elif oaces1 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break

                            elif oaces == 2:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oaces2 = int(input('!¡Por favor dijita numero de opcion¡!:'))
                                    
                                    if oaces2 == 1:
                                        while True:
                                            for eg62 in estudiantes.gd62:
                                                p(eg62)
                                            es()
                                            eg62s = str(input('Escribe s para salir:')).lower()
                                            while eg62s != s:
                                                eg62s = str(input('¡!Escribe s para salir!¡:')).lower()    
                                            break
                                    
                                    elif oaces2 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break

                            elif oaces == 3:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oaces3 = int(input('¡!Por favor dijita numero de opcion¡!:'))

                                    if oaces3 == 1:
                                        while True:
                                            for eg63 in estudiantes.gd63:
                                                p(eg63)
                                            es()
                                            eg63s = str(input('Escribe s para salir:')).lower
                                            while eg63s != s:
                                                eg63s = str(input('¡!Escribe s para salir!¡:'))
                                            break    


                                    elif oaces3 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break
                            elif oaces == 4:
                                p('Saliendo*.*')
                                es()
                                break

                    elif oace == 2:
                        while True:
                            p('1* Septimo 1')
                            p('2* Septimo 2')
                            p('3* Septimo 3')
                            p('4* salir')
                            es()
                            oacesp = int(input('¡!Por favor dijita numero de opcion¡!:'))

                            if oacesp == 1:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oacesp1 = int(input('¡!Por favor dijita numero de opcion!¡:'))

                                    if oacesp1 == 1:
                                        while True:
                                            for eg71 in estudiantes.gd71:
                                                p(eg71)
                                            es()
                                            eg71s = str(input('Escribe s para salir')).lower()
                                            while eg71s != s:
                                                eg71s = str(input('¡!Escribe s para salir!¡'))
                                            break

                                    elif oacesp1 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break     

                            elif oacesp == 2:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oacesp2 = int(input('¡!Por favor dijita numero de opcion!¡:'))

                                    if oacesp2 == 1:
                                        while True:
                                            for eg72 in estudiantes.gd72:
                                                p(eg72)
                                            es()
                                            eg72s = str(input('Escribe s para continuar:')).lower()
                                            while eg72s != s:
                                                eg72s = str(input('¡!Escribe s para continuar:')).lower()
                                            break


                                    elif oacesp2 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break

                            elif oacesp == 3:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oacesp3 = int(input('¡!Por favor dijita numero de opcion!¡'))

                                    if oacesp3 == 1:
                                        while True:
                                            for eg73 in estudiantes.gd73:
                                                p(eg73)
                                            es()
                                            eg73s = str(input('Escribe s para salir')).lower()
                                            while eg73s != s:
                                                eg73s = str(input('¡!Escribe s para salir!¡')).lower()
                                            break

                                    elif oacesp3 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break
                            
                            elif oacesp == 4:
                                p('Saliendo*.*')
                                es()
                                break


                    elif oace == 3:
                        while True:
                            p('1* Octavo 1')
                            p('2* Octavo 2')
                            p('3* salir')
                            oaceo = int(input('¡!Por favor dijita numero de opcion¡!'))

                            if oaceo == 1:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oaceo1 = int(input('¡!Por favor escribe numero de opcion!¡'))

                                    if oaceo1 == 1:
                                        while True:
                                            for eg81 in estudiantes.gd81:
                                                p(eg81)
                                            es()
                                            eg81s = str(input('Escribe s para salir')).lower()
                                            while eg81s != s:
                                                eg81s = str(input('¡!Escribe s para salir!¡')).lower()
                                            break    

                                    elif oaceo1 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break
                            
                            elif oaceo == 2:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oaceo2 = int(input('¡!Por favor dijita numero de opcion'))

                                    if oaceo2 == 1:
                                        while True:
                                            for eg82 in estudiantes.gd82:
                                                p(eg82)
                                            es()
                                            eg82s = str(input('Escribe s para salir:')).lower()
                                            while eg82s != s:
                                                eg82s = str(input('¡!Escribe s para salir!¡:')).lower()
                                            break         

                                    elif oaceo2 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break


                            elif oaceo == 3:
                                p('Saliendo*.*')
                                es()
                                break
                    
                    elif oace == 4:
                        while True:
                            p('1* Noveno 1')
                            p('2* Noveno 2')
                            p('3* saliendo')
                            es()
                            oacen = int(input('¡!Por favor dijita numero de opcion!¡'))

                            if oacen == 1:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    oacen1 = int(input('¡!Por favor dijita numero de opcion!¡'))

                                    if oacen == 1:
                                        while True:
                                            for eg91 in estudiantes.gd91:
                                                p(eg91)
                                            es()
                                            eg91s = str(input('Escribe s para salir:')).lower()
                                            while eg91s != s:
                                                eg91s = str(input('¡!Escribe s para salir!¡:')).lower()
                                            break

                                    elif oacen == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break

                            elif oacen == 2:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oacen2 = int(input('¡!Por favor dijita numero opcion!¡:'))

                                    if oacen2 == 1:
                                        while True:
                                            for eg92 in estudiantes.gd92:
                                                p(eg92)
                                            es()
                                            eg92s = str(input('Escribe s para salir:')).lower()
                                            while eg92s != s:
                                                eg92s = str(input('¡!Escribe s para salir!¡:')).lower()
                                            break

                                    elif oacen == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break                                 


                            elif oacen == 3:
                                p('Saliendo*.*')
                                es()
                                break                   

                    elif oace == 5:
                        while True:
                            p('1* Decimo 1')
                            p('2* Decimo 2')
                            p('3* salir')
                            es()
                            oaced = int(input('¡!Por favor dijita numero de opcion!¡:'))

                            if oaced == 1:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oaced1 = int(input('¡!Por favor dijita numero de opcion!¡:'))

                                    if oaced1 == 1:
                                        while True:
                                            for eg101 in estudiantes.gd101:
                                                p(eg101)
                                            es()
                                            eg101s = str(input('Escribe s para salir:')).lower()
                                            while eg101s != s:
                                                eg101s = str(input('¡!Escribe s para salir!¡:')).lower()
                                            break
                                    
                                    elif oaced1 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break

                            elif oaced == 2:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oaced2 = int(input('¡!Por favor dijita numero de opcion!¡:'))

                                    if oaced2 == 1:
                                        while True:
                                            for eg102 in estudiantes.gd102:
                                                p(eg102)
                                            es()
                                            eg102s = str(input('Escribe s para salir:')).lower()
                                            while eg102s != s:
                                                eg102s = str(input('¡!Escribe s para salir!¡:')).lower()
                                            break

                                    elif oaced2 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break        


                            elif oaced == 3:
                                p('Saliendo*.*')
                                es()
                                break

                    elif oace == 6:
                        while True:
                            p('1* Undecimo 1')
                            p('2* Undecimo 2')
                            p('3* salir')
                            es()
                            oaceu = int(input('¡!Por favor dijita numero de opcion!¡:'))

                            if oaceu == 1:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oaceu1 = int(input('¡!Por favor dijita numero de opcion!¡:'))

                                    if oaceu1 == 1:
                                        while True:
                                            for eg111 in estudiantes.gd111:
                                                p(eg111)
                                            es()
                                            eg111s = str(input('Escribe s para salir:')).lower()
                                            while eg111s != s:
                                                eg111s = str(input('¡!Escribe s para salir¡!:')).lower()
                                            break

                                    elif oaceu1 == 2:
                                        while True:
                                            for eg112 in estudiantes.gd112:
                                                p(eg112)
                                            es()
                                            eg112s = str(input('Escribe s para salir')).lower()
                                            while eg112s != s:
                                                eg112s = str(input('¡!Escribe s para salir¡!:')).lower()
                                            break       

                                    elif oaceu1 == 3:
                                        p('Saliendo*.*')
                                        es()
                                        break                         


                    elif oace == 7:
                        p('Saliendo*.*')
                        es()
                        break

            elif oac == 2:
                while True:
                    p('=^=^=^=^=^ Docentes de area =^=^=^=^=^')
                    es()
                    p('1* Naturales')
                    p('2* Fisica')
                    p('3* Sociales')
                    p('4* Filosofia')
                    p('5* Ingles')
                    p('6* Edu Fisica')
                    p('7* Religion')
                    p('8* Etica')
                    p('9* Castellano')
                    p('10* Tecnologia')
                    p('11* Economia politica')
                    p('12 *Matematicas')
                    es()
                    p('13* salir')
                    oacd = int(input('¡!Por favor dijita numero de opcion!¡:'))

                    if oacd == 1:
                        es()
                        p('= Ciencias naturales =')
                        es()
                        p('1* dora')
                        p('2* jhon')
                        p('3* angelica')
                        pause()

                    elif oacd == 2:
                        es()
                        p('== Fisica ==')
                        es()
                        p('1* angela')
                        p('2* alex')
                        p('3* angel')
                        pause()

                    elif oacd == 3:
                        es()
                        p('=== Sociales ===')
                        es()
                        p('1* magdalena')
                        p('2* mario')
                        p('2* capera')
                        pause() 

                    elif oacd == 4:
                        es()
                        p('==== Filosofia ====')
                        es()
                        p('1* capera')
                        p('2* elsa')
                        pause()

                    elif oacd == 5:
                        es()
                        p('===== Ingles =====')
                        es()
                        p('carlos')
                        p('sara')
                        pause()

                    elif oacd == 6:
                        es() 
                        p('====== Edu fisica =====')
                        es()
                        p('sebastian')
                        pause()

                    elif oacd == 7:
                        es()
                        p('======= Religion =======')
                        es()
                        p('luz')
                        pause()

                    elif oacd == 8:
                        es()
                        p('======= Etica ========')
                        es()
                        p('luz')
                        pause()

                    elif oacd == 9:
                        es()
                        p('========= Castellano =========')
                        es()
                        p('1* magdalena')
                        p('2* sofia')
                        pause()

                    elif oacd == 10:
                        es() 
                        p('========== Tecnologia ==========')
                        es()
                        p('geovanny')
                        pause()

                    elif oacd == 11:
                        es()
                        p('=========== Economia y Politica ===========')
                        es()
                        p('capera')
                        pause()

                    elif oacd == 12:
                        es()
                        p('=========== Matematicas ============')
                        es()  
                        p('1* ruben')
                        p('2* angela')
                        pause()

                    elif oacd == 13:
                        es()
                        p('Saliendo*.*')
                        es()
                        break            

            elif oac == 3:
                while True:
                    p('********* Directivos *********')
                    p('******** institucionales ********')
                    es()
                    p('1* Rector')
                    p('2* Cordinador')
                    p('3* Psicologa')
                    p('4* Secretario academico')
                    p('5* salir')
                    es()
                    oaci = int(input('¡!Por favor dijita numero de opcion!¡:'))

                    if oaci == 1:
                        while True:
                            p('RECTOR')
                            es()
                            p('1* Persona acargo')
                            p('2* Funcion')
                            p('3* salir')
                            es()
                            oacir = int(input('!¡Porfavor dijite numero de opcion¡!'))
                            es()
            
                            if oacir == 1:
                                while True:
                                    p('== Rector institucional ==')
                                    p('jhon jairo vernal')
                                    es()
                                    oacir1 = str(input('Escribe s para salir:')).lower()
                                    while oacir1 != s:
                                        oacir1 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break

                            elif oacir == 2:
                                while True:
                                    p('** Funcion rector **')
                                    p('Es la maxima autoridad de el colegio se encarga')
                                    p('de dirigir la institucion, tomar deciciones y supervisar')
                                    p('el funcionamiento de el colegio')
                                    es()
                                    oacir2 = str(input('Escribe s para salir:')).lower()
                                    while oacir2 != s:
                                        oacir2 = str(input('¡!Escribe s para salir¡!:')).lower()
                                    break

                            elif oacir == 3:
                                p('Saliendo*.*')
                                es()
                                break     

                    elif oaci == 2:
                        while True: 
                            p('CORDINADOR')
                            es()
                            p('1* Persona acargo')
                            p('2* Funcion')
                            p('3* salir')
                            es()
                            oacic = int(input('!¡Porfavor dijita numero de opcion¡!'))
                            es()

                            if oacic == 1:
                                while True:
                                    p('==== Cordinador ====')
                                    p('elder sanchez')
                                    es()
                                    oacic1 = str(input('Escribe s para salir:')).lower()
                                    while oacic1 != s:
                                        oacic1 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break

                            elif oacic == 2:
                                while True: 
                                    p('**** Funciones rector ****')
                                    p('se encarga de organizar las clases, horarios')
                                    p('materias, y actividades academicas')
                                    p('tambien supervisa el trabajo de docente')
                                    es()
                                    oacic2 = str(input('Escribe s para salir:')).lower()
                                    while oacic2 != s:
                                        oacic2 = str(input('¡!Escribe s para continuar!¡:')).lower()
                                    break

                            elif oacic == 3:
                                p('Saliendo*.*')
                                es()
                                break             

                    elif oaci == 3:
                        while True:
                            p('PSICOLOGA')
                            es()
                            p('1* Persona acargo')
                            p('2* Funcion')
                            p('3* salir')
                            es()
                            oacip = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                            es()

                            if oacip == 1:
                                while True:
                                    p('====== Psicologa ======')
                                    p('tatiana mendes')
                                    es()
                                    oacip1 = str(input('Escribe s para salir:')).lower()
                                    while oacip1 != s:
                                        oacip1 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break    

                            elif oacip == 2:
                                while True:
                                    p('******* funciones psicologa ********')
                                    p('Se encarga principalmente de ayudar al bienestar emocional,')
                                    p('social y academico de los estudiantes')
                                    es()
                                    oacip2 = str(input('Escribe s para salir:')).lower()
                                    while oacip2 != s:
                                        oacip2 = str(input('¡!Escribe s para salir!¡')).lower()
                                    break 

                            elif oacip == 3:
                                p('Saliendo*.*')
                                es()
                                break       

                    elif oaci == 4:
                        while True:
                            p('SECRETARIO ACADEMICO')
                            es()
                            p('1* Persona acargo')
                            p('2* Funcion')
                            p('3* salir')
                            es()
                            oacis = int(input('!¡Porfavor dijita numero de opcion¡!'))
                            es()

                            if oacis == 1:
                                while True:
                                    p('======== Secretario academico ========')
                                    p('carlos ruben espitia')
                                    es()
                                    oacis1 = str(input('Escribe s para salir:')).lower()
                                    while oacis1 != s:
                                        oacis1 = str(input('¡!Escribe s para salir¡!:')).lower()
                                    break 

                            elif oacis == 2:
                                while True:
                                    p('********** funciones secretario academico **********') 
                                    p('Se encarga de las bases de datos,l registrar nuevos estudiantes')
                                    es()
                                    oacis2 = str(input('Escribe s para salir:')).lower()
                                    while oacis2 != s:
                                        oacis2 = str(input('¡!Escribe s para salir¡!:')).lower()
                                    break

                            elif oacis == 3:
                                p('Saliendo*.*')
                                es()
                                break
                                
                    elif oaci == 5:
                        p('Saliendo*.*')
                        es()
                        break

            elif oac == 4:
                while True:
                    p('********** Eventos **********')
                    p('****** Institucionales *****')
                    es()
                    p('1* Dia cultura')
                    p('2* Feria de la ciencia')
                    p('3* Izada de bandera')
                    p('4* Dia de la independencia')
                    p('5* Reunion de padres de familia')
                    p('6* salir')
                    es()
                    oace = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                    es()

                    if oace == 1:
                        while True:
                            p('*=*=*=*= Dia de la cultura *=*=*=*=')
                            es()
                            p('1* Ver dia')
                            p('2* Explicacion')
                            p('3* salir')
                            es()
                            oacec = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                            es()

                            if oacec == 1:
                                while True:
                                    p('* Dia a desarrollar *')
                                    es()
                                    p('El dia a desarrollar este evento es el 1 de abril')
                                    es()
                                    oacec1 = str(input('Escribe s para salir:')).lower()
                                    while oacec1 != s:
                                        oacec1 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break     

                            elif oacec == 2:
                                while True:
                                    p('Evento donde los estudiantes presentan bailes, obras de teatro')
                                    p('musica y expociciones. objetivgo mostrar los talentos')
                                    p('artisticos')
                                    es()
                                    oacec2 = str(input('Escribe s para salir:')).lower()
                                    while oacec2 != s:
                                        oacec2 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break      


                            elif oacec == 3:
                                p('Saliendo*.*')
                                es()
                                break    

                    elif oace == 2:
                        while True:
                            p('*=*=*=*= Feria de la ciencia *=*=*=*=')
                            es()
                            p('1* Ver dia')
                            p('2* Explicacion')
                            p('3* salir')
                            es()
                            oacef = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                            es()

                            if oacef == 1:
                                while True:
                                    p('El dia a desarrollar este evento es el 20 de agosto')
                                    es()
                                    oacef1 = str(input('Escribe s para salir:')).lower()
                                    while oacef1 != s:
                                        oacef1 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break    

                            elif oacef == 2:
                                while True:
                                    p('Actividad academica donde los estudiantes presentan')
                                    p('experimentos cientificos, sirve para desarrollar la curiosidad,')
                                    p('la ivestigacion y el pensamiento critico')
                                    es()
                                    oacef2 = str(input('Escribe ese paea salir:')).lower()
                                    while oacef2 != s:
                                        oacef2 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break    

                            elif oacef == 3:
                                p('Saliendo*.*')
                                es()
                                break    

                    elif oace == 3:
                        while True:
                            p('*=*=*=*= Izada de bandera *=*=*=*=')
                            es()
                            p('1* Ver dias')
                            p('2* Explicacion')
                            p('3* salir')
                            es()
                            oacei = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                            es()

                            if oacei == 1:
                                while True:
                                    p('Esta actividad se desarrolla cada final de periodo,')
                                    p('es decir. abril 15, agosto 21, noviembre 21')
                                    es()
                                    oacei1 = str(input('Escribe s para salir:')).lower()
                                    while oacei1 != s:
                                        oacei1 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break    

                            elif oacei == 2:
                                while True:
                                    p('Acto civico donde donde se rinden honores ala bandera,')
                                    p('y se reconocen estudiantes destacados')
                                    es()
                                    oacei2 = str(input('Escribe s para salir:')).lower()
                                    while oacei2 != s:
                                        oacei2 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break    

                            elif oacei == 3:
                                p('Saliendo*.*')
                                es()
                                break    

                    elif oace == 4:
                        while True:
                            p('*=*=*=*= Dia de la independencia *=*=*=*=')
                            es()
                            p('1* Ver dias')
                            p('2* Explicacion')
                            p('3* salir')
                            es()
                            oacein = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                            es()

                            if oacein == 1:
                                while True:
                                    p('El dia de el desarrollo de el evento es')
                                    p('20 de agosto')
                                    es()
                                    oacein1 = str(input('Escribe s para salir:')).lower()
                                    while oacein1 != s:
                                        oacein1 = str(input('¡!Escribe s para salir¡!:')).lower()
                                    break

                            elif oacein == 2:
                                while True:
                                    p('Es una actividad donde el colegio conmemora')
                                    p('la historia de el pais, con actos civicos')
                                    p('memorias culturales')
                                    es()
                                    oacein2 = str(input('Escribe s para salir:')).lower()
                                    while oacein2 != s:
                                        oacein2 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break    

                            elif oacein == 3:
                                p('Saliendo*.*')
                                es()
                                break

                    elif oace == 5:
                        while True:
                            p('*=*=*=*= Reunion de acudientes *=*=*=*=')
                            es()
                            p('1* Ver dias')
                            p('2* Explicacion')
                            p('3* salir')
                            es()
                            oacer = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                            es()

                            if oacer == 1:
                                while True:
                                    p('El dia de el desarrollo es dos dias despues')
                                    p('de el final de periodo')
                                    p('es decir. abril 15, agosto 21, noviembre 21')
                                    es()
                                    oacer1 = str(input('Escribe s para salir:')).lower()
                                    while oacer1 != s:
                                        oacer1 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break

                            elif oacer == 2:
                                while True:
                                    p('Reuniones organizadas por el colegio')
                                    p('para orientar a los acudientes sobre la educacion,')
                                    p('convivencia y desarrollo de los estudiantes')
                                    es()
                                    oacer2 = str(input('Escribe s para salir:')).lower()
                                    while oacer2 != s:
                                        oacer2 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break    

                            elif oacer == 3:
                                p('Saliendo*.*')
                                es()
                                break

                    elif oace == 6:
                        p('Saliendo*.*')
                        es()
                        break    

            elif oac == 5:
                p('Saliendo*.*')
                es()
                break

    elif persona == e:
        while True:  
            p('=*=*=*= Menu estudiantes =*=*=*=')
            p('1* Temas')
            p('2* Docentes')
            p('3* Directivos')
            p('4* Grados')
            p('5* salir')
            es()
            oe = int(input('¡!Por favor dijita numero de opcion!¡:'))

            if oe == 1:
                while True:
                    p('/////////// temas de cada area /////////////')
                    es()
                    p('1* Naturales')
                    p('2* Fisica')
                    p('3* Sociales')
                    p('4* Filosofia')
                    p('5* Ingles')
                    p('6* Edu Fisica')
                    p('7* Religion')
                    p('8* Etica')
                    p('9* Castellano')
                    p('10* Tecnologia')
                    p('11* Economia politica')
                    p('12* Matematicas')
                    es()
                    p('^^^^^^ Info ^^^^^')
                    es()
                    p('13* salir')

                    oet = int(input('!¡Porfavor dijite numero de  opcion¡!:'))
                    es()

                    if oet == 1:
                        p('*Temas ciencias naturales *')
                        p('*Animales')
                        p('*Celulas')
                        p('*Medio ambiente')
                        p('*Quimica')
                        p('*Laboratorio')
                        pause()

                    elif oet == 2:
                        p('** Temas fisica materia **')
                        es()
                        p('*Mru')
                        p('*Factores de conversion')
                        p('*Unidades de medida')
                        pause()

                    elif oet ==3:
                        p('**** Temas sociales ****')
                        es()
                        p('*Imperialismo')
                        p('*Socialismo')
                        p('*Comunismo')
                        p('*Nacionalismo')
                        pause()

                    elif oet == 4:
                        p('***** Temas filosofia *****')
                        es()
                        p('*Inicios de la filosofia')
                        p('*Principales pensadores de la edad media')
                        pause()
            
                    elif oet == 5:
                        p('******* Temas ingles ******')
                        es()
                        p('*Verb to be')
                        p('*Lisenig')
                        p('*Read')
                        pause()

                    elif oet == 6:
                        p('******* Temas edu. fisica ******')
                        es()
                        p('*Juegos tradicionales')
                        p('*Historia de el basquetball')
                        p('*Historia de el fottball')
                        pause()
            
                    elif oet == 7:
                        p('******** Temas religion ********')
                        es()    
                        p('*Sin sentidos')
                        p('*Sentidos')
                        p('*Yo pertenezco a jesus')
                        pause()

                    elif oet == 8:
                        p('********* Temas etica *********')
                        es()
                        p('*Sentimientos')
                        p('*Perdon')
                        p('*Valores')
                        pause()

                    elif oet == 9:
                        p('********** Temas  castellano **********')
                        es()
                        p('*La vida feliz')
                        p('*La metarmofosis')
                        p('*Noches blancas')
                        pause()            

                    elif oet == 10:
                        p('*********** Temas tecnologia ***********')
                        es()
                        p('*Diagrama de flujo')
                        p('*Makecode')
                        p('*Python')
                        pause()

                    elif oet == 11:
                        p('************ Temas ciencias economicas y politicas ************')
                        es()
                        p('*Pensadores')
                        p('*Origen')
                        p('*Importancia')
                        pause()

                    elif oet == 12:
                        p('************* Temas matematicas *************')
                        es()
                        p('*Seno')
                        p('*Coseno')
                        p('*Tangente')
                        pause()

                    elif oet == 13:
                        p('Saliendo*.*')
                        es()
                        break


            elif oe == 2:
                while True:
                    p('=^=^=^=^=^ Docentes de area =^=^=^=^=^')
                    es()
                    p('1* Naturales')
                    p('2* Fisica')
                    p('3* Sociales')
                    p('4* Filosofia')
                    p('5* Ingles')
                    p('6* Edu Fisica')
                    p('7* Religion')
                    p('8* Etica')
                    p('9* Castellano')
                    p('10* Tecnologia')
                    p('11* Economia politica')
                    p('12 *Matematicas')
                    es()
                    p('13* salir')
                    oed = int(input('¡!Por favor dijita numero de opcion!¡:'))

                    if oed == 1:
                        es()
                        p('= Ciencias naturales =')
                        es()
                        p('1* dora')
                        p('2* jhon')
                        p('3* angelica')
                        pause()

                    elif oed == 2:
                        es()
                        p('== Fisica ==')
                        es()
                        p('1* angela')
                        p('2* alex')
                        p('3* angel')
                        pause()

                    elif oed == 3:
                        es()
                        p('=== Sociales ===')
                        es()
                        p('1* magdalena')
                        p('2* mario')
                        p('2* capera')
                        pause() 

                    elif oed == 4:
                        es()
                        p('==== Filosofia ====')
                        es()
                        p('1* capera')
                        p('2* elsa')
                        pause()

                    elif oed == 5:
                        es()
                        p('===== Ingles =====')
                        es()
                        p('carlos')
                        p('sara')
                        pause()

                    elif oed == 6:
                        es() 
                        p('====== Edu fisica =====')
                        es()
                        p('sebastian')
                        pause()

                    elif oed == 7:
                        es()
                        p('======= Religion =======')
                        es()
                        p('luz')
                        pause()

                    elif oed == 8:
                        es()
                        p('======= Etica ========')
                        es()
                        p('luz')
                        pause()

                    elif oed == 9:
                        es()
                        p('========= Castellano =========')
                        es()
                        p('1* magdalena')
                        p('2* sofia')
                        pause()

                    elif oed == 10:
                        es() 
                        p('========== Tecnologia ==========')
                        es()
                        p('geovanny')
                        pause()

                    elif oed == 11:
                        es()
                        p('=========== Economia y Politica ===========')
                        es()
                        p('capera')
                        pause()

                    elif oed == 12:
                        es()
                        p('=========== Matematicas ============')
                        es()  
                        p('1* ruben')
                        p('2* angela')
                        pause()

                    elif oed == 13:
                        p('Saliendo*.*')
                        es()
                        break

            elif oe == 3:
                while True:
                    p('********* Directivos *********')
                    p('******** institucionales ********')
                    es()
                    p('1* Rector')
                    p('2* Cordinador')
                    p('3* Psicologa')
                    p('4* Secretario academico')
                    p('5* salir')
                    es()
                    oedi = int(input('¡!Por favor dijita numero de opcion!¡:'))

                    if oedi == 1:
                        while True:
                            p('RECTOR')
                            es()
                            p('1* Persona acargo')
                            p('2* Funcion')
                            p('3* salir')
                            es()
                            oedir = int(input('!¡Porfavor dijite numero de opcion¡!'))
                            es()
            
                            if oedir == 1:
                                while True:
                                    p('== Rector institucional ==')
                                    p('jhon jairo vernal')
                                    es()
                                    oedir1 = str(input('Escribe s para salir:')).lower()
                                    while oedir1 != s:
                                        oedir1 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break

                            elif oedir == 2:
                                while True:
                                    p('** Funcion rector **')
                                    p('Es la maxima autoridad de el colegio se encarga')
                                    p('de dirigir la institucion, tomar deciciones y supervisar')
                                    p('el funcionamiento de el colegio')
                                    es()
                                    oedir2 = str(input('Escribe s para salir:')).lower()
                                    while oedir2 != s:
                                        oedir2 = str(input('¡!Escribe s para salir¡!:')).lower()
                                    break

                            elif oedir == 3:
                                p('Saliendo*.*')
                                es()
                                break     

                    elif oedi == 2:
                        while True: 
                            p('CORDINADOR')
                            es()
                            p('1* Persona acargo')
                            p('2* Funcion')
                            p('3* salir')
                            es()
                            oedic = int(input('!¡Porfavor dijita numero de opcion¡!'))
                            es()

                            if oedic == 1:
                                while True:
                                    p('==== Cordinador ====')
                                    p('elder sanchez')
                                    es()
                                    oedic1 = str(input('Escribe s para salir:')).lower()
                                    while oedic1 != s:
                                        oedic1 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break

                            elif oedic == 2:
                                while True: 
                                    p('**** Funciones rector ****')
                                    p('se encarga de organizar las clases, horarios')
                                    p('materias, y actividades academicas')
                                    p('tambien supervisa el trabajo de docente')
                                    es()
                                    oedic2 = str(input('Escribe s para salir:')).lower()
                                    while oedic2 != s:
                                        oedic2 = str(input('¡!Escribe s para continuar!¡:')).lower()
                                    break

                            elif oedic == 3:
                                p('Saliendo*.*')
                                es()
                                break             

                    elif oedi == 3:
                        while True:
                            p('PSICOLOGA')
                            es()
                            p('1* Persona acargo')
                            p('2* Funcion')
                            p('3* salir')
                            es()
                            oedip = int(input('!¡Porfavor dijita numero de opcion¡!:'))
                            es()

                            if oedip == 1:
                                while True:
                                    p('====== Psicologa ======')
                                    p('tatiana mendes')
                                    es()
                                    oedip1 = str(input('Escribe s para salir:')).lower()
                                    while oedip1 != s:
                                        oedip1 = str(input('¡!Escribe s para salir!¡:')).lower()
                                    break    

                            elif oedip == 2:
                                while True:
                                    p('******* funciones psicologa ********')
                                    p('Se encarga principalmente de ayudar al bienestar emocional,')
                                    p('social y academico de los estudiantes')
                                    es()
                                    oedip2 = str(input('Escribe s para salir:')).lower()
                                    while oedip2 != s:
                                        oedip2 = str(input('¡!Escribe s para salir!¡')).lower()
                                    break 

                            elif oedip == 3:
                                p('Saliendo*.*')
                                es()
                                break       

                    elif oedi == 4:
                        while True:
                            p('SECRETARIO ACADEMICO')
                            es()
                            p('1* Persona acargo')
                            p('2* Funcion')
                            p('3* salir')
                            es()
                            oedis = int(input('!¡Porfavor dijita numero de opcion¡!'))
                            es()

                            if oedis == 1:
                                while True:
                                    p('======== Secretario academico ========')
                                    p('carlos ruben espitia')
                                    es()
                                    oedis1 = str(input('Escribe s para salir:')).lower()
                                    while oedis1 != s:
                                        oedis1 = str(input('¡!Escribe s para salir¡!:')).lower()
                                    break 

                            elif oedis == 2:
                                while True:
                                    p('********** funciones secretario academico **********') 
                                    p('Se encarga de las bases de datos,l registrar nuevos estudiantes')
                                    es()
                                    oedis2 = str(input('Escribe s para salir:')).lower()
                                    while oedis2 != s:
                                        oedis2 = str(input('¡!Escribe s para salir¡!:')).lower()
                                    break
 
                    elif oedi == 5:
                        p('Saliendo*.*')
                        es()
                        break



            elif oe == 4:
                while True:
                    p('1* Grado sexto')
                    p('2* Grado septimo')   
                    p('3* Grado octavo')
                    p('4* Grado noveno')
                    p('5* Grado decimo')
                    p('6* Grado once')
                    p('7* Salir')
                    es()

                    oee = int(input('!¡Por favor dijita numero de opcion¡!:'))
                    es()

                    if oee == 1:
                        while True:
                            p('1* Sexto 1')
                            p('2* Sexto 2')
                            p('3* Sexto 3')
                            p('4* salir')
                            oees = int(input('!¡Por favor dijita numero de opcion¡!:'))
                            if oees == 1:
                                while  True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oees1 = int(input('!¡Por favor escribe numero de opcion¡!:'))

                                    if oees1 == 1:
                                        while True:
                                            for eg61 in estudiantes.gd61:
                                                p(eg61)
                                                es()
                                            eg61s = str(input('Escribe s para salir:')).lower()
                                            while eg61s != s:
                                                eg61s = str(input('¡!Escribe s paea salir¡!:')).lower()
                                            break

                                    elif oees1 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break

                            elif oees == 2:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oees2 = int(input('!¡Por favor dijita numero de opcion¡!:'))
                                    
                                    if oees2 == 1:
                                        while True:
                                            for eg62 in estudiantes.gd62:
                                                p(eg62)
                                            es()
                                            eg62s = str(input('Escribe s para salir:')).lower()
                                            while eg62s != s:
                                                eg62s = str(input('¡!Escribe s para salir!¡:')).lower()    
                                            break
                                    
                                    elif oees2 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break

                            elif oees == 3:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oees3 = int(input('¡!Por favor dijita numero de opcion¡!:'))

                                    if oees3 == 1:
                                        while True:
                                            for eg63 in estudiantes.gd63:
                                                p(eg63)
                                            es()
                                            eg63s = str(input('Escribe s para salir:')).lower
                                            while eg63s != s:
                                                eg63s = str(input('¡!Escribe s para salir!¡:'))
                                            break    


                                    elif oees3 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break
                            elif oees == 4:
                                p('Saliendo*.*')
                                es()
                                break

                    elif oee == 2:
                        while True:
                            p('1* Septimo 1')
                            p('2* Septimo 2')
                            p('3* Septimo 3')
                            p('4* salir')
                            es()
                            oeesp = int(input('¡!Por favor dijita numero de opcion¡!:'))

                            if oeesp == 1:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oeesp1 = int(input('¡!Por favor dijita numero de opcion!¡:'))

                                    if oeesp1 == 1:
                                        while True:
                                            for eg71 in estudiantes.gd71:
                                                p(eg71)
                                            es()
                                            eg71s = str(input('Escribe s para salir')).lower()
                                            while eg71s != s:
                                                eg71s = str(input('¡!Escribe s para salir!¡'))
                                            break

                                    elif oeesp1 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break     

                            elif oeesp == 2:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oeesp2 = int(input('¡!Por favor dijita numero de opcion!¡:'))

                                    if oeesp2 == 1:
                                        while True:
                                            for eg72 in estudiantes.gd72:
                                                p(eg72)
                                            es()
                                            eg72s = str(input('Escribe s para continuar:')).lower()
                                            while eg72s != s:
                                                eg72s = str(input('¡!Escribe s para continuar:')).lower()
                                            break


                                    elif oeesp2 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break

                            elif oeesp == 3:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oeesp3 = int(input('¡!Por favor dijita numero de opcion!¡'))

                                    if oeesp3 == 1:
                                        while True:
                                            for eg73 in estudiantes.gd73:
                                                p(eg73)
                                            es()
                                            eg73s = str(input('Escribe s para salir')).lower()
                                            while eg73s != s:
                                                eg73s = str(input('¡!Escribe s para salir!¡')).lower()
                                            break

                                    elif oeesp3 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break
                            
                            elif oeesp == 4:
                                p('Saliendo*.*')
                                es()
                                break


                    elif oee == 3:
                        while True:
                            p('1* Octavo 1')
                            p('2* Octavo 2')
                            p('3* salir')
                            oeeo = int(input('¡!Por favor dijita numero de opcion¡!'))

                            if oeeo == 1:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oeeo1 = int(input('¡!Por favor escribe numero de opcion!¡'))

                                    if oeeo1 == 1:
                                        while True:
                                            for eg81 in estudiantes.gd81:
                                                p(eg81)
                                            es()
                                            eg81s = str(input('Escribe s para salir')).lower()
                                            while eg81s != s:
                                                eg81s = str(input('¡!Escribe s para salir!¡')).lower()
                                            break    

                                    elif oeeo1 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break
                            
                            elif oeeo == 2:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oeeo2 = int(input('¡!Por favor dijita numero de opcion'))

                                    if oeeo2 == 1:
                                        while True:
                                            for eg82 in estudiantes.gd82:
                                                p(eg82)
                                            es()
                                            eg82s = str(input('Escribe s para salir:')).lower()
                                            while eg82s != s:
                                                eg82s = str(input('¡!Escribe s para salir!¡:')).lower()
                                            break         

                                    elif oeeo2 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break


                            elif oeeo == 3:
                                p('Saliendo*.*')
                                es()
                                break
                    
                    elif oee == 4:
                        while True:
                            p('1* Noveno 1')
                            p('2* Noveno 2')
                            p('3* saliendo')
                            es()
                            oeen = int(input('¡!Por favor dijita numero de opcion!¡'))

                            if oeen == 1:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    oeen1 = int(input('¡!Por favor dijita numero de opcion!¡'))

                                    if oeen1 == 1:
                                        while True:
                                            for eg91 in estudiantes.gd91:
                                                p(eg91)
                                            es()
                                            eg91s = str(input('Escribe s para salir:')).lower()
                                            while eg91s != s:
                                                eg91s = str(input('¡!Escribe s para salir!¡:')).lower()
                                            break

                                    elif oeen1 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break

                            elif oeen == 2:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oeen2 = int(input('¡!Por favor dijita numero opcion!¡:'))

                                    if oeen2 == 1:
                                        while True:
                                            for eg92 in estudiantes.gd92:
                                                p(eg92)
                                            es()
                                            eg92s = str(input('Escribe s para salir:')).lower()
                                            while eg92s != s:
                                                eg92s = str(input('¡!Escribe s para salir!¡:')).lower()
                                            break

                                    elif oeen2 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break                                 

                            elif oeen == 3:
                                p('Saliendo*.*')
                                es()
                                break                   

                    elif oee == 5:
                        while True:
                            p('1* Decimo 1')
                            p('2* Decimo 2')
                            p('3* salir')
                            es()
                            oeed = int(input('¡!Por favor dijita numero de opcion!¡:'))

                            if oeed == 1:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oeed1 = int(input('¡!Por favor dijita numero de opcion!¡:'))

                                    if oeed1 == 1:
                                        while True:
                                            for eg101 in estudiantes.gd101:
                                                p(eg101)
                                            es()
                                            eg101s = str(input('Escribe s para salir:')).lower()
                                            while eg101s != s:
                                                eg101s = str(input('¡!Escribe s para salir!¡:')).lower()
                                            break
                                    
                                    elif oeed1 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break

                            elif oeed == 2:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oeed2 = int(input('¡!Por favor dijita numero de opcion!¡:'))

                                    if oeed2 == 1:
                                        while True:
                                            for eg102 in estudiantes.gd102:
                                                p(eg102)
                                            es()
                                            eg102s = str(input('Escribe s para salir:')).lower()
                                            while eg102s != s:
                                                eg102s = str(input('¡!Escribe s para salir!¡:')).lower()
                                            break

                                    elif oeed2 == 2:
                                        p('Saliendo*.*')
                                        es()
                                        break        


                            elif oeed == 3:
                                p('Saliendo*.*')
                                es()
                                break

                    elif oee == 6:
                        while True:
                            p('1* Undecimo 1')
                            p('2* Undecimo 2')
                            p('3* salir')
                            es()
                            oeeu = int(input('¡!Por favor dijita numero de opcion!¡:'))

                            if oeeu == 1:
                                while True:
                                    p('1* Ver estudiantes')
                                    p('2* salir')
                                    es()
                                    oeeu1 = int(input('¡!Por favor dijita numero de opcion!¡:'))

                                    if oeeu1 == 1:
                                        while True:
                                            for eg111 in estudiantes.gd111:
                                                p(eg111)
                                            es()
                                            eg111s = str(input('Escribe s para salir:')).lower()
                                            while eg111s != s:
                                                eg111s = str(input('¡!Escribe s para salir¡!:')).lower()
                                            break

                                    elif oeeu1 == 2:
                                        while True:
                                            for eg112 in estudiantes.gd112:
                                                p(eg112)
                                            es()
                                            eg112s = str(input('Escribe s para salir')).lower()
                                            while eg112s != s:
                                                eg112s = str(input('¡!Escribe s para salir¡!:')).lower()
                                            break       



                                    elif oeeu1 == 3:
                                        p('Saliendo*.*')
                                        es()
                                        break                         

                    elif oee == 7:
                        p('Saliendo*.*')
                        es()
                        break
            
            elif oe == 5:
                p('Saliendo*.*')
                es()
                break

    if persona == i:
        while True:
            es()
            with open("info.txt", "r") as archivo:
                for linea in archivo:
                    p(linea.strip())
            sa = int(input('Escribe 1* para salir'))
            while sa != 1:
                sa = int(input('!¡Escribe 1 para salir¡!'))
            break                
                                                 
