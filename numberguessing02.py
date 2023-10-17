import random
top_range=input('enter max limit: ')
if top_range.isdigit():
    top_range=int(top_range)
    if top_range<0:
        print('enter a higher number')
        quit()

else:
        print('enter a valid number')
        quit()
random=random.randint(0,top_range)
guess=0
while True:
    guess+=1
    user_guess=input('make a guess: ')
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print('enter a valid number')
        continue

    if user_guess==random:
        print('you got it in ',guess,' tries' )
        break
    elif user_guess > random:
        print('Your guess was too high.')
    else:
        print('Your guess was too low.')

