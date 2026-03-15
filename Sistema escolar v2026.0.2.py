#Sistema escolar v2026.0.1
#desarrollador Cuz-Dev
#Si lo puedes imaginar lo puedes programar

#Funcion personalizada que mostrara el numero de version,cuando sea llamada.
def v():
    print('V2026.0.2')

#Conjunto que almacena todos loes estudiantes de el grado 6:1
gre6:1 = {
    "1* Elnora Padilla",
    "2* Rodney Tran",
    "3* Callie Gray",
    "4* Jean Simpson",
    "5* Lloyd Johnston",
    "6* Harry Wright",
    "7* Elmer McLaughlin",
    "8* Harold Fields",
    "9* Lelia Sparks",
    "10* Beulah Flowers",
    "11* Christopher Rodriquez",
    "12* Mayme Armstrong",
    "13* Gavin Mathis",
    "14* Clara Payne",
    "15* Bessie KimBertha Reynolds",
    "16* Ricky Myers",
    "17* Jackson Torres",
    "18* Mike Cooper",
    "19* Hilda Pittman",
    "20* Olive Howard",
    "21* Mollie Berry"
}

v()
#variable llamada colegio que pide un dato cadena al usuario "str"
#lo almacenara en la variable para usarlo despues.
#Usa una funcion para cadena llamda lower(), la cual convertira todos los elementos em minuscula.
colegio = str(input('!¡Por favor escribe el nombre de este colegio para continuar: ')).lower()

#Funcion personalizada llamada es(), su funcion es evitar tner que poner espacios con print
#manualmente.
def es():
    print('     ')

#funcion personalizada llamada p(), cumplira la funcion de print
def p(mensaje):
        print(mensaje)

#Variable que almacena el nombre de el colegio
c = 'colegio python'

#Bucle while se repetira asta que la entrada de el usuario ponga el nombre de colegio correcto
while c != colegio:
    es()
    colegio = str(input('!colegio incorrecto!:')).lower()
es()    

#Pinta en pantalla la bienvenido al menu con la funcion personalizada
p('========== !¡Hola este es al menu¡! ==========')
p('********** ¡!sede bachiller¡! ************')


#Pìnta en pantalla el mensaje bienvenido al menu
es()
p('******** !¡Bienvenido al sistema!¡ ********')
es()

#Variable que pide al usuario una entrada en tipo de dato cadena,
#en donde el usuario escribira a que menu quiere entrar, Las funcion lower(),
#convertira todo lo que escriba el usuario en minusculas.
persona = str(input('?Eres  cordinador , docente , estudiante , acudiente¿: ')).lower()

#Variables que contienen los datos necesarios para la ejecucion de el codigo
d = 'docente'
e = 'estudiante'
co = 'cordinador'
c = 202614
cod = 202601
acu = 'acudiente'
es()

#Condicional, evalua si la entrada de el usuario almacena en la variable persona es igual al dato
#guardado en la variable d
if persona == d:
    cd = int(input('!Hola profe¡, porfavor escribe tu clave:'))
    while  cd != c:
        es()
        cd = int(input('!Clave incorrecta¡, ?acaso no eres docente¿:'))

#Despues de alamacenar una entrada de usuario en dato entero, en la variable cd
#Usara el bucle while, para que se repita asta que se cumpla la condicion,

    es()
    p('!¡Bienvenido profe¡!')
    es()
    p('============== MENU DE OPCIONES DOCENTE ===============')
    p(' ========== opciones ==========')
    p('1* Ver areas')
    p('2* Eventos')
    p('3* Directivos')
    p('=*=*^=*=*=^=*=*=^')


#variable od que almacena dato de usuario en dato entero,
    od = int(input('!Porfavor dijite numero de opcion¡:'))
    es()

#Condicional anidado, evalua si la entrada de el usuarion almacenada en la variable od si
#es 1, entonces mostrara el menu de docentes 
    if od == 1:
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

#Variable odp que almacena entrada de el usuario en dato entero
        odp = int(input('!Porfavor dijite su opcion¡: '))
        es()
