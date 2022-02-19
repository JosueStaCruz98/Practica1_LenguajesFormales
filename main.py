from helpers import Menu, Leer_Data, Leer_Intrucciones, reporte
from LexicoInstrucciones import LexicoInstrucciones

def main():
    txt_data = ""
    txt_intrucciones = ""
    opcion = Menu()
    lexico_intrucciones = None
    while opcion != 4 :
        if opcion == 1:
           txt_data = Leer_Data()
        if opcion == 2:
            txt_intrucciones = Leer_Intrucciones()
            print(txt_intrucciones)
        elif opcion == 3:
            lexico_intrucciones = LexicoInstrucciones(txt_intrucciones)
            lexico_intrucciones.printTokens()
            lexico_intrucciones.GuardarDatos()
        elif opcion ==4:
            print("Imprimiendo reporte")
            reporte()
        elif opcion ==5:
            print("Terminando el programa...")
            exit()#Termina la ejecución del programa
        opcion = Menu()


if __name__ == "__main__":
    main()