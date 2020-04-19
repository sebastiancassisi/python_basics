day_of_week = input('What day of the week is it today?').lower()

if day_of_week == 'Monday':
    print("Have a great start to you week!")
elif day_of_week == 'Tuesday':
    print("It´s Tuesday")
else:
    print("Full speed ahead!")


friends = ['Rolf', 'Bob', 'Jen']
print('Jen' in friends)

movies_wached = {'The matrix', 'Green book', 'Her'}
user_movie = input("Enter somethings you´ve whached recently:")
if user_movie in movies_wached:
    print(f"I´ve wached {user_movie} too!")
else:
    print("I´ havent wached that yet.")

