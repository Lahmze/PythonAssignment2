class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance  # private attribute (name-mangled)

    def deposit(self, amount=None):
        if amount is None:
            try:
                amount = float(input("Enter deposit amount: "))
            except ValueError:
                print("Invalid input. Please enter a numeric amount.")
                return False

        if amount <= 0:
            print("Invalid deposit amount.")
            return False

        self.__balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        return True

    def withdraw(self, amount=None):

        if amount is None:
            try:
                amount = float(input("Enter withdrawal amount: "))
            except ValueError:
                print("Invalid input. Please enter a numeric amount.")
                return False

        if amount <= 0:
            print("Invalid withdrawal amount.")
            return False

        if amount > self.__balance:
            print("Insufficient funds.")
            return False

        self.__balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
        return True

    def get_balance(self):
        return self.__balance

    def display_balance(self):
        print(f"{self.owner}'s current balance: ${self.__balance:.2f}")


def main():
    account = BankAccount("Lameck", 1000)
    account.display_balance()

    account.deposit()
    account.withdraw()
    account.withdraw()
    account.deposit()

    account.display_balance()

    # Demonstrating encapsulation:
    try:
        print(account.__balance)   # direct access fails
    except AttributeError as e:
        print(f"Direct access blocked: {e}")

    print("Underlying mangled attribute (not meant to be accessed this way):",
          account._BankAccount__balance)


if __name__ == '__main__':
    main()