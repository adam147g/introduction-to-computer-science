print('Liczenie par liczb o zadanym iloczynie')
import random
def generuj(n):
    return[random.randint(1,9) for _ in range(n)]
def licz_pary(l,s):
    licz=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]*l[j]==s:
                licz=licz+1
    print('pary',licz)
#end def
t=generuj(20)
licz_pary(t,24)

print('Licz pary w tablicy 2-wymiarowej')
N=10
licz=0
suma=int(input('Wpisz liczbe(ile ma wynosic suma): '))

T=[[random.randint(1,9) for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                if i!=k or j!=l:
                    if T[i][j]+T[k][l]==suma:
                        licz +=1

licz = licz/2   #bo każdą parę liczymy 2 razy

print(licz)


print('Linearyzacja tablicy. Czyli zamiana tablicy 2-wymiarowej na 1-wymiarową')
for i in range(N*(N-1)):
    for j in range(i+1,N*N):
        if T[i%N][i//N]+T[j%N][j//N]==s:
            licz+=1
print(licz)

print('Przykład - Licz trójki')
def licz_trojki(l,s):
    licz=0
    for i in range(len(l-2)):
        if s%l[i]==0:
            for j in range(i+1,len(l-1)):
                if s%l[j]==0:
                    for k in range(j+1,len(l)):
                        if l[i]*l[j]*l[k]==s:
                            licz+=1
    print('Trójki: ',licz)
#end def
t=generuj(20)
licz_trojki(t,24)

print('Policz n-ki')
def licz_n_ki(l,s,n,p=0):               #l- tablica, s- iloczyn szukany, n- wielkość tych n-ek, p- pomocniczy parametr
    global licznik
    if n==1:
        for i in range(p,len(l)):
            if l[i]==s: licznik+=1
    else:
        for i in range(p,len(l)):
            if s%l[i]==0:   licz_n_ki(l,s//l[i],n-1,i+1)
#end def
t=generuj(20)
licznik=0
licz_n_ki(t,24,4)
print('n-ki',licznik)