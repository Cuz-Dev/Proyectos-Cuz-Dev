#nivel_arcade

while True:
    try:
        from configuracion import configuraciones as cf
        from UI import interfaz_terminal as i
        break
    except ModuleNotFoundError:
        print("No se encontro un archivo")
    
class Nivel_:
    def __init__(self):
        self.puntaje = 0

    def juego(self):
        while True:
            cf.limpiar_pantalla()
            i.juego_nivel(self.puntaje)
            self.maquina = cf.maquina_seleccion()
            self.usuario = cf.pedir_opcion()
            cf.limpiar_pantalla()
            opcines_maquina = {
                "piedra":self.piedra,
                "papel":self.Papel,
                "tijera":self.Tijera
            }

            if self.usuario == 0:
                cf.guardar_puntaje(self.puntaje)

            elif self.maquina in opcines_maquina:
                cf.limpiar_pantalla()
                opcines_maquina[self.maquina]()
                
            else:
                cf.limpiar_pantalla()
                break

    def piedra(self):
        while True:
            if self.usuario == 1:
                cf.limpiar_pantalla()
                i.empate(self.puntaje,self.maquina)
                cf.pausa()
                break

            elif self.usuario == 2:
                self.puntaje =+ 10
                cf.limpiar_pantalla()
                i.ganaste(self.puntaje,self.maquina)
                cf.pausa()
                break
            
            elif self.usuario == 3:
                self.puntaje -= 10
                cf.limpiar_pantalla()
                i.perdiste(self.puntaje,self.maquina)
                cf.pausa()
                break
            
            else:
                cf.limpiar_pantalla()
                print("e")
                break

    def Papel(self):
        while True:
            if self.usuario == 1:
                self.puntaje -= 10
                cf.limpiar_pantalla()
                i.perdiste(self.puntaje,self.maquina)
                cf.pausa()
                break

            elif self.usuario == 2:
                cf.limpiar_pantalla()
                i.empate(self.puntaje,self.maquina)
                cf.pausa()
                break
            
            elif self.usuario == 3:
                self.puntaje += 10
                cf.limpiar_pantalla()
                i.ganaste(self.puntaje,self.maquina)
                cf.pausa()
                break

            else:
                cf.limpiar_pantalla()
                break

    def Tijera(self):
        while True:
            if self.usuario == 1:
                self.puntaje += 10
                cf.limpiar_pantalla()
                i.ganaste(self.puntaje,self.maquina)
                cf.pausa()
                break
            elif self.usuario == 2:
                self.puntaje -= 10
                cf.limpiar_pantalla()
                i.perdiste(self.puntaje,self.maquina)
                cf.pausa()
                break
            elif self.usuario == 3:
                cf.limpiar_pantalla()
                i.empate(self.puntaje,self.maquina)
                cf.pausa()
                break

            else:
                break
