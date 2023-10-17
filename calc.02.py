enter=input('Enter number of digits> ')
lst=[]
if enter.isdigit():
    enter=int(enter)
else:
    print('invalid input')
    quit()
for i in range(enter):
    que=int(input('Enter value> '))
    lst.append(que)
avg=sum(lst)/enter
print('The average is',avg)
