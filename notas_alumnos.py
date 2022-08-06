#INGRESAR UNA CANTIDAD n DE ALUMNOS Y 3 NOTAS, PARA LUEGO PROMEDIARLAS
#Y FINALMENTE MOSTRAR CADA ALUMNO Y SU PROMEDIO. ADEMAS UN MENSAJE QUE INDIQUE
#SI EL ALUMNO APROBÒ EL CURSO (>13 ES NOTA APROBATORIA)
#MUESTE A CADA ALUMNO EN UNA FILA CON SUS RESPECTIVOS DATOS MENCIONADOS

print("ARREGLO BIDIMENSIONAL DE DATOS MIXTOS")
filas=int(input("Ingrese la cantidad de alumno a registrar : "))
columnas=4
print()
print("Ahora por favor ingrese ordenadamente como se le indica :")
bidimensional=[] #lista vacia
for i in range(filas):
    unidimensional=[] #lista vacia
    for j in range(columnas):
        if j==0:
           texto=input(f"Ingrese el nombre del Alumno : {i+1} --> ")
        else:
            texto=float(input(f"Ingrese al Alumno : {i+1} su nota {j} --> "))
        unidimensional.append(texto)
        
    bidimensional.append(unidimensional)

for i in range(filas):
    suma=0
    promedio=0
    for j in range(columnas):
        if(j!=0):
            suma=suma+bidimensional[i][j]
    promedio=suma/3
    if (promedio>=13):
        print("El alumno ",bidimensional[i][0]," tiene de promedio: ",promedio," y esta APROBADO")
    else:
        print("El alumno ",bidimensional[i][0]," tiene de promedio: ",promedio," y esta DESAPROBADO")
        
input("Presione enter para salir")








