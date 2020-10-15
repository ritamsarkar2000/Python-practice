#created on 14th October , 2020 by Ritam Sarkar

import random

n = int(input('enter the number of elements: '))
list_1 = []
for i in range(n):
    list_1.append(int(input('enter the elements')))
k = 0

while list_1 != sorted(list_1):
    i = random.randint(0, len(list_1)-1)
    j = random.randint(0, len(list_1)-1)
    if i != j:
        k += 1
        print(k)
        a = list_1[i]
        list_1[i] = list_1[j]
        list_1[j] = a


for m in range(len(list_1)):
    if m < len(list_1)-1:
        print(list_1[m], end = ' ')
    else:
        print(list_1[m], end = '')


