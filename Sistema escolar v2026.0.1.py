#Sistema escolar v2026.0.1
#Creador Cuz-Dev

colegio = str(input('!¡Por favor escribe el nombre de este colegio para continuar: ')).lower()

def es():
    print('     ')


c = 'colegio python'

while c != colegio:
    es()
    colegio = str(input('!colegio incorrecto!')).lower()

print('========== hola este es al menu ==========')
print('********** sede bachiller ************')



es()
print('******** ¡bienvenido al sistema! ********')
es()


persona = str(input('?eres  cordinador , docente , estudiante , acudiente¿: ')).lower()

d = 'docente'
e = 'estudiante'
co = 'cordinador'
c = 202614
cod = 202601
acu = 'acudiente'
es()


if persona == d:
    cd = int(input('!hola profe¡, por favor escribe tu clave:'))
    while  cd != c:
        cd = int(input('!clave incorrecta¡, ?acaso no eres docente¿:'))

    print('!bienvenido profe¡')
    es()
    print('============== MENU DE OPCIONES DOCENTE ===============')
    print(' ========== opciones ==========')
    print('1* ver areas')
    print('2* eventos')
    print('3* directivos')
    print('=*=*^=*=*=^=*=*=^')
    
    od = int(input('!por favor dijite numero de opcion¡:'))

    if od == 1:
        print('*********** Areas ***********')
        es()
        print('/////////// temas de cada area /////////////')
        es()
        print('1* naturales')
        print('2* fisica')
        print('3* sociales')
        print('4* filosofia')
        print('5* ingles')
        print('6* edu Fisica')
        print('7* religion')
        print('8* etica')
        print('9* castellano')
        print('10* tecnologia')
        print('11* economia politica')
        print('12 *matematicas')
        es()
        print('^^^^^^ info ^^^^^')
        es()
        print('13* *=*=*=*= Ver docente de cada area *=*=*=*=')

        odp = int(input('!por favor dijite su opcion¡: '))

        if odp == 1:
            print('* Temas ciencias naturales *')
            print('*animales')
            print('*celulas')
            print('*medio ambiente')
            print('*quimica')
            print('*laboratorio')

        elif odp == 2:
            print('** Temas fisica materia **')
            es()
            print('*mru')
            print('*factores de conversion')
            print('*unidades de medida')

        elif odp ==3:
            print('**** Temas sociales ****')
            es()
            print('*imperialismo')
            print('*socialismo')
            print('*comunismo')
            print('*nacionalismo')

        elif odp == 4:
            print('***** Temas filosofia *****')
            es()
            print('*inicios de la filosofia')
            print('*principales pensadores de la edad media')

        elif odp == 5:
            print('******* Temas ingles ******')
            es()
            print('*verb to be')
            print('*lisenig')
            print('*read')

        elif odp == 6:
            print('******* Temas edu. fisica ******')
            es()
            print('*juegos tradicionales')
            print('*historia de el basquetball')
            print('*historia de el fottball')

        elif odp == 7:
            print('******** Temas religion ********')
            es()
            print('*sin sentidos')
            print('*sentidos')
            print('*yo pertenezco a jesus')

        elif odp == 8:
            print('*********Temas etica *********')
            es()
            print('*sentimientos')
            print('*perdon')
            print('*valores')

        elif odp == 9:
            print('********** castellano **********')
            es()
            print('*la vida feliz')
            print('*la metarmofosis')
            print('*noches blancas') 

        elif odp == 10:
            print('*********** Temas tecnologia ***********')
            es()
            print('*diagrama de flujo')
            print('*makecode')
            print('*python')

        elif odp == 11:
            print('************ Temas ciencias economicas y politicas ************')
            es()
            print('*pensadores')
            print('*origen')
            print('*importancia')

        elif odp == 12:
            print('************* Temas matematicas *************')
            es()
            print('*seno')
            print('*coseno')
            print('*tangente')

        elif odp == 13:
            print('=^=^=^=^=^ Docentes de area =^=^=^=^=^')
            es()
            print('1* naturales')
            print('2* fisica')
            print('3* sociales')
            print('4* filosofia')
            print('5* ingles')
            print('6* edu Fisica')
            print('7* religion')
            print('8* etica')
            print('9* castellano')
            print('10* tecnologia')
            print('11* economia politica')
            print('12 *matematicas')

            odpd = int(input('!por favor dijita el numero de opcion¡:'))

            if odpd == 1:
              print('= Ciencias naturales =')
              es()
              print('1* dora')
              print('2* jhon')
              print('3* angelica')

            elif odpd == 2:
              print('== Fisica ==')
              es()
              print('1* angela')
              print('2* alex')
              print('3* angel')

            elif odpd ==3:
              print('=== Sociales ===')
              es()
              print('1* magdalena')
              print('2* mario')
              print('2* capera')

            elif odpd == 4:
              print('==== Filosofia ====')
              es()
              print('1* capera')
              print('2* elsa')

            elif odpd == 5:
              print('===== Ingles =====')
              es()
              print('1* carlos')
              print('2* bonilla')

            elif odpd == 6:
              print('====== Edu fisica')
              es()
              print('sebastian')

            elif odpd == 7:
              print('======= Religion =======')
              es()
              print('luz')

            elif odpd == 8:
              print('======= Etica ========')
              es()
              print('luz')

            elif odpd == 9:
              print('========= Castellano =========')
              es()
              print('1* magdalena')
              print('2* sofia') 

            elif odpd == 10:
              print('========== Tecnologia ==========')
              es()
              print('geovanny')

            elif odpd == 11:
              print('=========== Economia y Politica ===========')
              es()
              print('capera')

            elif odpd == 12:
              print('=========== Matematicas ============')
              es()  
              print('1* ruben')
              print('2* angela')
        

    elif od == 2:
        print('********** Eventos **********')
        print('****** Institucionales *****')
        es()
        print('1* dia cultura')
        print('2* feria de la ciencia')
        print('3* izada de bandera')
        print('4* dia de la independencia')
        print('5* reunion de padres de familia')
        es()
        ode = int(input('!¡ por favor dijita tu numero de opcion ¡!'))
        es()
        
        if ode == 1:
            print('*=*=*=*= Dia de la cultura *=*=*=*=')
            es()
            print('1* ver dia')
            print('2* explicacion')
            es()
            odec = int(input('!¡ por favor dijita tu opcion ¡!'))
            es()

            if odec == 1:
                print('* Dia a desarrollar *')
                es()
                print('El dia a desarrollar este evento es el 1 de abril')
 

            elif odec == 2:
                print('Evento donde los estudiantes presentan bailes, obras de teatro')
                print('musica y expociciones. objetivgo mostrar los talentos')
                print('artisticos')

        elif ode == 2:
            print('*=*=*=*= Feria de la ciencia *=*=*=*=')
            es()
            print('1* ver dia')
            print('2* explicacion')
            es()
            odef = int(input('!¡ por favor dijita tu opcion ¡!'))
            es()

            if odef == 1:
                print('el dia a dessarrollar este evento es el 20 de agosto')

            elif odef == 2:
                print('Actividad academica donde los estudiantes presentan')
                print('experimentos cientificos, sirve para desarrollar la curiosidad,')
                print('la ivestigacion y el pensamiento critico')

        elif ode == 3:
            print('*=*=*=*= Izada de bandera *=*=*=*=')
            es()
            print('1* ver dias')
            print('2* explicacion')
            es()
            odei = int(input('!¡ por favor dijita tu opcion ¡!'))
            es()

            if odei == 1:
                print('Esta actividad se desarrolla cada final de periodo,')
                print('es decir. abril 15, agosto 21, noviembre 21')

            elif odei == 2:
                print('Acto civico donde donde se rinden honores ala bandera,')
                print('y se reconocen estudiantes destacados')



        elif ode == 4:
            print('*=*=*=*= Dia de la independencia *=*=*=*=')
            es()
            print('1* ver dias')
            print('2* explicacion')
            es()
            odein = int(input('!¡ por favor dijita tu opcion ¡!'))
            es()

            if odein == 1:
                print('El dia de el desarrollo de el evento es')
                print('20 de agosto')

            elif odein == 2:
                print('Es uba actividad donde el colegio conmemora')
                print('la historia de el pais, con actos civicos')
                print('memorias culturales')

        elif ode == 5:
            print('*=*=*=*= Reunion de acudientes *=*=*=*=')
            es()
            print('1* ver dias')
            print('2* explicacion')
            es()
            oder = int(input('!¡ por favor dijita tu opcion ¡!'))
            es()

            if oder == 1:
                print('El dia de el desarrollo es dos dias despues')
                print('de el final de periodo')
                print('es decir. abril 15, agosto 21, noviembre 21')

            elif oder == 2:
                print('Reuniones organizadas por el colegio')
                print('para orientar a los acudientes sobre la educacion,')
                print('convivencia y desarrollo de los estudiantes')


    elif od == 3:
        print('********* Directivos *********')
        print('******** institucionales ********')
        es()
        print('1* Rector')
        print('2* Cordinador')
        print('3* psicologa')
        print('4* secretario academico')
        es()

        odd = int(input('!¡ por favor dijita tu numero de opcion ¡!'))
        if odd == 1:
            print('RECTOR')
            es()
            print('1* persona acargo')
            print('2* Funcion')
            es()
            oddr = int(input('!¡ por favor dijite numero de opcion¡!'))
            es()
            
            if oddr == 1:
                print('== Rector institucional ==')
                print('jhon jairo vernal')

            elif oddr == 2:
                print('** Funcion rector **')
                print('Es la maxima autoridad de el colegio se encarga')
                print('de dirigir la institucion, tomar deciciones y supervisar')
                print('el funcionamiento de el colegio')

        elif odd == 2:
            print('CORDINADOR')
            es()
            print('1* persona acargo')
            print('2* Funcion')
            es()
            oddc = int(input('!¡ por favor dijite numero de opcion¡!'))
            es()

            if oddc == 1:
                print('==== Cordinador ====')
                print('elder sanchez')

            elif oddc == 2: 
                print('**** funciones rector ****')
                print('se encarga de organizar las clases, horarios')
                print('materias, y actividades academicas')
                print('tambien supervisa el trabajo de docente')    

