print('Welcome')
playing=input('Do you want to play a game? ').lower()
if playing!='yes':
    print('Bye')+quit()

print('Okay lesss go!')
score=0

a=input('Whats  CPU? ').lower()
if a =='central proc unit':
    print('1 point')
    score+=1
else:
    print('incorrect')

a = input('Whats GPU? ').lower()
if a == 'graph proc unit':
    print('1 point')
    score += 1
else:
    print('incorrect')

a = input('Whats RAM? ').lower()
if a == 'random access memo':
    print('1 point')
    score += 1
else:
    print('incorrect')

a = input('Whats PS? ').lower()
if a == 'play station':
    print('1 point')
    score += 1
else:
    print('incorrect')

print('You got ' + str(score) +' questions correct!')
print('You got ' + str((score/4)*100) +'%')
