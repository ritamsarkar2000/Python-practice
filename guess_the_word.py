import random


# for choosing the word

def choose():
    words = ['Juxtaposition', 'Sex', 'Controversy', 'Taboo', 'Forbidden', 'Psychology', 'Crime', 'Health', 'freedom',
             'Opposition', 'Feminism', 'Poverty', 'Corruption', 'Justice', 'Oppression', 'Fear', 'Awareness',
             'Pollution', 'Science', 'Racism', 'Ignorance', 'Politics', 'Leaders', 'Murder', 'Stereotype', 'Toxicity',
             'Ego', 'Masculinity', 'Femininity', 'Equality', 'Homosexuality', 'Bisexuality', 'Transgender', 'Queer',
             'Rich', 'Love', 'Humanity', 'Cruelty', 'Livelihood', 'Life', 'Education', 'Shelter', 'Food', 'Clothing',
             'Rights', 'Economy', 'Climate']
    sort = random.choice(words)
    return sort


# For jumbling the word

def jumble(sort):
    jumbles = "".join(random.sample(sort, len(sort)))
    return jumbles


def play():
    np = input('Enter number of players (2/1): ')
    np = int(np)
    if np == 2:
        p1 = input('enter your name:')
        p2 = input('enter your name:')
        pp1 = 0
        pp2 = 0
        turn = 0
        while True:
            # computer's task
            pick = choose()
            qn = jumble(pick)
            # for player 1
            if turn % 2 == 0:
                print(p1, 'its your turn ')
                print('your word is: ', qn)
                ans = input('please enter your ans: ')
                if ans == pick:
                    pp1 = pp1 + 1
                    print(p1, 'correct, your score: ', pp1)
                else:
                    print(' wrong, try again ')
                    ans_again = input('your new answer: ')
                    if ans_again == pick:
                        pp1 = pp1 + 1
                        print(p1, 'correct, your score: ', pp1)
                    else:
                        print('wrong, the correct word was: ', pick)
                c = input(' Please , enter 1 to continue or 0 to stop the game')
                c = int(c)
                if c == 0:
                    s = input(' do you want to quit? enter 0 for yes and 1 for continue: ')
                    s = int(s)
                    if s == 0:
                        print(' thank you for playing, have a nice day, good bye,'
                              ' your scores are (player 1s score , player 2score): ', pp1, pp2)
                        break
            # for player 2
            else:
                print(p2, 'its your turn ')
                print('your word is: ', qn)
                ans = input('please enter your ans: ')
                if ans == pick:
                    pp2 = pp2 + 1
                    print(p2, 'correct, your score: ', pp2)
                else:
                    print(' wrong, try again ')
                    ans_again = input('your new answer: ')
                    if ans_again == pick:
                        pp2 = pp2 + 1
                        print(p2, 'correct, your score: ', pp2)
                    else:
                        print('wrong, the correct word was: ', pick)
                c = input(' Please , enter 1 to continue or 0 to stop the game')
                c = int(c)
                if c == 0:
                    s = input(' do you want to quit? enter 0 for yes and 1 for continue: ')
                    s = int(s)
                    if s == 0:
                        print(' thank you for playing, have a nice day,'
                              ' good bye and your scores are (player 1s score , player 2score): ', pp1, pp2)
                        break
            turn = turn + 1
    else:
        p1 = input('enter your name: ')
        pp1 = 0
        k = 1
        while k == 1:
            pick = choose()
            qn = jumble(pick)
            print(p1, ' your word is', qn)
            ans = input('Please wnter your answer: ')
            if ans == pick:
                pp1 = pp1 + 1
                print('correct, your score is: ', pp1)
            else:
                print(' wrong try again')
                new = input('your new answer is: ')
                if new == pick:
                    pp1 = pp1 + 1
                    print('correct , your score is: ', pp1)
            k = input('Enter 1 to continue and 0 to stop: ')
            k = int(k)
        print('Thank you for playing, have a nice day!')


play()
