# a = 20
# b = 20
# while a < b:
#     print(f"{a} Hello World!")
#     a += 1
# print('Nothing doing')


# BREAK STATEMENT
#   CONTINUE STATEMENT
# DIFFERENT BETWEEN BREAK AND CONTINUE

# for va in "Kyaw Khine":
#     if va == "i":
#         break
#     print(va)
# print('________________________________ending')

# for va in "Kyaw Khine":
#     if va == "i":
#         continue #skip
#     print(va)
# print('________________________________ending')

# ls = [1, 2, 3, 4, 5]  # list
# data = 99
# found = False  # flag
# index = 0

# while index < len(ls):
#     if ls[index] == data:
#         found = True
#         break
#     index += 1
# if not found:
#     ls.append(data)
# print(ls)
ls = [1, 2, 3, 99, 4, 5, 67]
data = 99

if data not in ls:
    ls.append(data)

print(ls)
