import math
a,b,n = map(int,input().split())
x=0
y=0

 
while((n-x)>=0 or (n-y)>0):
    x = math.gcd(a,n)
    n = n-x
    if (n-x)< 0:
        print("0")
    else:
        y = math.gcd(b,n)
        n = n-y
        if (n-y)<0:
            print("1")
        




