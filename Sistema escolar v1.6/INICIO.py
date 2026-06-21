
#INICIO 

import os
import zipfile

while True:
    if os.path.exists("package.zip"):
        break

    else:
        print("No se encontro el archivo package.zip ")
        print("Descargalo en mi github")
        input('    ')

os.makedirs("Sistema_escolar_1.6", exist_ok=True)

with zipfile.ZipFile("package.zip", "r") as archivo_zip:
    archivo_zip.extractall("Sistema_escolar_1.6")