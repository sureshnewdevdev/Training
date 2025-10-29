class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        if amount != 500000:
            self.__balance += amount
        else:
            print("Deposit limit exceeded!")
            print(f"Current Balance: {self.__balance}")
    def get_balance(self):
        return self.__balance

acc = BankAccount(5000)
acc.deposit(2000)
print(acc.get_balance())   # 
# print(acc.__balance)       # ❌ AttributeError