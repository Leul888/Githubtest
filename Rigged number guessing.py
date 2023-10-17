lst2=[1,2,3,4,5]
lst=[1,2,3,4,5,6,7,8,9,10]
guess=5
for i in lst2:
    g1 = int(input('Make a guess between 1 and 10: '))
    b=lst.remove(g1)
    guess-=1
    print(guess,'guesses remaining')
    #print(lst)
print('the number was:',lst.pop())
