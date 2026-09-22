class StudentAccount:
    # This class attribute counts all account objects created.
    account_count = 0

    def __init__(self, student_name, registration_number, programme, balance, pin, daily_limit):
        self.student_name = student_name  # Public: ordinary identity information.
        self.registration_number = registration_number  # Public: used to identify records.
        self._programme = programme  # Protected: subclasses may use it, but callers should not overwrite it casually.
        self.__balance = balance  # Private/name-mangled: balance must change through account behaviour.
        self.__pin = pin  # Private/name-mangled: PIN should not be exposed directly.
        self._daily_limit = daily_limit  # Protected: controlled account rule for subclasses.
        self.transactions = []
        StudentAccount.account_count += 1

    def deposit(self, amount):
        # Deposits increase only this account's private balance.
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.__balance += amount

    def make_payment(self, amount, service):
        # A successful payment reduces the balance and records the service used.
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        if amount > self.__balance:
            raise ValueError("Payment cannot exceed the available balance.")
        self.__balance -= amount
        self.transactions.append((service, amount))

    def get_balance(self):
        return self.__balance

    def display_summary(self):
        print(f"{self.student_name} | {self.registration_number} | {self._programme}")
        print(f"Balance: UGX {self.__balance:,.0f} | Daily limit: UGX {self._daily_limit:,.0f}")
        print(f"Transactions: {len(self.transactions)}")


if __name__ == "__main__":
    brian = StudentAccount("Elimu Brian Joshua", "S25B13/083", "BSIT", 30000, "1234", 15000)
    grace = StudentAccount("Grace Namusoke", "S25B13/084", "BSIT", 20000, "5678", 10000)
    daniel = StudentAccount("Daniel Okello", "S25B13/085", "BSE", 10000, "9012", 5000)

    brian.deposit(5000)
    brian.make_payment(3000, "PRINTING")
    brian.display_summary()
    print("Grace balance is unchanged:", grace.get_balance())
    print("Created accounts:", StudentAccount.account_count)

    print("Public attribute:", brian.student_name)
    print("Protected attribute (available by convention):", brian._programme)
    try:
        print(brian.__balance)
    except AttributeError as error:
        print("Direct private access fails:", error)
    print("Name-mangled access for investigation only:", brian._StudentAccount__balance)
    print("Double underscore is name mangling, not encryption or absolute security.")
