from math import acos, tan, cos, sin, pi
print("//////////////////////////////-UTEC-BMI-//////////////////////////////")
altura = float(input("ingrese altura (metros): "))
peso = float(input("ingrese  peso (kilogramos): "))

BMI = peso / (altura**2)
print("el indice de masa corporal es: ", BMI)

print("//////////////////////////////-UTEC-WCI-//////////////////////////////")
T = float(input("temperatura (centigrados) Max=10: "))
V = float(input("velocidad (km/h) Min=4.8: "))

WCI = 13.12 + (0.6215 * T) - (11.37 * (V **0.16)) + (0.3965 * T * (V **0.16))

print("la percepcion de frio es: ", WCI)

print("//////////////////////////////-UTEC-verificacion de triangulo-//////////////////////////////")
s1 = float(input("ingrese primer lado: "))
s2 = float(input("ingrese segundo lado: "))
s3 = float(input("ingrese tercer lado: "))

if (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
	print("es triangulo valido")
else:
	print("no es triangulo")

print("//////////////////////////////-UTEC-Area de un triangulo-///////////////////////////////")
base = float(input("ingrese base: "))
altura = float(input("ingrese altura: "))

area = (base * altura) / 2
print("el area de un triangulo es: ", area)

print("//////////////////////////////-UTEC-Invertir numero-//////////////////////////////")
numero = int(input("ingrese un numero entero de 5 digitos: "))
resultado = 0
resultado = resultado * 10
resultado += numero % 10
numero = numero // 10
resultado = resultado * 10 
resultado += numero % 10 
numero = numero // 10
resultado = resultado * 10 
resultado += numero % 10 
numero = numero // 10
resultado = resultado * 10 
resultado += numero % 10 
numero = numero // 10
resultado = resultado * 10 
resultado += numero % 10 
numero = numero // 10

print(resultado)

print("//////////////////////////////-UTEC-Area de un poligono regular-//////////////////////////////")
s = float(input("ingrese la longuitud de lado: "))
n = int(input("ingrese numero de lados: "))

area = (n * s**2)/(4 * tan(pi/n))
print(area)

print("//////////////////////////////-UTEC-Distancia entre dos puntos-//////////////////////////////")
print("ingrese el punto 1")
t1 = float(input("ingrese la latitud 1: "))
g1 = float(input("ingrese la longitud 1: "))
print("ingrese el punto 2")
t2 = float(input("ingrese la latitud 2: "))
g2 = float(input("ingrese la longitud 2: "))

distancia = 6317.01*acos(sin(pi*t1/180)*sin(pi*t2/180) + cos(pi*t1/180)*cos(pi*t2/180)*cos(pi*(g1-g2)/180))

distancia = int(distancia*10**2)/10**2
print("la distancia entre punto 1 y punto 2 es: ", distancia)

