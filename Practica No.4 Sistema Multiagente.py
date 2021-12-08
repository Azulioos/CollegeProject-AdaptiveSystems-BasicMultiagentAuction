#Autor: Luis Daniel Garcìa 					|| Matricula: 1857391
#Facultad de ingenerìa mecànica y elèctrica || 21/11/2020
import random
from collections import deque
from numpy import *

print("-----CONFIGURACION DE PARAMETROS-----")

def Objeto():
	Lista_Objeto = []
	Precio_Obj = 0
	Objeto = input("Ingrese el nombre del objeto que desea vender: ")
	Lista_Objeto.append(Objeto)

	while(Precio_Obj < 1 or Precio_Obj > 2000):
		Precio_Obj = int(input("Ingrese el precio de la/el : " + Objeto + " que desea vender: "))

		if(Precio_Obj < 1 or Precio_Obj > 2000):
			print("El precio inicial de dicho objeto no puede sobrepasar los 2000 y tiene que ser un valor positivo")
	Estado = True
	Lista_Objeto.append(Precio_Obj)
	Lista_Objeto.append(Estado)
	return(Lista_Objeto)

def Configuracion():
	Capital_Agente = 0
	while(Capital_Agente < 2000 or Capital_Agente > 10000):
		Capital_Agente = int(input("Ingrese la capital del agente: "))

		if(Capital_Agente < 2000 or Capital_Agente > 10000):
			print("Para participar en la subasta es necesario contar con un minimo de 2000.00 $ y como maximo 10 000.00 $")
	return(Capital_Agente)


def Agente(Objeto_Activo, Agente_Capital, Probabilidad):
	Resolucion = []

	Probabilidad = Probabilidad + ((Agente_Capital - Objeto_Activo[1])/100)
	if Probabilidad < 30:
		print("El Agente no parece muy interesado en la subasta.")
	else:
		if Probabilidad < 70:
			print("El Agente parece estar medianamente interesado en la subasta actual.")
		else:
			print("El Agente parece estar interesado en la subasta!!")


	Respuesta=random.randint(1,100)

	if Respuesta < Probabilidad:
		if Agente_Capital <= Objeto_Activo[1]:
			print("El Agente no puede seguir ofreciendo mayores cantidades. Por lo que saldra de la subasta.")
			Respuesta = False
			Aumento = False
			Resolucion.append(Respuesta)
			Resolucion.append(Aumento)
		else:
			Respuesta = True
			print("Woah! Nuestro agente ha decidido aumentar la oferta!")
			Aumento = random.randint(1,4)
			Aumento = Aumento/10
			Aumento = Objeto_Activo[1] + ((Agente_Capital) * Aumento)
			if Aumento > Agente_Capital:
				Aumento = Agente_Capital
			print("El agente esta pensando ofrecer una cantidad de: ", Aumento)
			Resolucion.append(Respuesta)
			Resolucion.append(Aumento)

	else:
		print("Buah... El agente ha perdido el interes, por consiguiente saldra de la subasta.")
		Respuesta = False
		Aumento = False
		Resolucion.append(Respuesta)
		Resolucion.append(Aumento)
	print("_______________________________________________________")
	return(Resolucion)


Lista_Objeto_1 = Objeto()
#Lista_Objeto_2 = Objeto()
#Lista_Objeto_3 = Objeto()

Agente_1_Capital = Configuracion()
Agente_2_Capital = Configuracion()
Agente_3_Capital = Configuracion()

print("===========================================================")
print("Comienza la subasta!!!")
print("===========================================================")
Objeto_Activo = Lista_Objeto_1


Ronda = 70
print("Agente No.1: ")
Resultado_1 = Agente(Objeto_Activo, Agente_1_Capital, Ronda)
print("Agente No.2: ")
Resultado_2 = Agente(Objeto_Activo, Agente_2_Capital, Ronda)
print("Agente No.3: ")
Resultado_3 = Agente(Objeto_Activo, Agente_3_Capital, Ronda)
Parametro = False
Interacciones = 3

while Objeto_Activo[2] == True:
	if Parametro == True:
		if Objeto_Activo[2] == True:
			print("===========================================================")
			print("Siguiente ronda!!")
			Interacciones = 0
			if Resultado_2[0] == True or Resultado_3[0] == True:
				if Resultado_1[0] == True:
					print("Agente No.1: ")
					Resultado_1 = Agente(Objeto_Activo, Agente_1_Capital, Ronda)
					Interacciones = Interacciones + 1
			if Resultado_1[0] == True or Resultado_3[0] == True:
				if Resultado_2[0] == True:
					print("Agente No.2: ")
					Resultado_2 = Agente(Objeto_Activo, Agente_2_Capital, Ronda)
					Interacciones = Interacciones + 1
			if Resultado_1[0] == True or Resultado_2[0] == True:
				if Resultado_3[0] == True:
					print("Agente No.3: ")
					Resultado_3 = Agente(Objeto_Activo, Agente_3_Capital, Ronda)
					Interacciones = Interacciones + 1

	if Resultado_1[1] >= Resultado_2[1] and Resultado_1[1] >= Resultado_3[1]:
		Objeto_Activo[1] = Resultado_1[1]
		print("_______________________________________________________")
		print("Se ha tomado la oferta del agente No.1 que es de: ", Objeto_Activo[1])
		if Interacciones <= 1:
			Objeto_Activo[2] = False
			Agente_1_Capital - Objeto_Activo[1]
			Venta = Resultado_1[1]

	if Resultado_2[1] >= Resultado_1[1] and Resultado_2[1] >= Resultado_3[1]:
		Objeto_Activo[1] = Resultado_2[1]
		print("_______________________________________________________")
		print("Se ha tomado la oferta del agente No.2 que es de: ", Objeto_Activo[1])
		if Interacciones <= 1:
			Objeto_Activo[2] = False
			Agente_2_Capital - Objeto_Activo[1]
			Venta = Resultado_2[1]

	if Resultado_3[1] >= Resultado_1[1] and Resultado_3[1] >= Resultado_2[1]:
		Objeto_Activo[1] = Resultado_3[1]
		print("_______________________________________________________")
		print("Se ha tomado la oferta del agente No.3 que es de: ", Objeto_Activo[1])
		if Interacciones <= 1:
			Objeto_Activo[2] = False
			Agente_3_Capital - Objeto_Activo[1]
			Venta = Resultado_3[1]
	
	Ronda - 10
	Parametro = True

print("FIN DE LA SUBASTA!")
print("Objeto vendido por: ",  Venta)