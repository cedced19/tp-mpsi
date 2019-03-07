import math
import matplotlib.pyplot as pl
import numpy as np

def euler1(F, a, b, x0, y0, n):
    Ly = [y0]
    Lx = [x0]
    x= x0
    y= y0
    h=(b-a)/n
    while x <= b:
        y= h*F(x,y)+y
        x+=h 
        Lx.append(x) 
        Ly.append(y)
    x= x0
    y= y0
    while x >= a:
        y= -h*F(x,y)+y
        x-=h 
        Lx.insert(0, x) 
        Ly.insert(0,y)
    return Lx, Ly
    


def show_euler1():
    a = -5.0
    b = 5.0
    n = 60
    x0, y0 = 0, 1
    
    Lx, Ly = euler1(lambda x, y:y, a, b, x0, y0, n)
    pl.plot(Lx, Ly, label='euler1') # courbe approché
    x= np.linspace(a, b, n)
    pl.plot(x, np.exp(x), label='exp') # courbe exact
    pl.legend()
    pl.show()

#show_euler1()


def euler2(F, a, b, x0, y0, z0, n):
    Ly = [y0]
    Lx = [x0]
    x= x0
    y= y0
    y1 = z0
    h=(b-a)/n
    while x <= b:
        y2=F(x,y,y1) 
        y= h*y1+y
        y1= h*y2+y1
        x+=h 
        Lx.append(x) 
        Ly.append(y)
    x= x0
    y= y0
    y1 = z0
    while x >= a:
        y2=F(x,y,y1) 
        y= -h*y1+y
        y1= -h*y2+y1
        x-=h 
        Lx.insert(0, x) 
        Ly.insert(0,y)
    return Lx, Ly

def show_euler2():
    a = -30
    b = 30
    n = 1000
    x0, y0, z0 = 0, 0, 1
    
    Lx, Ly = euler2(lambda x, y, y1:-y, a, b, x0, y0, z0, n)
    pl.plot(Lx, Ly, label='euler2') # courbe approché
    x= np.linspace(a, b, n)
    pl.plot(x, np.sin(x), label='sin') # courbe exact
    pl.legend()
    pl.show()

#show_euler2()

def G(x, Y):
    u,v = Y 
    return np.array([v,-u])
    
def show_methode2():
    a = -30
    b = 30
    n = 1000
    x0, y0, z0 = 0, 0, 1
    
    Lx, Ly = euler1(G, a, b, x0, np.array([y0, z0]), n)
    pl.plot(Lx, np.array(Ly)[:,0], label='euler1 vect') # courbe methode 2
    
    Lx, Ly = euler2(lambda x, y, y1:-y, a, b, x0, y0, z0, n)
    pl.plot(Lx, Ly, label='euler2') # courbe approché
    x= np.linspace(a, b, n)
    pl.plot(x, np.sin(x), label='sin') # courbe exact
    pl.legend()
    
#show_methode2()

def pend(x, Y):
    u, v = Y
    return np.array([v, -np.sin(u)])

def show_pend(z0):
    
    a = 0
    b = 20
    n = 1000
    x0, y0 = a, 0
    
    for i in range(len(z0)):
        Lx, Ly = euler1(pend, a, b, x0, np.array([y0, z0[i]]), n)
        l = 'z0 =' + str(z0[i])
        pl.plot(np.array(Ly)[:,0], np.array(Ly)[:,1], label=l) # courbe methode 2
        pl.legend()
        pl.show()
    
#show_pend([0.5,1,2,2.05,2.4])

def heun(F, a, b, x0, y0, n):
    Ly = [y0]
    Lx = [x0]
    x= x0
    y= y0
    h=(b-a)/n
    while x <= b:
        f = F(x,y)
        y= (h/2)*(f+F(x+h,y+h*f))+y
        x+=h 
        Lx.append(x) 
        Ly.append(y)
    x= x0
    y= y0
    while x >= a:
        f = F(x,y)
        y= (-h/2)*(f+F(x-h,y-h*f))+y
        x-=h 
        Lx.insert(0, x) 
        Ly.insert(0,y)
    return Lx, Ly
    
def show_heun():
    a = -5.0
    b = 5.0
    n = 30
    x0, y0 = 0, 1
    
    Lx, Ly = euler1(lambda x, y:y, a, b, x0, y0, n)
    pl.plot(Lx, Ly, label='euler1') # courbe approché
    Lx, Ly = heun(lambda x, y:y, a, b, x0, y0, n)
    pl.plot(Lx, Ly, label='heun') # courbe approché
    x= np.linspace(a, b, n)
    pl.plot(x, np.exp(x), label='exp') # courbe exact
    pl.legend()
    pl.show()

show_heun()

