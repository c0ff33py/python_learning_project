# calculator program
# add
# subtract
# multiply
# divide

# print("Press 1: for addition:")
# print("Press 2: for substract")
# print("Press 3: for multiply")
# print("Press 4: for divide")


# userInput = int(input("Please choose a number from 1 to 4: "))
# firtst_number = int(input("Please enter first numbers: "))
# second_number = int(input("Please enter second numbers: "))

# if userInput == 1:
#     result = firtst_number+second_number
# elif userInput == 2:
#     result = firtst_number-second_number
# elif userInput == 3:
#     result = firtst_number * second_number
# elif userInput == 4:
#     result = firtst_number / second_number
# else:
#     print('You must enter only 1,2,3,4!!!')
# print(f' The result number is :{result}')


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return 'Cannot divide by zero'
    return n1 / n2


print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    try:
        choice = input("Enter choice(1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f'num1 + num2 = {add(num1, num2)}')
            elif choice == '2':
                print(f'num1 - num2 = {subtract(num1, num2)}')
            elif choice == '3':
                print(f'num1 * num2 = {multiply(num1, num2)}')
            elif choice == '4':
                print(f'num1 / num2 = {divide(num1, num2)}')
            break  # exit the loop after a successful calculation
        else:
            print("Invalid input. Please enter 1, 2, 3, or 4.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")
