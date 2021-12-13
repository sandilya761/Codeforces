n,k,l,c,d,p,nl,np = map(int,input().split())

toasts_drinks = int((k*l)/nl)
toasts_salt = int(p/np)
toasts_slices = c*d

total = int(min(toasts_drinks,toasts_salt,toasts_slices)/n)

print(total)

