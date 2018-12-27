#!/usr/bin/python3

def bonjour():
	print('Bonjour!')

def commentva():
	print('Comment ça va ?')


bonjour()
commentva()

def somme(L):
	s = 0
	for val in L:
		s+=val
	return s

def produit(L):
	s = 1
	for val in L:
		s*=val
	return s

def moyenne(L):
	return somme(L) / len(L)

def maximum(L):
	m = 0
	for val in L:
		if (val > m) :
			m = val
	return m

def minimum(L):
	m = maximum(L)
	for val in L:
		if (val < m) :
			m = val
	return m

print(somme([1,2,3]))
print(moyenne([1,2,3]))
print(produit([1,2,3]))
print(maximum([1,2,4,3]))
print(minimum([1,2,4,0.5,3]))

def variance(L):
	v = 0
	for i in range(0, len(L)):
		v += (L[i] - moyenne(L))**2
	return v/len(L)
	
print(variance([4,3,8,1,7]))

def pairT_impairF(x):
	"""renvoit Vrai si pair Faux si impair"""
	assert type(x) is int
	if x%2 == 0 :
		return True
	else :
		return False

def carrepair(x):
	assert type(x) is int
	c = x**2
	if (pairT_impairF(c)):
		return c
	else:
		return 0

print(carrepair(2)) # doit renvoyer 4 car 2**2 est pair
print(carrepair(3)) # doit renvoyer 0 car 3**2 est impair

def f(x):
	if x%2 == 0:
		return(x//2)
	else:
		return(3*x+1)

def syrac_terme(a,n):
	for i in range(n):
		a = f(a)
	return a

print(syrac_terme(97,1))
print(syrac_terme(97,2))
print(syrac_terme(97,3))
print(syrac_terme(97,4))
print(syrac_terme(97,10))
print(syrac_terme(97,11))
print(syrac_terme(97,100))

def syracuse(a):
	L=[]
	while((a != 1) & (a!=2) & (a!=4)):
		L.append(a)
		a=f(a)
	return L

print(syracuse(97))
print(syracuse(5))

def syrac_plus(a):
	valInitial = a;
	tv = 0
	cta=0
	ta=None
	h=0
	ih=0
	while (a != 1):
		if(ta != None):
			cta+=1 #compteur pour ta
		tv+=1
		if (a>h):
			h=a
			ih=tv
		if((ta != None) & a<=valInitial):
			ta=cta-1
		a=f(a)
		
	return(tv,ta,ih,h)
			

print(syrac_plus(97))
print(syrac_plus(10))
print(syrac_plus(8))
print(syrac_plus(5))
print(syrac_plus(7))
print(syrac_plus(11))
print(syrac_plus(29))

def syracuseUntilOne(a):
	L=[]
	while((a != 1)):
		L.append(a)
		a=f(a)
	L.append(1)
	return L

def syracs(maxi, val):
	s=[]
	for i in range(1,maxi+1):
		L=syracuseUntilOne(i)
		if (val in L):
			s.append(i)
	return s
print(syracs(1000,1223))