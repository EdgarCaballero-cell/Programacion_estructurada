import os

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("Presiona una tecla para continuar...")

def menuPrincipal():
    print("\n\t..::: 💾💾 Sistema Para la Gestion de Agenda de Contactos 💾💾  :::...\n  ")
    print(" 1.- 👤 Agregar Contacto")
    print(" 2.- 💾 Buscar contacto por Nombre ")
    print(" 3.- 📂 Mostrar Todos los Contactos ")
    print(" 4.- 💾 modificar contacto por Nombre ")
#    print(" 4.- 📝 Agregar Calificación")
#    print(" 5.- 💾 Calcular Calificaciones")
#    print(" 6.- Borrar Característica o Calificación de Alumno")
    print(" 5.- 🚪 Borrar contacto")
    print("6. SALIR ")
    return input("Elige una opción del (1-6): ").strip()
# agenda.py P2_2C_CLA/...
# agenda.py P2_2A_CLA/... X main.py

def modificar_contacto(agenda):
    borrarPantalla()
    print("Modificar Contactos")
    if not agenda:
        print("No hay contactos")
    else:
        nombre=input("Nombre: ").upper().strip()
        if nombre in agenda:
            print(f"{'Nombre':<15}{'Telefono':<15}{'Email':<15}")
            print(f"{'-'*60}")
            print(f"{nombre:<15}{agenda[nombre][0]:<15}{agenda[nombre][1]:<15}")
            resp=input("¿Desea modificar el contacto? (Si/No) ").lower().strip()
            if resp=="si":
                tel=input("Telefono: ").strip()
                email=input("Email: ").upper().strip()
                agenda[nombre]=[tel,email]
                print("Accion realizada con exito")
            else:
                print("No-existente el contacto")

def agregar_contacto(agenda):
    borrarPantalla()
    print("Agregar Contactos")
    nombre=input("Nombre: ").upper().strip()
    if nombre in agenda:
        print("Contacto existente")
    else:
        tel=input("Telefono: ").strip()
        email=input("Email: ").upper().strip()
        agenda[nombre]=[tel,email]
        print("Accion realizada con exito")

def mostrar_contacto(agenda):
    borrarPantalla()
    print("Mostrar Contactos")
    if not agenda:
        print("No hay contactos")
    else:
        print(f"{'Nombre':<15}{'Telefono':<15}{'Email':<15}")
        print(f"{'-'*60}")
        for nombre,datos in agenda.items():
            print(f"{nombre:<15}{datos[0]:<15}{datos[1]:<15}")
            print(f"{'-'*60}")

