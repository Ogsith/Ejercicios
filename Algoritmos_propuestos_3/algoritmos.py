from random import randint
import os
import time

print(" _________________________________________________")
print(" |      Integrantes del Grupo       |    Código  |")
print(" |__________________________________|____________|")
print(" |Anthony Gianpierre Terrazas Tello | PT77091210 |")
print(" |Jose Luis Bautista Trujillo       | PT75087473 |")
print(" |Fabrizio Alonso Solis López       | PT72674443 |")
print(" |Luis Angel Barboza Giraldo        | PT72935564 |")
print(" |Luis Neyra Huisa                  | PT72387290 |") 
print(" -------------------------------------------------\n")

print("                       - PROBLEMA 01 -                      ") 
print(".......................Teclado a Ascci......................\n")

N_veces = int(input("Ingrese la cantidad de veces que ingresara una tecla: "))
ascii(N_veces)
for i in range(1, N_veces+1):
    print("-------------------------------------------------------\n")
    tecla = input(f"Ingrese la tecla {i}: ")
    x = ord(tecla)
    print(f"La tecla {tecla} presionada en ascii es ---> {x}")
print("-------------------------------------------------------")
print("                 -Gracias, Vuelva pronto-\n")

print("                       - PROBLEMA 02 -                      ")
print(".......................Op. Aritméticas......................\n")

n1 = 1
n2 = 1

suma = 0
resta = 0
multiplicacion = 0
division = 0

while n1!=0 and n2!=0:
    print("------------------------------------------")
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))

    if n1!=0 and n2!=0:    
        suma = suma + (n1 + n2)
        resta = resta + (n1 - n2)
        multiplicacion = multiplicacion + (n1 * n2)
        division = division + (n1 / n2)
   
    else:
        suma = suma + (n1 + n2)
        resta = resta + (n1 - n2)
        multiplicacion = multiplicacion + (n1 * n2)
        print("\nRecuerde que no se puede dividir por 0")
        
print("------------------------------------------")
print(f"La Suma de los numeros es ==> {suma}")
print(f"La Resta de los numeros es ==> {resta}")
print(f"La Multiplicación de los numeros es ==> {multiplicacion}")
print(f"La División de los numeros es ==> {round(division,2)}")
print("------------------------------------------")
print("         -Gracias, Vuelva pronto-\n")

print("                       - PROBLEMA 03 -                      ")
print(".....................N Primeros Terminos....................\n")

N = int(input("Ingrese N final de los términos: "))
print("---------------------------------------")
print("Los N primeros términos son:\n")
contador = 0
i = 5
while i<N:
    print(i, end=", ")
    contador +=1
    i += 1 + contador
print("...")
print("\nFin de la serie.")
print("---------------------------------------")
print("          -Gracias, Vuelva pronto-\n")

print("                       - PROBLEMA 04 -                      ")
print("......................Promedio de Notas.....................\n")

L_Nombre=[]
for i in range(1):
    Nombre = input("Ingrese el nombre del alumno: ")
    L_Nombre.append(Nombre)
    
    L_Notas=[]
    suma = 0
    print("-------------------------------------------------")
    print("Ingrese 10 notas para sacar el promedio del Curso")
    print("-------------------------------------------------")
    for j in range(10):
        Notas = int(input("Ingrese la nota: "))
        while Notas<0 or Notas>20:
            Notas = int(input("Ingrese nuevamente una nota correspondiente: "))
        L_Notas.append(Notas)
        suma = suma + L_Notas[j]

    print("-------------------------------------------------")
    promedio = suma /len(L_Notas)
    print(f"EL promedio de {Nombre} es {round(promedio,1)}")
    print("-------------------------------------------------")
print("              -Gracias, Vuelva pronto-\n")

print("                       - PROBLEMA 05 -                      ")
print("........................Tipo de Dato........................\n")

lista = []

cadena = input("Ingrese el dato: ")
print("----------------------------------")
for i in cadena:
    lista.append(i)
print(lista)

if "." in lista:
    print("\nEs un tipo de dato Real")
elif ("a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "ñ" or "o" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z") in lista:
    print("\nEs un tipo de dato alfanumerico")
else:
    print("\nEs un tipo de dato entero")

print("----------------------------------")
print("     -Gracias, vuelva pronto-\n")

print("                       - PROBLEMA 06 -                      ")
print(".........................Reembolso..........................\n")

NumUsuarios = int(input("Ingrese número de usuarios: "))
Tasa = float(input("Ingrese tasa de interes anual: "))

Usuario = 1
for i in range(Usuario, NumUsuarios+1):
    print("-------------------------------------\n")
    Codigo = input("Código: ")
    Prestamo = int(input("Prestamo: "))
    Cantidad_A = int(input("Cantidad de Años: "))

    Tasa = Tasa / 100
    #Calcular potencia
    Base = 1 + Tasa
    Potencia = 1
    contador = 1
    for j in range(contador,Cantidad_A+1):
        Potencia = pow(Base,Cantidad_A)
    #Calcular Factor de Reembolso
    FactorReemb = Tasa * Potencia / (Potencia-1)
    #Calcular reembolso
    Reembolso = Prestamo * FactorReemb
    #Escribir Resultado
    print("-------------------------------------")
    print(f"Reembolso: {round(Reembolso, 1)}")
