from time import sleep
import threading
import time
import random

OCUPADO = 0 #Var semaforo ocupado

#Semaforos
S4D = threading.Semaphore(OCUPADO) 
S4T = threading.Semaphore(OCUPADO)
S5D = threading.Semaphore(OCUPADO)
S5T = threading.Semaphore(OCUPADO)
S7D = threading.Semaphore(OCUPADO)
S7I = threading.Semaphore(OCUPADO)
S10DD = threading.Semaphore(OCUPADO)
S10DI = threading.Semaphore(OCUPADO)
S10T = threading.Semaphore(OCUPADO)
S11TD = threading.Semaphore(OCUPADO)
S11TI = threading.Semaphore(OCUPADO)

#Ingresar chasis
def E1():
		print("01 - Ingresando el chasis a la linea de produccion...")
		t_espera = random.randint(1,9)
		sleep(t_espera)
		print("01 - Finalizado de ingresar chasis. Tardo: ", t_espera, " seg")
#fin

#Depositar chasis
def E2():
		print("02 - Depositando carroceria sobre el chasis...")
		t_espera = random.randint(1,9)
		sleep(t_espera)
		print("02 - Finalizado depositar carroceria. Tardo: ", t_espera, " seg")

#fin

#Levantar pieza acoplada
def E3():
		print("03 - Levantando pieza acoplada...");
		t_espera = random.randint(1,9)
		sleep(t_espera);
		print("03 - Finalizado levantar pieza acoplada. Tardo: ", t_espera, " seg")
#fin

#Soldadura delantera
def E4D():
		
		print("04 - Realizando soldaduras en la parte delantera")
		t_espera = random.randint(1,9)
		sleep(t_espera)
		
		print("04 - Finalizado soldaduras parte delantera. Tardo: ", t_espera, " seg")
		S4D.release()
#fin

#Soldadura trasera
def E4T():
		print("04 - Realizando soldaduras en la parte trasera")
		t_espera = random.randint(1,9)

		sleep(t_espera)
		print("04 - Finalizado soldaduras parte trasera. Tardo: ", t_espera, " seg")
		S4T.release()
#fin

#Antioxidante delantero
def E5D():
		S4D.acquire()
		S4D.release()
		print("05 - Aplicando producto protector en la soldadura de la parte delantera")
		t_espera = random.randint(1,9)
		sleep(t_espera)
		print("05 - Finalizado antioxidante parte delantera. Tardo: ", t_espera, " seg")
		S5D.release()

#Antioxidante trasero
def E5T():
		S4T.acquire()
		S4T.release()
		print("05 - Aplicando producto protector en la soldadura de la parte trasera")
		t_espera = random.randint(1,9)
		sleep(t_espera)
		print("05 - Finalizado antioxidante parte trasera. Tardo: ", t_espera, " seg")
		S4D.release()
		S5T.release()
#fin

#Bajar pieza acoplada
def E6():
		S5D.acquire()
		S5D.release()
		S5T.acquire()
		S5T.release()
		print("06 - Se baja pieza acoplada");
		t_espera = random.randint(1,9)
		sleep(t_espera)
		print("06 - Finalizado bajar pieza acoplada. Tardo: ", t_espera, " seg")
		
#fin

#Soldaduras derecha
def E7D():
		print("07 - Realizando soldaduras en el interior del coche, seccion derecha")
		t_espera = random.randint(1,9)
		sleep(t_espera)
		print("07 - Finalizado soldaduras Derecha. Tardo: ", t_espera, " seg")
		S7D.release()
#fin

#Soldaduras izquierda
def E7I():
		print("07 - Realizando soldaduras en el interior del coche, seccion izquierda")
		t_espera = random.randint(1,9)
		sleep(t_espera)
		print("07 - Finalizado soldaduras Izquierda. Tardo: ", t_espera, " seg")
		S7I.release()

#Aplicando pintura
def E8():
		S7D.acquire()
		S7D.release()
		S7I.acquire()
		S7I.release()
		print("08 - Aplicando pintura a la carroceria")
		t_espera = random.randint(1,9)
		sleep(t_espera)
		print("08 - Finalizado pintura a la carroceria. Tardo: ", t_espera, " seg")

#fin

#Aplicando tapizado interior
def E9():
		print("09 - realizando tapizado interior de carroceria")
		t_espera = random.randint(1,9)
		sleep(t_espera)
		print("09 - Finalizado tapizado interior de carroceria. Tardo: ", t_espera, " seg")
