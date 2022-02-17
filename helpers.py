from io import open
from tkinter import filedialog
from tkinter import Tk

def Leer_Data():
    Tk().withdraw()
    file = filedialog.askopenfile(
        title = "Selecciona un archivo.",
        initialdir = "./",
        filetypes = (
            ("Únicamente .data", "*.data"),
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

def reporte():
    global students
    global ascendente
    global descendente
    global parameters
    global listaGanadores
    global listaPerdedores
    global promedio
    global nameCurse
    global notaMayor
    global notaMenor
    global numberStudents
    global ganadores
    global perdedores
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
                <h2>Nombre: Josue Santa Cruz Ramírez <a target="_blank">{numberStudents}</a></h2>
                <h2>Carné: 202006692 <a target="_blank"></a></h2>
                <h3>Listado como fue cargado.</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody>
                """
    file.write(head)
    for for1 in students:
        f1 = f"""
         <tr>
         <td>{for1.nombre}</td>
         <td>{for1.calificacion}</td>
         </tr>
         """
        file.write(f1)
    end1 = f"""
         </tbody>
         </table>
         """
    file.write(end1)
    for para in parameters:
        if para == "ASC":
            para1 = f"""
            <h3>Listado de forma ASCENDENTE.</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para1)
            for for2 in ascendente:
                f2 = f"""
                <tr>
                <td>{for2.nombre}</td>
                <td>{for2.calificacion}</td>
                </tr>
                """
                file.write(f2)
            end2 = f"""
             </tbody>
             </table>
             """
            file.write(end2)
        if para == " ASC":
            para1 = f"""
            <h3>Listado de forma ASCENDENTE.</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para1)
            for for2 in ascendente:
                f2 = f"""
                <tr>
                <td>{for2.nombre}</td>
                <td>{for2.calificacion}</td>
                </tr>
                """
                file.write(f2)
            end2 = f"""
             </tbody>
             </table>
             """
            file.write(end2)
        if para == "ASC ":
            para1 = f"""
            <h3>Listado de forma ASCENDENTE.</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para1)
            for for2 in ascendente:
                f2 = f"""
                <tr>
                <td>{for2.nombre}</td>
                <td>{for2.calificacion}</td>
                </tr>
                """
                file.write(f2)
            end2 = f"""
             </tbody>
             </table>
             """
            file.write(end2)
        if para ==" ASC ":
            para1 = f"""
            <h3>Listado de forma ASCENDENTE.</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para1)
            for for2 in ascendente:
                f2 = f"""
                <tr>
                <td>{for2.nombre}</td>
                <td>{for2.calificacion}</td>
                </tr>
                """
                file.write(f2)
            end2 = f"""
             </tbody>
             </table>
             """
            file.write(end2)
        if para == "DESC":
            para2 = f"""
            <h3>Listado de forma DESCENDENTE.</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para2)
            for for3 in descendente:
                f3 = f"""
                <tr>
                <td>{for3.nombre}</td>
                <td>{for3.calificacion}</td>
                </tr>
                """
                file.write(f3)
            end3 = f"""
             </tbody>
             </table>
             """
            file.write(end3)
        if para ==" DESC":
            para2 = f"""
            <h3>Listado de forma DESCENDENTE.</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para2)
            for for3 in descendente:
                f3 = f"""
                <tr>
                <td>{for3.nombre}</td>
                <td>{for3.calificacion}</td>
                </tr>
                """
                file.write(f3)
            end3 = f"""
             </tbody>
             </table>
             """
            file.write(end3)
        if para ==  "DESC ":
            para2 = f"""
            <h3>Listado de forma DESCENDENTE.</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para2)
            for for3 in descendente:
                f3 = f"""
                <tr>
                <td>{for3.nombre}</td>
                <td>{for3.calificacion}</td>
                </tr>
                """
                file.write(f3)
            end3 = f"""
             </tbody>
             </table>
             """
            file.write(end3)
        if para == " DESC ":
            para2 = f"""
            <h3>Listado de forma DESCENDENTE.</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para2)
            for for3 in descendente:
                f3 = f"""
                <tr>
                <td>{for3.nombre}</td>
                <td>{for3.calificacion}</td>
                </tr>
                """
                file.write(f3)
            end3 = f"""
             </tbody>
             </table>
             """
            file.write(end3)
        if para == "AVG":
            para3 = f"""
            <h3>El PROMEDIO de notas del curso: .</h3>
                <table class="container">
                 <tbody>
                 <tr>
                 <td>Promedio</td>
                 <td>{promedio}</td>
                 </tr>
                 </tbody>
                 </table>
            """
            file.write(para3)
        if para ==" AVG":
            para3 = f"""
            <h3>El PROMEDIO de notas del curso: .</h3>
                <table class="container">
                 <tbody>
                 <tr>
                 <td>Promedio</td>
                 <td>{promedio}</td>
                 </tr>
                 </tbody>
                 </table>
            """
            file.write(para3)
        if para =="AVG ":
            para3 = f"""
            <h3>El PROMEDIO de notas del curso: .</h3>
                <table class="container">
                 <tbody>
                 <tr>
                 <td>Promedio</td>
                 <td>{promedio}</td>
                 </tr>
                 </tbody>
                 </table>
            """
            file.write(para3)
        if para ==" AVG ":
            para3 = f"""
            <h3>El PROMEDIO de notas del curso: .</h3>
                <table class="container">
                 <tbody>
                 <tr>
                 <td>Promedio</td>
                 <td>{promedio}</td>
                 </tr>
                 </tbody>
                 </table>
            """
            file.write(para3)
        if para == "MIN":
            para4 = f"""
            <h3>El estudiante con la nota mas BAJA del curso fue: .</h3>
                <table class="container">
                 <tbody>
                 <tr>
                 <td>Peor estudiante</td>
                 <td>{notaMenor}</td>
                 </tr>
                 </tbody>
                 </table>
            """
            file.write(para4)
        if para ==" MIN":
            para4 = f"""
            <h3>El estudiante con la nota mas BAJA del curso fue: .</h3>
                <table class="container">
                 <tbody>
                 <tr>
                 <td>Peor estudiante</td>
                 <td>{notaMenor}</td>
                 </tr>
                 </tbody>
                 </table>
            """
            file.write(para4)
        if para =="MIN ":
            para4 = f"""
            <h3>El estudiante con la nota mas BAJA del curso fue: .</h3>
                <table class="container">
                 <tbody>
                 <tr>
                 <td>Peor estudiante</td>
                 <td>{notaMenor}</td>
                 </tr>
                 </tbody>
                 </table>
            """
            file.write(para4)
        if para ==" MIN ":
            para4 = f"""
            <h3>El estudiante con la nota mas BAJA del curso fue: .</h3>
                <table class="container">
                 <tbody>
                 <tr>
                 <td>Peor estudiante</td>
                 <td>{notaMenor}</td>
                 </tr>
                 </tbody>
                 </table>
            """
            file.write(para4)
        if para == "MAX":
            para5 = f"""
            <h3>El estudiante con la nota mas ALTA del curso fue: .</h3>
                <table class="container">
                 <tbody>
                 <tr>
                 <td>Mejor estudiante</td>
                 <td>{notaMayor}</td>
                 </tr>
                 </tbody>
                 </table>
            """
            file.write(para5)
        if para == " MAX":
            para5 = f"""
            <h3>El estudiante con la nota mas ALTA del curso fue: .</h3>
                <table class="container">
                 <tbody>
                 <tr>
                 <td>Mejor estudiante</td>
                 <td>{notaMayor}</td>
                 </tr>
                 </tbody>
                 </table>
            """
            file.write(para5)
        if para =="MAX ":
            para5 = f"""
            <h3>El estudiante con la nota mas ALTA del curso fue: .</h3>
                <table class="container">
                 <tbody>
                 <tr>
                 <td>Mejor estudiante</td>
                 <td>{notaMayor}</td>
                 </tr>
                 </tbody>
                 </table>
            """
            file.write(para5)
        if para ==" MAX ":
            para5 = f"""
            <h3>El estudiante con la nota mas ALTA del curso fue: .</h3>
                <table class="container">
                 <tbody>
                 <tr>
                 <td>Mejor estudiante</td>
                 <td>{notaMayor}</td>
                 </tr>
                 </tbody>
                 </table>
            """
            file.write(para5)
        if para == "APR":
            para6 = f"""
            <h3>El numero de estudiantes aprobados fue: {ganadores}.</h3>
            <h3>Listado de estudiantes aprobados: .</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para6)
            for for3 in listaGanadores:
                f3 = f"""
                <tr>
                <td>{for3.nombre}</td>
                <td>{for3.calificacion}</td>
                </tr>
                """
                file.write(f3)
            end3 = f"""
             </tbody>
             </table>
             """
            file.write(end3)
        if para ==" APR":
            para6 = f"""
            <h3>El numero de estudiantes aprobados fue: {ganadores}.</h3>
            <h3>Listado de estudiantes aprobados: .</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para6)
            for for3 in listaGanadores:
                f3 = f"""
                <tr>
                <td>{for3.nombre}</td>
                <td>{for3.calificacion}</td>
                </tr>
                """
                file.write(f3)
            end3 = f"""
             </tbody>
             </table>
             """
            file.write(end3)
        if para =="APR ":
            para6 = f"""
            <h3>El numero de estudiantes aprobados fue: {ganadores}.</h3>
            <h3>Listado de estudiantes aprobados: .</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para6)
            for for3 in listaGanadores:
                f3 = f"""
                <tr>
                <td>{for3.nombre}</td>
                <td>{for3.calificacion}</td>
                </tr>
                """
                file.write(f3)
            end3 = f"""
             </tbody>
             </table>
             """
            file.write(end3)
        if para ==" APR ":
            para6 = f"""
            <h3>El numero de estudiantes aprobados fue: {ganadores}.</h3>
            <h3>Listado de estudiantes aprobados: .</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para6)
            for for3 in listaGanadores:
                f3 = f"""
                <tr>
                <td>{for3.nombre}</td>
                <td>{for3.calificacion}</td>
                </tr>
                """
                file.write(f3)
            end3 = f"""
             </tbody>
             </table>
             """
            file.write(end3)
        if para == "REP":
            para7 = f"""
            <h3>El numero de estudiantes reprobados fue: {perdedores}.</h3>
            <h3>Listado de estudiantes reprobados: .</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para7)
            for for4 in listaPerdedores:
                f4 = f"""
                <tr>
                <td>{for4.nombre}</td>
                <td>{for4.calificacion}</td>
                </tr>
                """
                file.write(f4)
            end4 = f"""
             </tbody>
             </table>
             """
            file.write(end4)
        if para == " REP":
            para7 = f"""
            <h3>El numero de estudiantes reprobados fue: {perdedores}.</h3>
            <h3>Listado de estudiantes reprobados: .</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para7)
            for for4 in listaPerdedores:
                f4 = f"""
                <tr>
                <td>{for4.nombre}</td>
                <td>{for4.calificacion}</td>
                </tr>
                """
                file.write(f4)
            end4 = f"""
             </tbody>
             </table>
             """
            file.write(end4)
        if para == "REP ":
            para7 = f"""
            <h3>El numero de estudiantes reprobados fue: {perdedores}.</h3>
            <h3>Listado de estudiantes reprobados: .</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para7)
            for for4 in listaPerdedores:
                f4 = f"""
                <tr>
                <td>{for4.nombre}</td>
                <td>{for4.calificacion}</td>
                </tr>
                """
                file.write(f4)
            end4 = f"""
             </tbody>
             </table>
             """
            file.write(end4)
        if para ==" REP ":
            para7 = f"""
            <h3>El numero de estudiantes reprobados fue: {perdedores}.</h3>
            <h3>Listado de estudiantes reprobados: .</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para7)
            for for4 in listaPerdedores:
                f4 = f"""
                <tr>
                <td>{for4.nombre}</td>
                <td>{for4.calificacion}</td>
                </tr>
                """
                file.write(f4)
            end4 = f"""
             </tbody>
             </table>
             """
            file.write(end4)
    endd = f"""
         </body>
         </html>
         """
    file.write(endd)
    file.close()
