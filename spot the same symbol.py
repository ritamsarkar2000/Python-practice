# created on July 14, 2020
# by Ritam Sarkar

import string
import random

symbols = []
symbols = list(string.ascii_letters)  # to create a list of alphabetical symbols

card1 = [0]*5
card2 = [0]*5

pos1 = random.randint(0, 4)
pos2 = random.randint(0, 4)

same_symbol = random.choice(symbols)
symbols.remove(same_symbol)

if pos1 == pos2:
    card1[pos2] = same_symbol
    card2[pos2] = same_symbol
else:
    card1[pos1] = same_symbol
    card2[pos2] = same_symbol
    card1[pos2] = random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1] = random.choice(symbols)
    symbols.remove(card2[pos1])
for i in range(5):
    if i != pos1 and i != pos2:
        alphabet1 = random.choice(symbols)
        card1[i] = alphabet1
        symbols.remove(alphabet1)
        alphabet2 = random.choice(symbols)
        card2[i] = alphabet2
        symbols.remove(alphabet2)

print('spot the same character ')
print(card1)
print(card2)

ans = input('the different character is: ')
if ans == same_symbol:
    print('correct')
else:
    ans2 = input('wrong, try again. enter your answer again: ')
    if ans2 == same_symbol:
        print('correct')
    else:
        print('False, the correct answer is: ', same_symbol)


