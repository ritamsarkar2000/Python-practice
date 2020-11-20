n = int(input('Enter the size of the matrix, Format: If size is n*n, only enter n: '))

m = []
a = 1
for i in range(n):          #to take the matrix as input 
    li = list(map(int, input('enter the row of the matrix in sequence  including spaces between each element: ').split()))
    m.append(li)
    a += 1
k = 0; l = 0
row = n - 1; col = n - 1

lis = []
while k <= row and l <= col:
    for i in range(k, row + 1):
        lis.append(m[i][l])
    l += 1

    for i in range(l, col + 1):
        lis.append(m[row][i])
    row -= 1

    for i in range(row, k - 1, -1):
        lis.append(m[i][col])
    col -= 1

    for i in range(col, l - 1, -1):
        lis.append(m[k][i])
    k += 1

for i in range(len(lis)):
    if i == len(lis) - 1:
        print(lis[i], end='')
    else:
        print(lis[i], end=' ')