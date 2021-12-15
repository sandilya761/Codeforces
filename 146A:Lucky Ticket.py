
n = int(input())
s = input()
l=[]
l = list(map(int,s))
c = 0
for i in range(len(l)):
    if l[i]!=4 and l[i]!=7:
        c = c+1
if(c>=1):
    print("NO")
        
if(c==0) :
    l_left=[]
    l_right=[]
    l_left = l[0:n//2]
        #print(l_left)
    l_right = l[n//2:n+1]
    #print(l_right)
    if sum(l_left)==sum(l_right):
        print("YES")
    else:
        print("NO")    
