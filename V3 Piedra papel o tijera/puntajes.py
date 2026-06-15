#puntajes
import os
while True:
    try:
        from configuracion import configuraciones as cf
        break

    except ModuleNotFoundError:
        print("No se encontro un archivo")

class Puntaje:
    @staticmethod
    def ver_puntaje():
        while True:
            try:
                for archivo in os.listdir("Puntajes/"):
                    ruta = f"Puntajes/{archivo}"
                with open(ruta, "r") as f:
                    puntaje = int(f.read())
                nombre = archivo.replace(".txt", "  ")
                print(nombre, puntaje)
                cf.pausa()
                break
            except:
                print("Un archivo u carpeta no existe")
                print("Primero guarde un puntaje")
                break