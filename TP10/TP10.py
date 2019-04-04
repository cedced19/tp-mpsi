import numpy as np
import matplotlib.pyplot as plt
from math import *

#plt.figure()
#X = np.linspace(-np.pi, np.pi, 256)
#C = [np.cos(x) for x in X]
#S = [np.sin(x) for x in X]
#plt.plot(X, C)
#plt.plot(X, S)
#plt.show()

def f(x,mu):
    return mu*x*(1-x)

def logistique1 (mu,x0, n):
    Ly=[x0]
    Lx=[0]
    x=0
    yn = x0
    for i in range(n):
        yn = f(yn,mu)
        Ly.append(yn)
        x+=1
        Lx.append(x)
    plt.figure()
    plt.plot(Lx, Ly, marker="s")
    plt.show()
    
#logistique1(1.6, 0.9,20)

def logistique2 (mu,x0, n):
    Ly=[0]
    Lx=[x0]
    yn = x0
    for i in range(n):
        Lx.append(yn)
        yn = f(yn,mu)
        Ly.append(yn)
        Lx.append(yn)
        Ly.append(yn)
    plt.figure()
    X = np.linspace(0, 1, 256)
    S = [f(x,mu) for x in X]
    C = [x for x in X]
    plt.plot(X, S)
    plt.plot(X, C)
    plt.plot(Lx, Ly, marker="s")
    plt.ylim(0,1)
    plt.show()

#logistique2(2.8, 0.9,10)
# mu ∈ [0,1] (converge vers 0)
#logistique2(0.5, 0.9,10)
# mu ∈ [1,2] (converge vers mu-1/mu)
#logistique2(1.5, 0.9,10)
# mu ∈ [2,3] (converge plus vite vers mu-1/mu que mu ∈ [1,2] )
#logistique2(2.5, 0.9,10)
# mu = 3.05 (converge lentement)
#logistique2(3.05, 0.9,10)
# mu = 3.5
#logistique2(3.5, 0.9,10)
# mu = 3.86
#logistique2(3.86, 0.9,10)

def cycle(mu):
    n=0
    x0=0.9
    L=[]
    for i in range(200):
        x0 = f(x0,mu)
        n+=1
        if (n>=101):
            #print(n, round(x0,3))
            x=round(x0,3)
            if ((x in L) == False):
                L.append(x)
    return L


#print(cycle(3.4))

def bifurcation(a,b,pas):
    N=(b-a)/pas
    mu=a
    plt.figure()
    for i in range(int(N+1)):
      val = cycle(mu)
      plt.plot([mu]*len(val), val, marker=',', linestyle='')
      mu+=pas  
    plt.ylim(0,1)
    plt.show()
    
#bifurcation(2,4,0.002)

def f1(x,mu):
    return mu-mu*2*x

def lyapunov(mu, x0, n):
    s=0
    yn=x0
    Ly=[x0]
    for i in range(n):
        yn = f(yn,mu)
        Ly.append(yn)
    for k in Ly:
        s+=log(abs(f1(k,mu)))
    return s/n
    
#print(lyapunov(2.5, 0.9, 200))

def lyapunov_diag(mumin, mumax, N, interne):
    pas=(mumax-mumin)/N
    mu=mumin
    Lx=[]
    Ly=[]
    plt.figure()
    for i in range(int(N)):
      Ly.append(lyapunov(mu, 0.9, interne))
      Lx.append(mu)
      mu+=pas  
    print(Lx, Ly)
    plt.plot(Lx, Ly)
    plt.xlim(mumin,mumax)
    X = np.linspace(mumin, mumax, 256)
    C = [0 for x in X]
    plt.plot(X, C)
    plt.show()
    
lyapunov_diag(3,4,512,100)
