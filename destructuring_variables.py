student_age = {"Rolf": 96, "Bob": 80, "Anne": 100}

# Lista de tuplas
print(list(student_age.items()))

# Tuplas individuales
for t in student_age.items():
    print(t)

# Destructuracion de tupla
for student, age in student_age.items():
    print(f"{student}:{age}")


people = [("Rolf", 42, "Mechanic"), ("James", 24,
                                     "Artist"), ("Harry", 32, "Lecturer")]

for person in people:
    print(f"Name:{person[0]}, Age:{person[1]}, Profession:{person[2]}")


person = ("Bob", 42, "Mechanic")
name, _, profession = person
print(name, profession)


head, *tail = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(head)
print(tail)