#Condicional si la entrada de el usuario en la variable odp  es 1,
#entonces mostrara los temas de ciencias naturales
        if odp == 1:
            p('* Temas ciencias naturales *')
            p('*Animales')
            p('*Celulas')
            p('*Medio ambiente')
            p('*Quimica')
            p('*Laboratorio')
#Condicional sino, la entrada de el usuario en la variable odp es 2,
#entonces mostrara los temas de fisica materia
        elif odp == 2:
            p('** Temas fisica materia **')
            es()
            p('*Mru')
            p('*Factores de conversion')
            p('*Unidades de medida')
#Condicional sino, la entrada de el usuario en la variable odp es 3,
#entonces mostrara los temas de sociales
        elif odp ==3:
            p('**** Temas sociales ****')
            es()
            p('*Imperialismo')
            p('*Socialismo')
            p('*Comunismo')
            p('*Nacionalismo')
#Condicional sino, la entrada de el usuario en la variable odp es 4,
#entonces mostrara los temas de filosofia   
        elif odp == 4:
            p('***** Temas filosofia *****')
            es()
            p('*Inicios de la filosofia')
            p('*Principales pensadores de la edad media')
#Condicional sino, la entrada de el usuario en la variable odp es 5,
#enronces mostrara los temas de ingles            
        elif odp == 5:
            p('******* Temas ingles ******')
            es()
            p('*Verb to be')
            p('*Lisenig')
            p('*Read')
#Condicional sino, la entrada de el usuario en la variable odp es 6,
#entonces mostrara los temas de edu fisica
        elif odp == 6:
            p('******* Temas edu. fisica ******')
            es()
            p('*Juegos tradicionales')
            p('*Historia de el basquetball')
            p('*Historia de el fottball')
#Condicional sino, la entrada de el usuario en la variable odp es 7,
#entonces mostrara los temas de religion            
        elif odp == 7:
            p('******** Temas religion ********')
            es()
            p('*Sin sentidos')
            p('*Sentidos')
            p('*Yo pertenezco a jesus')
#Condicional sino, la entrada de el usuario en la variable odp es 8
#entonces mostrara los temas de etica
        elif odp == 8:
            p('*********Temas etica *********')
            es()
            p('*Sentimientos')
            p('*Perdon')
            p('*Valores')
#Condicional sino, la entrada de el usuario en la variable odp es 9,
#entonces mostrara los temas castellano
        elif odp == 9:
            p('********** Temas  castellano **********')
            es()
            p('*La vida feliz')
            p('*La metarmofosis')
            p('*Noches blancas')            
#Condicional sino, la entrada de el usuario en la variable odp es 10,
#entonces mostrara los temas de tecnologia
        elif odp == 10:
            p('*********** Temas tecnologia ***********')
            es()
            p('*Diagrama de flujo')
            p('*Makecode')
            p('*Python')
#Condicional sino, la entrad de el usuario en la variable odp es 11,
#entonces mostrara los temas de ciencias economicas y politicas
        elif odp == 11:
            p('************ Temas ciencias economicas y politicas ************')
            es()
            p('*Pensadores')
            p('*Origen')
            p('*Importancia')
#Condional sino, la entrada de el usuario en la variable odp es 12,
#entonces mostrara los temas de matematicas
        elif odp == 12:
            p('************* Temas matematicas *************')
            es()
            p('*Seno')
            p('*Coseno')
            p('*Tangente')
