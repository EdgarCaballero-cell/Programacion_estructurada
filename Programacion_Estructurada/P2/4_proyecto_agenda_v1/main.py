import agenda

def main():
    opcion = True
    datos = []
    while opcion:
        agenda.borrarPantalla()
        seleccion = agenda.menuPrincipal()

        match seleccion:
            case "1":
                agenda.agregar_contacto(datos)
                agenda.esperarTecla()

            case "2":
                agenda.buscar_contatosnombre(datos)
                agenda.esperarTecla()

            case "3":
                agenda.mostrar_contactos(datos)
                agenda.esperarTecla()
            case "5":
                agenda.eliminar_contacto(datos)
                agenda.esperarTecla()

#            case "4":
#                agenda.crearAlumno(datos)
#                agenda.esperarTecla()

                
#            case 
#            case "7":
#               opcion = False
#              print("Terminaste la ejecución del programa.")
#
            case _:
                input("Opción inválida. Vuelve a intentarlo por favor...")

if __name__ == "__main__":
    main()
