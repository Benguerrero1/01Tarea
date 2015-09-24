import numpy as np
from astropy import constants as const

print (np.pi**4/15)
int_t=1366.09079684
kb=const.k_B.value
c=const.c.value
h=const.h.value
T=5778
y=[0,np.pi/16,np.pi/8,3*np.pi/16,np.pi/4,5*np.pi/16,3*np.pi/8,7*np.pi/16,np.pi/2]
def integral_pto_medio (x,func):
    '''
    Recibe un array x y una funcion f(x) y retorna la integral de esa función usando 
    el mérodo del punto medio para cada par de elementos de x.
    '''
    int_m=0
    for i in range (len(x)-1):
         m=(x[i]+x[i+1])/2
         Fm=func(m)
         int_m=int_m+(x[i+1]-x[i])*Fm
    return int_m
         
def funcion1 (x):
    Fx=((np.tan(x)**3)*(1+np.tan(x)**2))/(np.exp(np.tan(x))-1)
    return Fx

integralm=integral_pto_medio (y,funcion1)
integral2=integralm*((2*np.pi*h)/c**2)*((kb*T/h)**4)
print (integralm)
print (integral2)
As=integral2/int_t
r=np.sqrt(As/4*np.pi)
print(r)
