import cmath

a=int(input('enter a:'))
b=int(input('enter b:'))
c=int(input('enter c: '))

d=(b**2)-(4*a*c)
x=(-b+cmath.sqrt(d))/(2*a)
x2=(-b-cmath.sqrt(d))/(2*a)
print('the soln is/are:',x,x2)
