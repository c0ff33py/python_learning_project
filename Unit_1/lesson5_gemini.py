# def add(n1, n2):
# 	return n1 + n2

# def sub(n1, n2):
# 	return n1 - n2

# def multiply(n1, n2):
# 	return n1 * n2

# def divide(n1, n2):
# 	if n2 == 0:
# 		return "cannot divided by 0"
# 	return n1 / n2

# print("Press 1: Addition")
# print("Press 2: Subtract")
# print("Press 3: multiply")
# print("Press 4: divided")

# choice = input("Please choose a number(1/2/3/4): ")

# while True:
# 	try:
# 		if choice in ('1','2','3','4'):
# 			num1 = float(input("Enter first number: "))
# 			num2 = float(input("Enter second number: "))
# 			if choice == "1":
# 				print(f'num1 + num2 : {(num1 + num2)}')
# 			if choice == "2":
# 				print(f'num1 - num2: {(num1 - num2)}')
# 			if choice == "3":
# 				print(f'num1 * num2: {(num1 * num2)}')
# 			if choice == "4":
# 				print(f'num1 / num2: {(num1 / num2)}')
# 			break
# 		else:
# 			print('Invalid number!, Please enter only (1,2,3,4)')
# 	except ValueError:
# 		print("Invalid input. Please enter a number")
# 	except Exception as e:
# 		print(f'An error occur: {e}')


#	first code for foumula example: add,sub,multi,divide
#	Print menu of program
#	ask user to chose menu
#	code for user input



def addition(n1, n2):
	return n1 + n2

def substract(n1, n2):
	return n1 - n2 

def multiply(n1, n2):
	return n1 * n2 

def divide(n1, n2):
	if n2 == 0:
		print("Cannot divided by 0")
	return n1 / n2 

print("Enter 1: Addition")
print("Enter 2: Substract")
print("Enter 3: Multiply")
print("Enter 4: Divition")

user_choices = input("Pls choose a number from (1/2/3/4): ")

while True:
	try:
		if user_choices in ('1','2','3','4'):
			num1 = float(input("Please enter numbers: "))
			num2 = float(input("Please enter numbers: "))

		
			if user_choices == '1':
				print(f'num1 + num2 = {(num1 + num2)}')
			if user_choices == '2':
				print(f'num1 - num2 = {(num1 - num2)}')
			if user_choices == '3':
				print(f'num1 * num2 = {(num1 * num2)}')
			if user_choices == '4':
				print(f'num1 / num2 = {(num1 / num2)}')
			break
		else:
			print("Please enter only number(1/2/3/4)!!!")

	except ValueError:
		print("Invalid input, enter numbers!")
	except Exception as e:
		print(f"An error occur as {e}")