Enunciado de problemas del archivo algoritmos.py 

PROBLEMA_1:

Los días de la semana se identifican por un número de la siguiente forma: 0 para Domingo. 1 para Lunes, 2 para Martes, 3 para Miercoles, etc. Determinar el día que corresponda a un número ingresado dando un mensaje adecuado, para el caso que el número dado no corresponda al dia de la semana tambien mostrara un mensaje adecuado a este.

PROBLEMA_2:

En una olimpiada de tiro al blanco se llega a un acuerdo entre los participantes para que el puntaje obtenido sea calculado en base al puntaje original (0 a 10) alcanzado en el tiro, multipicado por un factor:
	 ______________________________
	|PUNTAJE ORIGINAL   |	FACTOR	|
	|___________________|__________|
	|	0           |	  0	|
	|	1...5       |	  6	|
	|	6...8       |	  9	|
	|	9,10        |	  10	|
	|___________________|__________|

Para un tiro realizado determinar su puntaje correspondiente.

PROBLEMA_3:

Una tienda de ropa ha establecido los porcentajes de descuento, que se indican a continuación, de acuerdo a ciertas características del comprador: nacionalidad (1,2) y del producto que compra: sexo (H,M), talla (Niño, Joven, Adulto). Se sabe que una persona puede comprar varios productos por lo que se desea mostrar como resultado lo siguiente: nombre del comprador, cantidad de productos comprados, importe comprado, importe descontado y el importe a pagar; para lo cual se deben ingresar los datos que sean necesarios. El proceso para la compra de una persona termina cuando al ingresar el nombre del comprador se presiona ENTER.

			Niño	Joven	Adulto
			sexo	sexo	sexo
	NACIONALIDAD	H M	H M	H M
	     
	     1		5 4	7 9	10 12
	     2		4 5	9 7	12 10

PROBLEMA_4:

EL TURBO PASCAL dispone de varios tipos de dato entero que son: ShortInt, Byte, Interger, Word, LongInt; cada uno de los cuales tiene un rango de valores enteros que lo definen de la siguiente manera:

			  Rango de Valores
	Tipo de Dato	Desde		Hasta
	  ShortInt	-128		+127
	  Byte		0		255
	  Interger	-32768		+32767
	  Word		0		65535
	  LongInt	-2147483648	+2147483647
	  
Al ingresar la primera letra del tipo de dato mostrar su rango de valores correspondientes.

PROBLEMA_5:

Ingresar un número en forma de ARABICO (entero) y mostrar su equivalente en ROMANO asumiendo que el número ingresado es correcto y no debe ser mayor a 3999.

PROBLEMA_6:
Dos automoviles parten simultaneamente uno de Lima y el otro de Huacho con destino a Trujillo, con velocidades promedios de 120 Km/h y 66 Km/h respectivamente. Se pide mostrar la distancia recorrida por cada automovil con respecto a Lima, cada minuto hasta que el automovil con mayor velocidad pase al otro. Considerar las siguientes distancias en toda la ruta:

Lima			Huacho			Trujillo
			 130 Km
|-------------------------|			   570 Km
|--------------------------------------------------|

PROBLEMA_7:

Determinar la velocidad promedio ponderado de un vehiculo que recorre una misma distancia N veces, pero en diferentes tiempos cada vez. Utilizar la siguiente formula:
	
	VPP = distancia * numero de veces / suma de los tiempos

PROBLEMA_8:

Evaluar el resultado de la siguiente serie para los N primeros terminos donde N no debe ser mayor que 15:
	
	1 + x/2 + (x)^2/4 + (x)^3/8 + (x)^4/16 + (x)^5/32 + ...

PROBLEMA_9:

Una farmacia ha clasificado sus productos de la siguiente manera:
	
	 ________________________
	|  Tipo   |	Clase	  |
	|_________|______________|           
	|   G	  | analgésicos  | 
	|   R	  | antibióticos |
	|   P	  | antipiréticos|
	|   T	  |	otros	  |
	|_________|______________|
	
Cada clase puede ser de prcedencia Nacional o Importada. En un proceso repetitivo se ingresan los siguientes datos, procedencia (N, I, ENTER), tipo de operación (Entrada, Salida), tipo de producto (G,R,P,T), cantidad. El proceso termina cuando al ingresar la procedencia se presiona ENTER debiendo mostrar a continuación el stock de cada tipo de producto de acuerdo a su procedencia, asumiendo que el proceso empieza con stock 0 para todos los tipos de producto.

PROBLEMA_10:

Un grupo de inteligencia militar desea codificar los mensajes secretos de tal forma que no puedan ser interpretados con una lectura directa; para lo cual han establecido las siguientes reglas:

	a)Todo mensaje debe estar sus letras en mayúsculas.
	b)Reemplzar cada letra por la que sigue según abecedario excepto la "Z" que deberá reemplazarse con la letra "A".
	c)Reemplazar cada digito encontrado por el que le precede según su orden excepto el "0" que deberá reemplazarse por el "9".

Ingresar un mensaje y mostrar su codificación secreta resultante.
