import os

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("Presiona una tecla para continuar...")

def menuPrincipal():
    print("\n\t💾💾 Escuela Número 24 💾💾 \n..::: Sistema Para La Gestión de Calificaciones :::...")
    print(" 1.- 👤 Crear Nuevo Alumno")
    print(" 2.- ❌ Borrar Alumno")
    print(" 3.- 📂 Mostrar Alumno")
    print(" 4.- 📝 Agregar Calificación")
    print(" 5.- 💾 Calcular Calificaciones")
#    print(" 6.- Borrar Característica o Calificación de Alumno")
    print(" 6.- 🚪SALIR")
    return input("Elige una opción del (1-6): ").strip()

def crearAlumno(datos):
    borrarPantalla()
    print("\n\t:: Crear Nuevo Alumno ::\n")
    nombre = input("Ingresa el nombre del alumno: ").strip().title()
    calificacion = input("Ingresa una o varias calificaciones separadas por comas (opcional): ").strip()
    califs = []
    if calificacion:
        try:
            califs = [float(x) for x in calificacion.split(",") if x.strip() != ""]
        except ValueError:
            print("Error: Solo números separados por comas.")
            esperarTecla()
            return
    alumno = {
        "nombre": nombre,
        "calificaciones": califs
    }
    datos.append(alumno)
    print("\n ✅Alumno creado con éxito✅.")
    esperarTecla()

def mostrarAlumno(datos):
    borrarPantalla()
    print("\n\t:: Mostrar Alumno(s) ::\n")
    if datos:
        for i, alumno in enumerate(datos, start=1):
            print(f"\nAlumno {i}:")
            for clave, valor in alumno.items():
                if clave == "calificaciones" and isinstance(valor, list):
                    print(f"  {clave.capitalize()}: {', '.join(map(str, valor)) if valor else 'No hay calificaciones'}")
                else:
                    print(f"  {clave.capitalize()}: {valor}")
    else:
        print("No hay alumnos registrados.")
    esperarTecla()

def eliminarAlumno(datos):
    borrarPantalla()
    print("\n\t:: Eliminar Alumno ::\n")
    if datos:
        mostrarAlumno(datos)
        try:
            indice = int(input("\nNúmero del alumno a eliminar: ")) - 1
            if 0 <= indice < len(datos):
                eliminado = datos.pop(indice)
                print(f"Alumno '{eliminado['nombre']}' eliminado con éxito.")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Debes ingresar un número válido.")
    else:
        print("No hay alumnos registrados.")
    esperarTecla()

#def agregarCaracteristicasAlumno(datos):
    borrarPantalla()
    print("\n\t:: Agregar Característica o Calificación a un Alumno ::\n")
    if datos:
        mostrarAlumno(datos)
        try:
            indice = int(input("\nNúmero del alumno a modificar: ")) - 1
            if 0 <= indice < len(datos):
                alumno = datos[indice]
                clave = input("Nombre de la característica (usa 'calificaciones' para agregar notas): ").lower().strip()
                if clave == "calificaciones":
                    nuevas_califs = input("Ingresa una o varias calificaciones separadas por comas: ").strip()
                    try:
                        nuevas = [float(x) for x in nuevas_califs.split(",") if x.strip() != ""]
                        alumno.setdefault("calificaciones", []).extend(nuevas)
                        print(f"Se agregaron {len(nuevas)} calificaciones.")
                    except ValueError:
                        print("Error: Solo números separados por comas.")
                else:
                    valor = input("Valor de la característica: ").strip()
                    alumno[clave] = valor
                    print("Característica agregada con éxito.")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Debes ingresar un número válido.")
    else:
        print("No hay alumnos registrados.")
    esperarTecla()

#def borrarCaracteristicaAlumno(datos):
    borrarPantalla()
    print("\n\t:: Borrar Característica o Calificación de un Alumno ::\n")
    if datos:
        mostrarAlumno(datos)
        try:
            indice = int(input("\nNúmero del alumno a modificar: ")) - 1
            if 0 <= indice < len(datos):
                alumno = datos[indice]
                print("\nCaracterísticas disponibles:")
                for clave in alumno.keys():
                    print(f"- {clave}")
                eliminar = input("Escribe la característica que deseas borrar: ").lower().strip()
                if eliminar in alumno:
                    if eliminar == "calificaciones" and isinstance(alumno[eliminar], list):
                        if alumno[eliminar]:
                            print("\nCalificaciones actuales:")
                            for i, cal in enumerate(alumno[eliminar], start=1):
                                print(f"{i}. {cal}")
                            try:
                                cal_elim = int(input("Número de la calificación a eliminar: ")) - 1
                                if 0 <= cal_elim < len(alumno[eliminar]):
                                    valor_elim = alumno[eliminar].pop(cal_elim)
                                    print(f"Calificación {valor_elim} eliminada.")
                                else:
                                    print("Número inválido.")
                            except ValueError:
                                print("Debes ingresar un número válido.")
                        else:
                            print("No hay calificaciones para eliminar.")
                    else:
                        del alumno[eliminar]
                        print("Característica eliminada.")
                else:
                    print("Esa característica no existe.")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Debes ingresar un número válido.")
    else:
        print("No hay alumnos registrados.")
    esperarTecla()

def calcularCalificaciones(datos):
    borrarPantalla()
    print("\n\t:: Calcular Promedio de Calificaciones ::\n")
    if datos:
        mostrarAlumno(datos)
        try:
            indice = int(input("\nNúmero del alumno a calcular: ")) - 1
            if 0 <= indice < len(datos):
                califs = datos[indice].get("calificaciones", [])
                if isinstance(califs, list) and califs:
                    promedio = sum(califs) / len(califs)
                    print(f"Promedio de {datos[indice]['nombre']}: {promedio:.2f}")
                else:
                    print("No hay calificaciones para este alumno.")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Debes ingresar un número válido.")
    else:
        print("No hay alumnos registrados.")
    esperarTecla()
