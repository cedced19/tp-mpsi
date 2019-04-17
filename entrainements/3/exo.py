
def binomial (k, n):
	num = 1
	den = 1
	for i in range(n-k+1,n+1):
		num*= i
	for i in range(1,k+1):
		den*= i
	return num // den


def coeff (n,alpha):
    def aux(n,alpha,l,c,arr):
        if n == c:
            return arr
        else:
            l=l*(alpha-c+1)/c
            arr.append(l)
            return aux(n,alpha,l,c+1,arr)
    return aux(n+1,alpha,1,1,[1])


#print(coeff(3,-1/2))

def puissance (n,p,ordre):
    arr = []

    # puissance (x^k)^p
    k=1
    while k*p <= ordre and k<n+1:
        arr.append((1,k*p))
        k+=1

    # puissance (k parmi n)*(x^a)^i*(x^b)^j
    for i in range(1,p):
        j=p-i
        koef=binomial(i, p)
        for a in range(1,n+1):
            if a*i > ordre:
                break
            else:
                for b in range(a+1,n+1):
                    if b*j > ordre:
                        break
                    else:
                        if (a*i+b*j <= ordre):
                            arr.append((koef,a*i+b*j))

    return arr

#print(puissance(4,3,4))

def get_poly(n,alpha):
    k_list = coeff(n,alpha)
    print(k_list)
    poly=[0]*(n+1)
    poly[0] = k_list[0]
    for i in range(1, n+1):
        for monome in puissance(n,i,n):
            if(monome[1] == 8):
                print(k_list[i], monome)
            poly[monome[1]]=poly[monome[1]]+monome[0]*k_list[i]
    return poly

print(get_poly(8,-1/2))