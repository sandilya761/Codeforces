n = int(input())
answer = []
while(n>0):
    n1 =int(input())
    l = list(map(int,input().split()))
    if len(set(l))==1:
        answer.append("YES")
    else:
        if len(l)==1:
            answer.append("YES")
        else:
            l.sort()
            #print(l)
            i = 1
            j = 1
            while(j<=n1):
                if len(l)==1:
                    answer.append("YES")
                else:
                    k = l[i-1]-l[i]
                    if abs(k)<=1:
                        l.remove(min(l[i],l[i-1]))
                        #print(len(l))
                        l.sort()
                        #print(l)
                        #print(j)
                j = j+1
            if len(l)!=1:
                answer.append("NO")
                        
            #print(l)
    n = n-1


for i in range(len(answer)):
    print(answer[i])





