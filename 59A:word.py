s = input()

count_lower=0
count_upper = 0
for i in range(len(s)):
    if s[i].islower():
        count_lower = count_lower+1
    else:
        count_upper = count_upper+1

if count_upper>count_lower:
    print(s.upper())

else:
    print(s.lower())
