#monti hall

import random

doors = [0] * 3
goat_doors = [0] * 2
swap = 0    #no of wins by swaping
dont_swap = 0     #no of wins by not swaping
swaped = 0 #to know how many times swaped

j = 1
while j <= 10:    #as we can keep track of the swap and don't swap for 10 times
    x = random.randint(0,2)
    doors[x] = 'world tour'
    for i in range(2):
        if i == x:
            continue
        else:
            doors[i] = 'Goat'
            goat_doors.append(i)
    choice = int(input('enter your door choice [0,1,2] ')) #this will choose the door to be open as a player
    print('the guest / player chosen door is : ', choice)
    door_open = random.choice(goat_doors)   #this will choose the door to be opened as the show anchor
    print('the door to be opened by anchor ', door_open)
    while door_open == choice:
        door_open = random.choice(goat_doors)  #as the player and anchor should not choose the same door
    s = int(input('do you want to swip ? 0 = no /1 = yes '))    #this will choose whether to swap or not
    if s == 1:
        swaped += 1
        print(' the player is swaping')
        if doors[choice] == 'Goat':
            print('win')
            swap += 1
        else:
            print('lost')
    else:
        print('the player will not swap ')
        if doors[choice] == 'Goat':
            print('lost')
        else:
            print('win')
            dont_swap += 1
    j += 1

print('no is swapping ', swaped)
print('number of wins with swapping ', swap)
print('number of wins without swapping ', dont_swap)



