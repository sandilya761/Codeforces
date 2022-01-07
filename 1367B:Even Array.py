t = int(input())
while t:
    t=t-1
    n = int(input())
    l = list(map(int,input().split()))
    count = 0
    count_1 = 0
    for i in range(n):
        if i%2!=l[i]%2:
            if i%2==0:
                count = count + 1
            else:
                count_1 = count_1+1
    if count==count_1:
        print(count)
    else:
        print(-1)