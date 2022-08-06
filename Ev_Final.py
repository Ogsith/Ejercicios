from random import randint

print("-----------------------------------------")
print("Seleccionar entre las opciones mostradas")
print("-----------------------------------------\n")
print("1) INGRESO DE NOTAS")
print("2) NOTA SUSTITUTORIA")
print("3) PREMIO DE AZAR\n")
print("-----------------------------------------\n")

opcion = input("Ingrese una de las opciones: ")

if opcion == "1":
    print("\n-----------------------------------------")
    print("Eligio la Opcion 1: Ingreso de notas")
    print("-----------------------------------------\n")
    curso = input("Ingrese un curso: ")
    nombre = input("Ingrese su nombre: ")
    cant_notas = int(input("Ingrese la cantidad de notas que desea registrar: "))

    cantidad_notas = 1
    suma = 0
    promedio = 0
    num_random = 0

    while cantidad_notas<cant_notas:
        nota = int(input("Ingrese una nota: "))
        if nota>=0 and nota<=20:
            suma += nota
            num_aleatorio = randint(0, 20)
            promedio = (suma + num_aleatorio)/ cant_notas

            cantidad_notas += 1
        else:
            print("Ha escrito una nota invalida. Escriba nuevamente su nota.")
    
    print("Alumno ",nombre, ", del curso de", curso , ". Su promedio total es ", round(promedio,2))

elif opcion == "2":

    peso1 = 0.04
    peso2 = 0.12
    peso3 = 0.24
    peso4 = 0.6

    print("\n-----------------------------------------")
    print("Eligio la Opcion 2: Nota sustitutoria")
    print("-----------------------------------------\n")
    notas = []
    curso = input("Ingrese el curso: ")
    for i in range(4):
        notas.append(randint(0,20))
    print("-----------------------------------------")
    print(f"Notas del curso: {curso}")
    print("-----------------------------------------\n")
    print("Evaluación Continua 1: ", notas[0],"--> Peso de 4%")
    print("Evaluación Continua 2: ", notas[1],"--> Peso de 12%")
    print("Evaluación Continua 3: ", notas[2],"--> Peso de 24%")
    print("Evaluación Final: ", notas[3],"     --> Peso de 60%")

    promedio = (notas[0]*peso1) + (notas[1]*peso2) + (notas[2]*peso3) + (notas[3]*peso4)
    print("-----------------------------------------")
    print(f"El promedio del curso de {curso} es: {round(promedio,2)}")
    print("-----------------------------------------\n")
    
    if notas[0] <= 10:
        notas[0]= int(input("Ingrese la nueva nota de EC1: "))
    if notas[1] <= 10:
        notas[1] = int(input("Ingrese la nueva nota de EC2: "))
    if notas[2] <= 10:
        notas[2] = int(input("Ingrese la nueva nota de EC3: "))
    if notas[3] <= 10:
        notas[3] = int(input("Ingrese la nueva nota de EF: "))

    print("-----------------------------------------")
    print(f"Notas del curso: {curso}")
    print("-----------------------------------------\n")
    print("Evaluación Continua 1: ", notas[0],"--> Peso de 4%")
    print("Evaluación Continua 2: ", notas[1],"--> Peso de 12%")
    print("Evaluación Continua 3: ", notas[2],"--> Peso de 24%")
    print("Evaluación Final: ", notas[3],"     --> Peso de 60%")

    npromedio = (notas[0]*peso1) + (notas[1]*peso2) + (notas[2]*peso3) + (notas[3]*peso4)
    print("-----------------------------------------")
    print(f"El nuevo promedio del curso de {curso} es: {round(npromedio,2)} ")
    print("-----------------------------------------\n")

elif opcion == "3":
    print("\n-----------------------------------------")
    print("Eligio la Opcion 3: Premio de Azar")
    print("-----------------------------------------\n")
    numeros=[]
    nombre_3=input("Ingrese su nombre: ")
    for i in range(7):
        numero=int(input("Ingrese un numero entre 30 y 50: "))
        while numero<30 or numero>50:
            numero=int(input("ERROR,Ingrese un numero entre 30 y 50: "))
        numeros.append(numero)

    aleatorios=[]
    for k in range(7):
        rando = randint(30,50)
        aleatorios.append(rando)
        
    print("")
    repetidos=[]
    for i in range(7):        
        N=0
        for j in range(7):
            if aleatorios[i]==numeros[j]:
                N=N+1
        if N>=1:
            print("El numero",aleatorios[i],"se repite")
            repetidos.append(aleatorios[i])

    if len(repetidos)>=3:
        estado="Aprobado"
    else:
        estado="Desaprobado"
            
    print("")
    print("Alumno",numeros)       
    print("TINKA",aleatorios)
    print("Repetidos",repetidos)
    print("Acertastes",len(repetidos),"entonces estas",estado)