#Condicional sino, la entrada de el usuario en la varible odp es 13,
#entonces mostrara un menu con los docentes de cada area
        elif odp == 13:
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
            #Variable odpd que almacena entrada de usuario en dato entero
            odpd = int(input('!Porfavor dijita el numero de opcion¡:'))
            es()
            #Condicional si, la entrada de el usuario en la variable odpd es 1,
            #mostrara los docentes en la asignatura de ciencias naturales
            if odpd == 1:
                p('= Ciencias naturales =')
                es()
                p('1* dora')
                p('2* jhon')
                p('3* angelica')
            #Condicional sino, la entrada de el usuario en la variable odpd es 2,
            #mostrara los docentes en la asignatura de fisica
            elif odpd == 2:
                p('== Fisica ==')
                es()
                p('1* angela')
                p('2* alex')
                p('3* angel')
            #Condicional sino, la entrada de el usuario en la variable odpd es 3,
            #mostrara los docentes en la asignatura de sociales    
            elif odpd ==3:
                p('=== Sociales ===')
                es()
                p('1* magdalena')
                p('2* mario')
                p('2* capera')
            #Condional sino, la entrada de el usuario en la variable odpd es 4,
            #mostrara los docentes en la asignatura de filosofia
            elif odpd == 4:
                p('==== Filosofia ====')
                es()
                p('1* capera')
                p('2* elsa')
            #Condicional sino, la entrada de el usuario en la variable odpd es 5,
            #mostrara los docentes en la asignatura de ingles
            elif odpd == 5:
                p('===== Ingles =====')
                es()
                p('carlos')
                p('sara')
            #Condional sino, la entrada de el usuario en la variable odpd es 6,
            #mostrara los docentes en la asignatura de edu fisica
            elif odpd == 6:
                p('====== Edu fisica =====')
                es()
                p('sebastian')
            #Condicional sino, la entrada de el usuario en la variable odpd es 7,
            #mostrara los docente en la asigantura de religion
            elif odpd == 7:
                p('======= Religion =======')
                es()
                p('luz')
            #Condional sino, la entrada de el usuario en la variable odpd es 8,
            #mostrara los docentes en la asignatura de etica 
            elif odpd == 8:
                p('======= Etica ========')
                es()
                p('luz')
            #Condional sino, la entrada de el usario en la variable odpd es 9,
            #mostrara los docentes en la asignatura de castellano
            elif odpd == 9:
                p('========= Castellano =========')
                es()
                p('1* magdalena')
                p('2* sofia') 
            #Condional sino, la entrada de el usuario en la variable odpd es 10,
            #mostrara los docentes en la asignatura de tecnologia
            elif odpd == 10:
                p('========== Tecnologia ==========')
                es()
                p('geovanny')
            #Condional sino, la entrada de el usurio en la variable odpd es 11,
            #mostrara los docentes en la sasignatura de ciencias economicas y politica    
            elif odpd == 11:
                p('=========== Economia y Politica ===========')
                es()
                p('capera')
            #Condicional sino, la entrada de el usuario en la variable odpd es 12,
            #mostrara los docentes en la asignatura de matematicas    
            elif odpd == 12:
                p('=========== Matematicas ============')
                es()  
                p('1* ruben')
                p('2* angela')
        
#Condional anidado sino, evalua si la entrada de el usuario almacenada en la variable od
#es 2, entonces mostrara el menu de eventos institucionales
    elif od == 2:
        p('********** Eventos **********')
        p('****** Institucionales *****')
        es()
        p('1* Dia cultura')
        p('2* Feria de la ciencia')
        p('3* Izada de bandera')
        p('4* Dia de la independencia')
        p('5* Reunion de padres de familia')
        es()
        ode = int(input('!¡ Porfavor dijita tu numero de opcion ¡!'))
        es()
