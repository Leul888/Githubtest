name=input('Enter Your name: ')
print('Welcome '+name)
game=input('Wanna go on an adventure?(yes/no) ').lower()
if game=='yes':
    question1=input('Choose a door:(A/B/C): ').lower()
    if question1=='a':
        print('You have been eaten by the castle demon.')
    elif question1=='b':
        print('You have been captured by the castle guards.')
    elif question1=='c':
        question02=input('1,2,or 3: ').lower()
        if question02=='1':
            import random
            print('Less play a number guessing game.')

            tries = 0
            max_val = input('Enter max limit: ')
            if max_val.isdigit():
                max_val = int(max_val)
            else:
                print('Enter a valid nunber.')
                quit()
            rand_val = random.randint(0, max_val)
            while True:

                make_guess = input('Make a guess: ')
                if make_guess.isdigit():
                    make_guess = int(make_guess)
                    tries += 1
                else:
                    print('Invalid Input')
                    quit()

                if make_guess == rand_val:
                    print('You got it!')
                    break
                elif make_guess > rand_val:
                    print('Too high')
                else:
                    print('Too low')

            print('It took you', tries, 'attempts!')

        elif question02=='2':
            import random

            user_point = 0
            ai_point = 0
            draw = 0
            my_list = ['rock', 'paper', 'scissors']
            print('Welcome to a game of rock,paper,scissors.')

            while True:
                my_pick = input('Rock,paper,scissors or E to quit: ').lower()
                if my_pick == 'e':
                    break
                elif my_pick not in my_list:
                    print('Pick One')
                    continue
                random_val = random.randint(0, 2)
                ai_pick = my_list[random_val]
                print('ai chose', ai_pick + '.')

                if my_pick == ai_pick:
                    print('Draw')
                    draw += 1

                elif my_pick == 'rock' and ai_pick == 'scissors':
                    print('You won!')
                    user_point += 1
                elif my_pick == 'paper' and ai_pick == 'rock':
                    print('You won!')
                    user_point += 1

                elif my_pick == 'scissors' and ai_pick == 'paper':
                    print('You won!')
                    user_point += 1
                else:
                    print('AI won')
                    ai_point += 1

            print('You won', user_point, 'times!')
            print('Ai won', ai_point, 'times.')
            print('Draw', draw, 'times.')
            print('Good Bye')

        elif question02=='3':
            print('Welcome to the quiz game.')
            x = input('Are you ready to proceed? ').lower()

            if x == 'yes':
                print('Less go')
            else:
                quit()
            score = 0
            question = input('Whats 10+1? ')
            if question == '11':
                print('1 point')
                score += 1
            else:
                print('Incorrect')

            question = input('Whats 5*3? ')
            if question == '15':
                print('1 point')
                score += 1
            else:
                print('Incorrect')
            question = input('Whats 25/5? ')
            if question == '5':
                print('1 point')
                score += 1
            else:
                print('Incorrect')
            print('You got ' + str(score) + ' qusetions right!')
            print('that is ' + str((score / 3) * 100) + ' percent ')

        else:
            print('Invalid option')
            quit()




    else:
        print('enter a valid option')
elif game=='np':
    print('See you another time.')
    quit()
else:
    print('enter a valid option',name,)
