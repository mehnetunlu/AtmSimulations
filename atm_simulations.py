class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} dollars deposited.")
        else:
            print("Invalid amount! Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount} dollars withdrawn.")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Your account balance is {self.balance} dollars.")


def authenticate_user():
    correct_username = "admin"
    correct_password = "12345"

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == correct_username and password == correct_password:
        print("Account successfully logged in")
        return True
    else:
        print("Username or password is incorrect")
        return False


if __name__ == "__main__":
    if authenticate_user():
        account = Account("12345", 10000)

        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check balance")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            elif choice == "3":
                account.check_balance()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
    else:
        print("Incorrect username or password.")