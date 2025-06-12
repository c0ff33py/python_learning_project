# control structure
# if statement
# if else statement
# elif
# largest number sample program

# a = 30
# b = 30

# if a < b:
#     print('a < b')
# elif a == b:
#     print('a==b')
# else:
#     print('a>b')

# # largest number
# a = 190
# b = 85
# c = 83
# d = 100

# if a > b and a > c and a > d:
#     largestNumber = a
# elif b > a and b > c and b > d:
#     largestNumber = b
# elif c > a and c > b and c > d:
#     largestNumber = c
# else:
#     largestNumber = d

# print(f'largestnumber is {largestNumber}')

# ---------------->Practice from Gemini <----------------
a = 90
b = 100
c = 140
d = 230
e = 210

largestNumber = max(a, b, c, d, e)
# using max() function
print(f'Largest Number is {largestNumber}')


numbers = [901, 825, 853, 120]
largestNumber = numbers[0]
for number in numbers:
    if number > largestNumber:
        largestNumber = number
print(f'Largest Number is {largestNumber}')
