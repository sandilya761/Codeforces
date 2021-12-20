n,m = map(int,input().split())
m %= (n * (n + 1) / 2)
i=1
if m<i:
    print("0")

else:
    while(i<=n):
        #print(i)
        if m<i:
            break

        m = m-i
        i=i+1

    print(int(m))

