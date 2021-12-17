n = int(input())

l = list(map(int,input().split()))
ans = [0]*n
for i in range(1,len(l)+1):
    ans[l[i-1]-1] = i   #assign the ans list with the index of the list

for i in range(len(ans)):
    print(ans[i],end=" ")



