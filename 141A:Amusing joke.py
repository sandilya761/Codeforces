from collections import OrderedDict

guest = input()
host = input()
pile = input()

temp = guest+host

temp_freq = {}

for i in temp:
	if i in temp_freq:
		temp_freq[i] += 1
	else:
		temp_freq[i] = 1

#print (str(temp_freq))

pile_freq = {}
for j in pile:
	if j in pile_freq:
		pile_freq[j] += 1
	else:
		pile_freq[j] = 1

#print(str(pile_freq))

temp_sort = OrderedDict(sorted(temp_freq.items()))

pile_sort = OrderedDict(sorted(pile_freq.items()))

if temp_sort==pile_sort:
    print("YES")

else:
    print("NO")



