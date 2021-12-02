n = int(input())

count = 0

for i in range(n):
    p,s,t = map(int,input().split())
    if (p==1 and s==1 and t==0) or (p==1 and t==1 and s==0) or (s==1 and t==1 and p==0) or (p==1 and s==1 and t==1):
        count = count+1

print(count)
