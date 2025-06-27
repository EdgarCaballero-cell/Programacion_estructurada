#Dict u objeto para almacenarr los atributos (nombre,categoria,clasificacion,genero,idioma) y sus varables

pelicula={
    "nombre:",
    "categoria:",
    "clasificacion:",
    "genero:",
    "nombre:",
}

pelicula={}

def borrarPantalla():
    
def esperarTecla():
    print("Preciona una tecla prra continuar ")
    input()
def crearPeliculas():
    borrarPantalla()
    print("\n\t Crear Peliculas \n")
    pelicula.update(input({"nombre":input("Ingresa el nombre")}).upper().strip())
    #pelicula["nombre"]=input("Ingresa el nombre").upper().strip()----------------------------------------------->otra forma de hacerlo 
    pelicula.update(input({"categoria":input("Ingresa el categoria")}).upper().strip())
    pelicula.update(input({"clasificacion":input("Ingresa el clsificacion")}).upper().strip())
    pelicula.update(input({"genero":input("Ingresa el genero")}).upper().strip())
    pelicula.update(input({"idioma":input("Ingresa el idioma")}).upper().strip())
    print("\n\t\t OPERACION REALIZADA CON EXITO")
def mostrarPeliculas():
    borrarPantalla()
    print("\n\t Mostar las caracteristicas de la Pelicula \n")
    if len(pelicula)>0:
        print(f"{(i)} : {pelicula}")
    else:
        print("NO hay peliculas en el sistema")
def borrarPelicula():
    borrarPantalla()
    print("\n\n\t Borrar todas las peliculas ")
    resp=input("Deseas borra TODAS LAS PELICULAS SISTEMA?SI/NO")
    if resp=="SI":
        pelicula.clear()
        print("\n\n LA OPERACION SE REALIZO CON EXITO")
def agregarCaracteristicasPelicula():
    borrarPantalla()
    print("Agregar Caracteristicas de la pelicula ")
    atributo=input("Ingresa la nueva caracteristica de la pelicula: ").lower().strip()
    valor=input("Ingresa el valor de las caracteristicas de la pelicula ").upper().strip()
    pelicula.update({atributo:input("Ingresa el nombre").upper().strip()})
    pelicula[atributo]=valor
    resp="si"
    print("LA OPERACION SE REALIZO CON EXITO")
def modificarCaracteristicasPelicula():
    borrarPantalla()
    print("Modificar Caracteristicas de la pelicula ")
    atributo=input("Ingresa la caracteristica que deseas modificar: ").lower().strip()
    if atributo in pelicula:
        valor=input("Ingresa el nuevo valor: ").upper().strip()
        pelicula[atributo]=valor
        print("LA OPERACION SE REALIZO CON EXITO")
    else:
        print("La caracteristica no existe en el sistema")
 
def borrarCaracteristicasPelicula():
    esperarTecla()
    print("BORRA caracteristicas de las peliculas:") 
    print("\n Los valores actuales: ") 
    
    if len(pelicula)>0:
        for i in pelicula:
            print(f"{i}")
        print("")
        opc=input(" ¿Desea borrar alguna de las caracteristica (Si/No)? ‣ ").lower().strip()
        if opc=="si": 
            atribu=input("A continuacion ingresa la caracteristica que desas bora  ").lower().strip()
            try:
                pelicula.pop(atribu)
                print("LA OPERACION SE REALIZO CON EXITO!!!")
            except KeyError:
                print("Caracteristica de pelicula no encontrada...")
        else:
            print("Operacion realizada")
    elif len(pelicula)<=0:
        print("Oprima cualquier tecla para continuar ")