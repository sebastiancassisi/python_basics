""" def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
    return total


print(multiply(1, 3, 4))


def add(x, y):
    return x+y


nums = [3, 4]
print(add(*nums))


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No es un operador valido"


print(apply(1, 3, 4, 5, 6, 7, operator="*")) """


def named(**kwargs):
    print(kwargs)


named(name="Sebastian", age=35)
