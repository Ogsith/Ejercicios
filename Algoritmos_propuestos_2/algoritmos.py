import time

print(" _________________________________________________")
print(" |      Integrantes del Grupo       |    Código  |")
print(" |__________________________________|____________|")       
print(" |Anthony Gianpierre Terrazas Tello | PT77091210 |")
print(" |Jose Luis Bautista Trujillo       | PT75087473 |")
print(" |Fabrizio Alonso Solis López       | PT72674443 |")
print(" |Luis Angel Barboza Giraldo        | PT72935564 |")      
print(" -------------------------------------------------")

print("\n                         - PROBLEMA 01 -                      ") 
print(".......................Dia Correspondiente......................\n")

dia = {0:"Domingo", 1:"Lunes", 2:"Martes", 3:"Miércoles", 4:"Jueves", 5:"Viernes", 6:"Sábado"}

numero = int(input("Ingrese un número: ")) 

if numero in dia:
    print(f"El dia correspondiente de {numero} es {dia[numero]}")
else:
    print(f"El numero {numero} ingresado no corresponde a ningun dia de la semana")
print("                  -Gracias, vuelva pronto-                \n")

print("                         - PROBLEMA 02 -                      ") 
print(".....................Puntaje Correspondiente....................\n")

puntaje = int(input("Ingrese su puntaje original: "))
factor = [0,6,9,10]

if puntaje ==0:
    puntajec= puntaje*factor[0]
    print(f"El puntaje que le corresponde es {puntajec}")
elif puntaje>=1 and puntaje<=5:
    puntajec= puntaje*factor[1]
    print(f"El puntaje que le corresponde es {puntajec}")
elif puntaje>=6 and puntaje<=8:
    puntajec= puntaje*factor[2]
    print(f"El puntaje que le corresponde es {puntajec}")
elif puntaje>=9 and puntaje<=10:
    puntajec= puntaje*factor[3]
    print(f"El puntaje que le corresponde es {puntajec}")
else:
    print("El valor digitado no se encuentra en el rango de esta opecaión")

print("                 -Gracias, vuelva pronto-                 \n")

print("                         - PROBLEMA 03 -                      ") 
print("..........................Tienda de Ropa........................\n")

P_compra = 0.13

nacionalidad=input("Ingrese 1 o 2 según su nación: ")

if nacionalidad == "1":
    talla = str(input("Digite una talla, ya sea Niño, Joven o Adulto: "))
    if talla == "Niño":

        sexo = str(input("Ingrese el sexo H o M: "))
        if sexo == "H":
            precio = 50
            C_productos = int(input("Ingrese la cantidad de los productos a comprar: "))
            Import_dscto = precio * (0.05*C_productos)
            Import_compra = (precio - Import_dscto) * P_compra
            Import_pagar = precio - Import_dscto + Import_compra

        elif sexo == "M":
            precio = 40
            C_productos = int(input("Ingrese la cantidad de los productos a comprar: "))
            Import_dscto = precio * (0.04*C_productos)
            Import_compra = (precio - Import_dscto) * P_compra
            Import_pagar = precio - Import_dscto + Import_compra

    elif talla == "Joven":

        sexo = str(input("Ingrese el sexo H o M: "))
        if sexo == "H":
            precio = 70
            C_productos = int(input("Ingrese la cantidad de los productos a comprar: "))
            Import_dscto = precio * (0.07*C_productos)
            Import_compra = (precio - Import_dscto) * P_compra
            Import_pagar = precio - Import_dscto + Import_compra

        elif sexo == "M":
            precio = 60
            C_productos = int(input("Ingrese la cantidad de los productos a comprar: "))
            Import_dscto = precio * (0.09*C_productos)
            Import_compra = (precio - Import_dscto) * P_compra
            Import_pagar = precio - Import_dscto + Import_compra

    elif talla == "Adulto":

        sexo=str(input("Ingrese el sexo H o M: "))
        if sexo == "H":
            precio = 90
            C_productos = int(input("Ingrese la cantidad de los productos a comprar: "))
            Import_dscto = precio * (0.10*C_productos)
            Import_compra = (precio - Import_dscto) * P_compra
            Import_pagar = precio - Import_dscto + Import_compra

        elif sexo == "M":
            precio = 80
            C_productos = int(input("Ingrese la cantidad de los productos a comprar: "))
            Import_dscto = precio * (0.12*C_productos)
            Import_compra = (precio - Import_dscto) * P_compra
            Import_pagar = precio - Import_dscto + Import_compra

