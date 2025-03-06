def add_hollow_item(lst):
    lst.append(" ")  # None represents an empty/hollow item in Python
    return lst

a = []
for i in range(4):
    a.append(int(input()))

# Add hollow item at the end
a = add_hollow_item(a)
print(a)

