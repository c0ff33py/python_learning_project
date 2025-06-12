# def myFun(x):
#     return x # terminate

# def myGen(g):
#     yield g
#     yield g+1
#     yield g+2 # supspend

# def myGen():
#     data = 10
#     yield data
#     yield data + 1
#     yield data * 2
#     yield data + 5


# results = myGen()
# print(results)
# print(results.__next__())
# print(results.__next__())
# print(results.__next__())
# print(results.__next__())


# results = myGen()
# print(results)
# for i in results:
#     print(i)


# def my_generator():
#     n = 1
#     print("This is the first yield.")
#     yield n  # ပထမဆုံးအကြိမ် n ကို yield လုပ်သည်။

#     n += 1
#     print("This is the second yield.")
#     yield n

#     n += 1
#     print("This is the third yield.")
#     yield n


# # To make generator object
# gen = my_generator()

# # to get value using with next() function
# print(next(gen))
# print(next(gen))
# print(next(gen))

# # using yield with for loop


# def count_up_to(max_num):
#     count = 1
#     while count <= max_num:
#         yield count
#         count += 1


# # using for loop
# for num in count_up_to(5):
#     print(num)

# List comprehension (memory usage will too much)
my_list = [x * 2 for x in range(1000000)]

# To memory Efficiency
my_generator_exp = (x * 2 for x in range(1000000))

print(next(my_generator_exp))
print(next(my_generator_exp))
