m = int(input("rows :"))
n = int(input("column:"))

matrix = []
for i in range(0,m):
    matrix.append([])
    for j in range(0,n):
        matrix[i].append(0)

print(matrix)