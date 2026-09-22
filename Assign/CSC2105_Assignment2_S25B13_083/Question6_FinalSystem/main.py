from pathlib import Path


class CampusService:
    def __init__(self, name, location):
        self.name = name
        self.location = location


class Transaction:
    def __init__(self, registration_number, transaction_type, amount, service, balance):
        self.registration_number = registration_number
        self.transaction_type = transaction_type
        self.amount = amount
        self.service = service
        self.balance = balance

    def record(self):
        return f"{self.registration_number} | {self.transaction_type} | {self.amount:.0f} | {self.service} | {self.balance:.0f}\n"


class StudentAccount:
    # Each object owns its own balance, spending total and transaction list.
    account_count = 0

    def __init__(self, student_name, registration_number, programme, balance, pin, daily_limit):
        self.student_name = student_name
        self.registration_number = registration_number
        self._programme = programme
        self.__balance = balance
        self.__pin = pin
        self._daily_limit = daily_limit
        self._daily_spent = 0
        self.transactions = []
        StudentAccount.account_count += 1

    def get_balance(self):
        return self.__balance

    @property
    def daily_limit(self):
        return self._daily_limit

    @daily_limit.setter
    def daily_limit(self, value):
        if value <= 0:
            raise ValueError("Daily limit must be positive.")
        self._daily_limit = value

    @property
    def transaction_count(self):
        return len(self.transactions)

    def deposit(self, amount, file_path):
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero.")
        self.__balance += amount
        self._record("DEPOSIT", amount, "ACCOUNT", file_path)

    def make_payment(self, amount, service, file_path):
        # Both the balance and the daily spending limit must allow the payment.
        if amount <= 0:
            raise ValueError("Payment must be greater than zero.")
        if amount > self.__balance:
            raise ValueError("Payment exceeds available balance.")
        if self._daily_spent + amount > self.daily_limit:
            raise ValueError("Payment exceeds daily spending limit.")
        self.__balance -= amount
        self._daily_spent += amount
        self._record("PAYMENT", amount, service.name, file_path)

    def _record(self, transaction_type, amount, service, file_path):
        # Keep an in-memory transaction and save the same record for later retrieval.
        transaction = Transaction(self.registration_number, transaction_type, amount, service, self.__balance)
        self.transactions.append(transaction)
        with open(file_path, "a", encoding="utf-8") as transaction_file:
            transaction_file.write(transaction.record())

    def summary(self):
        return (f"{self.student_name} | {self.registration_number} | {self._programme} | "
                f"Balance UGX {self.__balance:,.0f} | Transactions {self.transaction_count}")


def show_history(file_path):
    print("\nSAVED TRANSACTION HISTORY")
    try:
        with open(file_path, "r", encoding="utf-8") as transaction_file:
            print(transaction_file.read(), end="")
    except FileNotFoundError:
        print("No saved transactions yet.")


if __name__ == "__main__":
    # Run a short scenario with valid and invalid student transactions.
    file_path = Path(__file__).with_name("transactions.txt")
    file_path.unlink(missing_ok=True)

    printing = CampusService("PRINTING", "Library")
    cafeteria = CampusService("CAFETERIA", "Main block")
    laboratory = CampusService("LABORATORY", "Science block")

    student_a = StudentAccount("Elimu Brian Joshua", "S25B13/083", "BSIT", 10000, "1234", 8000)
    student_b = StudentAccount("Grace Namusoke", "S25B13/084", "BSIT", 15000, "5678", 7000)
    student_c = StudentAccount("Daniel Okello", "S25B13/085", "BSE", 4000, "9012", 3000)

    print("Accounts created:", StudentAccount.account_count)
    student_a.deposit(5000, file_path)
    student_a.make_payment(2500, printing, file_path)
    student_b.make_payment(3000, cafeteria, file_path)

    try:
        student_c.make_payment(5000, laboratory, file_path)
    except ValueError as error:
        print("Handled invalid Student C transaction:", error)

    print("Student A balance changed independently:", student_a.get_balance())
    print("Student B balance is independent:", student_b.get_balance())
    print("Protected programme:", student_a._programme)
    print("Private balance through getter:", student_a.get_balance())
    print("Read-only transaction count:", student_a.transaction_count)
    show_history(file_path)
    print("\nFINAL ACCOUNT SUMMARIES")
    for account in (student_a, student_b, student_c):
        print(account.summary())
