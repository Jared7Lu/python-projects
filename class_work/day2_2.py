def algo(n):
    if n == 0:
        return('n = 0')
    else:
        print(n)
        algo(n-1)
algo(5)

def natural_numbers(n, i=1):
    if i > n:
        return
    else:
        print(i)
        natural_numbers(n, i+1)

print('break')

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(5))

def exponent(a, b):
    if b == 1:
        return a
    else:
        return a * exponent(a, b-1)

def palindrome(str):
    if len(str) == 1 or len(str) == 0:
        return True
    else: 
        return(str[0] == str[-1]) and palindrome(str[1: -1])