#!/usr/bin/python3

import math
import matplotlib.pyplot as pl

# pi
def f(x):
	return(4/(1+x**2))

# 0.693147
def g(x): 
	return(1/x)

# pi
def h(x): 
	return(6/(math.sqrt(1-x**2)))

def rectangle(f,a,b,n):
	s=0
	d = (b-a)/n 
	xk=a
	
	for i in range(0,n):
		s+=f(xk+d/2)
		xk+=d
	return (s*d)


print(rectangle(f,0,1,1000))


def trapeze_naif(f,a,b,n):
	s=0
	d = (b-a)/n 
	xk=a
	
	for i in range(0,n):
		s+=(f(xk)+f(xk+d))/2
		xk+=d
	return (s*d)


print(trapeze_naif(f,0,1,1000))

def trapeze(f,a,b,n):
	s=0
	d = (b-a)/n 
	xk=a
	
	for i in range(0,n):
		xk+=d
		s+=(f(xk))
	
	xk+=d
	s+=(f(xk)/2)
		
	return (s*d)


print(trapeze(f,0,1,1000))


def simpson_naif(f,a,b,n):
	s=0
	d = (b-a)/n 
	xk=a
	
	for i in range(0,n):
		s+=(f(xk)+4*f(xk+d/2)+f(xk+d))
		xk+=d
		
	return (s*d*1/6)

print(simpson_naif(f,0,1,1000))

def simpson(f,a,b,n):
	
	d = (b-a)/n 
	xk=a
	s=f(xk)+4*f(xk+d/2)
	
	for i in range(1,n):
		xk+=d
		s+=2*f(xk)+4*f(xk+d/2)
		
	
	xk+=d
	s+=(f(xk))
	
	return (s*d*1/6)

print(simpson(f,0,1,1000))


def pre_list(n):
	pre=[]
	x=0.1
	for i in range(n):
		x=x/2
		pre.append(x)
	return(pre)

listepre=pre_list(20)

def nb_appel(methode,f,a,b,exact,listepre):
	L=[]
	for i in range(20):
		c=1
		while(abs(exact-methode(f,a,b,c))>listepre[i]):
			c+=1
		# en fonction de la methode on devrait avoir c, c+1 ou 2*c+1 mais au final c'est négligeable
		L.append(c)
	return L

#print(nb_appel(trapeze,f,0,1,math.pi,listepre))
#print(nb_appel(simpson,f,0,1,math.pi,listepre))





def show():
	# affiche graphique
	for i in ['trapeze', 'simpson', 'rectangle']:
		y=nb_appel(eval(i),f,0,1,math.pi,listepre)
		x=[math.log(elt)/math.log(10) for elt in listepre]
		pl.plot(x,y,label=i)
		pl.legend()
		pl.xlabel('precision en 10^x')
		pl.ylabel('nombres appels à f')
		pl.title('fonction f')
	pl.show()
		
#show()


# la méthode simpson est celle qui demande le moins d'appel à f pour avoir une grande précision

def isRectangle(a,b,c):
	if (a== max(a,b,c)):
		if (a**2 == b**2 + c**2):
			return True
	elif (b == max(a,b,c)):
		if (b**2 == a**2 + c**2):
			return True
	else:
		if (c**2 == b**2 + a**2):
			return True
	return False

def triangle1(p):
	l=[]
	for a in range (1,p+1):
		for b in range (1,p+1):
			for c in range (1,p+1):
				if ((a+b+c) == p) & isRectangle(a,b,c):
					l.append((a,b,c))
	return l

#print(triangle1(12))

def triangle2(p):
	l=[]
	for a in range (1,p+1):
		for b in range (1,p+1):
				c=p-a-b
				if (isRectangle(a,b,c)) & (c>=1):
					l.append((a,b,c))
	return l

print(triangle2(12))