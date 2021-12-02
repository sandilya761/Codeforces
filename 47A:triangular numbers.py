n = int(input())
l = []
for i in range(1,501):
    k = (i*(i+1))/2
    l.append(k)

if n in l:
    print("YES")

else:
    print("NO")
            