if nacionalidad == "2" :
    talla = str(input("Digite una talla, ya sea Niño, Joven o Adulto: "))
    if talla == "Niño":

        sexo = str(input("Ingrese el sexo H o M: "))
        if sexo == "H":
            precio = 60
            C_productos = int(input("Ingrese la cantidad de los productos a comprar: "))
            Import_dscto = precio * (0.04*C_productos)
            Import_compra = (precio - Import_dscto) * P_compra
            Import_pagar = precio - Import_dscto + Import_compra

        elif sexo == "M":
            precio = 50
            C_productos = int(input("Ingrese la cantidad de los productos a comprar: "))
            Import_dscto = precio * (0.05*C_productos)
            Import_compra = (precio - Import_dscto) * P_compra
            Import_pagar = precio - Import_dscto + Import_compra

    elif talla == "Joven":

        sexo = str(input("Ingrese el sexo H o M: "))
        if sexo == "H":
            precio = 80
            C_productos = int(input("Ingrese la cantidad de los productos a comprar: "))
            Import_dscto = precio * (0.09*C_productos)
            Import_compra = (precio - Import_dscto) * P_compra
            Import_pagar = precio - Import_dscto + Import_compra

        elif sexo == "M":
            precio = 70
            C_productos = int(input("Ingrese la cantidad de los productos a comprar: "))
            Import_dscto = precio * (0.07*C_productos)
            Import_compra = (precio - Import_dscto) * P_compra
            Import_pagar = precio - Import_dscto + Import_compra

    elif talla == "Adulto":

        sexo=str(input("Ingrese el sexo H o M: "))
        if sexo == "H":
            precio = 100
            C_productos = int(input("Ingrese la cantidad de los productos a comprar: "))
            Import_dscto = precio * (0.12*C_productos)
            Import_compra = (precio - Import_dscto) * P_compra
            Import_pagar = precio - Import_dscto + Import_compra

        elif sexo == "M":
            precio = 90
            C_productos = int(input("Ingrese la cantidad de los productos a comprar: "))
            Import_dscto = precio * (0.10*C_productos)
            Import_compra = (precio - Import_dscto) * P_compra
            Import_pagar = precio - Import_dscto + Import_compra

persona = str(input("Ingrese el nombre del comprador: "))
input("Precione ENTER para terminar con la compra\n")

print("Procesando...")
time.sleep(3)

print("\n----------------------------------------------------------")
print(f"Nombre del Comprador             ---> {persona}")
print(f"Cantidad de Producotos Comprados ---> {C_productos}")
print(f"Importe Comprado                 ---> {int(Import_compra)}")
print("-----------------------------------------------------------")
print(f"Importe a Pagar                  ---> {int(Import_pagar)}\n")
print("                   -Gracias, vuelva pronto-               \n")

print("                         - PROBLEMA 04 -                      ") 
print(".........................Rango de Valores.......................\n")

print("\nTipos de Datos a eleguir:")
print("-------------------------")
print("- ShortInt")
print("- Byte") 
print("- Interger")
print("- Word")
print("- LongInt")
print("-------------------------\n")

tipo_dato = str(input("Ingrese la letra inicial en mayuscula o minuscula: "))

if tipo_dato =="S" or tipo_dato =="s":
    for i in range(-128, 128):
        print(i,end=" ",)
elif tipo_dato =="B" or tipo_dato =="b":
    for j in range(0,256):
        print(j,end=" ")
elif tipo_dato =="I" or tipo_dato =="i":
    for k in range(-32768, 32768):
        print(k, end=" ")
elif tipo_dato =="W" or tipo_dato =="w":
    for l in range(0, 65536):
        print(l,end=" ")
elif tipo_dato =="L" or tipo_dato =="l":
    for m in range(-2147483648, 2147483648):
        print(m,end=" ")
else:
    print("La letra que digito no es una inicial del tipo de dato")
    
