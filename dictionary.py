users = [
    (0, "Sebastian", "3129"),
    (1, "Juan", "fdsf33"),
    (2, "Federico", "bgh6"),
    (3, "Martin", "asdasa")
]

username_mapping = {user[1]: user for user in users}

print(username_mapping)
print(username_mapping["Sebastian"])

username_input = input("Ingrese su usuario: ")
password_input = input("Ingrese su contraseña: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Los datos son correctos")
else:
    print("Los datos son incorrectos!!!")
