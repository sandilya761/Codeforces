n = int(input())
a = 10
d = n-a
#print(d)
if n<10:
    print("0")
else:    
    if d==10:
        print("15")

    elif d==11:
        print("4")

    elif d==0 or d==15:
        print("0")
    elif d>10:
        print("0")    
    else:
        print("4")