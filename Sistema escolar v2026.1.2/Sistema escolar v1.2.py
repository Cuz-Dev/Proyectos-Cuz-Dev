#🧮Sistema escolar dev-v2026.1.2
#🚀desarrollador Cuz-Dev🚀
#🌪️Si lo puedes imaginar lo puedes programar🌪️
def error_():
    print('[Errror critico] No se encuentran los demas archivos:')

while True:
    try:
        from menus import MenuDocente, MenuCoordinador, MenuRector, Acudiente, Menu_herramientas
        break

    except ModuleNotFoundError:
        error_()

while True:
    try:
        from menus import MenuInfo, Menu_Estudiante, secretario_virtual
        break

    except ModuleNotFoundError:
        error_()

while True:
    try:
        from estudiantes import estudiantes_sistema, menu_añadir_nota, notas_estudiante, mostrar_estudiantes
        break

    except ModuleNotFoundError:
        error_()

while True:
    try:
        from UI import menu_principal_
        break

    except ModuleNotFoundError:
        error_()

while True:
    try:
        from logins import login_menu_principal
        break

    except ModuleNotFoundError:
        error_()

while True:
    try:
        from error import fallas
        break

    except ModuleNotFoundError:
        error_()

while True:
    try:
        from configuracion import limpiar_pantalla, error_usuario
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

    def iniciar(self):
        self.pantalla.menu_principal()

class pantalla_principal:
    def __init__(self, sistema):
        self.sistema = sistema

    def menu_principal(self):
        limpiar_pantalla()
        login_menu_principal()
        while True:
            limpiar_pantalla()
            menu_principal_()
            persona = str(input('¡!Escribe el nombre de el menu al que quieres entrar!¡:')).lower().strip()

            if persona == 'docente':
                self.sistema.docente.menu_docente()

            elif persona == 'rector':
                self.sistema.RECTOR.Menu_rector()

            elif persona == 'coordinador':
                self.sistema.coordinador.menu_coordinador()

            elif persona == 'acudiente':
                self.sistema.acudiente.menu_acudiente()

            elif persona == 'estudiante':
                self.sistema.estudiante.menu_estudiante()            

            elif persona == 'herramientas':
                self.sistema.herramientas.menu_herramientas()

            elif persona == 'info':
                self.sistema.info.menu_info()

            elif persona == 'secretaria':
                self.sistema.secretario.menu_secretario()

            else:
                error_usuario()

empezar = Sistema_escolar()
empezar.iniciar()


def error_():
    print('[Errror critico] No se encuentran los demas archivos:')