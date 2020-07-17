# guess the movie name
# created on 17th July

import random

movies = ['titanic', 'moonlight', 'call me by your name', 'harry potter', 'star wars', 'interstellar',
          'taare zamin paar',
          'avatar', 'la la land', 'kung fu panda', 'the jungle book', 'fantastic beasts', 'lucy', 'enter the dragon']


def create_qn(movie):
    s = list(movie)
    encoded_qn = []
    for i in s:
        if i == ' ':
            encoded_qn.append(' ')
        else:
            encoded_qn.append('*')
    string = ''.join(encoded_qn)
    return string


def unlocking(letters, movie):
    c = movie.count(letters)
    if c == 0:
        unlock = False
    else:
        unlock = True
    return unlock


def modified(qn, letters, movie):
    s = list(movie)
    qn_list = list(qn)
    temp = []
    for i in range(len(movie)):
        if s[i] == ' ' or s[i] == letters:
            temp.append(s[i])
        else:
            if qn_list[i] == '*':
                temp.append('*')
            else:
                temp.append(qn_list[i])
    string = ''.join(str(x) for x in temp)
    return string


def play():
    p1 = input('Player 1 , enter your name: ')
    p2 = input('Player 2 , enter your name: ')
    pp1 = 0
    pp2 = 0
    turn = 0

    k = True
    while k:
        qn = random.choice(movies)
        created_qn = create_qn(qn)
        if turn % 2 == 0:
            # player 1
            print(p1, ' , your turn')
            print(created_qn)
            modified_question = created_qn
            not_said = True
            while not_said:
                letters = input('Enter the letter')
                unlock = unlocking(letters, qn)
                if unlock:
                    modified_question = modified(modified_question, letters, qn)
                    print(modified_question)
                    d = int(input('press 1 to guess the movie or to unlock more press 0: '))
                    if d == 1:
                        ans = input('Your answer: ')
                        if ans == qn:
                            pp1 += 1
                            print('correct, your score is: ', pp1)
                            not_said = False
                        else:
                            print('wrong , your score is ', pp1, 'try again')
                            try_again = int(input('press 1 to try again and 0 to stop: '))
                            if try_again == 0:
                                not_said = False
                else:
                    print('sorry , can not find the letter, your score is ', pp1)

            k = int(input('press 1 to continue and 0 to stop: '))
            if k == 0:
                print('thank you for playing, your scores are: ', pp1, ' ', pp2)

        else:
            # player 2
            print(p2, ' , your turn')
            print(created_qn)
            modified_question = created_qn
            not_said = True
            while not_said:
                letters = input('Enter the letter')
                unlock = unlocking(letters, qn)
                if unlock:
                    modified_question = modified(modified_question, letters, qn)
                    print(modified_question)
                    d = int(input('press 1 to guess the movie or to unlock more press 0: '))
                    if d == 1:
                        ans = input('Your answer: ')
                        if ans == qn:
                            pp2 += 1
                            print('correct, your score is: ', pp2)
                            not_said = False
                        else:
                            print('wrong , your score is ', pp2, 'try again')
                            try_again = int(input('press 1 to try again and 0 to stop: '))
                            if try_again == 0:
                                not_said = False
                else:
                    print('sorry , can not find the letter, your score is ', pp1)

            k = int(input('press 1 to continue and 0 to stop: '))
            if k == 0:
                print('thank you for playing, your scores are: ', pp1, ' ', pp2)

        turn += 1


play()
