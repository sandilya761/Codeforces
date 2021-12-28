x = int(input())
s = []
for i in range(x):
    s.append(input())

for n in range(x):
    ones = []
    count = 0
    for c in s[n]:
        if c == '1':
            count += 1
        else:
            if count:
                ones.append(count)
                
                count = 0
    if count:
        ones.append(count)
    #print(ones)
    onessorted = sorted(ones, reverse=True)
    #print(onessorted)
    print(sum(onessorted[0::2]))