def buscar_contacto(agenda):
    borrarPantalla()
    print("Buscar Contactos")
    if not agenda:
        print("No hay contactos en la Agenda")
    else:
        nombre=input("Nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            print(f"{'Nombre':<15}{'Telefono':<15}{'Email':<15}")
            print(f"{'-'*60}")
            print(f"{nombre:<15}{agenda[nombre][0]:<15}{agenda[nombre][1]:<15}")
        else:
            print("No-existente el contacto")

def eliminar_contacto(agenda):
    borrarPantalla()
    print("Eliminar Contactos")
    if not agenda:
        print("No hay contactos en la Agenda")
    else:
        nombre=input("Nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            print(f"{'Nombre':<15}{'Telefono':<15}{'Email':<15}")
            print(f"{'-'*60}")
            print(f"{nombre:<15}{agenda[nombre][0]:<15}{agenda[nombre][1]:<15}")
            resp=input("¿Desea eliminar los valores? (Si/No) ").lower().strip()
            if resp=="si":
                agenda.pop(nombre)
                print("Accion Realizada con exito")
            else:
                print("Este contacto no existe")


#def agregarCaracteristicasAlumno(datos):
#    print("\n\t:: Agregar Característica o Calificación a un Alumno ::\n")
#    if datos:
#        mostrarAlumno(datos)
#        try:
#            indice = int(input("\nNúmero del alumno a modificar: ")) - 1
#            if 0 <= indice < len(datos):
#                alumno = datos[indice]
#                clave = input("Nombre de la característica (usa 'calificaciones' para agregar notas): ").lower().strip()
#                if clave == "calificaciones":
#                    nuevas_califs = input("Ingresa una o varias calificaciones separadas por comas: ").strip()
#                    try:
#                        nuevas = [float(x) for x in nuevas_califs.split(",") if x.strip() != ""]
#                        alumno.setdefault("calificaciones", []).extend(nuevas)
#                        print(f"Se agregaron {len(nuevas)} calificaciones.")
#                    except ValueError:
#                        print("Error: Solo números separados por comas.")
#                else:
#                    valor = input("Valor de la característica: ").strip()
#                    alumno[clave] = valor
#                    print("Característica agregada con éxito.")
#            else:
#                print("Índice inválido.")
#        except ValueError:
#            print("Debes ingresar un número válido.")
#    else:
#        print("No hay alumnos registrados.")
#    esperarTecla()

#def borrarCaracteristicaAlumno(datos):
#   borrarPantalla()
#    print("\n\t:: Borrar Característica o Calificación de un Alumno ::\n")
#    if datos:
#        mostrarAlumno(datos)
#        try:
#            indice = int(input("\nNúmero del alumno a modificar: ")) - 1
#            if 0 <= indice < len(datos):
#                alumno = datos[indice]
#                print("\nCaracterísticas disponibles:")
#                for clave in alumno.keys():
#                    print(f"- {clave}")
#                eliminar = input("Escribe la característica que deseas borrar: ").lower().strip()
#                if eliminar in alumno:
#                    if eliminar == "calificaciones" and isinstance(alumno[eliminar], list):
#                        if alumno[eliminar]:
#                            print("\nCalificaciones actuales:")
#                            for i, cal in enumerate(alumno[eliminar], start=1):
#                                print(f"{i}. {cal}")
#                            try:
#                                cal_elim = int(input("Número de la calificación a eliminar: ")) - 1
#                                if 0 <= cal_elim < len(alumno[eliminar]):
##                                    valor_elim = alumno[eliminar].pop(cal_elim)
 #                                   print(f"Calificación {valor_elim} eliminada.")
#                                else:
#                                    print("Número inválido.")
#                            except ValueError:
#                                print("Debes ingresar un número válido.")
#                        else:
#                            print("No hay calificaciones para eliminar.")
#                    else:
#                        del alumno[eliminar]
#                        print("Característica eliminada.")
#                else:
#                    print("Esa característica no existe.")
#            else:
#                print("Índice inválido.")
# #        except ValueError:
# #            print("Debes ingresar un número válido.")
# #    else:
# #        print("No hay alumnos registrados.")
#     esperarTecla()

# # def calcularCalificaciones(datos):
#     borrarPantalla()
#     print("\n\t:: Calcular Promedio de Calificaciones ::\n")
#     if datos:
#         mostrarAlumno(datos)
#         try:
#             indice = int(input("\nNúmero del alumno a calcular: ")) - 1
#             if 0 <= indice < len(datos):
#                 califs = datos[indice].get("calificaciones", [])
#                 if isinstance(califs, list) and califs:
#                     promedio = sum(califs) / len(califs)
#                     print(f"Promedio de {datos[indice]['nombre']}: {promedio:.2f}")
#                 else:
#                     print("No hay calificaciones para este alumno.")
#             else:
#                 print("Índice inválido.")
#         except ValueError:
#             print("Debes ingresar un número válido.")
#     else:
#         print("No hay alumnos registrados.")
#     esperarTecla()
# def buscarAlumno(datos):
#     borrarPantalla()
#     print("\n\t:: Buscar Alumno ::\n")
#     if datos:
#         termino = input("Ingresa el nombre o parte del nombre del alumno a buscar: ").strip().lower()
#         encontrados = [a for a in datos if termino in a["nombre"].lower()]
#         if encontrados:
#             for i, alumno in enumerate(encontrados, start=1):
#                 print(f"\nResultado {i}:")
#                 for clave, valor in alumno.items():
#                     if clave == "calificaciones" and isinstance(valor, list):
#                         print(f"  {clave.capitalize()}: {', '.join(map(str, valor)) if valor else 'No hay calificaciones'}")
#                     else:
#                         print(f"  {clave.capitalize()}: {valor}")
#         else:
#             print("No se encontró ningún alumno con ese nombre.")
#     else:
#         print("No hay alumnos registrados.")
#     esperarTecla()
