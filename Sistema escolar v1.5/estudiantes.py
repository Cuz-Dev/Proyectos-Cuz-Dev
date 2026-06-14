#Estudiantes de SISTEMA
import json
import os
def error_():
    print('[Errror critico] No se encuentran los demas archivos:')

while True:
    try:
        from configuracion import limpiar_pantalla, s_n, borrado_exitoso,pause, pedir_nombre_acudiente
        from configuracion import error_nota_estudiante, error_anotacion_estudiante
        from configuracion import grado_invalido,curso_invalido, pedir_numero_boletin
        from configuracion import pedir_nombre_guardar, pedir_apellido_guardar
        from configuracion import pedir_grado_guardar, pedir_curso_guardar,numero_invalido
        from configuracion import cursos_validos, grados_validos,pedir_periodo
        from UI import submenu_añadir_es, submenu_notas, submenu_anotacion, submenu_anotacion_2
        from UI import submenu_añadir_acudiente
        from UI import submenu_quitar_estudiante, estudiantes_sistema_menu, submenu_añadir_boletin
        from configuracion import limpiar_pantalla, error, es, p, entrada_us, grado_ejemplo, curso_ejemplo
        from configuracion import anotacion_,error_clave,error_boletin_estudiante
        from configuracion import entrada
        from configuracion import volver, salir, linea_menu, linea_menu2, curso_inesistente, grado_inesistente, grado_es, curso_es
        from utilidades import pedir_apellido
        break

    except ModuleNotFoundError:
        error_()

class estudiantes_sistema:
    def __init__(self):
        self.guardar = guardar_estudiante()
        self.menu = MenuGuardado()
        
    
class SubMenu_estudiantes_directivos:
    def __init__(self):
        self.menu = MenuGuardado()
        self.ver = mostrar_estudiantes()
        self.guardado = estudiantes_sistema()
        self.añadir_notas = menu_añadir_nota()
        self.anotaciones = submenu_anotaciones()
        self.guardad = guardar_estudiante()
        self.boletin = sub_menu_añadir_boletin()

    def Submenu_estudiantes(self):
        while True:
            limpiar_pantalla()
            estudiantes_sistema_menu()
            opcion = entrada_us()
            opciones = {
                1:self.ver.ver_estudiante,
                2:self.guardado.menu.menu_guardado,
                3:self.añadir_notas.Menu_añadir,
                4:self.anotaciones.Sub_Menu_Anotacion,
                5:self.boletin.SubMenu_añadir_boletin
            }
            if opcion in opciones:
                limpiar_pantalla()
                opciones[opcion]()

            else:
                limpiar_pantalla()
                break
        

class MenuGuardado:
    def __init__(self):
        self.guardad = guardar_estudiante()
    def menu_guardado(self):
        while True:
            limpiar_pantalla()
            submenu_añadir_es()
            while True:
                try:
                    guardado = entrada_us()
                    break

                except ValueError:
                    error()

            if guardado == 1:
                limpiar_pantalla()
                self.guardad.datos_es()
                self.guardad.guardado()

            else:
                limpiar_pantalla()
                break

