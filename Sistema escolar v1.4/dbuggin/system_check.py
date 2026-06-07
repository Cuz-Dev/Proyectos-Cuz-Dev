import os
while True:
    try:
        from menus import MenuDocente, MenuCoordinador,MenuRector, Menu_Estudiante,Menu_herramientas
        from menus import MenuInfo, secretario_virtual,Acudiente,sub_menu_cambiar_contraseña
        from logins import login_docente, login_coordinador, login_rector
        from menus import SubmenuAreas, SubmenuDirectivos, SubmenuEventos, compromisos_,reuniones_,Docente_por_area
        from estudiantes import estudiante_ver,MenuGuardado, menu_añadir_nota
        from estudiantes import submenu_anotaciones, submenu_quitar
        break

    except ModuleNotFoundError:
        print('No se encuentra el archivo')

def pedir_comando():
    return str(input('debug_> ')).lower().strip()

def limpiar():
    if os.name == 'nt':
        os.system("cls")

    else:
        os.system("clear")

def comando_ivalido():
    print('comando ivalido')

class system_check:
    def __init__(self):
        self.docente = MenuDocente()
        self.coordinador = MenuCoordinador()
        self.rector = MenuRector()
        self.estudiante = Menu_Estudiante()
        self.herramientas = Menu_herramientas()
        self.info = MenuInfo()
        self.secretaria = secretario_virtual()
        self.log_docente = login_docente
        self.log_coordinador = login_coordinador
        self.log_rector = login_rector
        self.areas = SubmenuAreas()
        self.directivos = SubmenuDirectivos()
        self.eventos = SubmenuEventos()
        self.ver_es = estudiante_ver()
        self.guar_es = MenuGuardado()
        self.add_nota = menu_añadir_nota()
        self.anotaciones = submenu_anotaciones()
        self.quitar = submenu_quitar()
        self.acudiente = Acudiente()
        self.cambiar = sub_menu_cambiar_contraseña()
        self.compromisos = compromisos_()
        self.reuniones = reuniones_()
        self.docente_area = Docente_por_area()

    def menu_system(self):
        while True:
            limpiar()
            comando = pedir_comando()
            comandos = {
                'd/':self.docente.menu_docente,
                'c/':self.coordinador.menu_coordinador,
                'r/':self.rector.Menu_rector,
                'a/':self.acudiente.menu_acudiente,
                'e/':self.estudiante.menu_estudiante,
                'h/':self.herramientas.menu_herramientas,
                's/':self.secretaria.menu_secretario,
                'i/':self.info.menu_info,
                'd()': self.log_docente,
                'c()':self.log_coordinador,
                'r()':self.log_rector,
                '//e':self.ver_es.opcion_usuario,
                '//g':self.guar_es.menu_guardado,
                '//n':self.add_nota.Menu_añadir,
                '//an':self.anotaciones.Sub_Menu_Anotacion,
                '//r':self.quitar.Submenu_Quitar,
                '//d':self.directivos.submenu_directivos,
                '//ev':self.eventos.submenu_eventos,
                '//a':self.areas.submenu_areas,
                '//ca':self.cambiar.Sub_Menu_cambio,
                '//c':self.compromisos.compromisos,
                '//re':self.reuniones.reuniones,
                '//do':self.docente_area.submenu_docentes_area
            }
            if comando in comandos:
                limpiar()
                comandos[comando]()

            elif comando == 'pwf':
                limpiar()
                break

            else:
                comando_ivalido()






        