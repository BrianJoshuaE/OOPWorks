class ControlledAccount:
    def __init__(self, name, registration_number, programme, balance, daily_limit):
        # Sensitive values are stored privately and changed through controlled methods.
        self.name = name
        self.registration_number = registration_number
        self._programme = programme
        self.__balance = balance
        self.__daily_limit = daily_limit
        self._transactions = []

    def get_balance(self):
        return self.__balance

    def set_programme(self, programme):
        # Reject empty programme names before changing the stored value.
        if not isinstance(programme, str) or not programme.strip():
            raise ValueError("Programme must be a non-empty string.")
        self._programme = programme.strip()

    @property
    def daily_limit(self):
        return self.__daily_limit

    @daily_limit.setter
    def daily_limit(self, value):
        # The setter keeps the spending limit valid.
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Daily limit must be a positive number.")
        self.__daily_limit = value

    @property
    def transaction_count(self):
        # No setter is provided, so callers can read but not assign this value.
        return len(self._transactions)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero.")
        self.__balance += amount

    def make_payment(self, amount, service):
        if amount <= 0 or amount > self.__balance or amount > self.daily_limit:
            raise ValueError("Payment is outside the allowed limits.")
        self.__balance -= amount
        self._transactions.append((service, amount))

    def summary(self):
        return f"{self.name}: UGX {self.get_balance():,.0f}, limit UGX {self.daily_limit:,.0f}, transactions {self.transaction_count}"


if __name__ == "__main__":
    account = ControlledAccount("Elimu Brian Joshua", "S25B13/083", "BSIT", 25000, 10000)
    print("Classic getter:", account.get_balance())
    account.set_programme("Computer Science")
    print("Updated programme:", account._programme)
    try:
        account.set_programme("")
    except ValueError as error:
        print("Invalid programme rejected; last valid value remains:", error)

    print("Property read:", account.daily_limit)
    account.daily_limit = 12000
    print("Valid property update:", account.daily_limit)
    try:
        account.daily_limit = -1
    except ValueError as error:
        print("Invalid limit rejected; current value remains:", error)
    print("Current limit:", account.daily_limit)

    account.make_payment(3000, "LABORATORY")
    print("Read-only transaction_count:", account.transaction_count)
    try:
        account.transaction_count = 99
    except AttributeError as error:
        print("Read-only property cannot be assigned:", error)
    print(account.summary())
