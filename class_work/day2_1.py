def arb_args (*args):
    for arg in args:
        print(arg)

# arb_args(1, false, true)

def inner_func(int_1, int_2):
    def divide():
        return int_1 / int_2
    def modules():
        return int_1 % int_2
    print(divide() + modules())

def lunch_lady(str_1, str_2="Mystery Meat"):
    print(str_1, str_2)

lunch_lady('Ale', 'bread')
lunch_lady('alex')

def sum_n_product(int_1, int_2):
    return int_1+int_2, int_1*int_2
print(sum_n_product(1,2))

alias_arb_args = arb_args

def arb_mean(*args):
    if len(args) == 0:
        print('no args')
    else:
        total=0
        for arg in args:
            total += arg
        print(total / len(args))

def arb_longest_string(*args):
    longest_var = ''
    for arg in args:
        if len(arg) > len(longest_var):
            longest_var = arg
    return(longest_var)