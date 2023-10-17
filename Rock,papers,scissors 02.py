import random

user_point=0
ai_point=0
draw=0
my_list=['rock','paper','scissors']

while True:
    my_pick=input('Rock,paper,scissors or E to quit: ').lower()
    if my_pick== 'e':
        break
    elif my_pick not in my_list:
        print('Pick One')
        continue
    random_val=random.randint(0,2)
    ai_pick=my_list[random_val]
    print('ai chose',ai_pick+'.')

    if my_pick==ai_pick:
        print('Draw')
        draw+=1

    elif my_pick=='rock' and ai_pick=='scissors':
        print('You won!')
        user_point+=1
    elif my_pick=='paper' and ai_pick=='rock':
        print('You won!')
        user_point+=1

    elif my_pick=='scissors' and ai_pick=='paper':
        print('You won!')
        user_point+=1
    else:
        print('AI won')
        ai_point+=1

print('You won',user_point,'times!')
print('Ai won',ai_point,'times.')
print('Draw',draw,'times.')
print('Good Bye')
