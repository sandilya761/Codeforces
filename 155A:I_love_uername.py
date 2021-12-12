n = int(input())
l = list(map(int,input().split()))

maximum = 0
minimum = 0
a=0
b=0
c=0
for i in range(len(l)):
    if maximum<l[i]:
        a= a+1
    if minimum>l[i]:
        b = b+1

c = a+b-2
#print(c)


if a+b==n and maximum!=minimum:
    print(n-1)

else:
    if c<0:
        print("0")
    else:
        print(c)

