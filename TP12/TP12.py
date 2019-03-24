import  scipy  as sp
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math as m

from PIL import Image as Im

#im1=Im.open('/tmp/plazzaspania.png')
#im1.show()

#larg,haut=im1.size
#print(larg,haut)

#imNB=Im.new('RGB', (larg,haut))

#for y in range(haut):
    #for x in range(larg):
        #p=im1.getpixel((x,y))
        #gris=int((p[0]+p[1]+p[2])/3)
        #r=gris
        #g=gris
        #b=gris
        #imNB.putpixel((x,y), (r,g,b))
        
#imNB.save('/tmp/plazzaspaniaNoirBlanc.png')
#imNB.show()


def question1 (path):
    im1=Im.open(path)
    larg,haut=im1.size
    
    n=larg*haut
    
    s=[0]*256
    
    moyenne = 0
    for y in range(haut):
        for x in range(larg):
            p=im1.getpixel((x,y))
            g=(int((p[0]+p[1]+p[2])/3))
            s[g]+=1
            moyenne+=g
            
    moyenne=moyenne/n
    
    v = 0
    for y in range(haut):
        for x in range(larg):
            p=im1.getpixel((x,y))
            g=(int((p[0]+p[1]+p[2])/3))
            v += (g - moyenne)**2
    
    return n, s, moyenne, m.sqrt(v/n)
    
    
    
#print(question1('/tmp/plazzaspania.png'))



def histogramme(path):
    plt.plot(range(0, 256), question1(path)[1])
    plt.show()
    
#print(histogramme('/tmp/plazzaspania.png'))

def seuillage (path, val):
    im1=Im.open(path)
    larg,haut=im1.size
    
    imNB=Im.new('RGB', (larg,haut))
    
    for y in range(haut):
        for x in range(larg):
            p=im1.getpixel((x,y))
            g=(int((p[0]+p[1]+p[2])/3))
            if (g > val):
                result=255
            else:
                result=0
            r=result
            g=result
            b=result
            imNB.putpixel((x,y), (r,g,b))
            
    imNB.show()
    
#seuillage('/tmp/plazzaspania.png', 128)

def rot90 (path, trigo):
    im1=Im.open(path)
    larg,haut=im1.size
    
    imRot=Im.new('RGB', (haut, larg))
    
    if (trigo == False):
        for y in range(haut):
            for x in range(larg):
                imRot.putpixel((haut-y-1,x), im1.getpixel((x,y)))
    else:
         for y in range(haut):
            for x in range(larg):
                imRot.putpixel((y, x), im1.getpixel((x,y)))
                
    imRot.show()



#rot90('/tmp/plazzaspania.png', False)
#rot90('/tmp/plazzaspania.png', True)

def cadre (path, e, color):
    im1=Im.open(path)
    larg,haut=im1.size
    
    imNew=Im.new('RGB', (larg+2*e, haut+2*e))
    
    for y in range(haut+2*e):
        for x in range(larg+2*e):
            if ((x<e or x>e+larg) or (y<e or y>e+haut)):
                imNew.putpixel((x, y), color)
    for y in range(haut):
        for x in range(larg):
            imNew.putpixel((x+e, y+e), im1.getpixel((x,y)))
            
    imNew.show()

#cadre('/tmp/plazzaspania.png', 20, (258,0,0))

