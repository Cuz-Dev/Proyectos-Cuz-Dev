#Menus y submenus de sistema
def error_():
    print('[Errror critico] No se encuentran los demas archivos:')

while True:
    try:
        from configuracion import entrada_us, es, salir, error, limpiar_pantalla
        from configuracion import volver, entrada, salir_menu_info, mostrar_info
        from UI import menu_docente, menu_coordinador_, menu_acudiente_, menu_rector_, menu_secretario_, menu_es
        from UI import menu_herramientas_
        from UI import submenu_areas_, submenu_docentes_area_, submenu_reuniones, submenu_eventos_
        from UI import submenu_calculadora_, submenu_generador, submenu_juegos_
        from UI import eventos_lista, submenu_directivos_, directivos_lista
        from UI import submenu_eventos_1, submenu_eventos_2, submenu_eventos_3, submenu_eventos_4
        from UI import submenu_eventos_5
        from UI import submenu_directivos_1, submenu_directivos_2, submenu_directivos_3, submenu_directivos_4
        from UI import submenu_compromisos_, submenu_juegos_1, submenu_juegos_2, submenu_juegos_
        from UI import submenu_compromisos_, submenu_juegos_1, submenu_juegos_2, submenu_juegos_
        from logins import login_coordinador, login_docente, login_rector
        from utilidades import temas_area_lista, docentes_area
        from utilidades import compromisos_1, compromisos_2, compromisos_3, compromisos_4, compromisos_5
        from utilidades import reuniones_1, reuniones_2, reuniones_3, reuniones_4, reuniones_5
        from estudiantes import mostrar_estudiantes, estudiantes_sistema, menu_añadir_nota, notas_estudiante
        from estudiantes import SubMenu_estudiantes_directivos,Sub_menu_añadir_acudiente
        from herramientas import calculadora,menu_contraseñas, Number_hunter, Piedra_papel_tijera
        from estudiantes import submenu_anotaciones, submenu_anotaciones_2
        from auth.Auth import sub_menu_cambiar_contraseña
        from error import fallas
        break

    except ModuleNotFoundError:
        error_()

class MenuDocente:
    def __init__(self,):
        self.areas = SubmenuAreas()
        self.eventos = SubmenuEventos()
        self.directivos = SubmenuDirectivos()
        self.cambio = sub_menu_cambiar_contraseña()
        self.estudiantes = SubMenu_estudiantes_directivos()
        self.acudiente = Sub_menu_añadir_acudiente()

    def menu_docente(self):
        limpiar_pantalla()
        login_docente()
        while True:
            limpiar_pantalla()
            menu_docente()
            opcion_docente = entrada()
            opciones_docente = {

                1: self.areas.submenu_areas,
                2: self.eventos.submenu_eventos,
                3: self.directivos.submenu_directivos,
                4: self.estudiantes.Submenu_estudiantes,
                5: self.cambio.Sub_Menu_cambio,
                6:self.acudiente.SubMenu_añadir_acudiente,
                
            }

            if opcion_docente in opciones_docente:
                opciones_docente[opcion_docente]()

            else:
                salir()
                limpiar_pantalla()
                break
    
class SubmenuAreas:
    def submenu_areas(self):
        limpiar_pantalla()
        while True:      
            submenu_areas_()
            opcion_areas = entrada()
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
        while True:
            limpiar_pantalla()
            submenu_docentes_area_()      
            docente_area = entrada()
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
                limpiar_pantalla()
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
        while True:
            limpiar_pantalla()
            submenu_eventos_()
            eventos = entrada()
            opciones_area = {
                1: self.eventos_1.submenu_eventos1,
                2: self.eventos_2.submenu_eventos2,
                3: self.eventos_3.submenu_eventos3,
                4: self.eventos_4.submenu_eventos4,
                5: self.eventos_5.submenu_eventos5
            }
            if eventos in opciones_area:
                limpiar_pantalla()
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
            cultura = entrada()
            opciones_cultura = {
                1: eventos_lista[0],
                2: eventos_lista[1]
            }
                
            if cultura in opciones_cultura:
                limpiar_pantalla()
                opciones_cultura[cultura]()

            elif cultura == 3:
                volver()
                limpiar_pantalla()
                break    
class Eventos2:
    def submenu_eventos2(self):
        while True:
            limpiar_pantalla()
            submenu_eventos_2()
            feria = entrada()        
            opciones_feria = {
                1: eventos_lista[2],
                2: eventos_lista[3]
            }

            if feria in opciones_feria:
                limpiar_pantalla()
                opciones_feria[feria]()

            elif feria == 3:
                volver()
                limpiar_pantalla()
                break    