class guardar_estudiante:
    def __init__(self):
        self.estudiante = {}
        self.mostrar = estudiante_ver()

    def datos_es(self):
        limpiar_pantalla()
        self.nombre = pedir_nombre_guardar()
        es()
        self.apellido = pedir_apellido_guardar()
        es()
        grado_ejemplo()
        es()
        self.grado = pedir_grado_guardar()
        es()
        grados = grados_validos()
        cursos = cursos_validos()
        while True:
            if self.grado.isdigit():
                break
            else:
                limpiar_pantalla()
                numero_invalido()
                self.grado = pedir_grado_guardar()
        while True:
            if self.grado in grados:
                break
            else:
                limpiar_pantalla()
                grado_invalido()
                self.grado = pedir_grado_guardar()
        while True:
            curso_ejemplo()
            es()
            self.curso = pedir_curso_guardar()
            es()
            if self.curso.isdigit():
                break
            else:
                limpiar_pantalla()
                numero_invalido()
                self.curso = pedir_curso_guardar()
        while True:
            if self.curso in cursos:
                break
            else:
                limpiar_pantalla()
                curso_invalido()
                self.curso = pedir_curso_guardar()  

    def guardado(self):
        print(self.grado)
        print(self.curso)
        nuevo = {

            self.apellido: {
                'Nombre': self.nombre,
                'notas': {},
                'anotaciones': [],
                'acudiente': {},
                'boletines': []

            }

        }

        with open("estudiantes.json", "r") as f:
            self.estudiantes = json.load(f)

        self.estudiantes.setdefault(self.grado, {})
        self.estudiantes[self.grado].setdefault(self.curso, {})
        self.estudiantes[self.grado][self.curso].update(nuevo)

        with open("estudiantes.json", "w") as f:
            json.dump(self.estudiantes, f, indent=4)


    def notas_es(self):
        es()
        materias = [

            "Matematicas",
            "Edu fisica",
            "Catellano",
            "Ingles",
            "Biologia",
            "Filosofia",
            "Tecnologia",
            "Fisica",
            "Sociales",
            "Quimica",
            "Artistica",
        ]

        for i, materia in enumerate(materias):
            print(f"{i + 1}. {materia}")

        while True:
            try:
                seleccion_usuario = entrada_us()
                es()
                break

            except ValueError:
                error()
        limpiar_pantalla()
        self.mostrar.opcion_usuario()
        seleccion_es = pedir_apellido()
        with open("estudiantes.json", "r") as archivo:
            datos = json.load(archivo)

        while True:        
            nota = float(input("Ingrese nota: "))
            es()

            if nota > 0 and nota <= 5:
                materia = materias[seleccion_usuario - 1]
                while True:
                    try:
                        estudiante_nota = datos[self.mostrar.grado][self.mostrar.curso][seleccion_es]
                        break
                    except KeyError:
                        error_clave()
                        break
                while True:
                    try:
                        if "notas" not in estudiante_nota:
                            estudiante_nota["notas"] = {}
                        if materia not in estudiante_nota["notas"]:
                            estudiante_nota["notas"][materia] = []
                        estudiante_nota["notas"][materia].append(nota)
                        break

                    except UnboundLocalError:
                        error_nota_estudiante()
                        pause()
                        break

                with open("estudiantes.json", "w") as archivo_json:
                    json.dump(datos, archivo_json, indent=4)
                break

            else:
                print('nota invalida')

class menu_añadir_nota:
    def __init__(self):
        self.añadir = guardar_estudiante()
        self.ver_notas = notas_estudiante()

    def Menu_añadir(self):
        while True:
            limpiar_pantalla()
            submenu_notas()
            while True:
                try:
                    opcion_submenu = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            opciones = {

                1: self.añadir.notas_es,
                2: self.ver_notas.ver_notas
            }

            if opcion_submenu in opciones:
                limpiar_pantalla()
                opciones[opcion_submenu]()

            elif opcion_submenu == 3:
                volver()
                limpiar_pantalla()
                break


class mostrar_estudiantes:
    def __init__(self):
        self.estudiante = estudiante_ver()
        self.quitar = quitar_estudiante()

    def ver_estudiante(self):
        while True:
            limpiar_pantalla()
            linea_menu2()
            p('Estudiantes')
            linea_menu2()
            es()
            p('[1] Ver estudiante')
            p('[2] Borrar estudiante')
            p('[3] <<<< Volver')
            es()
            while True:
                try:
                    opcion_mostrar_estudiante = entrada_us()
                    es()
                    break

                except ValueError:
                    error()

            opciones = {
                1: self.estudiante.opcion_usuario,
                2: self.quitar.Quitar_estudiante
            }

            if opcion_mostrar_estudiante in opciones:
                limpiar_pantalla()
                opciones[opcion_mostrar_estudiante]()

            elif opcion_mostrar_estudiante == 3:
                volver()
                limpiar_pantalla()
                break

    def ver_estudiante_2(self):
        while True:
            limpiar_pantalla()
            linea_menu2()
            p('Estudiantes')
            linea_menu2()
            es()
            p('[1] Ver estudiante')
            p('[2] <<<< Volver')
            es()
            while True:
                try:
                    opcion_mostrar_2 = entrada_us()
                    es()
                    break

                except ValueError:
                    error()
            opciones = {
                1: self.estudiante.opcion_usuario
            }
            if opcion_mostrar_2 in opciones:
                limpiar_pantalla()
                opciones[opcion_mostrar_2]()

            else:
                volver()
                limpiar_pantalla()
                break

