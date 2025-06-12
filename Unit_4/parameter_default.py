def bshop(name, quantity, unit, tlist=None):
    if tlist is None:  # that make avoid default value problem
        tlist = []
    tlist.append(f'{name}, {quantity}, {unit}')
    return tlist


store1 = bshop('java', 1, 'book')
bshop('Go', 5, 'books', store1)
store2 = bshop('Python', 4, "books")
store3 = bshop('c++', 3, 'book')
print(store1)
print(store2)
print(store3)
