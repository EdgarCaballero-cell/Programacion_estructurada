import calificaciones 

def main():
    opcion = True
    datos = []
    while opcion:
        calificaciones.borrarPantalla()
        seleccion = calificaciones.menuPrincipal()

        match seleccion:
            case "1":
                calificaciones.crearAlumno(datos)
                calificaciones.esperarTecla()

            case "2":
                calificaciones.eliminarAlumno(datos)
                calificaciones.esperarTecla()

            case "3":
                calificaciones.mostrarAlumno(datos)
                calificaciones.esperarTecla()
#
#            case "4":
#                calificaciones.agregarCaracteristicasAlumno(datos)
#                calificaciones.esperarTecla()
#
            case "5":
                calificaciones.calcularCalificaciones(datos)
                calificaciones.esperarTecla()
#
#            case "6":
#               calificaciones.borrarCaracteristicaAlumno(datos)
#                calificaciones.esperarTecla()

            case "7":
                opcion = False
                print("Terminaste la ejecución del programa.")

            case _:
                input("Opción inválida. Vuelve a intentarlo por favor...")

if __name__ == "__main__":
    main()
