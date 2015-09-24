import numpy as np
import scipy

x,y = np.loadtxt('sun_AM0.dat', unpack=True)
s=x.size
a=x.item(0)
b=x.item(s-1)
Fa=y.item(0)
Fb=y.item(s-1)
int_ts=scipy.integrate.trapz(y,x)
print (int_ts)
Fm=lambda m: ((np.tan(m)**3)*(1+np.tan(m)**2))/(np.exp(np.tan(m))-1)
int_qs=scipy.integrate.quad(Fm,0,np.pi/2)
print (int_qs)