#Condional       
        if ode == 1:
            p('*=*=*=*= Dia de la cultura *=*=*=*=')
            es()
            p('1* Ver dia')
            p('2* Explicacion')
            es()
            odec = int(input('!¡ Porfavor dijita tu opcion ¡!'))
            es()

            if odec == 1:
                p('* Dia a desarrollar *')
                es()
                p('El dia a desarrollar este evento es el 1 de abril')
 

            elif odec == 2:
                p('Evento donde los estudiantes presentan bailes, obras de teatro')
                p('musica y expociciones. objetivgo mostrar los talentos')
                p('artisticos')

        elif ode == 2:
            p('*=*=*=*= Feria de la ciencia *=*=*=*=')
            es()
            p('1* Ver dia')
            p('2* Explicacion')
            es()
            odef = int(input('!¡ Porfavor dijita tu opcion ¡!'))
            es()

            if odef == 1:
                p('El dia a dessarrollar este evento es el 20 de agosto')

            elif odef == 2:
                p('Actividad academica donde los estudiantes presentan')
                p('experimentos cientificos, sirve para desarrollar la curiosidad,')
                p('la ivestigacion y el pensamiento critico')

        elif ode == 3:
            p('*=*=*=*= Izada de bandera *=*=*=*=')
            es()
            p('1* Ver dias')
            p('2* Explicacion')
            es()
            odei = int(input('!¡ Porfavor dijita tu opcion ¡!'))
            es()

            if odei == 1:
                p('Esta actividad se desarrolla cada final de periodo,')
                p('es decir. abril 15, agosto 21, noviembre 21')

            elif odei == 2:
                p('Acto civico donde donde se rinden honores ala bandera,')
                p('y se reconocen estudiantes destacados')



        elif ode == 4:
            p('*=*=*=*= Dia de la independencia *=*=*=*=')
            es()
            p('1* Ver dias')
            p('2* Explicacion')
            es()
            odein = int(input('!¡ Porfavor dijita tu opcion ¡!'))
            es()

            if odein == 1:
                p('El dia de el desarrollo de el evento es')
                p('20 de agosto')

            elif odein == 2:
                p('Es una actividad donde el colegio conmemora')
                p('la historia de el pais, con actos civicos')
                p('memorias culturales')

        elif ode == 5:
            p('*=*=*=*= Reunion de acudientes *=*=*=*=')
            es()
            p('1* Ver dias')
            p('2* Explicacion')
            es()
            oder = int(input('!¡ Porfavor dijita tu opcion ¡!'))
            es()

            if oder == 1:
                p('El dia de el desarrollo es dos dias despues')
                p('de el final de periodo')
                p('es decir. abril 15, agosto 21, noviembre 21')

            elif oder == 2:
                p('Reuniones organizadas por el colegio')
                p('para orientar a los acudientes sobre la educacion,')
                p('convivencia y desarrollo de los estudiantes')


    elif od == 3:
        p('********* Directivos *********')
        p('******** institucionales ********')
        es()
        p('1* Rector')
        p('2* Cordinador')
        p('3* Psicologa')
        p('4* Secretario academico')
        es()

        odd = int(input('!¡ Porfavor dijita tu numero de opcion ¡!'))
        if odd == 1:
            p('RECTOR')
            es()
            p('1* Persona acargo')
            p('2* Funcion')
            es()
            oddr = int(input('!¡ Porfavor dijite numero de opcion¡!'))
            es()
            
            if oddr == 1:
                p('== Rector institucional ==')
                p('jhon jairo vernal')

            elif oddr == 2:
                p('** Funcion rector **')
                p('Es la maxima autoridad de el colegio se encarga')
                p('de dirigir la institucion, tomar deciciones y supervisar')
                p('el funcionamiento de el colegio')


        elif odd == 2:
            p('CORDINADOR')
            es()
            p('1* Persona acargo')
            p('2* Funcion')
            es()
            oddc = int(input('!¡ Porfavor dijite numero de opcion¡!'))
            es()

            if oddc == 1:
                p('==== Cordinador ====')
                p('elder sanchez')

            elif oddc == 2: 
                p('**** Funciones rector ****')
                p('se encarga de organizar las clases, horarios')
                p('materias, y actividades academicas')
                p('tambien supervisa el trabajo de docente')    

        elif odd == 3:
            p('PSICOLOGA')
            es()
            p('1* Persona acargo')
            p('2* Funcion')
            es()
            oddp = int(input('!¡ Porfavor dijite numero de opcion¡!'))
            es()

            if oddp == 1:
                p('====== Psicologa ======')
                p('tatiana mendes')

            elif oddp == 2:
                p('******* funciones psicologa ********')
                p('Se encarga principalmente de ayudar al bienestar emocional,')
                p('social y academico de los estudiantes')

        
        elif odd == 4:
            p('SECRETARIO ACADEMICO')
            es()
            p('1* Persona acargo')
            p('2* Funcion')
            es()
            odds = int(input('!¡ Porfavor dijite numero de opcion¡!'))
            es()

            if odds == 1:
                p('======== Secretario academico ========')
                p('carlos ruben espitia')

            elif odds == 2:
                p('********** funciones secretario academico **********') 
                p('Se encarga de las bases de datos,l registrar nuevos estudiantes')   

