import math
n = int(input())

mat = []
for i in range(n):
   p = list(map(int,input().split()))
   mat.append(p)

#print(mat)
main_diagonal = 0
secondary_diagonal = 0

for i in range(0,n):
    main_diagonal = main_diagonal + mat[i][i]
    secondary_diagonal = secondary_diagonal + mat[i][n-i-1]

#print(main_diagonal,secondary_diagonal)

middle_row = math.ceil(n/2)-1
middle_column = math.ceil(n/2)-1

row_sum = sum(mat[middle_row])
#print(mat[middle_row])


def column(matrix, i):
    return [row[i] for row in matrix]

column_sum = sum(column(mat,middle_column))
#print((column_sum))

middle_element = math.ceil(len(mat[middle_row])/2)-1
l = mat[middle_row]
#print(l[middle_element])

total = main_diagonal+secondary_diagonal+column_sum+row_sum-(3*l[middle_element])

print(total)









