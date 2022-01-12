s = input()
count = 0

t= int(input())
while(t!=0):
    if len(s)%2 !=0 :
        #print(len(s))
        print("NET")

    else:
        #i = 1
        x = list(s)
        for i in range(1,len(x)):
            #print(abs(int(s[i])-int(s[i-1])))
            if abs(int(x[i])-int(x[i-1]))==1:
                
                del(x[i],x[i-1])
                count = count+1
                print(count)

        if count%2!=0:
            print("DA")

        else:
            print("NET")
    t = t-1        