print("-------------------------------------")
print("         -Gracias, Vuelva pronto-\n")

print("                       - PROBLEMA 07 -                      ")
print("........................Nota Aleatoria......................\n")

d={}
h={}

def generar_notas(m=1):
    l=[]
    for i in range(m):
        a=randint(0,20)
        l.append(a)
    return l

print("Ingrese 15 Nombres para cada alumno")
print("-----------------------------------\n")
for i in range(1,16):
    a=input(f"Nombre del alumno {i}: ")
    d[a]=generar_notas()
    h[a]=d[a]

e={}
f=[]

for i in d:
    a=d[i]
    def sumalista(a,b=len(a)-1):
        if b == 0:
            return a[0]
        else:
            return a[b] + sumalista(a,b-1)   
    e[i]=sumalista(a)/1
    f.append(sumalista(a)/1)

print("-----------------------------------\n")
print("Alumno aprobados: ")
for i in d:
    if (sumalista(d[i])/1)<11:
        del h[i]
print(h)

print("-----------------------------------\n")
for i in e:
    if e[i]==max(f):
        print("{} obtuvo una nota mayor".format(i))
for i in e:
    if e[i]==min(f):
        print("{} obtuvo una nota menor".format(i))
print("-----------------------------------")
print("             -Gracias, Vuelva pronto-\n")

print("                       - PROBLEMA 08 -                      ")
print("......................Mensaje por linea.....................\n")

n = int(input("Intoduce numero de filas y columnas: "))
print("---------------------------------------")

matriz = []
for i in range(n):
    matriz.append([])
    for j in range(n):
        valor = input("Fila {}, Columna {}: ". format(i+1, j+1))
        matriz[i].append(valor)
print("---------------------------------------")
for n in matriz:
    for elemento in n:
        print("{}".format(elemento))
print("---------------------------------------")
print("         -Gracias, Vuelva pronto-\n")

print("                       - PROBLEMA 09 -                      ")
print(".....................N p. terminos Suma.....................\n")

Nterminos = int(input("Ingrese el número final de Nterminos para determinar la suma: "))
suma = 0
print("------------------------------------------")

for i in range(7, Nterminos, 3):
    print(i,end=", ")
    suma = suma + i

print("...")
print("------------------------------------------")
print(f"La suma de los {Nterminos} primeros términos es {suma}")
print("------------------------------------------")
print("         -Gracias, Vuelva pronto-\n")

print("                       - PROBLEMA 10 -                      ")
print("........................Elecciones..........................\n")

def elecciones():
 votos_sí = 0
 votos_no = 0
 votos_otros = 0
 
 distritos = 42
 total = 0
 ganador = ""
 
 while distritos != "0":
  os.system("cls")
  print ("SISTEMA DE ELECCIONES")
  print ("")
  print ("Seleccione su votación, para salir digite 0")
  print ("")
  print ("1)Sí")
  print ("2)No")
  print ("3)Otros")
  print ("")
  distritos = input ("Su elección es : ")
  print ("")
  if distritos == "1" or distritos == "2" or distritos == "3":
   total += 1
  
  
  if distritos != "0" and distritos != "1" and distritos != "2" and distritos != "3":
   print ("Opcion no valida, intete de nuevo...")
   time.sleep(3)
  elif distritos == "1":
   votos_sí += 1
  elif distritos == "2":
   votos_no += 1
  elif distritos == "3":
   votos_otros += 1

 
 if total == 0:
  print ("No hubieron votos...")
  print ("")
  time.sleep(2)
  return 0
 else:
  porcen_sí = float(100 * votos_sí) / float (total)
  porcen_no = float(100 * votos_no) / float (total)
  porcen_otros = float(100 * votos_otros) / float (total)
  
  if votos_sí > votos_no and votos_sí > votos_otros:
   ganador = "El ganador fue Sí"  
  elif votos_no > votos_sí and votos_no > votos_otros:
   ganador = "El ganador fue No"
  elif votos_otros > votos_sí and votos_otros > votos_no:
   ganador = "El ganador fue Otros"
  elif votos_otros == votos_sí and votos_otros == votos_no:
   ganador = "Hubo un triple empate"
  elif votos_sí == votos_no and votos_sí > votos_otros:
   ganador = "Hubo un doble empate entre Sí  y No"
  elif votos_no == votos_otros and votos_no > votos_sí:
   ganador = "Hubo un doble empate entre No y Otros "
  elif votos_otros == votos_sí and votos_otros > votos_no:
   ganador = "Hubo un doble empate entre Otros y Sí"
 
 print ("Cantidad de votos: ", total)
 print ("")
 print ("Cantidad de votos para Sí: ", votos_sí, "--> %.2f" % porcen_sí + "%")
 print ("")
 print ("Cantidad de votos para No: ", votos_no, "--> %.2f" % porcen_no + "%")
 print ("")
 print ("Cantidad de votos para Otros ", votos_otros, "--> %.2f" % porcen_otros + "%")
 print ("")
 print (ganador)
 print ("--------------------------------------")
 print("        -Gracias, Vuelva pronto-\n")
 
elecciones()

