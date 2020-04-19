numbers = [1, 3, 5]
doubled = [x*2 for x in numbers]
print(doubled)


friends = ['Sam', 'Samantha', 'Jen', 'Claudio']
starts_s = [friend for friend in friends if friend.startswith("S")]
print(starts_s)
