"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
import os
os.system("clear")

paises={"Mexico","Brasil","España","Canada"}
print(paises)

#Funciones u operaciones 
for i in paises:
    print(i)

paises.add("México")
print(paises)

paises.pop()
print(paises)

paises.remove("México")
print(paises)


email=(input("Ingresa los email de los laumnos de la UTD: "))
lados={email}
print(lados)

input("Deseaes ingresar otro valorn???")

i="si"




datos = {} 
contador = 1  


while True:
    dato = input(f"Ingrese el dato {contador}: ")  
    datos[f"dato_{contador}"] = dato  
    
    continuar = input("¿Quieres ingresar otro dato? (s/n): ").strip().lower()
    if continuar != 's':
        break  
    
    contador += 1  # Incrementa el contador para la siguiente entrada

print("\nDatos almacenados:")
for clave, valor in datos.items():
    print(f"{clave}: {valor}")

#Ejemplo del maestro 