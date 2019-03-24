#!/usr/bin/env python

from math import exp, sqrt
import matplotlib.pyplot as pl
 
def chameau (E_0, m, a, X_0, V_0, N, t_fin):
    h = t_fin/N
    x=0
    y=X_0
    y1=V_0
    Lx=[0]
    Ly=[X_0]
    for i in range(N+1):
        y2=((E_0)/(m*a**2))*2*y*(-1+(y**2)/(a**2))*exp(-(y**2)/(a**2))
        y=y+h*y1
        Ly.append(y)
        y1=y1+h*y2
        x+=h
        Lx.append(x)
    return Lx,Ly
 
def show_chameau(r):
    Lx, Ly = r
    pl.plot(Lx, Ly)
    pl.legend()
    pl.show()
#show_chameau(chameau(300,0.2565,50,12,15,10000,10))
 
def tartaglia(m, rho, S, C_x, X_0, V_X0, V_Y0, Y_0, N, t_fin):
    h = t_fin/N
    L_abs=[0]
    L_ord1=[X_0]
    L_ord2=[Y_0]
    p=0
    x=X_0
    x1=V_X0
    y=Y_0
    y1=V_Y0
    for i in range(N):
        x2=-(1/(2*m))*rho*S*C_x*sqrt(x1**2 + y1**2)*x1
        y2=-9.8-(1/(2*m))*rho*S*C_x*sqrt(x1**2 + y1**2)*y1
        x=h*x1+x
        y= y + h*y1
        x1=h*x2+x1
        y1=h*y2+y1
        p=p+h
        L_abs.append(p)
        L_ord1.append(x)
        L_ord2.append(y)
 
    return L_abs, L_ord1, L_ord2
 
def show_tartaglia(r):
    Lt, Lx, Ly = r
    pl.plot(Lt, Ly, label='y')
    pl.plot(Lt, Lx, label='x')
    pl.xlabel('$t$')
    pl.legend()
    pl.show()
 
# tartaglia(m, rho, S, C_x, X_0, V_X0, V_Y0, Y_0, N, t_fin)
# show_tartaglia(tartaglia(1.5,1.25,5.7,1,5,5,7,10,10000,5))