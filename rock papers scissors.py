import random

computer_wins=0
user_wins=0
my_list=['rock','paper','scissors']

while True:
    user_pick=input('Choose rock,paper,scissors or q to end: ').lower()
    if user_pick== 'q':
        break
    if user_pick not in my_list:
        continue

    random_val=random.randint(0,2)

    computer_pick=my_list[random_val]
    print('Computer picked',computer_pick+'.')

    if user_pick== 'rock' and computer_pick=='scissors':
        print('You won!')
        user_wins+=1
    elif user_pick=='paper' and computer_pick=='rock':
        print('You won')
        user_wins += 1
    elif user_pick=='scissors'and computer_pick=='paper':
        print('You won')
        user_wins += 1

    elif user_pick == 'rock' and computer_pick == 'rock':
        print('Draw')

    elif user_pick == 'paper' and computer_pick == 'paper':
        print('Draw')

    elif user_pick == 'scissors' and computer_pick == 'scissors':
        print('Draw')
    else:
        print('Computer Won')
        computer_wins+=1

print('Computer Won',computer_wins,'times.')
print('You won',user_wins,'times.')
print('Goodbye User')