elif persona == co:
    code = int(input('¡hola cordinador por favor dijita tu clave!:'))
    while code != cod:
        code = int(input('?acaso no eres el cordinador¿'))

    print('!bienvenido cordinador¡')
    print('=============== menu cordinador ===============')
    print('1* compromisos')
    print('2* reuniones')
    print('3* docentes disponibles en plantel')
    print('=*=*^=*=*=^=*=*=^')
    opc = int(input('!por favor dijita el numero de opcion'))

    if opc == 1:
        print('******* Compromisos *******')

    elif opc == 2:
        print('******* reuniones *******')

    elif opc == 3:
        print('******* docentes disponibles en plantel *******')

    else:
        print('!¡por favor selecciona una opcion valida!¡')     
    
elif persona == acu:
    acue = str(input('!Hola acudiente cual es el nombre de tu acudido¿?'))
    print('tu acudido es' + acue)

        
        
else:
    nombre = str(input('?cual es tu nombre¿: '))
    apellido = str(input('?cual es tu apellido¿: '))
    años = int(input('?cual es tu edad¿: '))
    grado = int(input('?que grado cursa¿: '))
    datos = [nombre, apellido, años, grado,]

    if grado == 6:
        print('****** Bienvenido al menu de el grado sexto ******')
        print('     ')
        gr6 = str(input('cual es tu grupo 1, 2 ,3'))
        print('     ')

        if gr6 == 1:
            print('/ Bienvenido al menu de el grado 6:1 /')

        elif gr6 == 2:
            print('/ Bienvenido al menu de el grado 6:2 /')

        else:
            print('/ Bienvenido al menu de el grado 6:3 /')

    elif grado == 7:
        print('******* Bienvenido al menu de el grado septimo ********')
        print('      ')
        gr7 = str(input('cual es tu grupo 1, 2, 3,'))
        print('    ')
        if gr7 == 1:
            print('// Bienvenido al grado 7:1 //')

        elif gr7 == 2:
            print('// Bienvenido al grado 7:2 //')

        else:
            print('// Bienvenido al grado 7:2 //')

    elif grado == 8:
        print('******** Bienvenido al grado octavo ********')
        print('    ')
        gr8 = str(input('cual es tu grupo 1, 2,'))
        print('    ')

        if gr8 == 1:
            print('/// Bienvenido al grado 8:1 ///')

        elif gr8 == 2:
            print('/// Bienvenido al grado 8:2 ///') 


    elif grado == 9:
        print('********* Bienvenido al grado noveno *********')
        print('    ')
        gr9 = str(input('cual es tu grupo 1, 2'))
        print('     ')

        if gr9 == 1:
            print('//// Bienvenido al grado 9:1 ////')

        elif gr9 == 2:
            print(' //// Bienvenido al grado 9:2 ////')

    elif grado == 10:
        print('********** Bienvenido al grado decimo **********')
        print('    ')
        gr10 == str(input('cual es tu grado 1, 2'))
        print('     ')

        if gr10 == 1:
            print('///// Bienvenido al grado 10:1 /////')

        elif gr10 == 2:
            print('///// Bienvenido al grado 10.2 /////') 

    elif grado == 11:
        print('*********** Bienvenido al grado decimo ***********')
        print('    ')
        gr11 = str(input('cual es tu grado 1, 2'))
        print('     ')

        if gr11 == 1:
            print('////// Bienvenido al grupo 11:1 //////')

        elif gr11 == 2:
            print('////// Bienvenido al grupo 11:2 //////')                       