print("\n                         -Gracias, vuelva pronto-      \n")

print("                         - PROBLEMA 05 -                      ") 
print("........................Arabico a Romano........................\n")

numero = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
romano = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

while True:
    n = int(input("Ingrese un número mayor a 0 y menor a 4000: ")) 
    if n<1 or n>3999:
        print("El numero no debe ser menor a 1 o mayor a 3999, vuelva a colocar un numero valido")
        break
    inicio=0
    res =""
    while n>0 and n<4000:
        div= n//numero[inicio]
        n %= numero[inicio]
        while div:
            res += romano[inicio]
            div -=1
        inicio +=1
    print(f"El número ingresado en número romano es {res}")
    break
print("                 -Gracias, vuelva pronto-                 \n")

print("                         - PROBLEMA 06 -                      ") 
print(".......................Distancia Recorrida......................\n")

veloc1 = int(input("Ingrese la velocidad del auto que parte de Lima: ")) #veloc1 = 120
veloc2 = int(input("Ingrese la velocidad del auto que parte de Huacho: ")) #veloc2 = 66
recorrido = int(input("Ingrese la distancia entre Lima y Trujillo: ")) #recorrido = 570
interv = 1
#Inicializar elementos
dist1 = 0
dist2 = 130
tiempo = 0

print("\nDISTANCIAS RECORRIDAS RUTA: LIMA - TRUJILLO\n")
print("MINUTOS\t\tde LIMA\t\tde HUACHO")
while (dist1 <= dist2):
    tiempo += interv/60
    dist1 += veloc1 * tiempo
    dist2 += veloc2 * tiempo
    
    print(f"  {round(tiempo*60,1)}\t\t  {dist1}\t\t  {round(dist2,1)}")
print("El de Lima paso a de Huacho!!!")
print("                    -Gracias, vuelva pronto-             \n ")

print("                         - PROBLEMA 07 -                      ") 
print(".......................Velocidad Promedio.......................\n")

distancia = int(input("Ingrese distancia en Km: "))
Nveces = int(input("Ingrese número de veces: "))

suma =0
contador =1

print("---------------------------------------\n")
while contador <= Nveces:
    tiempo = int(input(f"Ingresar el tiempo  {contador} en horas: "))
    suma += tiempo
    contador += 1 
Vpromedio = (distancia * Nveces)/suma
print("---------------------------------------")
print(f"Velocidad promedio en Km/hr: {round(Vpromedio,2)}")
print("                     -Gracias, vuelva pronto-             \n")

print("                         - PROBLEMA 08 -                      ") 
print("......................N Primeros Terminos.......................\n")

NumTerm = int(input("Ingrese el número de terminos menores que 15: "))
x = int(input("Ingrese valor de x: "))

suma = 0
contador = 1
numerador = 1
denominador = 1

print("-------------------------------------------\n")
print("Termino  Numerador  Denominador  Resultado")
print("-------------------------------------------")

while (contador<=NumTerm) and (NumTerm<=15):
    resultado = (numerador/denominador)
    suma += resultado
    print(f"   {contador}\t     {numerador}\t\t {denominador}\t    {resultado}")
    numerador = numerador *(x*(+1))
    denominador = denominador *2
    contador = contador + 1
print("--------------------------------------------")
print(f"La suma de los {NumTerm} primeros terminos es: {suma}\n")
print("                     -Gracias, vuelva pronto-             \n")

print("                         - PROBLEMA 09 -                      ") 
print("......................Productos de Farmacia.....................\n")

stockGN = 0
stockGI = 0
stockRN = 0
stockRI = 0
stockPN = 0
stockPI = 0
stockTN = 0
stockTI = 0

fin = False

