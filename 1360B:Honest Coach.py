t = int(input())

ans = []
while(t!=0):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    l1 = []
    a = 0
    i = 1
    for i in range(len(l)):
        a = l[i]-l[i-1]
        l1.append(abs(a))

    ans.append(min(l1))    
    t = t-1
for j in range(len(ans)):
    print(ans[j])
    




    






