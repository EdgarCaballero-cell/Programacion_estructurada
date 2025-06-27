""""""""""import peliculas

opcion=True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Crear  \n 2.-  Borrar \n 3.- Mostrar \n 4.- Agregar Caracteristica  \n 5.- Modificar Caracteristica  \n 6.- Borrar Caracteristica   \n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.eliminarPeliculas()
            peliculas.esperarTecla()
            print(".:: Eliminar Peliculas ::.") 
            input("Oprima cualquier tecla para continuar ...") 
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
            print(".:: Modificar Peliculas ::.") 
            input("Oprima cualquier tecla para continuar ...")    
        case "4":
            peliculas.agregarCaracteristicaPeliculas() 
            peliculas.esperarTecla()
        case "5": 
            peliculas.modificarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "6": 
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion=False    
            print("Terminaste la ejecucion del SW")
        case _: 
            input("Opción invalida vuelva a intentarlo ... por favor")""""""""""
            
import peliculas
opcion=True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Crear  \n 2.-  Borrar \n 3.- Mostrar \n 4.- Agregar Caracteristica  \n 5.- Modificar Caracteristica  \n 6.- Borrar Caracteristica   \n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPelicula()
            peliculas.esperarTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.agregarCaracteristicasPelicula()
            peliculas.esperarTecla()
        case "5": 
            peliculas.modificarCaracteristicasPelicula()
            peliculas.esperarTecla()
        case "6": 
            peliculas.borrarCaracteristicasPelicula()
            peliculas.esperarTecla()
        case "7":
            opcion=False    
            print("Terminaste la ejecucion del SW")
        case _: 
            input("Opción invalida vuelva a intentarlo ... por favor")
