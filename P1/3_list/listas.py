

#EJEMPLO 1. Crear una lista de numeros e imprimir el contenido
mylist=[100,200,300,400]

#1.IMPRIMIR A TRABES DEL PRINT
print(mylist)


#2.IMPRIMIR LISTA POR UN CICLO
for i in mylist:
    print(i)
    
#3.DE MANERA INDICE 
for i in range(0,len(mylist)):
    print(mylist[i])
    
    
    
    
    
    
#EJEMPLO 2.Crear una lista de palabras  y posteriormente buscar la posicion 
palabras=["Hola","Cuatro", "Carro"]
print(palabras)
print("Cuatro " in palabras)

#1.Formaa 

palabras=["Hola","Cuatro", "Carro"] 
palabra_buscar=input("Dame la palabra buscar")
if palabra_buscar in palabras:
    print("Se encontro en la lista")
else:
    print("No se encontr la palabra")

#2.Forma 
encontro=False
for i in palabras:
    if i== palabra_buscar:
        encontro=True

if encontro:
    print("SI se encontro ")
else:
    print("NO se encontro")

#3. Forma 

encontro=False
for i in range(0,len(mylist)):
    if mylist[i]== palabra_buscar:
        encontro=True

if encontro:
    print("SI se encontro ")
else:
    print("NO se encontro")


#EJEMPLO 3. aAlladir elementos a una lista
numeros=[]
opc="si"
while opc=="si":
    numero=float(input("Dame un numero: "))
    numeros.append(numero)
    opc=input("Deseas uncluir otro numero").lower()
print(numeros)


#Forma3
numeros=[]
opc="si"
while opc=="si":
    numeros.append(float(input("Dame un numero: ")))
    opc=input("Deseas uncluir otro numero").lower()
print(numeros)


#Ejemplo4. Crear una lista multidimencional (matriz) que almacene el mombre y numero de 4 personas 


agenda=[
    ["Carlos","123123123"],
    ["Alberto","123123123"],
    ["Martin","123123213213"]
]

print(agenda)
va=""
for r in range(0,2):
    for c in range(0,2):
        val+=f"{agenda[r][c]}"
    val+="\n"
print=(val)