class estudiante_ver:
    def opcion_usuario(self):
        while True:
            grados = grados_validos()
            cursos = cursos_validos()
            while True:
                self.grado = grado_es()
                if self.grado.isdigit():
                    break
                else:
                    limpiar_pantalla()
                    numero_invalido()
                    self.grado = grado_es()
            while True:
                if self.grado in grados:
                    break
                else:
                    limpiar_pantalla()
                    grado_invalido()
                    self.grado = grado_es()
            while True:
                self.curso = curso_es()
                if self.curso.isdigit():
                    break
                else:
                    limpiar_pantalla()
                    numero_invalido()
                    self.curso = curso_es()
            while True:
                if self.curso in cursos:
                    break
                else:
                    limpiar_pantalla()
                    curso_invalido()
                    self.curso = curso_es()

            limpiar_pantalla()
            with open("estudiantes.json", "r") as f:
                archivo = json.load(f)

            if self.grado in archivo:
                if self.curso in archivo[self.grado]:
                    lista = archivo[self.grado][self.curso]
                    p(f"Grado:{self.grado}")
                    p(f"    Curso: {self.curso}")
                    for i, (apellido, datos) in enumerate(lista.items(), start=1):
                        print(f"{i}: {datos['Nombre']} {apellido}")
                    pause()
                    return lista
                else:
                    limpiar_pantalla()
                    curso_inesistente()
            else:
                limpiar_pantalla()
                grado_inesistente()
            break
        return self.grado
        return self.curso

class notas_estudiante:
    def ver_notas(self):
        grado = grado_es()
        es()
        curso = curso_es()
        es()
        with open("estudiantes.json", "r") as read:
            archivo = json.load(read)

        if grado in archivo:
            if curso in archivo[grado]:
                list = archivo[grado][curso]
                p(f"Grado: {grado}")
                p(f"Curso: {curso}")
                for i, (apellido, datos) in enumerate(list.items(), start=1):
                    print(f"{i}: {datos['Nombre']}{apellido}") 
                    print(f"{datos['notas']}")
                pause()

            else:
                curso_inesistente()

        else:
            grado_inesistente()

class anotacion:
    def __init__(self):
        self.mostrar = estudiante_ver()
        self.g = guardar_estudiante()
        self.estudiante = {}

    def añadir_anotacion(self):
        with open('estudiantes.json', 'r') as d:
            archivo = json.load(d)

        self.mostrar.opcion_usuario()
        selecion_us = pedir_apellido()
        limpiar_pantalla()
        an = anotacion_()
        while True:
            try:
                anotaciones = archivo[self.mostrar.grado][self.mostrar.curso][selecion_us]
                break
            except KeyError:
                limpiar_pantalla()
                error_clave()
                break
        while True:
            try:
                if 'anotaciones' not in anotaciones:
                    anotaciones['anotaciones'] = []
                anotaciones['anotaciones'].append(an)
                break

            except UnboundLocalError:
                limpiar_pantalla()
                error_anotacion_estudiante()
                pause()
                break

        with open('estudiantes.json', 'w') as j:
            json.dump(archivo, j, indent=4)

    def mostrar_anotacion(self):
        with open('estudiantes.json', 'r') as j:
            leer = json.load(j)
        self.mostrar.opcion_usuario()
        seleccion = entrada_us()
        limpiar_pantalla()
        lista_estudiantes = list(leer[self.mostrar.grado][self.mostrar.curso].keys())
        while True:
            try:
                apellido = lista_estudiantes[seleccion - 1]
                break

            except IndexError:
                break
        while True:
            try:
                anotaciones = leer[self.mostrar.grado][self.mostrar.curso][apellido]['anotaciones']
                for i, texto in enumerate(anotaciones, start=1):
                    print(f"{i}. {texto}")
                pause()
                break

            except UnboundLocalError:
                break