while not fin:
    procedencia = str(input("Ingresar la procedencia, ENTER para terminar, N o I para continuar: "))
    if procedencia == "":
        fin = True
    elif procedencia !="N" and procedencia !="I":
        print("\n\tPor favor ingrese nuevamente el dato correcto\n")
    elif procedencia =="N" or procedencia == "I":
        tipo_pr = str(input("Ingresar el tipo de producto, G o R o T o P: "))
        tipo_op = str(input("Ingresar el tipo de operación, E o S: "))
        cantidad = int(input("Ingrese la cantidad: "))

        if tipo_pr =="G":
            if procedencia == "N":
                if tipo_op =="E":
                    stockGN = stockGN + cantidad

                elif tipo_op =="S":
                    stockGN = stockGN - cantidad

            elif procedencia == "I":
                if tipo_op == "E":
                    stockGI = stockGI + cantidad

                elif tipo_op =="S":
                    stockGI = stockGI - cantidad

        elif tipo_pr =="R":
            if procedencia == "N":
                if tipo_op =="E":
                    stockRN = stockRN + cantidad

                elif tipo_op =="S":
                    stockRN = stockRN - cantidad

            elif procedencia == "I":
                if tipo_op == "E":
                    stockRI = stockRI + cantidad

                elif tipo_op =="S":
                    stockRI = stockRI - cantidad

        elif tipo_pr =="P":
            if procedencia == "N":
                if tipo_op =="E":
                    stockPN = stockPN + cantidad

                elif tipo_op =="S":
                    stockPN = stockPN - cantidad

            elif procedencia == "I":
                if tipo_op == "E":
                    stockPI = stockPI + cantidad

                elif tipo_op =="S":
                    stockPI = stockPI - cantidad

        elif tipo_pr =="T":
            if procedencia == "N":
                if tipo_op =="E":
                    stockTN = stockTN + cantidad

                elif tipo_op =="S":
                    stockTN = stockTN - cantidad

            elif procedencia == "I":
                if tipo_op == "E":
                    stockTI = stockTI + cantidad

                elif tipo_op =="S":
                    stockTI = stockTI - cantidad

print("\n----------------------------------------")
print("PRODUCTO\tPROCEDENCIA\tSTOCK")
print("----------------------------------------\n")
print(f"Analgésicos\tNacional\t{stockGN}")
print(f"Analgésicos\tImportado\t{stockGI}")

print(f"Antibióticos\tNacional\t{stockRN}")
print(f"Antibióticos\tImportado\t{stockRN}")

print(f"Antipiréticos\tNacional\t{stockPN}")
print(f"Antipiréticos\tImportado\t{stockPN}")

print(f"Otros\t\tNacional\t{stockTN}")
print(f"Otros\t\tImportado\t{stockTN}")
print("\n                  -Gracias, vuelva pronto-              \n")

print("                         - PROBLEMA 10 -                      ") 
print("......................Codificación secreta......................\n")

class CustomMessage():
#Clase para el menejo de mensajes.

    LETTER_BY_NUMBERS = {"A": "b","B": "c","C": "d","D": "e","E": "f","F": "g","G": "h","H": "i","I": "j","J": "k","K": "l","L": "m","M": "n","N": "ñ","Ñ": "o","O": "p","P": "q","Q": "r","R": "s","S": "t","T": "u","U": "v","V": "w","W": "x","X": "y","Y": "z","Z": "a","1":"2","2":"3","3":"4","4":"5","5":"6","6":"7","7":"8","8":"9","9":"0"}

    def __init__(self, message):
#Constructor
        self.message = message


    def return_letter_associated_with_umber(self, letter):
#Método para verificar si una letra tiene asociado un número
        l = letter.upper()
        if l in self.LETTER_BY_NUMBERS:
            return self.LETTER_BY_NUMBERS[l]
        else:
            return l


    def substitute_letters_by_numbers(self):
#Método para convertir un mensaje a un mensaje combinado con números
        words = self.message.split(" ")
        new_message = []

        for word in words:
            new_word = ''
            for letter in word:
                new_word += self.return_letter_associated_with_umber(letter)

            new_message.append(new_word)

        return ' '.join(new_message)


print("BIENVENIDO AL GRUPO DE INTELIGENCIA MILITAR")
print("-------------------------------------------\n")

def start():
#Método para iniciar el proceso de conversión de letras a números
    message = str(input("Ingrese el mensaje a codificar: "))
    m = CustomMessage(message)
    new_message = m.substitute_letters_by_numbers()
    print("-------------------------------------------------")
    print("Codificación Secreta: ",new_message.upper())
    print("-------------------------------------------------")
    print("             -Gracias, vuelva pronto-                 \n")

if __name__ == '__main__':
    start()
