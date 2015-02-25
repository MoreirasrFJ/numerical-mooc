# -*- coding: utf-8 -*-

import numpy 
from matplotlib import pyplot


#Inicialización
T = 28.5
dt = 0.1
N = int(T/dt)+1


#Constantes
ms=50.
g=9.81
rh=1.091
r=0.5
A=pi*r*r
ve=325.
cd=0.15
mp0=100.0
c_mp=20.


#Funcion para calcular mp
def mp(t):
    t
    if t<(5-dt):
        mp = mp0-c_mp*t
    else:
        mp=0
    return mp
    
#Funcion para calcular la aceleración       
def acelaracion(t):
    
    if t <(5-dt):
        a=(c_mp*ve)/(ms+mp(t))-g-(0.5*rh*A*cd*u[1]**2)/(ms+mp(t))
    elif t==(5-dt) or t>(5-dt):
        a=-g-(0.5*rh*A*cd*u[1]**2)/(ms+mp(t))
        
    else:
        a=-g-(0.5*rh*A*cd*u[1]**2)/(ms+mp(t))
    return a

# initial conditions
z0 = 0.0  #altura inicial
v0  = 0.0   #velocidad inicial
t = 0.0   #Tiempo inicial


u = numpy.array([z0, v0])

# initialize an array to hold the changing angle values
z = numpy.zeros(N)
z[0] = z0 

v = numpy.zeros(N)
v[0] = v0   

# time-loop using Euler's method
for n in range(1,N):
       
    u=u+dt*numpy.array([u[1],acelaracion(t)])
    
    z[n] = u[0]
    v[n]=u[1]
    t=t+dt
    print n,t,u  
   
 
t=numpy.arange(0,T+dt,dt)

pyplot.plot(t,v, )
pyplot.plot(t,z, )
