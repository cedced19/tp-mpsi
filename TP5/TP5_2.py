#!/usr/bin/python3

from math import *
import random

def Fibonacci(un_2, un_1):
	return un_2+un_1

print('\nFibonacci')	
print(Fibonacci(0,1))
print(Fibonacci(1,Fibonacci(0,1)))

def Fibonacci_liste(n):
	L=[]
	for i in range(n):
		if ((i==0) | (i==1)):
			L.append(i)
		else:
			L.append(Fibonacci(L[len(L)-1],L[len(L)-2]))
	return L
		

print('\nFibonacci_liste')	
print(Fibonacci_liste(0))
print(Fibonacci_liste(1))
print(Fibonacci_liste(2))
print(Fibonacci_liste(6))

def Fibonacci_rap(L):
	if (len(L)>1):
		rapport=[]
		for i in range(2, len(L)):
			rapport.append(L[i]/L[i-1])
		return rapport
print('\nFibonacci_rap')
print(Fibonacci_rap(Fibonacci_liste(15)))


def Fibonacci_rap_lim(eps):
	gold=(1+sqrt(5))/2
	un=1
	un_1=1
	i=1
	while (abs(un_1/un - gold) >= eps):
		(un, un_1) = (un_1, Fibonacci(un,un_1))
		i+=1
	return i
	
print('\nFibonacci_rap_lim')
print(Fibonacci_rap_lim(0.0000001))

def rechmot(motif, ch):
	count=0
	i=0
	found=False
	while (count <= len(ch)):
		if (i == len(motif)):
			found=True
			break
		if(motif[i] == ch[count]):
			i+=1
		else:
			i=0
		count+=1
	if found == True:
		return(count-len(motif)+1)
	else:
		return 0
	
print('\nRecherche de mot')
print(rechmot('ba', 'abibac'))

def rechmot_mult(motif, ch):
	L=[]
	i=0
	found=False
	for k in range(len(ch)):
		if(motif[i] == ch[k]):
			i+=1
		else:
			i=0
		if (i == len(motif)):
			L.append(k)
			found=True
			i=0
	if found == True:
		return L
	else:
		return []

print('\nRecherche des mots')
print(rechmot_mult('ba', 'abibaoubac'))

def monte_carlo(n):
	count=0
	for i in range(n):
		x=random.random()
		y=random.random()
		if (x**2 + y**2 <= 1):
			count+=1
	return(count/n*4)

print('\nMonte Carlo')
print(monte_carlo(100000))
print(monte_carlo(5))
print(monte_carlo(4))


def monte_carlo_test(eps):
	n=1
	while (abs(monte_carlo(n) - pi) >= eps):
		n+=1
	return n

print('\nMonte Carlo Test')
print(monte_carlo_test(0.1))
print(monte_carlo_test(0.01))

def monte_carlo_test_opti(eps):
	n=1
	ratio=0
	count=0
	while (abs(ratio - pi) >= eps):
		x=random.random()
		y=random.random()
		if (x**2 + y**2 <= 1):
			count+=1
		ratio=(count/n*4)
		n+=1
	return n

print('\nMonte Carlo Test Optimisé')
print(monte_carlo_test_opti(0.1))
print(monte_carlo_test_opti(0.01))