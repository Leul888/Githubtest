import random
top_num=input('type a num: ')
if top_num.isdigit():
    top_num=int(top_num)

    if top_num <=0:
        print('enter a higher value')
        quit()
else:
    print('enter a number')
    quit()

random_number=random.randint(0,top_num)
guesses=0

while True:
    guesses+=1
    user_guess=input('make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('enter a number')
        continue
    if user_guess == random_number:
        print('you got it!')
        break
    elif user_guess>random_number:
            print('you were above the number!')
    else:
            print('you were below the number!')


print('you got it in',guesses,'guesses')


