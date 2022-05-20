import time 

print("                       - PROBLEMA 01 -                      ") 
print("........................Restaurante.........................\n")
#DATO DE ENTRADA
consumo = float(input("Ingrese el valor del monto consumido: "))
#DATOS PROPUESSTOS
P_descuento = 0.2
P_impuesto = 0.15
#IMPLEMENTO DE CONDICION
if consumo>30:
    #DESCUENTO DE 20%
    descuento = consumo * P_descuento
else:
    #NO HAY DESCUENTO
    descuento = 0
#CALCULO DE IMPUESTO
impuesto = (consumo - descuento) * P_impuesto
#CALCULO DE IMPORTE
importe = consumo - descuento + impuesto

print(f"Consumo:         S/. {round(consumo,1)}")
print(f"Descuento:       S/. {round(descuento,1)}")
print(f"Impuesto:        S/. {round(impuesto,1)}")
print(f"Importe a pagar: S/. {round(importe,1)}")
print("\n      -Gracias, Vuelva pronto-\n")

print("                       - PROBLEMA 02 -                      ")
print("........................Menor Valor.........................\n")
#DATOS DE ENTRADA 
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: ")) 
num3 = int(input("Ingrese el tercero numero: ")) 
num4 = int(input("Ingrese el cuarto numero: ")) 
num5 = int(input("Ingrese el quinto numero: "))
#DATO PARA ALMACENAR EL VALOR 
minimo=0
#IMPLEMENTO DE CONDICION
if ((num1<num2) and (num1<num3) and (num1<num4) and (num1<num5)):
    minimo += num1
    print(f"\nEl valor minimo de los 5 numeros ingresados es {minimo}\n")
elif ((num2<num1) and (num2<num3) and (num2<num4) and (num2<num5)):
    minimo += num2
    print(f"\nEl valor minimo de los 5 numeros ingresados es {minimo}\n")
elif ((num3<num1) and (num3<num2) and (num3<num4) and (num3<num5)):
    minimo += num3
    print(f"\nEl valor minimo de los 5 numeros ingresados es {minimo}\n")
elif ((num4<num1) and (num4<num2) and (num4<num3) and (num4<num5)):
    minimo += num4
    print(f"\nEl valor minimo de los 5 numeros ingresados es {minimo}\n")
else:
    minimo += num5
    print(f"\nEl valor minimo de los 5 numeros ingresados es {minimo}\n")


print("                       - PROBLEMA 03 -                      ")
print(".......................Nota Bonificada......................\n")
#DATO DE ENTRADA
nombre = input("Ingrese el nombre del alumno: ")
nota = int(input("Ingrese la nota del alumno: "))
#OTROS DATOS
descuento = 0 
points_bonif = 0
residuo = nota % 5 
#IMPLEMENTO DE CONDICION
if nota<5:
    points_bonif += 3
elif nota>=5 and nota<10:
    points_bonif += 2
elif nota>=10 and nota<15:
    points_bonif += 1
elif nota>=15 and nota<=20:
    #DESCUENTO DEL RESIDUO DE LA NOTA
    descuento +=  residuo
#CALCULO DE LA NOTA BONIFICADA
nota_bonif = nota - descuento + points_bonif
print("_____________________________________")
print(f"Nombre del Alumno:        {nombre}")
print(f"Nota:                     {nota}")
print("_____________________________________")
print(f"Descuento:                {descuento}")
print(f"Puntos de bonificación:   {points_bonif}")
print("_____________________________________")
print(f"Nota bonificada:          {nota_bonif}")
print("\n       -Gracias, Vuelva pronto-\n")

print("                       - PROBLEMA 04 -                      ")
print(".....................Cambio de Identidad....................\n")
#DATOS DE ENTRADA
print("A continuación ingresara sus datos (1er Persona)\n")
nombre_1 = str(input("Ingrese su nombre: "))
direccion_1 = str(input("Ingrese su direccion: "))
telefono_1 = str(input("Ingrese su numero de teléfono: "))
edad_1 = int(input("Ingrese su edad: "))
print("\nA continuación ingresara sus datos (2da Persona)\n")
nombre_2 = str(input("Ingrese su nombre: "))                          
direccion_2 = str(input("Ingrese su direccion: "))                    
telefono_2 = str(input("Ingrese su numero de teléfono: "))            
edad_2 = int(input("Ingrese su edad: ")) 
#DIFERENCIA DE EDADES
resta_edad = edad_1 - edad_2
#IMPLEMENTO DE CONDICION
if edad_1 > edad_2:
    if resta_edad <=4:
        print("\nProcesando...")
        time.sleep(5) #ESPERAR 5 SEGUNDOS
        print("\nSi puede cambiar de identidad ")
        print("A continuación pueden digitar sus nuevos datos")
        time.sleep(5) #ESPERAR 5 SEGUNDOS
        print("\n-----Ingrese su nueva identidad (1er Persona)-----")
        n_nombre_1 = str(input("Nombre nuevo: "))
        n_direccion_1 =str(input("Dirección nueva: "))
        n_telefono_1 = str(input("Teléfono nuevo: "))
        n_edad_1 = int(input("Nueva edad: "))
        time.sleep(5) #ESPERAR 5 SEGUNDOS
        print("\n-----Ingrese su nueva identidad (2da Persona)-----")
        n_nombre_2 = str(input("Nombre nuevo: "))
        n_direccion_2 =str(input("Dirección nueva: "))
        n_telefono_2 = str(input("Teléfono nuevo: "))
        n_edad_2 = int(input("Nueva edad: "))
        print("\nGuardando datos...")
        time.sleep(5) #ESPERAR 5 SEGUNDOS
        #RESULTADO  SI LA CONDICION ES VERDADERA
        print("-----Nueva identidad (1era Persona)-----")
        print(f"Nombre:    {n_nombre_1}         Teléfono: {n_telefono_1 }")
        print(f"Dirección: {n_direccion_1}      Edad:     {n_edad_1}")
        print("-----Nueva identidad (2da Persona)------")
        print(f"Nombre:    {n_nombre_2}         Teléfono: {n_telefono_2 }")
        print(f"Dirección: {n_direccion_2}      Edad:     {n_edad_2}")

    else:
        #RESULTADO SI LA CONDICION ES FALSA
        print("\nProcesando...")
        time.sleep(5) #ESPERAR 5 SEGUNDOS
        print("La diferencia de edades es mayor a 4")
        print(f"Diferencia de edad: {resta_edad}")
        print(f"No pueden realizar un intercambio de sus identidades")

