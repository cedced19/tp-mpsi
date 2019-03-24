from math import * 

def degre(P):
	for i in range(len(P)-1, 0, -1):
		if P[i] != 0:
			return i
	return 0

#print(degre([0,1,2,3,0,5,9,0]))
#print(degre([0]))
#print(degre([0,0,0]))
#print(degre([0,1]))
#print(degre([0,1,2,3,0,5,0,0]))

def reduc(P):
	c = len(P)-1
	r = False
	while (c >= 1 and r == False):
		if P[c] == 0:
			P.pop(c)
		else:
			r = True
		c-=1
	return P

#print(reduc([0,1,2,3,0,5,0,0]))
#print(reduc([0,1,2,3,0,5]))
#print(reduc([1]))
#print(reduc([0]))
#print(reduc([0,0,0]))
#print(reduc([0,0,0,0,0,0,0]))

def poly_add(P, Q):
	n=len(P)
	m=len(Q)
	if m>n:
		P=P+[0]*(m-n)
	else:
		Q=Q+[0]*(n-m)
	for i in range(len(P)):
		P[i]+=Q[i]
	return reduc(P)

#print(poly_add([2,3],[3,4]))

def poly_scal(P, a):
	for i in range(len(P)):
		P[i]*=a
	return reduc(P)

#print(poly_scal([2,3],3))

def poly_multi(P, Q):
	n=len(P)
	m=len(Q)
	S=[]
	if m>n:
		P=P+[0]*(m-n)
	else:
		Q=Q+[0]*(n-m)
	for k in range(n+m+1):
		v=0
		for i in range(len(P)):
			for j in range(len(Q)):
				if i+j==k:
					v+=P[i]*Q[j]
		S.append(v)
	return reduc(S)

#print(poly_multi([1,1,1],[1,1,1]))

def eval_naif(P,a):
	S=0
	pw=1
	for i in range(len(P)):
		S+=P[i]*pw
		pw*=a
	return S

def Horner(P,a):
	P=reduc(P)
	p=len(P)-1
	cnt=P[p]
	for i in range(p-1, -1, -1):
		cnt=P[i]+a*cnt
	return cnt

#print(eval_naif([1,1,1],2))
#print(Horner([1,1,1],2))

def tchebychev(n):
	t0 = [1]
	t1 = [0,1]
	
	for i in range(2, n+1):
		(t1, t0)  = (poly_add(poly_multi(poly_scal([0,1],2),t1), poly_scal(t0,-1)), t1)
	return t1

#print(tchebychev(2))

def binomial (k, n):
	num = 1
	den = 1
	for i in range(n-k+1,n+1):
		num*= i
	for i in range(1,k+1):
		den*= i
	return num // den

def tchebychev_sigma(n):
	S=[]
	C=[1]
	D=[0]*(n)+[1]
	for k in range(n//2+1):
		S=poly_add(poly_scal(poly_multi(D, C), binomial(2*k, n)), S)
		D=[0]*(n-2*k-2)+[1]
		C=poly_multi(C, [-1,0,1])
	return S

#print(Horner(tchebychev(3),4))
#print(Horner(tchebychev_sigma(3),4))
#print(tchebychev(2))

#print(Horner(tchebychev(100),cos(5)))
#print(cos(500))

def div_poly(A, B):
	Q=[]
	R=A[:]
	n=degre(R)
	p=degre(B)
	b=B[p]
	for k in range(n,p-1,-1):
		a = R[k]
		Q.append(a/b)
		R = poly_add(R, poly_multi(poly_scal([0]*(k-p)+[1],-a/b), B))
	return(Q[::-1], R)

#print(div_poly([1,1,0,1], [1,1])) => ([2, -1, 1], [-1])

def div_poly_opt(A, B):
	Q=[]
	R=A[:]
	n=degre(R)
	p=degre(B)
	b=B[p]
	for k in range(n,p-1,-1):
		a = R[k]
		Q.append(a/b)
		for i in range(p+1):
			c = -a/b*B[i]
			R[k-p+i]+=c 
	return(Q[::-1], R)

#print(div_poly_opt([1,1,0,1], [1,1]))


def compose(P, Q):
	P=reduc(P)
	Qn = [1]
	R=[0]
	for i in range(len(P)):
		R=poly_add(poly_scal(Qn[:], P[i]), R) 
		Qn = poly_multi(Qn, Q)
	return R 

#print(compose([0,1,1], [1,1]))
