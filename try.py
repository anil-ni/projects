import getpass


class ATM:
    def __init__(self, balance=0, pin='1234'):
        self.balance = balance
        self.pin = pin

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. Current balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew {amount}. Current balance: {self.balance}"


def main():
    atm = ATM()

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            print("Current Balance:", atm.check_balance())
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            print(atm.deposit(amount))
        elif choice == '3':
            pin = getpass.getpass("Enter PIN: ")
            amount = float(input("Enter amount to withdraw: "))
            print(atm.withdraw(amount) if pin == atm.pin else "Invalid PIN")
        elif choice == '4':
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
