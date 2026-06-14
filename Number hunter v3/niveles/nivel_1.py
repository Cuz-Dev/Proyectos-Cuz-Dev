
# nivel 1

while True:
    try:
        import random
        from configuracion import configuraciones as cf
        from niveles.nivel_2 import Nivel_2
        break

    except ModuleNotFoundError:
        print("No se encontro el archivo")

class Nivel_1:
    @staticmethod
    def Nivel():
        puntaje = 0
        while True:
            cf.limpiar_pantalla()
            cf.p(f"➤Nivel 1  Puntaje actual: {puntaje}")
            cf.es()
            numero_maquina = random.randint(1, 10)
            numero_usuario = cf.pedir_numero()
            if numero_usuario == numero_maquina:
                Nivel_2.nivel()
            else:
                cf.limpiar_pantalla()
                cf.p(f"El numero era {numero_maquina}")
                cf.pausa()
                break
            