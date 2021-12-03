n = int(input())

l = []
if n%2==1:
    print("-1")

else:
    l.append(2)
    l.append(1)
    i = 3
    while (i<=n):
        l.append(i+1)
        l.append(i)
        i = i+2

    for i in l :
        print(i,end=" ")
