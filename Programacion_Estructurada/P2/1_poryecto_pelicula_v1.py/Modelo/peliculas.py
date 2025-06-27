peliculas=[]
def borrarPantalla():
    
def esperarTecla():
    print("Preciona una tecla prra continuar ")
    input()
def agregarPeliculas():
    borrarPantalla()
    print("\n\t Agregar Peliculas ")
    peliculas.append(input("Ingresar el nombre: ").upper().strip())
    print("\n\t\t OPERACION REALIZADA CON EXITO")
def consultarPeliculas():
    borrarPantalla()
    print("\n\t Consultar o Mostrar las paliculas ")
    
    if len(peliculas)>0:
        for i in range(0,len(peliculas)):
            print(f"\t {i+1}: {peliculas[i]}")
    else:
        print("\n\t No hay peliculas en el sistema ")
def vaciarPantalla():
def buscarPeliculas():
    borrarPantalla()
    print("\n\t Buscar pelicula ")
    pelicula_buscar=input("Ingresa el nombre de la pelicula ").upper().strip()
    encontro=0
    if not (pelicula_buscar in peliculas):
        print("\n\t NO se encontro la pelicula!!! ")
    else:
        for i in range(0,len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                print(f"\nLa pelicula {pelicula_buscar}si la tenemos y esta en la casilla {i+1}")
                encontro+=1
        print(f"Tenemos {encontro}pelicula(s)con este titulo")
        print("\n\t\t OPERACION REALIZADA CON EXITO")
def eliminarPeliculas():
    borrarPantalla()
    print("\n\t Borrar pelicula ")
    pelicula_buscar=input("Ingresa el nombre de la pelicula ").upper().strip()
    encontro=0
    if not (pelicula_buscar in peliculas):
        print("\n\t NO se encontro la pelicula!!! ")
    else:
        resp="si"
        while pelicula_buscar in peliculas and resp=="si":
            resp==("Deseas borra la pelicula del sistema ???(SI/NO)")
            if resp=="si":
                print(f"\n La pelicula que se borro es {pelicula_buscar} y estaba en la casilla {posicion+1}")
                peliculas.remove(pelicula_buscar)
                encontro+=1
                print("\n\t\t OPERACION REALIZADA CON EXITO")
                
        print(F"\n\t Se borro:{encontro} pelicula con el titulo  ")