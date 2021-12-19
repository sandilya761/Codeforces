n = input()
l1 = list(map(int,n))

k = len(n)
#print(l1)
#print(k)
l = [4,7]

lucky_digits = 0
count=0

#print(l[0]==l1[0] or l[1]==l1[0])

if (len(l1)==1):
    print("NO")

else:
    for i in range(k):
        
        if l1[i] == l[0] or l1[i]==l[1]:
            lucky_digits = lucky_digits+1

    #print(type(lucky_digits))
    
    lucky_digits_list = list(map(int,str(lucky_digits)))
    #print(lucky_digits)
    for i in range(len(lucky_digits_list)):
        if lucky_digits_list[i]==l[0] or lucky_digits_list[i]==l[1]:
            count = count+1
    #print(count)
    if count>0:
        print("YES")

    if count==0:
        print("NO")
                    