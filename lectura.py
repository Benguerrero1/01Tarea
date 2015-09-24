import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt('sun_AM0.dat', unpack=True)
print (x)
print (y)
#x= longitud de onda en nm
#y= espectro del Sol en Watts/(m^2*nm)
print type(x) #comprueba que es numpy.ndarray (analogo para y)
x=x*10 #convierte nm en agnstrom
y=y*0.0001 #convierte al sistema cgs
plt.plot(x,y)
plt.yscale('log')
plt.xscale('log') 
plt.ylabel("Espectro del sol ($\\frac{erg}{s*cm^2*cm}$)", fontsize=20)
plt.xlabel("Longitud de onda (A)",fontsize=20)
