
""" Funciones """


def say_hello():
    print('Hello!')


say_hello()


friends = []


def add_frieds():
    friends.append("ROLF")


add_frieds()
add_frieds()
add_frieds()
print(friends)


""" Funciones: ARgumentos y parametros """


def add(x, y):
    result = x+y
    print(result)


add(4, 6)


def say(name):
    print(f"Hello, {name}")


say("Sebastian")


def say2(name, surname):
    print(f"Hello, {name} {surname}")


say2(name="Sebastian", surname="Cassisi")


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend/divisor)
    else:
        print("No es posible dicidir")


divide(15, 0)

""" Funciones: Parametro por default """

default_y = 3


def add2(x, y=default_y):
    sum = x + y
    print(sum)


add2(4)
