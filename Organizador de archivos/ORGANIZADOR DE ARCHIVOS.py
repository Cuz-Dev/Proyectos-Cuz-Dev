#Organizador de archivos
#Desarrollador Cuz-Dev

import os
import time
class Organizador:
    @staticmethod
    def menu_organizador():
        while True:
            cf.limpiar_pantalla()
            print("╔══════════════════════════════════════════╗")
            print("║          Organizador de archivos         ║ ")
            print("║           Desarrollador Cuz-Dev          ║ ")
            print("╚══════════════════════════════════════════╝")
            print("╔                                          ╗")
            print("║  1^ Empezar      |                   ║ ")
            print("║  2^ Info         |                       ║")
            print("║  3^ SALIR        |                   ║ ")
            print("╚                                          ╝")
            entrada = cf.entrada_us()
            opciones = {}
            if entrada == 1:
                Organizacion_archivos.empezando()

            elif entrada == 2:
                cf.limpiar_pantalla()
                print("Organizador de archivos")
                print("Desarrollador cuz dev")
                cf.es()
                print("el programa no borra archivos")
                print("Los organiza en una carpeta diferente segun su extencion")
                input("CLICK ENTER PARA CONTINUAR")
                
            else:
                cf.limpiar_pantalla()
                break
extenciones_fotos = (".jpeg",".png",".jpg",".webp")
extencion_musica = (".mp3",".m4a")
extencion_java = (".java", ".class")
extencion_comprimidos = (".rar",".zip",".7z",".tar")

tipos = {
    "Fotos": (".jpeg",".png",".jpg",".webp"),
    "Videos": (".mp4"),
    "TXT": (".txt"),
    "Musica": (".mp3",".m4a"),
    "Python": (".py"),
    "Java": (".java",".class"),
    "C++": (".cpp"),
    "Json": (".json"),
    "Comprimidos": (".rar",".zip",".7z",".tar"),
    "Exe": (".exe"),
    "Pdf": (".pdf"),
    "Apk": (".apk"),
    "Utorrent": (".torrent"),
    "HEX": (".hex"),
    "Iso": (".iso")
}

class Organizacion_archivos:
    @staticmethod
    def empezando():
        while True:
            cf.limpiar_pantalla()
            print("➤ Archivos disponibles para Organizacion")
            cf.es()
            print("[Advertencia] se recomienda leer primero la info, opcion 2:")
            cf.es()
            print("Digita 0 para ordenar todos los archivos")
            cf.es()
            print("╔                                                         ╗")
            print("  1* Fotos            ║             6* Java                ")
            print("  2* Videos           ║             7* C++                 ")
            print("  3* Txt              ║             8* Json                ")
            print("  4* Musica           ║             9* Comprimidos         ")
            print("  5* Python           ║             10* Exe                ")
            print("╚                                                         ╝")
            entrada = cf.entrada_us()
            if entrada == 0:
                mover_archivos.mover_todo(tipos)
                break

            elif entrada == 1:
                mover_archivos.mover_archivo("Fotos",extenciones_fotos)
                break

            elif entrada == 2:
                mover_archivos.mover_archivo("Videos",extencion=".mp4")
                break

            elif entrada == 3:
                mover_archivos.mover_archivo("TXT",extencion=".txt")
                break

            elif entrada == 4:
                mover_archivos.mover_archivo("Musica",extencion_musica)
                break

            elif entrada == 5:
                mover_archivos.mover_archivo("Python",extencion=".py")
                break

            elif entrada == 6:
                mover_archivos.mover_archivo("Java",extencion_java)
                break

            elif entrada == 7:
                mover_archivos.mover_archivo("C++",extencion=".cpp")
                break

            elif entrada == 8:
                mover_archivos.mover_archivo("Json",extencion=".json")
                break

            elif entrada == 9:
                mover_archivos.mover_archivo("Comprimidos",extencion_comprimidos)
                break

            elif entrada == 10:
                mover_archivos.mover_archivo("Exe",extencion=".exe")
                break

            elif entrada == 11:
                mover_archivos.mover_archivo("Pdf",extencion=".pdf")

class mover_archivos:
    @staticmethod
    def mover_archivo(carpeta,extencion):
        os.makedirs(carpeta,exist_ok=True)
        for archivo in os.listdir():
            if archivo.endswith(extencion):
                os.rename(f"{archivo}", f"{carpeta}/{archivo}")

    @staticmethod
    def mover_todo(tipos):
        for carpeta, extencion in tipos.items():
            os.makedirs(carpeta,exist_ok=True)
            for archivo in os.listdir():
                if archivo.endswith(extencion):
                    os.rename(archivo,f"{carpeta}/{archivo}")

class configuracion:
    @staticmethod
    def entrada_us():
        while True:
            try:
                usuario = int(input("Digita numero de opcion: "))
                break
            except ValueError:
                print("Debes escribir un numero no una letra")
        return usuario
    @staticmethod
    def es():
        print("  ")
    @staticmethod
    def limpiar_pantalla():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    
    
cf = configuracion()

inicio = Organizador()
inicio.menu_organizador()