import secrets 
secretNumber = secrets.SystemRandom()

while True:
	try:
		press = int(input("Press 1 to read Rules and Press 2 to Play Game: "))

		if press == 1:
			print(">>> Age must be more than 18")
			print(">>> Name must be more than 2 words")
			print(">>> Show money must have at least $5000")
			print(">>> You must use $1000 in each round")

		if press == 2:
			uName = input("Please enter your name more than 2words: ")
			uAge = int(input("Please enter your age more than 18: "))
			
			while len(uName) > 2 and uAge >17:
				print("You Can Play Now!")
				print(f'Welcome Mr.{uName}')
				try:
					sMoney = int(input("Please enter your show money: "))
					if sMoney > 4999:
						while True:
							print(f"This is your $$$${sMoney}")
							inputMoney = int(input("Please enter bet money(at least 1000): "))
							luckyNumber = int(input("Please enter your luckyNumber (10, 99): "))
							if secretNumber == luckyNumber:
								print("You Won!")
							else:
								print("You loss!")
					else:
						print("Show money must have at least $5000")
				except ValueError:
					print("Please enter numbers ")

		if press not in (1,2):
			print("Invalid Numbers, Please correctly enter (1 or 2)")
	except ValueError:
		print("Just enter numbers (1 or 2)")
