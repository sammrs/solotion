def add (a):
    a.append(" ")
    return a
a = ["a", "b", "c"]
print(add(a))

print(a[0:1])
print(a)
print(a[::-1])
a.reverse()
print(a)