t = int(input())
a = []
b = []
count = 0
answer = []
while t:
    t = t-1
    #print(t)
    n = int(input())
    #print(n)
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    #print(a,b)
    a_min = min(a)
    b_min = min(b)
    for i in range(n):
        count = count + max(a[i]-a_min,b[i]-b_min)
    

    print(count)
