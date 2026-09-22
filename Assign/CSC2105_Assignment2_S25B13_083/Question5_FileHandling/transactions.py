from pathlib import Path


class TransactionAccount:
    def __init__(self, registration_number, balance):
        self.registration_number = registration_number
        self.balance = balance

    def deposit(self, amount, file_path):
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero.")
        self.balance += amount
        self._save("DEPOSIT", amount, "ACCOUNT", file_path)

    def pay(self, amount, service, file_path):
        if amount <= 0 or amount > self.balance:
            raise ValueError("Payment must be positive and affordable.")
        self.balance -= amount
        self._save("PAYMENT", amount, service, file_path)

    def _save(self, transaction_type, amount, service, file_path):
        # Append each successful transaction so earlier records are preserved.
        record = f"{self.registration_number} | {transaction_type} | {amount:.0f} | {service} | {self.balance:.0f}\n"
        with open(file_path, "a", encoding="utf-8") as transaction_file:
            transaction_file.write(record)


def display_previous_transactions(file_path):
    print("Previous transactions:")
    try:
        # Reading may fail on the first run because the file does not exist yet.
        with open(file_path, "r", encoding="utf-8") as transaction_file:
            contents = transaction_file.read()
    except FileNotFoundError:
        print("No transaction file exists yet.")
    else:
        print(contents, end="" if contents.endswith("\n") else "\n")
    finally:
        print("Finished reading transaction history.")


if __name__ == "__main__":
    file_path = Path(__file__).with_name("transactions.txt")
    account = TransactionAccount("S25B13/083", 25000)
    account.deposit(5000, file_path)
    account.pay(3000, "CAFETERIA", file_path)
    print("A transaction was written. The program may now be closed and run again.")
    display_previous_transactions(file_path)
    print("Current balance: UGX", f"{account.balance:,.0f}")

    print("Modes: r reads an existing file; w writes and replaces its contents; a appends new records.")
    print("open() obtains a file, read() gets text, write() stores text, and close() releases it.")
    print("The with statement closes the file automatically, even when an error occurs.")
