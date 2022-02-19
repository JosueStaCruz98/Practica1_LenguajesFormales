from io import open
from tkinter import filedialog
from tkinter import Tk
#Función que permite jalar el archivo .data
def Leer_Data():
    Tk().withdraw()
    file = filedialog.askopenfile(
        title = "Selecciona un archivo.",
        initialdir = "./",
        filetypes = (
            ("Únicamente .data", "*.data"),#Permite que solo se seleccionen archivos .data
            ("Todos los archivos", "*.*")
        )
    )
    if file is None:
        print("No has seleccioado ningún archivo.")
        return None
    else:
        datos = file.read()
        file.close()
        print("Tu archivo ha sido cargado exitosamente.")
        return datos
#Función que permite jalar el archivo .lfp
def Leer_Intrucciones():
    Tk().withdraw()
    file = filedialog.askopenfile(
        title = "Selecciona un archivo.",
        initialdir = "./",
        filetypes = (
            ("Únicamente .lfp", "*.lfp"),#Permite que solo se seleccionen archivos .lfp
            ("Todos los archivos", "*.*")
        )
    )
    if file is None:
        print("No has seleccioado ningún archivo.")
        return None
    else:
        texto = file.read()
        file.close()
        print("Tu archivo ha sido cargado exitosamente.")
        return texto
#Muestra el menú en la consola 
def Menu():
    print("============MENU============")
    print("│1. Cargar Data           │")
    print("│2. Cargar Instrucciones  │")
    print("│3. Analizar              │")
    print("│4. Reporte               │")
    print("│5. Salir                 │")
    print("============================")
    print("Seleccione la opción que necesita")
    entrada = int(input())
    return entrada

#Función que genera el reporte en un formato html
def reporte():
    file = open("Reporte.html", "w")
    head = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="reporte.css" type="text/css" />
                <title>Document</title>
                </head>
                <body>
                <h2>Nombre: Josue Santa Cruz Ramírez</h2>
                <h2>Carné: 202006692 <a target="_blank"></a></h2>
                <h3>Reporte Creado.</h3>
                """
    file.write(head)
    
    endd = f"""
         </body>
         </html>
         """
    file.write(endd)
    file.close()
