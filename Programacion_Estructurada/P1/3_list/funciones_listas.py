"""List(Array)
son colecciones o conjunto de datos/valores bajo un mismo 
nombre, para acceder a los valores se hace con un indice numerico

NOTA: sus  valores si son modificables 

La listas es una colección ordenada y modificable. Percmite miembros
duplicados """

import os
os.system("clear")

#Funciones mas comunes en las listas 

pais= ["Mexicó", "Brasil","España","Canada"]

numero=[23,12,100,34]

varios=["Hola",True,33,3.12] #En un arreglo no se puede diferentes tipos de dato y unna lista SI 



#Ordenar las listas 
print(numero)
print(pais)
print(varios)


#Los ordenamos 
numero.sort()
print(numero)

pais.sort()
print(pais)


#Agregar un elemento a lista (se pude repetir cosas )
#!.
print(pais)
pais.append("Honduras")
print(pais) 

print(pais)
pais.append("Honduras")
print(pais)

#2. Forma (Inserta de manera especifica)
pais.insert(1,"Honduras ")
print(pais)

#Eliminar un elemento 
#.1 Forma 
pais.sort()
print(pais)

pais.pop(4)#EN LA POSICION NUMERO 4 
print(pais)

#2.Forma 
pais.remove("Honduras")
print(pais)

#BUSCAR UN ELENTO DENTRO DE UNA LISTA
#pais= ["Mexicó", "Brasil","España","Canada"]

print("Brasil" in pais)


#CONTAR EL NUMERO DE QUE UN ELEMENTO QUE AHY EN UNA LISTA 

print(numero)
print(numero.count(12))
numero.insert(1,12)
print(numero)
print(numero.count(12))


#DARLE LA VUELTA A LAS LISTAS 

print(pais)
print(numero)
pais.reverse()
numero.reverse() 
print(pais)
print(numero)


#CONOCER EL INDECE O LA POSICION DE UN VALOR DE LA LISTA 

posicion=pais.index("España")
print(posicion)
#pais[posicion]="ESPAÑA"
#print(pais)

#UNIR EL CONTENIDO DE 2 O MAS LISTAS 
numero=[23,12,100,34]
numero2=[300,400,500]

print(numero)
print(numero2)
numero.extend(numero2)
print(numero)

numero=[23,12,100,34]
numero.extend(pais)
print(numero)