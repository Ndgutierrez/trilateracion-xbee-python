import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib import animation
import socket

#######################################################
HOST = '192.168.0.12' # Enter IP or Hostname of your server
PORT = 12345 # Pick an open Port (1000+ recommended), must match the server port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
#######################################################
x=0
y=0
"""se localiza el dispositivo por medio de las
fuerzas de las senales captadas y de la ubicacion de
las antenas
"""
d = 30
i = 25
j = -40
#se definen las coordenadas de la Antena A
ax = 0
ay = 0
#se define la cobertura Antena A
ar = 3
#se definen las coordenadas de la Antena B
bx = d
by = 0
#se define la cobertura Antena B
br = 3
#se definen las coordenadas de la Antena C
cx = i
cy = j
#se define la cobertura de la Antena c
cr = 3
#grafica
fig = plt.figure()
a = fig.add_subplot(111, aspect='equal')
#################antena1#####################
e1 = Ellipse(xy=(ax, ay), width=ar*2, height=ar*2, angle=0)
e1.set_clip_box(a.bbox)
e1.set_color('green')
e1.set_alpha(0.1)
a.add_patch(e1)
a.annotate("Antena A",
               xy=(ax, ay), xycoords='data',
               xytext=(ax-6, ay+6), textcoords='data',
               arrowprops=dict(arrowstyle="->",
                               connectionstyle="arc3"), 
               )
a.plot(ax,ay, "g^", mew=2, ms=12)
a.add_artist(e1)
#####################antena2####################
e2 = Ellipse(xy=(bx, by), width=br*2, height=br*2, angle=0)
e2.set_clip_box(a.bbox)
e2.set_color('red')
e2.set_alpha(0.1)
a.add_patch(e2)
a.annotate("Antena B",
               xy=(bx, by), xycoords='data',
               xytext=(bx+6, by+6), textcoords='data',
               arrowprops=dict(arrowstyle="->",
                               connectionstyle="arc3"))
a.plot(bx,by, "r^", mew=2, ms=12)
a.add_artist(e2)
e3 = Ellipse(xy=(cx , cy), width=cr*2, height=cr*2, angle=0)
e3.set_clip_box(a.bbox)
e3.set_color('blue')
e3.set_alpha(0.1)
a.add_patch(e3)
a.annotate("Antena C",
               xy=(cx, cy), xycoords='data',
               xytext=(bx+3.5, by-6), textcoords='data',
               arrowprops=dict(arrowstyle="->",
                               connectionstyle="arc3"))
a.plot(cx,cy, "b^", mew=2, ms=12)
a.add_artist(e3)
############################################
line, = a.plot([],[], 'k*', mew=3, ms=12)

def init():
    e1.set_visible(False)
    e2.set_visible(False)
    e3.set_visible(False)
    line.set_visible(False)
    line.set_data([], [])

    return [e1,e2,e3,line]
def animate(i):
    if i == 1:
        e1.set_visible(True)
        e2.set_visible(True)
        e3.set_visible(True)
        line.set_visible(True)
    #e3 = Ellipse(xy=(cx , cy), width=cr*2, height=cr*2, angle=0)
    #c.send(str(hex1)+","+str(hex2)+","+str(hex3)+","+" "+","+str(x)+","+str(y)+","+str(z)+"\n")
    reply = s.recv(4024)
    
    reply2 = reply.split(',')
    bal1=int(reply2[0])
    bal2=int(reply2[1])
    bal3=int(reply2[2])
    balx=float(reply2[4])
    baly=float(reply2[5])
    
    e1.width=bal1
    e1.height=bal1
    e2.width=bal2
    e2.height=bal2
    e3.width=bal3
    e3.height=bal3

    line.set_data(balx,baly)
    return [e1,e2,e3,line]
anim = animation.FuncAnimation(fig, animate, init_func=init, interval=100, blit=True)
plt.xlim(-100, 100)
plt.ylim(-100, 100)
plt.show()

