""" List """
l = ["mono", "perro", "gato"]

""" Tupla """
t = ("mono", "perro", "gato")

""" set """
s = {"mono", "perro", "gato", "mono"}


l[0] = "loro"
l.append("raton")
l.remove("perro")
print(l)
print(t)
print(s)


friends = {'Bob', 'Rolf', 'Anne'}
abroad = {'Bob', 'Anne'}
local_friends = friends.difference(abroad)
print(local_friends)


local = {'Rolf'}
abroad2 = {'Bob', 'Anne'}
friends2 = local.union(abroad2)
print(friends2)

art = {'Bob', 'Jean', 'Rolf', 'Anne', 'Charlie'}
science = {'Bob', 'Jean', 'Adam', 'Anne'}

both = art.intersection(science)
print(both)


notas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(notas))  # suma
print(len(notas))  # mayor
