friends_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
print(friends_ages["Rolf"])
friends_ages["Bob"] = 50
print(friends_ages)

friends = [
    {"name": "Rolf", "age": 30},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 30}
]
print(friends[0]["name"])


for friend, attendence in friends_ages.items():
    print(f"{friend}:{attendence}")

if "Rolf" in friends_ages:
    print(f"Rolf: {friends_ages['Rolf']}")
else:
    print("Rolf is not a student in the class")
