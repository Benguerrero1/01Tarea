import numpy as np

w,s = np.loadtxt('sun_AM0.dat', unpack=True)


def integral_trapezoidal (x,y):
    '''
	Recibe dos arrays, tal que y=f(x), y calcula la integral de la función y
 usando el método trapezoidal compuesto.
	'''
    t=x.size
    int_t1=0
    for i in range (t-1):
        a=x.item(i)
        b=x.item(i+1)
        Fa=y.item(i)
        Fb=y.item(i+1)
        int_t1=int_t1+((b-a)/2)*(Fa+Fb)
    return int_t1
integral1=integral_trapezoidal (w,s)
print (integral1) 