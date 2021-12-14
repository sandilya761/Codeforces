
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

if k==1 or l==1 or m==1 or n==1:
    print(d)
else:    
    a=[]
    i = k
    while(i<=d):# creates a list of multiples of k till d
        if i<=d:
            a.append(i)
            i = i+k
            
    b=[]
    j = l

    while(j<=d):# creates a list of multiples of l till d
        if j<=d:
            b.append(j)
            j = j+l
            
    c = []
    x = m
    while(x<=d):# creates a list of multiples of m till d
        if x<=d:
            c.append(x)
            x = x+m
            
    e = []
    y = n
    while(y<=d):# creates a list of multiples of n till d
        if y<=d:
            e.append(y)
            y = y+n
            
    complete = a+b+c+e  #combines all the multiple lists into a single list

    complete = set(complete)
    #print(complete)

    total = []
    for i in range(1,d+1):#total elements in the range of d
        total.append(i)

    total=set(total)

    #print(total)

    #print(len(total-complete))
    damaged_dragons = d-len(total-complete) # performs difference set operation and outputs the number of damaged dragons
    print(damaged_dragons)



