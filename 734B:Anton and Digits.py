k2,k3,k5,k6 = map(int,input().split())

x = min(k5,k6)

y = min(k2,k3)

#print(x,y)
#print(x+y>k2)

if x+y<=k2:
    a = (x*256) + (y*32)
    print(a)

elif x+y>k2:
    z = min(k2,k5,k6)
    if(z<=k2) :
        print((k2-z)*32 + z*256)
        
    else :
        print(z*256)
       