class Eventos3:
    def submenu_eventos3():
        while True:
            limpiar_pantalla()
            submenu_eventos_3()
            izada = entrada()
            opciones_izada = {
                1: eventos_lista[4],
                2: eventos_lista[5]
            }

            if izada in opciones_izada:
                limpiar_pantalla()
                opciones_izada[izada]()

            elif izada == 3:
                volver()
                limpiar_pantalla()
                break 

class Eventos4:
    def submenu_eventos4(self):
        while True:
            limpiar_pantalla()
            submenu_eventos_4()
            independencia = entrada()
            opciones_independencia = {
                1: eventos_lista[6],
                2: eventos_lista[7]
            }

            if independencia in opciones_independencia:
                limpiar_pantalla()
                opciones_independencia[independencia]()

            elif independencia == 3:
                volver()
                limpiar_pantalla()
                break

class Eventos5:
    def submenu_eventos5(self):
        while True:
            limpiar_pantalla()
            submenu_eventos_5()
            reunion_acu = entrada()
            opciones_reuniones = {
                1: eventos_lista[8],
                2: eventos_lista[9]
            }

            if reunion_acu in opciones_reuniones:
                limpiar_pantalla()
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
        while True:
            limpiar_pantalla()
            submenu_directivos_()
            directivos = entrada()
            opciones_directivos = {
                1: self.directivo_1.submenu_directivos1,
                2: self.directivo_2.submenu_directivos2,
                3: self.directivo_3.submenu_directivos3,
                4: self.dorectivo_4.submenu_directivos4
            }

            if directivos in opciones_directivos:
                limpiar_pantalla()
                opciones_directivos[directivos]()

            elif directivos == 5:
                volver()
                limpiar_pantalla()
                break

class directivo1:   
    def submenu_directivos1(self):
        while True:          
            limpiar_pantalla()
            submenu_directivos_1()
            Rector = entrada()
            opciones_rector = {
                1: directivos_lista[0],
                2: directivos_lista[1]
            }

            if Rector in opciones_rector:
                limpiar_pantalla()
                opciones_rector[Rector]()

            elif Rector == 3:
                volver()
                limpiar_pantalla()
                break

class directivo2:
    def submenu_directivos2(self):
        while True:
            limpiar_pantalla()
            submenu_directivos_2()
            Coordinador = entrada()
            opciones_coordinador = {
                1: directivos_lista[2],
                2: directivos_lista[3]
            }

            if Coordinador in opciones_coordinador:
                limpiar_pantalla()
                opciones_coordinador[Coordinador]()

            elif Coordinador == 3:
                volver()
                limpiar_pantalla()
                break       

class directivo3:
    def submenu_directivos3(self):
        while True:
            limpiar_pantalla()
            submenu_directivos_3()
            psicologa = entrada()
            opciones_psicologa = {
                1: directivos_lista[4],
                2: directivos_lista[5]
            }

            if psicologa in opciones_psicologa:
                limpiar_pantalla()
                opciones_psicologa[psicologa]()

            elif psicologa == 3:
                volver()
                limpiar_pantalla()
                break       

class directivo4:
    def submenu_directivos4(self):
        while True:
            limpiar_pantalla()
            submenu_directivos_4()
            secretario = entrada()
            opciones_secretario = {
                1: directivos_lista[6],
                2: directivos_lista[7]
            }

            if secretario in opciones_secretario:
                limpiar_pantalla()
                opciones_secretario[secretario]()

            elif secretario == 3:
                volver()
                break

class MenuCoordinador:
    def __init__(self):
        self.docentes_disponibles = Docente_por_area()
        self.Sub_menu_compromisos = compromisos_()
        self.Sub_menu_reuniones = reuniones_()
        self.cambio = sub_menu_cambiar_contraseña()
        self.estudiantes = SubMenu_estudiantes_directivos()
        self.acudiente = Sub_menu_añadir_acudiente()

    def menu_coordinador(self):
        limpiar_pantalla()
        login_coordinador()
        while True:
            limpiar_pantalla()
            menu_coordinador_()
            opcion_coordinador = entrada()
            opciones_coordinador = {
                1: self.Sub_menu_compromisos.compromisos,
                2: self.Sub_menu_reuniones.reuniones,
                3: self.docentes_disponibles.submenu_docentes_area,
                4: self.estudiantes.Submenu_estudiantes,
                5:self.cambio.Sub_Menu_cambio,
                6:self.acudiente.SubMenu_añadir_acudiente
            }

            if opcion_coordinador in opciones_coordinador:
                limpiar_pantalla()
                opciones_coordinador[opcion_coordinador]()

            else:
                salir()
                limpiar_pantalla()
                break

