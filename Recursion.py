#factorial(7) = 7*6*5*4*3*2*1
#factorial(7) = 6*5*4*3*2*1
#factorial(7) = 5*4*3*2*1
#factorial(7) = 4*3*2*1
#factorial(7) = 3*2*1

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)
print(factorial(4))
