#configuracion
import os
import random

class configuraciones:
    @staticmethod
    def limpiar_pantalla():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    @staticmethod
    def entrada_us():
        while True:
            try:
                entrada = int(input("Digita numero de opcion: "))
                break
            except ValueError:
                print("Debes escribir un numero no una letra: ")
        return entrada
    @staticmethod
    def p(mensaje):
        print(mensaje)
    @staticmethod
    def es():
        print("    ")
    @staticmethod
    def maquina_seleccion():
        opciones = ["piedra", "papel", "tijera"]
        maquina = random.choice(opciones)
        return maquina
    @staticmethod
    def pedir_opcion():
        while True:
            try:
                numero = int(input("Escribe numero de opcion: "))
                break
            except ValueError:
                print("Debes escribir un numero no una letra")
        return numero
    @staticmethod
    def pausa():
        input("CLICK ENTER PARA CONTINUAR")
    @staticmethod
    def guardar_puntaje(puntaje):
        os.makedirs("Puntajes",exist_ok=True)
        name = str(input("Escribe tu nombre para guardar puntaje: ")).capitalize()
        ruta = f"Puntajes/{name}.txt"
        puntaje_ = str(puntaje)
        with open(ruta, "w") as f:
            f.write(puntaje_ + "\n")



