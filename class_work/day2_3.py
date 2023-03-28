def name_args(**kwargs):
    for key in kwargs.keys():
        print(key, kwargs[key])
name_args(name='john', age=21)

#br

all_true = lambda itr: all(itr)

#br

def one_true(itr):
    return any(itr)

print(one_true([3, 2, False]))

#br

def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n + recursive_factorial(n-1)
print(recursive_factorial(4))

#br

def recursive_deduplicate(string, i=0):
    if len(string) == 1 or len(string) == 0:
        return ''
    else:
        return string[-1-i] + rec
