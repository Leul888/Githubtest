lst=[2,3,4,5,6,7,8,9]
guess=5
for i in range(5):
    g1 = int(input('Make a guess between 1 and 10: '))
    b=lst.remove(g1)
    guess-=1
    print(guess,'guesses remaining')
    #print(lst)
print('the number was:',lst.pop())
