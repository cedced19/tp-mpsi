import pickle

def crible(N):
	L=[True]*(N+1)
	L[0]=False
	L[1]=False 
	i=0
	while i*i <= N:
		if (L[i] == True):
			k=2
			while (i*k <= N):
				L[i*k]=False
				k+=1
		i+=1
	R=[]
	for i in range(2,N+1):
		if (L[i]==True):
			R.append(i)
	return R

#print(crible(10))

def test ():
	F = open('./test.txt', 'a')
	F.write('\nCeci est un test')
	F.close()
	
	F = open('./test.txt', 'r')
	print(F.read())
	F.close()
	
	F = open('./test.txt', 'rb')
	data = F.read()
	print(len(data))
	print([data[i] for i in range(len(data))])
	F.close()
	
	F = open('./test.txt', 'r')
	print(F.readlines())
	

#test()

def cribleNP(N):
	F = open('/tmp/NombrePremier_'+str(N), 'w')
	L=[True]*(N+1)
	L[0]=False
	L[1]=False 
	i=0
	while i*i <= N:
		if (L[i] == True):
			k=2
			while (i*k <= N):
				L[i*k]=False
				k+=1
		i+=1
	for i in range(2,N+1):
		if (L[i]==True):
			F.write(str(i) + '\n')
	F.close()

#cribleNP(10000)

def decomp(n):
	F = open('/tmp/NombrePremier_10000', 'r')
	data = F.readlines()
	for i in range(len(data)):
		data[i]= data[i].rstrip('\n')
	L=[]
	i=0
	while (n>1):
		p=int(data[i])
		while(n%p == 0):
			n = n // p
			L.append(p)
		i+=1
	return L

def decomp_PE(n):
	L=decomp(n)
	Le=[1]
	Li=[L[0]]
	for i in range(1,len(L)):
		if (L[i] != Li[len(Li)-1]):
			Li.append(L[i])
			Le.append(1)
		else:
			Le[len(Le)-1]+=1
	return Li, Le

#print(decomp_PE(3*3*3*3*11*17*23*23))

def PGCD(a,b):
	r = a % b
	while r != 0:
		a=b 
		b=r
		r=a%b 
	return b

#print(PGCD(2,3), PGCD(8,4))

def euclide (a,b):
	at=a
	bt=b
	au=1
	nu=0
	av=0
	nv=1
	q = at // bt
	r = at % bt
	while r != 0:
		(nu,au)=(au-q*nu,nu)
		(nv,av)=(av-q*nv,nv)
		at=bt 
		bt=r
		r=at%bt 
		q = at // bt
	return [bt, nu, nv]

print(euclide(3465,957))
print(euclide(9,3))
print(euclide(398746,91257))
print(euclide(156916,156913))