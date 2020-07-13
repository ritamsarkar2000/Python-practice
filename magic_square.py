# creating magic square (sum of each element in each row = sum of each element in each column = sum of each element in each diagonal)
# in a magic square every elemnt should be different

def magic_squarea(n):
    my_matrix = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        my_matrix.append(l) # This will creat a zero matrix of n * n

    i = n // 2
    j = n - 1

    for e in range(1, (n * n + 1)):
        if i == -1 and j == n:
            i = 0
            j = n - 2
        else:
            if i < 0:
                i = n - 1
            if j == n:
                j = 0
        if my_matrix[i][j] != 0:
            i = i + 1
            j = j - 2
            my_matrix[i][j] = e
        else:
            my_matrix[i][j] = e

        i -= 1
        j += 1

    return my_matrix


import numpy as np

x = np.array(magic_squarea(9))
print(x)

# if we want without [ ]

for i in x:
    for e in i:
        print(e, end=" ")
    print()
