import numpy as np 
import matplotlib.pyplot as plt

def mandelbrot (c):
    p = 0
    z = 0
    while (p < 50 and abs(z) <= 2):
        z = z**2 + c
        p+=1
    if (p<50):
        return p
    else:
        return -1

def show_mandelbrot (lng):
    x = np.linspace(-2,2,lng)
    y = np.linspace(-2,2,lng)
    iteration = np.zeros((lng, lng))
    for i in range(len(x)):
        for j in range(len(y)):
            iteration[i,j]=mandelbrot(complex(x[i],y[j]))
    plt.imshow(iteration)
    plt.show()

#show_mandelbrot(1000)

def julia (c, z):
    p = 0
    while (p < 50 and abs(z) <= 2):
        z = z**2 + c
        p+=1
    if (p<50):
        return p
    else:
        return -1

def show_julia (c, lng, save):
    x = np.linspace(-2,2,lng)
    y = np.linspace(-2,2,lng)
    iteration = np.zeros((lng, lng))
    for i in range(len(x)):
        for j in range(len(y)):
            iteration[i,j]=julia(c, complex(x[i],y[j]))
    fig=plt.imshow(iteration)
    if (save):
        plt.axis('off')
        plt.savefig('julia_' + str(c.real) + '+i(' + str(c.imag) + ').png', figsize=(lng, lng), bbox_inches='tight', pad_inches=0, dpi=lng)
    else:
        plt.show()

#show_julia(complex(0.28,0.53),15000, False)
#show_julia(complex(0.28,0.53),1000 False)
#show_julia(complex(-0.63,0.67),1000, False)
show_julia(complex(-0.85,0.2),1000, True)