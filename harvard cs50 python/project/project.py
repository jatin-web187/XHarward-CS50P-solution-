def take_out_cookies(balance, no_of_cookies):
    if no_of_cookies > 0 and no_of_cookies <= balance:
        balance -= no_of_cookies
        return balance, f"Took out {no_of_cookies} cookies. Now {balance} cookies left."
    elif no_of_cookies <= 0:
        return balance, "Number of cookies must be greater than 0"
    else:
        return balance, "You don't have that many cookies"


def add_cookies(balance, no_of_cookies):
    if no_of_cookies > 0:
        balance += no_of_cookies
        return balance, f"Added {no_of_cookies} cookies to the jar"
    else:
        return balance, "Number of cookies must be greater than zero"


def show_balance(balance):
    return f"You currently have {balance} cookies in the jar"


def main():
    balance = 0
    while True:
        print("\n************ Cookie Jar **********\n")
        print("1. Number of cookies available")
        print("2. Add cookies")
        print("3. Take out cookies")
        print("4. Exit\n")

        choice = input("Please enter your choice (1/2/3/4): ")

        if choice == "1":
            print(show_balance(balance))

        elif choice == "2":
            no_of_cookies = int(input("Enter number of cookies to add: "))
            balance, message = add_cookies(balance, no_of_cookies)
            print(message)

        elif choice == "3":
            no_of_cookies = int(input("Enter number of cookies to take out: "))
            balance, message = take_out_cookies(balance, no_of_cookies)
            print(message)

        elif choice == "4":
            print("Exiting... 🍪")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()




