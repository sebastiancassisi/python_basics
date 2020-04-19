prise = 9.99
discount = 0.2
result = prise * (1-discount)
print(result)

myName = "Sebastian"
print(myName)
print(myName * 2)

a = 25
b = a
print(b)

name = "Bob"
greeting = f"Hello {name}!"
print(greeting)


name2 = "Carlos"
greeting2 = "Hello {}!"
with_name = greeting2.format(name2)
print(with_name)


longer_phrase = "Hello {} , today is {}."
formatted = longer_phrase.format("Juan", "Monday")
print(formatted)
