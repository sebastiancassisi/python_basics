number = 7
while True:
    user_input = input("Would you like to play? (y/n) ").lower()

    if user_input == "n":
        break

    user_number = int(input("Guess our number:"))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) in (1, -1):
        print("You were off by one")
    else:
        print("Sorry, it´s wrong!")
    user_input = input("Would you like to play? (y/n) ").lower()


friends = ["Rolf", "Jen", "Bob", "Anne"]
for friend in friends:
    print(f"{friend} is my fried ")


grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)
for grade in grades:
    total += grade
print(total/amount)
