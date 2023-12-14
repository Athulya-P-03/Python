a = []
print("Square Matrix")
n = int(input("Enter number of rows and columns: "))
b = {}

a = [[] for i in range(n)]

print("\nEnter the elements of the matrix:")
for i in range(n):
    for j in range(n):
        a[i].append(int(input()))

print("\nGiven Matrix:")
for row in a:
    print(row)

for i in range(n):
    for j in range(n):
        if a[i][j] != 0:
            b[(i, j)] = a[i][j]

print("\nDictionary is:", b)
