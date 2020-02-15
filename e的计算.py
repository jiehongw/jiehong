import math
while True:
    n=input('please enter the number of n:')
    if len(n)==0:
        break
    else:
        a=int(n)
        e=(1+1/a)**a
        print('e=',e)
