import socket
import os

#print '\033[1;32mGreen \033[1;m'
#print '\033[1;34mBlue \033[1;m'
#print '\033[1;33mYellow \033[1;m'
#print '\033[1;m\033[1;31m' #rojo
#print '\033[1;m\033[1;33m' #amarillo
HOST = '192.168.0.12' 
PORT = 12345 

def datos ():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST,PORT))
	while True:
		reply = s.recv(4024)
		print reply
	s.close()
def datosg():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST,PORT))
	filer = open("Posdata.csv", "a")
	filer.write("intensidad1, intensidad2, intensidad3,x,y,z\n")
	while True:
		reply = s.recv(4024)
		print reply
		filer.write(reply)
		filer.flush()	
	filer.close()
	s.close()
def grafica ():
	print("abriendo grafica")
	cmd = 'python trilateracion.py'
	os.system(cmd)

###############################################################################
###############################################################################
###############################################################################
archivo = open("inicio.txt","r") 
f=archivo.read()
print(f) 
print '\033[1;m\033[1;33m' #amarillo
print("##################################################################################################")
print("############################################ADVERTENCIA###########################################")
print("##################################################################################################")
print("")
print '\033[1;m\033[1;31m' #rojo
print("##################################################################################################")
print("************Asegurese que el servidor este corriendo antes de ejecutar una opcion*****************")
print("##################################################################################################")
print("")
print("")
print("")
print '\033[1;m\033[1;32m' #verde
print("Opciones\n1.- datos\n2.- datos y guardado\n3.- interfaz grafica")

opciones  = { '1': datos, '2': datosg, '3': grafica}
seleccion = raw_input('Escoge una: ')
try:
	resultado = opciones[seleccion]()
	print resultado
except:
	print("Opcion invalida")
