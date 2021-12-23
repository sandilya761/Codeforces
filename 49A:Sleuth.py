
string = input()

l = ["a","e","i","o","u","y"]
m = ["A","E","I","O","U","Y"]

def remove(string):
	return string.replace(" ", "")
	

x = remove(string)
#print(x)
k = len(x)

#print(x[k-2])

if x[k-2] in l:
    print("YES")

elif x[k-2] in m:
    print("YES")
else:
    print("NO")