class submenu_anotaciones:
    def __init__(self):
        self.guardar = anotacion()

    def Sub_Menu_Anotacion(self):
        while True:
            limpiar_pantalla()
            submenu_anotacion()
            opcion = entrada()
            opciones_anotacion = {

                1:self.guardar.añadir_anotacion,
                2: self.guardar.mostrar_anotacion

            }

            if opcion in opciones_anotacion:
                limpiar_pantalla()
                opciones_anotacion[opcion]()

            elif opcion == 3:
                salir()
                limpiar_pantalla()
                break        
        
class submenu_anotaciones_2:
    def __init__(self):
        self.mostrar = anotacion()

    def Sub_Menu_Anotacion_2(self):
        while True:
            limpiar_pantalla()
            submenu_anotacion_2()
            opcion = entrada()

            opciones_anotacion_2 = {

                1:self.mostrar.mostrar_anotacion
            }

            if opcion in opciones_anotacion_2:
                limpiar_pantalla()
                opciones_anotacion_2[opcion]()

            elif opcion == 2:
                salir()
                limpiar_pantalla()
                break

class quitar_estudiante:
    def __init__(self):
        self.mostrar = estudiante_ver()

    def Quitar_estudiante(self):
        with open('estudiantes.json', 'r') as f:
            archivo = json.load(f)
        self.mostrar.opcion_usuario()
        es()
        selecion = pedir_apellido()
        opcion = s_n()

        if opcion == 's':
            if self.mostrar.grado in archivo:
                if self.mostrar.curso in archivo[self.mostrar.grado]:
                    while True:
                        try:
                            del archivo[self.mostrar.grado][self.mostrar.curso][selecion]
                            break

                        except KeyError:
                            limpiar_pantalla()
                            error_clave()
                            pause()
                            break

                    with open('estudiantes.json', 'w') as d:
                        json.dump(archivo, d, indent=4)
                    borrado_exitoso()

            else:
                grado_inesistente()

        elif opcion == 'n':
            limpiar_pantalla()

class submenu_quitar:
    def __init__(self):
        self.quitar = quitar_estudiante()

    def Submenu_Quitar(self):
        while True:
            submenu_quitar_estudiante()
            opcion = entrada_us()
            opciones = {
                1: self.quitar.Quitar_estudiante
            }

            if opcion in opciones:
                opciones[opcion]()

            else:
                volver()
                limpiar_pantalla()
                break

class acudientes:
    def __init__(self):
        self.mostrar = estudiante_ver()

    def añadir_acudiente(self):
        with open("estudiantes.json", "r") as f:
            archivo = json.load(f)
        self.mostrar.opcion_usuario()
        selecion = pedir_apellido()
        limpiar_pantalla()
        while True:
            try:
                acudientes = archivo[self.mostrar.grado][self.mostrar.curso][selecion]["acudiente"]
                nombre_acudiente = pedir_nombre_acudiente()
                if "nombres" not in acudientes:
                    acudientes["nombres"] = []
                acudientes["nombres"].append(nombre_acudiente)
                with open("estudiantes.json", "w") as d:
                    json.dump(archivo, d, indent=4)
                break

            except:
                limpiar_pantalla()
                error_clave()
                pause()
                break
        
    def ver_acudientes(self):
        with open("estudiantes.json", "r") as f:
            archivo = json.load(f)
        self.mostrar.opcion_usuario()
        selecion = pedir_apellido()
        limpiar_pantalla()
        while True:
            try:
                acudientes = archivo[self.mostrar.grado][self.mostrar.curso][selecion]["acudiente"]
                nombre = archivo[self.mostrar.grado][self.mostrar.curso][selecion]
                if "nombres" in acudientes:
                    print(f"Acudiente de {nombre["Nombre"]} {selecion}")
                    for nombre in acudientes["nombres"]:
                        print(nombre)
                        pause()
                else:
                    p('no hay acudientes registrados')
                    pause()
                break

            except:
                limpiar_pantalla()
                error_clave()
                pause()
                break

class Sub_menu_añadir_acudiente:
    def __init__(self):
        self.añadir = acudientes()

    def SubMenu_añadir_acudiente(self):
        while True:
            limpiar_pantalla()
            submenu_añadir_acudiente()
            opcion = entrada_us()
            opciones = {
                1:self.añadir.añadir_acudiente,
                2:self.añadir.ver_acudientes
            } 
            if opcion in opciones:
                limpiar_pantalla()
                opciones[opcion]()

            else:
                limpiar_pantalla()
                break
        
