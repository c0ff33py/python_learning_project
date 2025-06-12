import secrets
import sys


def display_Rules():
    print("\n-------Rules of the Game-------")
    print("1. Your name must have 2 or more letters.")
    print("2. Your age must be 18 or more.")
    print("3. Your show money must be $5000 or more.")
    print("4. You must be use at least $1000 per round.")
    print("5. If you guess the lucky number correctly, You win 10 times your bet.")
    print("6. If you guess incorrectly, you lose your bet.")
    print("7. The game ends when you run out of money or choose to exit.")


def get_user_detalil():
    user_name = input("Please Enter your name: ")
    user_age = int(input("Please enter your age: "))
    return user_name, user_age


def get_show_money():
    while True:
        show_money = int(
            input("Please enter your show money(minimum $5000: )"))
        if show_money >= 5000:
            return show_money
        else:
            print("Invalid amount.You must have at least $5000 to play!!!")


def play_round(show_money, secure_number_generator):
    while True:
        print(f'\n Your current balance: ${show_money}')

        try:
            bet_amount = int(input("Enter your bet amount(minium $1000): "))

            if bet_amount < 1000:
                print("Invalid amount. You must have at least $1000 to play.")
                continue

            if bet_amount > show_money:
                print(
                    "Insufficient funds. You cannnot bet more than your current balance.")
                continue

            lucky_number = int(input("Enter your lucky number (10-99): "))
            if lucky_number < 10 or lucky_number > 99:
                print("Invalid number. Please enter a number between 10 and 99.")
                continue
            system_number = secure_number_generator.randint(10, 99)
            print(f"The system number is: {system_number}")

            if lucky_number == system_number:
                winnings = bet_amount * 10
                show_money += winnings
                print(
                    f'Congratulations! You guessed correctly. You won ${winnings}.')
            else:
                show_money -= bet_amount
                print("Sorry, you guessed incorrectly. You lost your bet.")

            if show_money <= 1000:
                print("You have run out of money. Game over.")
                sys.exit(0)

            play_again = input("Do you wnat to play again? (y/n): ")
            if play_again.lower() != 'y':
                print("Thank you for playing! Goodbye.")
                sys.exit(0)

            print("\n--------New Round---------")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    secure_number_generator = secrets.SystemRandom()
    while True:
        print("-----------------------------------------------")
        print("_____________________WELCOME TO THE GAME________________")
        print("---------------------------------------------------------")

        choice = input("Enter 1 to read the rules, 2 to play the game: ")
        if choice == 1:
            display_Rules()
        elif choice == 2:
            user_name, user_age = get_user_detalil()
            if len(user_name) >= 2 and user_age >= 18:
                print(f"\nWelcome {user_name}! You are eligible to play.")
                show_money = get_show_money()
                play_round(show_money, secure_number_generator)
            else:
                print(
                    "Sorry, you do not meet the requirements to play. Please read the rules agains.")
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main___":
    main()
