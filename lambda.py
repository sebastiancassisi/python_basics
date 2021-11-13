sequence = [1, 3, 6, 9]

""" doubled = [(lambda x:x*2)(x) for x in sequence] """
doubled = list(map(lambda x: x*2, sequence))

print(doubled)
