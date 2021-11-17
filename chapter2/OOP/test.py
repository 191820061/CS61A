class Account:
    interest = 0.2

    def __init__(self, holder_name):
        self.holder_name = holder_name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def with_draw(self, amount):
        if amount > self.balance:
            return "Lack of balance"
        self.balance -= amount
        return self.balance


class SavingsAccount(Account):
    deposit_charge = 2

    def deposit(self, amount):
        return super().deposit(amount - self.deposit_charge)


class CheckingAccount(Account):
    withdraw_charge = 1
    interest = 0.01

    def with_draw(self, amount):
        return super().with_draw(amount + self.withdraw_charge)


class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, holder_name):
        super().__init__(holder_name)
        self.balance = 1


such_a_deal = AsSeenOnTVAccount("John")
print(such_a_deal.deposit(20))
print(such_a_deal.with_draw(5))
print([c.__name__ for c in AsSeenOnTVAccount.mro()])

print(such_a_deal.__getattribute__("holder_name"))