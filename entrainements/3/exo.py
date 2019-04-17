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

def poly_add(P, Q):
    n=len(P)
    m=len(Q)
    if m>n:
        P=P+[0]*(m-n)
        n=m
    else:
        Q=Q+[0]*(n-m)
        m=n
    for i in range(n):
        P[i]+=Q[i]
    return reduc(P)


def poly_scal(P, a):
	for i in range(len(P)):
		P[i]*=a
	return reduc(P)


def poly_multi(P, Q, order):
    n=len(P)
    m=len(Q)
    S=[]
    if m>n:
        P=P+[0]*(m-n)
        n=m
    else:
        Q=Q+[0]*(n-m)
        m=n
    for k in range(order+1):
        v=0
        for i in range(n):
            for j in range(n):
                if i+j==k:
                    v+=P[i]*Q[j]
        S.append(v)
    return reduc(S)


def coeff (n,alpha):
    def aux(n,alpha,l,c,arr):
        if n == c:
            return arr
        else:
            l=l*(alpha-c+1)/c
            arr.append(l)
            return aux(n,alpha,l,c+1,arr)
    return aux(n+1,alpha,1,1,[1])

def puissance (n):
    def aux(n,init,l,p,arr):
        if n == p:
            return arr
        else:
            l=poly_multi(init, l, n)
            arr.append(l)
            return aux(n,init,l,p+1,arr)
    
    arr=[1]*n
    arr[0]=0

    return aux(n,arr,arr,1,[arr])

def get_poly(n,alpha):
    k_list = coeff(n,alpha)
    poly_list = puissance(n) 
    l = [k_list[0]]
    for i in range(1,n+1):
        l = poly_add(poly_scal(poly_list[i-1], k_list[i]), l)
    return l

print(get_poly(10,-1/2))