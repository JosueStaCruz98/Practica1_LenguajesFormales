from io import open

def Leer_Data():
    archivos_texto = open('Entrada.data', 'r')
    texto = archivos_texto.read()
    return texto

def Leer_Intrucciones():
    archivos_texto = open('Reporte.lfp', 'r')
    texto = archivos_texto.read()
    return texto

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