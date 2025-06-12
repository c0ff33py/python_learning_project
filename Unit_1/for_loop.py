# for loop
# list_ls = [(1,1),(2,4),(3,6),(4,8)]
# a = "*"
# for i in a:
# 	print(f'{(a*4)}')


# s = "kyawkhine"
# tu = ("a", "b", "c", 1, 2, 3, 4, 6)
# lt = [(1, 2), (3, 4), (5, 6)]
# for i in lt:
#     print(i)

# for i in range(5):  # 0-4
#     print('________________________')
#     try:
#         z = 10/(i-3)
#         print(f'z value is: {z}')
#     except ZeroDivisionError:
#         print("Divide by Zero")
#     finally:
#         print('Always run')
#     print(i)


# age = 22
# # if age >= 18:
# #     message = 'Eligible'
# # else:
# #     message = "Not Eligible"

# message = "Eligible" if age >= 18 else "Not Eligible"
# print(message)


rows = int(input("Please enter rows: "))

for i in range(rows):
    print(' ' * (rows - 1 - i), end="") # that is display space (5-1-0)
    print('*' * (2 * i + 1), end='') #
    print('')
