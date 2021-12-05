s = input()

l = list(s) #convert the given string into a list of characters 
k = [] 
for i in l: #converts the characters into ascii values and appends to a list
    k.append(ord(i))

#print(k)
#print(chr(max(k)))
a = l.count(chr(max(k)))

p = []   #finding the character corresponding to the maximum ascii value
if chr(max(k)) in l:
    p.append(chr(max(k)))


#print(p)

while(a>0):
    print(chr(max(k)),end="")
    a = a-1


