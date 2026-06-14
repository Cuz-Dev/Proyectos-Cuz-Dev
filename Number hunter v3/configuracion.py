#configuracion 
import os
class configuraciones:
    @staticmethod
    def limpiar_pantalla():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    @staticmethod
    def es():
        print("   ")
    @staticmethod
    def p(mensaje):
        print(mensaje)    
    @staticmethod    
    def pausa():
        input("cLICK ENTER PARA CONTINUAR")
    @staticmethod
    def p(mensaje):
        print(mensaje)
    @staticmethod
    def entrada_us():
        while True:
            try:
                entrada = int(input("Digita numero de opcion: "))
                break

            except ValueError:
                print("Debes escribir un numero no una letra")
        return entrada
    @staticmethod
    def pedir_numero():
        while True:
            try:
                numero = int(input("Digita un numero random para pasar de nivel: "))
                break
            except ValueError:
                print("Debes escribir un numero no una letra: ")
        return numero
    @staticmethod
    def guardar_puntaje(puntaje):
        os.makedirs("Puntajes", exist_ok=True)
        nombre = str(input("Escribe tu nombre para guardar puntaje: ")).capitalize()
        ruta = f"Puntajes/{nombre}.txt"
        puntaje_ = str(puntaje)
        with open(ruta, "a") as f:
            f.write(puntaje_ + "\n")
    @staticmethod
    def game_over(maquina):
        print("Game over")
        print(f"El numero correcto era {maquina}")
            
    @staticmethod
    def game_win(puntaje_final):
        print(f"Felicidades te pasate el juego: Puntaje {puntaje_final}")
        input("Click enter para continuar")
        configuraciones.guardar_puntaje(puntaje_final)
        configuraciones.pausa()