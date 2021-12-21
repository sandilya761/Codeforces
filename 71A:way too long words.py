n = int(input())
l = []
answer = []
while(n>0):
    s = input()
    l.append(s)
    n = n-1

for i in range(len(l)):
    if len(l[i])<=10:
        answer.append(l[i])

    else:
        k = len(l[i])
        a = l[i]
        list(a)
        b = a[1:-1]
        c=[]
        c.append(a[0])
        c.append(k-2)
        c.append(a[-1])
        d = ''.join(map(str, c))
        #print(d)
        answer.append(d)


for j in range(len(answer)):
    print(answer[j])

