import os

def no_se_encontro_archivo(name):
    print(f"No se encontro : {name}")
    print("Descargar el archivo desde mi repo de github")

while True:
    if os.path.exists("configuracion.py"):
        break

    else:
        no_se_encontro_archivo(name="configuracion.py")

while True:
    if os.path.exists("info.py"):
        break
    
    else:
        no_se_encontro_archivo(name="info.py")

while True:
    if os.path.exists("info.txt"):
        break
    else:
        no_se_encontro_archivo(name="info.txt")

while True:
    if os.path.exists("main.py"):
        break
    else:
        no_se_encontro_archivo(name="main.py")

while True:
    if os.path.exists("puntajes.py"):
        break
    else:
        no_se_encontro_archivo(name="puntajes.py")

while True:
    if os.path.exists("UI.py"):
        break
    else:
        no_se_encontro_archivo(name="UI.py")

while True:
    if  os.path.exists("__init__.py"):
        break
    else:
        no_se_encontro_archivo(name="__init__.py")

while True:
    if os.path.exists("nivel_arcade.py"):
        break
    else:
        no_se_encontro_archivo(name="nivel_arcade.py")

os.makedirs("V3 Piedra papel o tijera/Juego",exist_ok=True)

os.rename("main.py", "Piedra papel o tijera.py")

os.rename("Piedra papel o tijera.py", "V3 Piedra papel o tijera/Piedra papel o tijera.py")

os.rename("configuracion.py", "V3 Piedra papel o tijera/configuracion.py")

os.rename("info.txt", "V3 Piedra papel o tijera/info.txt")

os.rename("info.py", "V3 Piedra papel o tijera/info.py")

os.rename("UI.py", "V3 Piedra papel o tijera/UI.py")

os.rename("puntajes.py", "V3 piedra papel o tijera/puntajes.py")

os.rename("__init__.py", "V3 Piedra papel o tijera/Juego/__init__.py")

os.rename("nivel_arcade.py", "V3 Piedra papel o tijera/Juego/nivel_arcade.py")

print("Ejecuta el archivo: Piedra papel o tijera.py")
print("En la carpeta: V3 Piedra papel o tijera ")