elif persona == co:
    code = int(input('¡!Hola cordinador por favor dijita tu clave!¡:'))
    while code != cod:
        code = int(input('?Acaso no eres el cordinador¿'))
    es()    

    p('!¡Bienvenido cordinador¡1')
    p('=============== Menu cordinador ===============')
    p('1* Compromisos')
    p('2* Reuniones')
    p('3* Docentes disponibles en plantel por area')
    p('=*=*^=*=*=^=*=*=^')
    opc = int(input('!¡ Porfavor dijita el numero de opcion ¡!'))
    es()

    if opc == 1:
        p('******* Compromisos *******')
        p('1* Velar por la disciplina')
        p('2* Apoyar a los docentes')
        p('3* Supervisar procesos')
        p('4* Atender a estudiantes y padres')
        p('5* Cordinar actividades institucionales')
        p('=*=*^=*=*=^=*=*=^')
        opcc = int(input('!¡ Porfavor dijita numero de opcion¡!'))
        es()

        if opcc == 1:
            p('=*=*=*= Velar por la disciplina =*=*=*=')
            p('Garantizar que los estudiantes cumplan con las normas')
            p('manual de convivencia de la institucion.')

        elif opcc == 2:
            p('=*=*=*= Apoyar al0os docentes =*=*=*=')
            p('Ayudar a los profesores en la organizacion de actividades academicas,')
            p('y resolver situaciones dentro del aula.')

        elif opcc == 3:
            p('=*=*=*= Supervisar procesos academicos =*=*=*=')
            p('Revisar que las clases, evaluaciones y actividades educativas')
            p('se desarrollen correctamente.')

        elif opcc == 4:
            p('=*=*=*= Atender a estudiantes y padres de familia =*=*=*=')
            p('Escuchar problemas, inquietudes o conflictos de estudiantes ')
            p('y acudientes para buscar soluciones')

        elif opcc == 5:
            p('=*=*=*= Coordinar actividades isntitucionales =*=*=*=')
            p('Organizar eventos academicos, reuniones, proyectos educativos')
            p('y actividades escolares')           

    elif opc == 2:
        p('******* Reuniones *******')
        p('1* Reuniones con docentes')
        p('2* Reunion con padres de familia')
        p('3* Reunion de convivencia escolar')
        p('4* Reunion de seguimiento academico')
        p('5* Reunion con directivos')
        p('=*=*^=*=*=^=*=*=^')
        
        opcr = int(input('!¡ Porfavor dijita tu numero de opcion'))
        es()

        if opcr == 1:
            p('=*=*=*= Reunion con docentes =*=*=*=')
            p('* Rendimientos academico de los estudiantes')
            p('* Planificar clases')
            p('* Actividades escolares')

        elif opcr == 2:
            p('=*=*=*= Reunion con padres de familia =*=*=*=')
            p('* Imformar sobre el comportamiento de los estudiantes')
            p('* Explicar el progreso academico')
            p('* Resolver inquietudes de los acudientes')

        elif opcr == 3:
            p('=*=*=*= Reunion de convivencia escolar =*=*=*=')
            p('* Tratar conflictos entre estudiantes')
            p('* Normas del colegio')
            p('* Mejora deel ambiente escolar')

        elif opcr == 4:
            p('=*=*=*= Reunion de seguimiento academico =*=*=*=')
            p('* Rendimiento de los estudiantes')
            p('* Dificultades en ciertas materias')
            p('* Estrategias para mejorar el aprendisaje')

        elif  opcr == 5:
            p('=*=*=*= Reunion con directivos =*=*=*=')
            p('El cordinador se reune con el rector y otros responsables')
            p('para planificar actividades y desiciones de el')
            p('colegio')                





    elif opc == 3:
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

        opcd = int(input('!¡ Porfavor dijite su opcion ¡!: '))
        es()

        if opcd == 1:
            p('= Ciencias naturales =')
            es()
            p('1* dora')
            p('2* jhon')
            p('3* angelica')

        elif opcd == 2:
            p('== Fisica ==')
            es()
            p('1* angela')
            p('2* alex')
            p('3* angel')

        elif opcd == 3:
            p('=== Sociales ===')
            es()
            p('1* magdalena')
            p('2* mario')
            p('2* capera')

        elif opcd == 4:
            p('==== Filosofia ====')
            es()
            p('1* capera')
            p('2* elsa')


        elif opcd == 5:
            p('===== Ingles =====')
            es()
            p('1* carlos')
            p('2* bonilla')

        elif opcd == 6:
            p('====== Edu fisica')
            es()
            p('sebastian')

        elif opcd == 7:
            p('======= Religion =======')
            es()
            p('luz') 

        elif opcd == 8:
            p('======= Etica ========')
            es()
            p('luz')

        elif opcd == 9:
            p('========= Castellano =========')
            es()
            p('1* magdalena')
            p('2* sofia') 

        elif opcd == 10:
            p('========== Tecnologia ==========')
            es()
            p('geovanny') 

        elif opcd == 11:
            p('=========== Economia y Politica ===========')
            es()
            p('capera')

        elif opcd == 12:
            p('=========== Matematicas ============')
            es()  
            p('1* ruben')
            p('2* angela')     
    
