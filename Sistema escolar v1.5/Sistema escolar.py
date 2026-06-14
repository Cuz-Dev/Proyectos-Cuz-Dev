#Sistema escolar v2026.1.4
#"Si lo puedes imaginar, lo puedes programar"
#Desarrollador Cuz-dev

def error_():
    print('[Error critico] No se encuentran los demas archivos:')

while True:
    try:
        from menus import MenuDocente, MenuCoordinador, MenuRector, Acudiente, Menu_herramientas
        from menus import MenuInfo, Menu_Estudiante, secretario_virtual
        from estudiantes import estudiantes_sistema, menu_añadir_nota, notas_estudiante, mostrar_estudiantes
        from configuracion import limpiar_pantalla, error_usuario, inicio_
        from dbuggin.system_check import system_check
        from error import fallas
        from UI import menu_principal_
        break

    except ModuleNotFoundError:
        error_()

class Sistema_escolar:
    def __init__(self):
        self.pantalla = pantalla_principal(self)
        self.docente = MenuDocente()
        self.coordinador = MenuCoordinador()
        self.acudiente = Acudiente()
        self.herramientas = Menu_herramientas()
        self.menu_fallos_es = fallas()
        self.info = MenuInfo()
        self.RECTOR = MenuRector()
        self.estudiante = Menu_Estudiante()
        self.guardado = estudiantes_sistema()
        self.ver = mostrar_estudiantes()  
        self.secretario = secretario_virtual()
        self.añadir_nota = menu_añadir_nota()
        self.ver_nota = notas_estudiante()
        self.comando = system_check()

    def iniciar(self):
        self.pantalla.menu_principal()

class pantalla_principal:
    def __init__(self, sistema):
        self.sistema = sistema

    def menu_principal(self):
        limpiar_pantalla()
        while True:
            limpiar_pantalla()
            menu_principal_()
            persona = inicio_()
            opciones_inicio = {
                'docente':self.sistema.docente.menu_docente,
                'rector':self.sistema.RECTOR.Menu_rector,
                'coordinador':self.sistema.coordinador.menu_coordinador,
                'acudiente':self.sistema.acudiente.menu_acudiente,
                'estudiante':self.sistema.estudiante.menu_estudiante,
                'herramientas':self.sistema.herramientas.menu_herramientas,
                'info':self.sistema.info.menu_info,
                'secretaria':self.sistema.secretario.menu_secretario,
                'pw':self.sistema.comando.menu_system
            }

            if persona in opciones_inicio:
                opciones_inicio[persona]()

            else:
                error_usuario()

empezar = Sistema_escolar()
empezar.iniciar()


def error_():
    print('[Errror critico] No se encuentran los demas archivos:')