#fin

#Instalando asiento y puerta delantera derecha
def E1011DD():
		print("10 - instalando asiento delantero derecho")
		t_espera = random.randint(1,9)
		sleep(t_espera)
		print("10 - Finalizado asiento delantero derecho. Tardo: ", t_espera, " seg")
  
		print("11 - instalando puerta delantera derecha")
		t_espera = random.randint(1,9)
		sleep(t_espera)
		print("11 - Finalizado puerta delantera derecha. Tardo: ", t_espera, " seg")
		S10DD.release()
 
#Instalando asiento y puerta delantera izquierda
def E1011DI():
		print("10 - instalando asiento delantero izquierdo")
		t_espera = random.randint(1,9)
		sleep(t_espera)
		print("10 - Finalizado asiento delantero izquierdo. Tardo: ", t_espera, " seg")
  
		print("11 - instalando puerta delantera izquierda")
		t_espera = random.randint(1,9)
		sleep(t_espera)
		print("11 - Finalizado puerta delantera izquierda. Tardo: ", t_espera, " seg")
		S10DI.release()
 
def E10T():
		print("10 - instalando asiento trasero")
		t_espera = random.randint(1,9)
		sleep(t_espera)
		print("10 - Finalizado asiento trasero derecho. Tardo: ", t_espera, " seg")
		S10T.release()
 
#Instalando puerta trasera derecha 
def E11TD():

		S10T.acquire()
		S10T.release()
		print("11 - instalando puerta trasera derecha")
		t_espera = random.randint(1,9)
		sleep(t_espera)
		print("11 - Finalizado puerta trasera derecha. Tardo: ", t_espera, " seg")
		S11TD.release()

#Instalando puerta trasera izquierda 
def E11TI():
		S10T.acquire()
		S10T.release()
  	
		print("11 - instalando puerta trasera izquierda")
		t_espera = random.randint(1,9)
		sleep(t_espera)
		print("11 - Finalizado puerta trasera izquierda. Tardo: ", t_espera, " seg")
		S11TI.release()
	
#Instalando capot y parabrisas
def E1112D():
		S10DD.acquire()
		S10DD.release()
		S10DI.acquire()
		S10DI.release()
		print("11 - instalando Capot")
		t_espera = random.randint(1,9)
		sleep(t_espera) 
		print("11 - Finalizado Capot. Tardo: ", t_espera, " seg")
  
		print("12 - Instalado Parabrisas")
		t_espera = random.randint(1,9)
		sleep(t_espera)
		print("12 - Finalizado Parabrisas. Tardo: ", t_espera, " seg")
  
#Instalando valija y vidrio trasero
def E1112T():
		S11TD.acquire()
		S11TD.release()
		S11TI.acquire()
		S11TI.release()
		print("11 - Instalado Valija")
		t_espera = random.randint(1,9)
		sleep(t_espera)
		print("11 - Finalizado Valija. Tardo: ", t_espera, " seg")

		print("12 - Instalado Vidrio Trasero")
		t_espera = random.randint(1,9)
		sleep(t_espera)
		print("12 - Finalizado Vidrio Trasero. Tardo: ", t_espera, " seg")
#fin
	
#Seteamos hilos
h4d = threading.Thread(target = E4D, args = () )
h4t = threading.Thread(target = E4T, args = () )
h5d = threading.Thread(target = E5D, args = () )
h5t = threading.Thread(target = E5T, args = () )
h7d = threading.Thread(target = E7D, args = () )
h7i = threading.Thread(target = E7I, args = () )
h1011DD = threading.Thread(target = E1011DD, args = () )
h1011DI = threading.Thread(target = E1011DI, args = () )
h10T = threading.Thread(target = E10T, args = () )
h11TD = threading.Thread(target = E11TD, args = () )
h11TI = threading.Thread(target = E11TI, args = () )
h1112D = threading.Thread(target = E1112D, args = () )
h1112T = threading.Thread(target = E1112T, args = () )

#Secuencia de ejecucion
E1()
E2()
E3()	
#COBEGIN	
h4d.start()
h4t.start()		
h5d.start()	
h5t.start()	
#COEND
E6()	
#COBEGIN
h7d.start()	
h7i.start()	
#COEND
E8()
E9()
#COBEING
h1011DD.start()
h1011DI.start()
h10T.start()
h11TD.start()
h11TI.start()
h1112D.start()
h1112T.start()
#COEND