class compromisos_:
    def compromisos(self):
        while True:
            limpiar_pantalla()
            submenu_compromisos_()
            Compromiso_s = entrada()
            compromisos_opcion = {
                1: compromisos_1,
                2: compromisos_2,
                3: compromisos_3,
                4: compromisos_4,
                5: compromisos_5
            }        
            
            if Compromiso_s in compromisos_opcion:
                limpiar_pantalla()
                compromisos_opcion[Compromiso_s]()

            elif Compromiso_s == 6:
                volver()
                limpiar_pantalla()
                break

class reuniones_:
    def reuniones(self):
        while True:
            limpiar_pantalla()
            submenu_reuniones()
            Reuniones = entrada()
            reuniones_opcion = {

                1: reuniones_1,
                2: reuniones_2,
                3: reuniones_3,
                4: reuniones_4,
                5: reuniones_5

            }

            if Reuniones in reuniones_opcion:
                limpiar_pantalla()
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
        self.mostrar = submenu_anotaciones_2()

    def menu_acudiente(self):
        limpiar_pantalla()        
        while True:
            menu_acudiente_()
            opcion_acudiente = entrada()
            opciones_acudiente = {
                1: self.ver.ver_estudiante_2,
                2: self.docentes.submenu_docentes_area,
                3: self.directivos.submenu_directivos,
                4: self.eventos.submenu_eventos,
                5: self.mostrar.Sub_Menu_Anotacion_2
            }

            if opcion_acudiente in opciones_acudiente:
                opciones_acudiente[opcion_acudiente]()

            elif opcion_acudiente == 6:
                salir()
                limpiar_pantalla()
                break

class Menu_Estudiante:
    def __init__(self):
        self.areas_temas = SubmenuAreas()
        self.directivos = SubmenuDirectivos()
        self.estudiantes_grado = mostrar_estudiantes()
        self.ver = mostrar_estudiantes()
        self.mostrar = submenu_anotaciones_2()

    def menu_estudiante(self):
        limpiar_pantalla()
        while True:
            menu_es()
            opcion_estudiante = entrada()
            estudiante_opcion = {

                1: self.areas_temas.submenu_areas,
                2: self.directivos.submenu_directivos,
                3: self.ver.ver_estudiante_2,
                4: self.mostrar.Sub_Menu_Anotacion_2
            }

            if opcion_estudiante in estudiante_opcion:
                estudiante_opcion[opcion_estudiante]()
                
            elif opcion_estudiante == 5:
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
            opcion_herramientas = entrada()
            if opcion_herramientas == 1:
                while True:
                    submenu_calculadora_()
                    opcion_calculadora = entrada()
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
                    herramientas_generador = entrada()                
                    if herramientas_generador == 1:
                        while True:
                            try:
                                menu_contraseñas()
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
                    opcion_juegos = entrada()
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
                            opcion_piedra_papel = entrada()
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
        mostrar_info()
        salir_menu_info()

class MenuRector:
    def __init__(self):
        self.areas_Temas = SubmenuAreas()
        self.docentes_Area = Docente_por_area()
        self.eventos_I = SubmenuEventos()
        self.directivos_I = SubmenuDirectivos()
        self.guardar = estudiantes_sistema()
        self.ver = mostrar_estudiantes()
        self.notas_estudiante = notas_estudiante()
        self.mostrar = submenu_anotaciones()
        self.cambio = sub_menu_cambiar_contraseña()
        self.estudiantes = SubMenu_estudiantes_directivos()
        self.acudiente = Sub_menu_añadir_acudiente()

    def Menu_rector(self):
        limpiar_pantalla()
        login_rector()
        while True:
            limpiar_pantalla()
            menu_rector_()
            opcion_rector = entrada()
            rector = {
                1: self.areas_Temas.submenu_areas,
                2: self.docentes_Area.submenu_docentes_area,
                3: self.eventos_I.submenu_eventos,
                4: self.directivos_I.submenu_directivos,
                5: self.estudiantes.Submenu_estudiantes,
                6: self.cambio.Sub_Menu_cambio,
                7:self.acudiente.SubMenu_añadir_acudiente
            }

            if opcion_rector in rector:
                limpiar_pantalla()
                rector[opcion_rector]()
                
            else:
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
            opcion_secretaria = entrada()
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

