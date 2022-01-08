t = int(input())

answer = []
while(t!=0):

    n = int(input())
    a = list(map(int, input().split()))
    a.sort()    
    l = list(set(a))
    answer.append(len(l))
    t = t-1

print('\n'.join(map(str, answer)))
