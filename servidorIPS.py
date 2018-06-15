# -*- coding: iso-8859-15 -*-


#print '\033[1;32mGreen \033[1;m'
#print '\033[1;34mBlue \033[1;m'
#print '\033[1;33mYellow \033[1;m'

########################################################################
#COORDINADOR: 00 13 A2 00 | 41 7B D1 88    >
#ROUTER     : 00 13 A2 00 | 40 B7 94 77    > 24 58

#C>R: 7E 00 0F 17 01 00 13 A2 00 40 B7 94 77 FF FE 02 44 42 AB
#7E                START
#00 0F                 LEN
#17                FRAME TYPE (AT REMOTE COMMAND REQUEST)
#01                FRAME ID
#00 13 A2 00 40 B7 94 77     DST ADDRESS 64BIT
#FF FE                    DST ADDRESS 16BIT
#02                REMOTE COMMAND OPTIONS
#44 42                COMMAND (ASCII DB)
#AB                CHECKSUM

#R>C:  7E 00 10 97 01 00 13 A2 00 40 B7 94 77 24 58 44 42 00 28 86
#7E                START
#00 10                LEN
#97                FRAME TYPE (AT REMOTE COMMAND RESPONSE)
#01                FRAME ID
#00 13 A2 00 40 B7 94 77        DST ADDRESS 64BIT
#24 58                DST ADDRESS 16BIT
#44 42                COMMAND (ASCII DB)
#00                STATUS OK
#28                RESPONSE
#86                CHECKSUM
######################################################################################




import serial
import time 
import cmath
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.0.12"
port = 12345
s.bind((host, port))
s.listen(5)
c = None


ser = serial.Serial('/dev/ttyUSB0', 9600)
hex1= ""
hex2= ""
hex3= ""
hex1m= ""
hex2m= ""
hex3m= ""

x=0
y=0
z=0

ax= ""
ay= ""
ar= ""
bx= ""
by= ""
br= ""
cx= ""
cy= ""
cr= ""




def router_1 ():
    global hex1
    trama_tx="\x7E\x00\x0F\x17\x01\x00\x13\xA2\x00\x40\xB7\x94\x77\xFF\xFE\x02\x44\x42\xAB"

    ser.write(trama_tx)

    i1=0
    intensidad_hex1=0
    resp1=""
    

    while(True):
        incoming1 = ser.read()
        resp1=resp1 + incoming1


        if i1==18:
            intensidad_hex1=":".join("{:02x}".format(ord(c)) for c in incoming1)

        if i1==19:
            """
            print '\033[1;m\033[1;33m' #amarillo
            print "*****************************************"
            print '\033[1;m\033[1;31m' #rojo
            print "intensidad router 1"
            print ""
            print ""
            print "Intensidad (hex)=",intensidad_hex1
            print "Intensidad (dec)=",int(intensidad_hex1,16),"%"
            print '\033[1;m\033[1;33m' #amarillo
            print "*****************************************"
            """
            hex1=int(intensidad_hex1,16)
            i1=0
            break

        i1+=1
def router_2 ():
    global hex2
 
    trama_tx2="\x7E\x00\x0F\x17\x01\x00\x13\xA2\x00\x40\xAD\xBD\x25\x5F\x11\x02\x44\x42\x6B"


    ser.write(trama_tx2)
    i2=0
    intensidad_hex2=0
    resp2=""


    while(True):
        incoming2 = ser.read()

        resp2=resp2 + incoming2
        if i2==18:
            intensidad_hex2=":".join("{:02x}".format(ord(c)) for c in incoming2)
            

        if i2==19:
            """
            print '\033[1;m\033[1;33m' #amarillo
            print "*****************************************"
            print '\033[1;m\033[1;31m' #rojo
            print "intencidad router 2"
            print ""
            print ""
            print "Intensidad (hex)=",intensidad_hex2
            print "Intensidad (dec)=",int(intensidad_hex2,16),"%"
            print '\033[1;m\033[1;33m' #amarillo
            print "*****************************************"
            """
            hex2=int(intensidad_hex2,16)

            break

        i2+=1
        
def router_3 ():
    global hex3
    trama_tx3="\x7E\x00\x0F\x17\x01\x00\x13\xA2\x00\x40\xB1\x8B\x5C\x76\x89\x02\x44\x42\xD3"
    ser.write(trama_tx3)
    i3 = 0
    intensidad_hex3=0
    resp3=""
    while(True):
        incoming3 = ser.read()
        resp3=resp3 + incoming3


        if i3==18:
            intensidad_hex3=":".join("{:02x}".format(ord(c)) for c in incoming3)
            

        if i3==19:
            """
            print '\033[1;m\033[1;33m' #amarillo
            print "*****************************************"
            print '\033[1;m\033[1;31m' #rojo
            print "intensidad router 3"
            print ""
            print ""
            print "Intensidad (hex)=",intensidad_hex3
            print "Intensidad (dec)=",int(intensidad_hex3,16),"%"
            print '\033[1;m\033[1;33m' #amarillo
            print "*****************************************"
            """
            hex3=int(intensidad_hex3,16)
        
            break

        i3+=1
        
def posicion ():
    global hex1
    global hex2
    global hex3
    global hex1m
    global hex2m
    global hex3m
    global x
    global y
    global z
    global ax
    global ay
    global ar
    global bx
    global by
    global br
    global cx
    global cy
    global cr 

    hex1m=(0.1259*hex1)-3.688
    hex2m=(0.1259*hex2)-3.688
    hex3m=(0.1259*hex3)-3.688

    
    """se localiza el dispositivo por medio de las
   fuerzas de las senales captadas y de la ubicacion de
   las antenas
    """
    d = 3
    i = 2.5
    j = -4
    #se definen las coordenadas de la Antena A
    ax = 0
    ay = 0
    #se define la cobertura Antena A
    ar = hex1m
    #se definen las coordenadas de la Antena B
    bx = d
    by = 0
    #se definen las coordenadas de la Antena C
    br = hex2m
    cx = i
    cy = j
    #se define la cobertura de la Antena c
    cr = hex3m
    
    
    #se localiza la ubicacion del receptor por medio de la formula de trilateracion
    x = (ar**2 - br**2 + d**2)/float((2*d))
    y = ((ar**2-cr**2+i**2+j**2)/(2*j))-((float(i/j))*x)
    z= cmath.sqrt(ar**2 - x**2 - y**2)
    
    
###################################################################################
######################################ejecutar#####################################
###################################################################################

#descomentar si se quiere dejar registro en la raspberry        
#filer = open("data.csv", "a")
#filer.write("intensidad1, intensidad2, intensidad3,x,y,z\n")

while (True):
	if c is None:

		print '[Esperando Conexion...]'
                c, addr = s.accept()
                print 'conexion recivida de:', addr
	
	else:
		router_1()
    		router_2()
    		router_3()
    		posicion()
    		print "La posicion en x,y,z es -> (%s,%s,%s)" %(x, y, z)
		c.send(str(hex1)+","+str(hex2)+","+str(hex3)+","+" "+","+str(x)+","+str(y)+","+str(z)+"\n")
		#descomentar si se quiere dejar registro en la raspberry  
    		#filer.write(str(hex1)+","+str(hex2)+","+str(hex3)+","+str(x)+","+str(y)+","+str(z)+"\n")
    		#filer.flush()
    		time.sleep(0.2)
		

s.close()
#descomentar si se quiere dejar registro en la raspberry  
#filer.close()


