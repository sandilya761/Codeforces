s = input()
#converting string into list 
l=[]
l[:0] = s


# avoiding repitions in the list
l1 = []

for i in l:
    if i not in l1:
        l1.append(i)



# decide whether the input string is boy or girl

if len(l1)%2 ==0:
    print("CHAT WITH HER!")

else:
    print("IGNORE HIM!")

    