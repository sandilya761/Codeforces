n,m = map(int,input().split())

lower = 2
upper = 50
prime = []

for num in range(lower, upper + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           prime.append(num)

if n in prime and m in prime:
    a = prime.index(n)
    b = prime.index(m)

    if b-a==1:
        print("YES")

    else:
        print("NO")

else:
    print("NO")