class boletines:
    def __init__(self):
        self.mostrar = estudiante_ver()

    def crear_boletin(self):
        with open("estudiantes.json", "r") as f:
            archivo = json.load(f)

        self.mostrar.opcion_usuario()
        self.seleccion = pedir_apellido()
        self.periodo = pedir_periodo()
        limpiar_pantalla()
        while True:
            try:
                self.nombre = archivo[self.mostrar.grado][self.mostrar.curso][self.seleccion]
                boletin = archivo[self.mostrar.grado][self.mostrar.curso][self.seleccion]["boletines"]
                boletin_ = self.escribir_boletin()
                boletin.append(boletin_)
                break

            except:
                error_boletin_estudiante()
                pause()
                break

        with open("estudiantes.json", "w") as d:
            json.dump(archivo, d, indent=4)

    def escribir_boletin(self):
        with open("estudiantes.json", "r") as g:
            notas = json.load(g)

        estudiante = notas[self.mostrar.grado][self.mostrar.curso][self.seleccion]
        boletin = f"""
        ===================================
        Boletin grado{self.mostrar.grado}
                curso{self.mostrar.curso}
        Periodo: {self.periodo}
        ===================================
        Estudiante: {self.seleccion} {self.nombre["Nombre"]}

        Notas:

        """
        for materia, notas in estudiante["notas"].items():
            boletin += f"{materia}: {notas} \n"
        return boletin
    

class SubMenu_mostrar_boletin:
    def __init__(self):
        self.mostrar = estudiante_ver()
    def mostrar_boletin(self):
        self.mostrar.opcion_usuario()
        self.apellido = pedir_apellido()
        limpiar_pantalla()
        with open("estudiantes.json", "r") as b:
            archivo = json.load(b)
        while True:
            try:
                ver_boletin = archivo[self.mostrar.grado][self.mostrar.curso][self.apellido]["boletines"]
                for i, boletin in enumerate(ver_boletin, start=1):
                    print(f"Boletin #{i}")
                    print(boletin)
                es()
                pause()
                break
            except:
                limpiar_pantalla()
                error_boletin_estudiante()
                pause()
                break

        return self.mostrar.grado
        return self.mostrar.curso

class exportar_boletin:
    def __init__(self):
        self.mostrar = estudiante_ver()
        self.ver_boletin = SubMenu_mostrar_boletin()

    def exportar_boletines(self):
        with open("estudiantes.json", "r")  as l:
            archivo = json.load(l)
        self.ver_boletin.mostrar_boletin()
        numero = pedir_numero_boletin()
        while True:
            try:
                boletin = archivo[self.ver_boletin.mostrar.grado][self.ver_boletin.mostrar.curso][self.ver_boletin.apellido]["boletines"][numero-1]
                os.makedirs("Boletines", exist_ok=True)
                os.makedirs(f"Boletines/{self.ver_boletin.mostrar.grado}", exist_ok=True)
                os.makedirs(f"Boletines/{self.ver_boletin.mostrar.grado}/{self.ver_boletin.mostrar.curso}", exist_ok=True)
                ruta = f"Boletines/{self.ver_boletin.mostrar.grado}/{self.ver_boletin.mostrar.curso}/boletin{self.ver_boletin.apellido}.txt"
                with open(ruta, "w", encoding="utf-8") as f:
                    f.write(boletin)
                break

            except:
                limpiar_pantalla()
                error_boletin_estudiante()
                pause()
                break

class sub_menu_añadir_boletin:
    def __init__(self):
        self.añadir = boletines()
        self.mostrar = SubMenu_mostrar_boletin()
        self.exportar = exportar_boletin()

    def SubMenu_añadir_boletin(self):
        while True:
            limpiar_pantalla()
            submenu_añadir_boletin()
            opcion = entrada_us()
            opciones = {
                1:self.añadir.crear_boletin,
                2:self.mostrar.mostrar_boletin,
                3:self.exportar.exportar_boletines
            }
            if opcion in opciones:
                limpiar_pantalla()
                opciones[opcion]()

            else:
                limpiar_pantalla()
                break
