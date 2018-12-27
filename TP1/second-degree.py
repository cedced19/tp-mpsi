#!/usr/bin/python3


a=(3,4)
b=(5,4)
c=(6,4)

def produit_c(z1, z2): # produit entre un complexe et un autre complexe
	return (z1[0]*z2[0]-z1[1]*z2[1], z1[0]*z2[1]+z1[1]*z2[0])

def produit_r(r, z): # produit entre un réel et un complexe
	return (z[0]*r, z[0]*r)

def somme(z1, z2): 
	return (z1[0]+z2[0], z1[1]+z2[1])

delta=somme(produit_c(b,b), produit_r(-4, produit_c(a, c)))

if (delta == (0,0)):
	print("l'équation admet ubne racine double -({}i{})/(2({}+i{}))".format(b[0], b[1], a[0], a[1]))
else:
	