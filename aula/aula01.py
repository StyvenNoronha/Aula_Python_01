def mul(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

print(mul(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def pi(num):
    re = num % 2 == 0
    if re:
        return 'par'    
    return 'impar'

print(pi(3))