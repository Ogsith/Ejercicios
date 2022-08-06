lnombre = []
i = 1
veces_nombre = int(input("Ingrese el número de veces que va a escribir un nombre: "))
while i<=veces_nombre:
    nombre = input(f"Ingrese el {i} nombre: ")
    lnombre.append(nombre)
    i+=1
    
    lnotas = []
    suma = 0
    print("--------------------------------------\n")
    veces_notas = int(input("Ingrese el numero de veces que pondra una nota para sacar el promedio: "))
    print("--------------------------------------\n")
    for j in range(veces_notas):
        notas = int(input(f"Ingrese la nota : "))
        while notas<0 or notas>20:
            #suma = suma + lnotas[j]
            notas = int(input("Ingrese nuevamente una nota correspondiente: "))
        lnotas.append(notas)
        suma = suma + lnotas[j]
    
    print("--------------------------------------\n")
    print(f"Las notas de {nombre} son {lnotas}\n")
    promedio =  suma /len(lnotas)
    print(f"El promedio de {nombre} es {round(promedio,1)}") 
    print("--------------------------------------\n")

print("NOMBRES")
print("\n" .join(lnombre))
print("--------------------------------------")
print("NOTAS")
print("\n".join(map(str,lnotas)))

print("             -GRACIAS-             \n")
