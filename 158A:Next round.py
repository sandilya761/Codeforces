n,k = map(int,input().split())
k1 = k-1
l = list(map(int,input().split()))
count = 0
for i in range(len(l)):
    if l[i]>=l[k1] and l[i]>0:
        count = count+1

print(count)

