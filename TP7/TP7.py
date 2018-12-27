#!/usr/bin/python3
############################################################
## RECHERCHE de ZEROS A UNE FONCTION
############################################################
import sys
from math import *

##################################################################
## Fonctions de tests avec leur dérivée
##################################################################
# zéro = pi dans [-6,6]
def fpi(x):
	return tan(x/4)-1
def fpi_1(x):
	return 1/4*(1+tan(x/4)*tan(x/4))
#-----------------------------------------------------------------
# zéro = 0 sur R mais fonction plus "plate"
def fp(x):
	return(x-sin(x))
def fp_1(x):
	return(1-cos(x))
#-----------------------------------------------------------------
# zéro = 0 mais fonction plus tordue
# elle fait diverger la méthode de Lagrange
def ftest(x):
	if x== 0 : return 0
	else : return tan(x)-x*sin(1/x)
def ftest_1(x):
	if x== 0 : return 0 #bien que pas dérivable en 0 --> div/0
	else :
		return 1+tan(x)*tan(x)-sin(1/x)+1/x*cos(1/x)
#-----------------------------------------------------------------
# zéro = 0 : fonction tordue et applatie
def ftestp(x):
	if x== 0 : return 0
	else : return ftest(x)*ftest(x)*ftest(x) 
def ftestp_1(x):
	if x== 0 : return 0 #entraine --> div/0 dans newton 
	else :
		return 3*ftest_1(x)*ftest(x)*ftest(x)

from scipy.optimize import fsolve
print("avec SciPy\t\t:\t",fsolve(ftestp,1))

##############################################################
#affichage des fonctions
##############################################################
#import matplotlib.pyplot as pl
#import numpy as np
#x=np.linspace(-6,6,200)
#y=[fpi(t) for t in x]
#pl.plot(x,y)  # on utilise la fonction sinus de Numpy
#y=[0 for t in x] #axe des abscisses
#pl.ylabel('fonction : fpi')
#pl.plot(x,y)
#pl.xlabel("l'axe des abcisses")
#pl.show()

#import matplotlib.pyplot as pl
#import numpy as np
#x=np.linspace(-1/3,1/3,1000)
#y=[ftestp(t) for t in x]
#pl.plot(x,y)  # on utilise la fonction sinus de Numpy
#y=[0 for t in x] #axe des abscisses
#pl.ylabel('fonction : fpi')
#pl.plot(x,y)
#pl.xlabel("l'axe des abcisses")
#pl.show()
##############################################################
#Comparaison des méthodes avec un graphe
##############################################################

#import matplotlib.pyplot as pl

def pre_list(n):
	pre=[]
	x=0.1
	for i in range(n):
		x=x/2
		pre.append(x)
	return(pre)	

def affichage(a,b,f,f1,N,exact):
	for fct in [dicho_m,lagrange_opt_m,newtona_opt_m,newtonb_opt_m,totale_m] :
		listepre=pre_list(30)
		y=[]
		for pre in listepre:
			(val,bol,appel)=fct(a,b,f,f1,N,pre,exact)
			if bol:
				y.append(appel)
			else:
				y.append(0)
		x = [log(elt)/log(30) for elt in listepre]
		#pl.xlim(0,N)
		pl.plot(x,y,label=fct.__name__)
	pl.legend() #préparation affichage de la légende
	pl.xlabel('precision en 10^x') #légende en x
	pl.ylabel('nombres d\'appels à f') #légende en y
	pl.title('fonction '+ f.__name__) # titre
	pl.show() #Affichage à l'écran	
	
	
print(fsolve(fpi,1))
print('valeur de pi\t:\t',pi)

def dicho(aa,bb,f,pre):
    a = aa; b = bb
    c = (a+b)/2
    fa = f(a)
    fb = f(b)
    while  (b-a) > 2*pre:
        fc = f(c)
        if fc<0:
            a = c
            fa = fc
        else:
            b = c
            fb = fc
        c = (a+b)/2
    return c

print(dicho(-6,6,fpi,0.0000000000001))

def dicho_eps(aa,bb,f,N,pre):
    a = aa; b = bb
    c = (a+b)/2
    fa = f(a)
    fb = f(b)
    n=2
    eps=sys.float_info.epsilon
    while  ((b-a) > 2*pre) & (n<N):
        fc = f(c)
        n+=1
        if fc<0:
            a = c
            fa = fc
        else:
            b = c
            fb = fc
        c = (a+b)/2
        if abs(fc)<=eps:
            break
    if (n==N):
        return (c, False, n)
    else:
        return (c, True, n)


print(dicho_eps(-6,6,fpi,100,1e-8))
print(dicho_eps(-6,6,fpi,100,1e-12))
print(dicho_eps(-6,6,fpi,100,1e-16))

def lagrange(aa,bb,f,N):
	a = aa; b = bb
	fa=f(a)
	fb=f(b)
	c=(a*fb-b*fa)/(fb-fa)
	n=1
	while (n<N):
		fc = f(c)
		n+=1
		if fc<0:
			a = c
			fa = fc
		else:
			b = c
			fb = fc
		c=(a*fb-b*fa)/(fb-fa)
	return c

print(lagrange(-6,6,fpi,1))
print(lagrange(-1000000,1000000,fp,50))
print(lagrange(-1,3/2,ftestp,100))
print(lagrange(-1,3/2,ftestp,500))

lagrange_opt = lagrange  # déjà optimisé

def newtona(aa,bb,f,f1,N):
	a = aa
	fa=f(a)
	f1a=f1(a)
	n=1
	while (n<N):
		a=-fa/f1a + a
		fa = f(a)
		f1a = f1(a)
		n+=1
	return a

print(newtona(-6,6,fpi,fpi_1,100))
print(newtona(-1,3/2,ftestp,ftestp_1,100))
print(newtona(-1,3/2,ftestp,ftestp_1,500))

def totale(a,b,f,f1,N,pre):
	
	fa = f(a)
	fb = f(b)
	c = (a+b)/2
	n=0
	
	while ((b-a) > 2*pre) & (n<=N):
		n+=1
		
		# Dicho
		fc = f(c)
		if fc<0:
			a = c
			fa = fc
		else:
			b = c
			fb = fc
		
		# Lagrange
		c=(a*fb-b*fa)/(fb-fa)
		if (a<c) & (c<b):
			fc=f(c)
			
			if fc<0:
				a = c
				fa = fc
			else:
				b = c
				fb = fc
				
		# Newton en a
		fa1 = f1(a)
		c=-fa/fa1 + a
		if (a<c) & (c<b):
			if (f(c)<0):
				a=c
				fa=f(a)
			else:
				b=c
				fb=f(b)
		
		# Newton en b
		f1b = f1(b)
		c=-fb/f1b + b
		if (a<c) & (c<b):
			if (f(c)<0):
				a=c
				fa=f(a)
			else:
				b=c
				fb=f(b)
		
		c = (a+b)/2
	
	if (n==N): 
		return (c, False,n)
	else: 
		return (c,True,n)

print(totale(-6,6,fpi,fpi_1,50000,1e-12))
print(totale(-1,3/2,fp,fp_1,50000,1e-8))
print(totale(-1,3/2,ftest,ftest_1,50000,1e-12))
print(totale(-1,3/2,ftestp,ftestp_1,50000,1e-19))


