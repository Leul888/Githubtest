import random

tries=0
max_val=input('Enter max limit: ')
if max_val.isdigit():
    max_val=int(max_val)
else:
    print('Enter a valid nunber.')
    quit()
rand_val=random.randint(0,max_val)
while True:

    make_guess=input('Make a guess: ')
    if make_guess.isdigit():
        make_guess=int(make_guess)
        tries += 1
    else:
        print('Invalid Input')
        quit()

    if make_guess==rand_val:
            print('You got it!')
            break
    elif make_guess>rand_val:
        print('Too high')
    else:
        print('Too low')

print('It took you',tries,'attempts!')