elif persona == acu:
    p('============== Menu acudientes  ============== ')
    


        
        
elif persona == e:
    nombre = str(input('?Cual es tu nombre¿: '))
    es()
    apellido = str(input('?Cual es tu apellido¿: '))
    es()
    años = int(input('?Cual es tu edad¿: '))
    es()
    grado = int(input('?Que grado cursa¿: '))
    es()
    datos = (nombre, apellido, años, grado)
    es()

    if grado == 6:
        p('****** Bienvenido al menu de el grado sexto ******')
        es()
        gr6 = int(input('Cual es tu grupo 1, 2 ,3'))
        es()

        if gr6 == 1:
            p('/ Bienvenido al menu de el grado 6:1 /')
            p('= Opciones grado 6:1')
            p('1* Seleccionar nombre')
            p('2* Simulacro tipo icfes incognito')

        elif gr6 == 2:
            p('/ Bienvenido al menu de el grado 6:2 /')
            p('= Opciones grado 6:2 =')

        elif gr6 == 3:
            p('/ Bienvenido al menu de el grado 6:3 /')
            p('1* Seleccionar nombre')
            p('2* Simulacro tipo icfes incognito')

    elif grado == 7:
        p('******* Bienvenido al menu de el grado septimo ********')
        es()
        gr7 = int(input('Cual es tu grupo 1, 2, 3,'))
        es()
        if gr7 == 1:
            p('// Bienvenido al grado 7:1 //')

        elif gr7 == 2:
            p('// Bienvenido al grado 7:2 //')

        elif gr7 == 3:
            p('// Bienvenido al grado 7:2 //')

    elif grado == 8:
        p('******** Bienvenido al grado octavo ********')
        es()
        gr8 = int(input('Cual es tu grupo 1, 2,'))
        es()

        if gr8 == 1:
            p('/// Bienvenido al grado 8:1 ///')

        elif gr8 == 2:
            p('/// Bienvenido al grado 8:2 ///')    

    elif grado == 9:
        p('********* Bienvenido al grado noveno *********')
        es()
        gr9 = int(input('Cual es tu grupo 1, 2'))
        es()

        if gr9 == 1:
            p('//// Bienvenido al grado 9:1 ////')

        elif gr9 == 2:
            p(' //// Bienvenido al grado 9:2 ////')

    elif grado == 10:
        p('********** Bienvenido al grado decimo **********')
        es()
        gr10 = int(input('Cual es tu grado 1, 2'))
        es()

        if gr10 == 1:
            p('///// Bienvenido al grado 10:1 /////')

        elif gr10 == 2:
            p('///// Bienvenido al grado 10.2 /////') 

    elif grado == 11:
        p('*********** Bienvenido al grado decimo ***********')
        es()
        gr11 = int(input('Cual es tu grado 1, 2'))
        es()

        if gr11 == 1:
            p('////// Bienvenido al grupo 11:1 //////')

        elif gr11 == 2:
            p('////// Bienvenido al grupo 11:2 //////')                       

