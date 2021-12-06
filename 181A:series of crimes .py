n,m = map(int,input().split())


mat = []
for i in range(n):
   p = list(map(str, input().split()))
   mat.append(p)
l=[]
for i in range(n):
    for j in range(m):
        if mat[i][j]=='*':
            temp = [i,j]
            l.append(temp)
                
l1,l2,l3 =l[0],l[1],l[2]

#print(l1,l2,l3)


if l1[1]==l2[1]:
    x = abs(l1[0]-l2[0])
    x_new = abs(l3[0]-x)
    print(x_new+1,l3[1]+1)

if l2[1]==l3[1]:
    x = abs(l2[0]-l3[0])
    x_new = abs(l1[0]-x)
    print(x_new+1,l1[1]+1)

if l3[1]==l1[1]:
    x = abs(l1[0]-l3[0])
    x_new = abs(l2[0]-x)
    print(x_new+1,l2[1]+1)



        



