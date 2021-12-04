n,m = map(int,input().split())

k = n-m
#print(k)
count = 0   

b = 0
#a_square = a**2


while(b*b<=m and b<=n):
    a = m-b*b
    if b+(a*a)==n:
        count = count+1
    b = b+1    


print(count)