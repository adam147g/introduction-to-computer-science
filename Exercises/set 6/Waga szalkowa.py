print('Dany jest zestaw odważników(odw). Jakie ciężary można odważyć za użyciem tych odważników?')
odw=[1,3,5,10,16,24]

def waga(li,n,p=0):
    if n==0:    return True
    if n<0: return False
    if p==len(li):  return False   #len to długość listy li
    return waga(li,n-li[p],p+1) or waga(li,n,p+1)
#end def

for w in range(0,50):               #sprawdzamy czy to wszystko zachodzi dla liczb 0-49
    print(w,waga(odw,w))            #lub print(w,waga(odw,w,0))


print('To samo, ale można dodawać odważniki do obu stron wagi')
odw=[1,3,5,10,16,24]

def waga(li,n,p=0):
    if n==0:    return True
    if p==len(li):  return False
    return waga(li,n-li[p],p+1) or waga(li,n,p+1) or waga(li,n+li[p],p+1)
#end def

for w in range(0,50):
    print(w,waga(odw,w))

print('To co wcześniej, ale z wypisywaniem rozwiązań')
odw=[1,3,5,10,16,24]

def waga(li,n,p=0,res=[]):
    if n==0:
        print(res)
        return True
    if p==len(li):
        return False
    return waga(li,n-li[p],p+1,res+[li[p]]) or waga(li,n,p+1,res) or waga(li,n+li[p],p+1,res+[-li[p]])
#end def

for w in range(0,50):
    print(w,waga(odw,w))