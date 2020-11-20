n = int(input())

m = []

for i in range(n):
    li = list(map(int, input().split()))
    m.append(li)

    
#to keep the track
k = 0;
l = 0
row = n - 1;
col = n - 1

while k < row and l < col:

    prv = m[k + 1][l]

    for i in range(l, col + 1):
        c = m[k][i]
        m[k][i] = prv
        prv = c
    k += 1

    for i in range(k, row + 1):
        c = m[i][col]
        m[i][col] = prv
        prv = c
    col -= 1

    for i in range(col, l - 1, -1):
        c = m[row][i]
        m[row][i] = prv
        prv = c
    row -= 1

    for i in range(row, k - 1, -1):
        c = m[i][l]
        m[i][l] = prv
        prv = c
    l += 1

for i in range(n):
    for j in range(n):
        if (j == n - 1):
            print(m[i][j], end="")
        else:
            print(m[i][j], end=" ")
    if (i != n - 1):
        print()
