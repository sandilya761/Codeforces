s1,s2,s3,s4 = map(int,input().split())

l = [s1,s2,s3,s4]

l1 = []

for i in l:
    if i not in l1:
        l1.append(i)

print(4-len(l1))



