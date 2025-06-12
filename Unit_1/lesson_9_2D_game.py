import secrets 
secureNumber = secrets.SystemRandom()

while True:
	print("_____WELCOME TO 2D GAME_____")
	press = int(input("Press 1 to Read Rule or Press 2 To play Game."))
	if press == 1:
		print('> Age must be more than 18: ')
		print('> Show money more than 5000')
		print('>U must use more than 1000 each time')
	if press ==2:
		uName = input('Please enter your name: ')
		uAge = int(input('Please enter your Age:> '))

		while len(uName) > 2 and uAge > 17:
			print("You can play NOW.")
			print(f'Welcome {uName}')
			while True:
				sMoney = int(input("Please enter your show money: "))
				while sMoney > 5000:
					while True:
						print(f'This is your Money {sMoney}')

						inputMoney = int(input("Please enter money to Play: "))
						luckyNumber = int(input("Please enter yout luckyNumber: "))
						systemNumber = secureNumber.randint(10,99)
						while luckyNumber == systemNumber:
							print("You Won!")
						print(f"Try again!.....luckyNumber is {systemNumber}")
						sMoney = sMoney - inputMoney
						if sMoney < 1000:
							print(f"You haven't enough money, $:{sMoney}")
							break
			print('Please more money')
	print('Please read again rule')