print("\n      -Gracias, vuelva pronto-     \n")

print("                       - PROBLEMA 05 -                      ") 
print(".........................Sueldo Neto........................\n") 

#SUELDO BASICO MENSUAL
sueldo_basico = 450
p_descuento = 0.10
#DATOS DE INSTRUCCION
qto_sec = 0.05
tecnico = 0.10
profesional = 0.20
#DATOS DE CONDICION SOCIAL
casado = 0.03                                                         
p_hijo = 0.02                                                           
sin_vivienda = 0.05  
#DATO DE ENTRADA DE NOMBRE
nombre = input("Ingrese el nombre del trabajador: ")
#OPCIONES
time.sleep(3) #ESPERAR 3 SEGUNDOS
print("\nAhora elige una de las siguientes opciones segun su Instrucción\n")
print("1) 5to Secundaria")
print("2) Técnico")
print("3) Profesional")
print("4) salir\n")
print("------------------------------------")
#DATO DE ENTRADA DE LAS OPCIONES
instruccion = input("Ingrese una opción: ")
#IMPLEMENTO DE CONDICION 1
if instruccion == "1":
    
    print("Tiene una instrucción de Quinto de Secundaria\n")
    bonif_i = sueldo_basico * qto_sec
    nuevo_s_0 = sueldo_basico + bonif_i
    #DATO DE ENTRADA DE LA CONDICION SOCIAL
    c_social = input("Ingrese su condición social: ")
    if c_social =="casado":
        bonif_c = sueldo_basico * casado
        nuevo_s_1 = sueldo_basico + bonif_c
    elif c_social == "por cada hijo":
        #DATO DE ENTRADA DE LA CANTIDAD DE HIJOS
        c_hijo = int(input("\nIngrese la cantidad de hijos: "))
        bonif_h = sueldo_basico * (p_hijo * c_hijo)
        nuevo_s_1 = sueldo_basico + bonif_h
    elif c_social == "sin vivienda":
        bonif_sv = sueldo_basico * sin_vivienda 
        nuevo_s_1 = sueldo_basico + bonif_sv
#IMPLEMENTO DE CONDICION 2
elif instruccion == "2":
    
    print("Tiene una instrucción de Técnico\n")
    bonif_i = sueldo_basico * tecnico
    nuevo_s_0 = sueldo_basico + bonif_i
    #DATO DE ENTRADA DE LA CONDICION SOCIAL
    c_social = input("Ingrese su condición social: ")
    if c_social =="casado":
        bonif_c = sueldo_basico * casado
        nuevo_s_1 = sueldo_basico + bonif_c
    elif c_social == "por cada hijo":
        #DATO DE ENTRADA DE LA CANTIDAD DE HIJOS
        c_hijo = int(input("\nIngrese la cantidad de hijos: "))
        bonif_h = sueldo_basico * (p_hijo * c_hijo)
        nuevo_s_1 = sueldo_basico + bonif_h
    elif c_social == "sin vivienda":
        bonif_sv = sueldo_basico * sin_vivienda 
        nuevo_s_1 = sueldo_basico + bonif_sv
#IMPLEMENTO DE CONDICION 3
elif instruccion == "3":
    
    print("Tiene una instrucción de Profesional\n") 
    bonif_i = sueldo_basico * profesional
    nuevo_s_0 = sueldo_basico + bonif_i
    c_social = input("Ingrese su condición social: ")
    if c_social =="casado":
        bonif_c = sueldo_basico * casado
        nuevo_s_1 = sueldo_basico + bonif_c
    elif c_social == "por cada hijo":
        c_hijo = int(input("\nIngrese la cantidad de hijos: "))
        bonif_h = sueldo_basico * (p_hijo * c_hijo)
        nuevo_s_1 = sueldo_basico + bonif_h
    elif c_social == "sin vivienda":
        bonif_sv = sueldo_basico * sin_vivienda
        nuevo_s_1 = sueldo_basico + bonif_sv
#IMPLEMENTO DE CONDICION DE SALIDA
else:
    exit()
#CALCULO DEL SUELDO
sueldo = nuevo_s_0 + nuevo_s_1
#CONDICION VERDADERA O FALSA SI ES MAYOR A 700
if sueldo > 700:
    #CALCULO DE DESCUENTO
    descuento = sueldo * p_descuento
else:
    descuento = 0
#CALCULO DEL PAGO A RECIBIR
pago = sueldo - descuento

time.sleep(3) #ESPERAR 3 SEGUNDOS
print("------------------------------------")
print(f"Nombre del trabajador ---> {nombre}")
print(f"Sueldo a recibir ---> {pago}")
print("\n            -Gracias, vuelva pronto-\n")

