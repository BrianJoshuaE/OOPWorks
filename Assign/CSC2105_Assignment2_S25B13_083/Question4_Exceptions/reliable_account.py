class ReliableAccount:
    def __init__(self, name, balance, daily_limit):
        if balance < 0:
            raise ValueError("Opening balance cannot be negative.")
        if daily_limit <= 0:
            raise ValueError("Daily spending limit must be greater than zero.")
        self.name = name
        self.balance = balance
        self.daily_limit = daily_limit

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount

    def make_payment(self, amount, service):
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Payment cannot exceed the available balance.")
        if amount > self.daily_limit:
            raise ValueError("Payment cannot exceed the daily spending limit.")
        self.balance -= amount
        return f"{service} payment accepted: UGX {amount:,.0f}"


def read_money(user_text):
    # Convert user input safely instead of allowing invalid text to crash the program.
    try:
        amount = float(user_text)
    except ValueError:
        print("Invalid number: enter a numeric amount such as 5000.")
        return None
    else:
        print("Numeric input accepted.")
        return amount
    finally:
        print("Input processing finished.")


def prompt_for_money(prompt="Enter amount: "):
    """Safely convert a value typed by a user into a number."""
    return read_money(input(prompt))


def run_test(label, action, expected):
    # This helper lets each valid or invalid operation complete without stopping the demo.
    print(f"\nTEST: {label}\nExpected: {expected}")
    try:
        result = action()
    except (ValueError, TypeError) as error:
        print("Handled error:", error)
    else:
        print("Result:", result)
    finally:
        print("Test complete.")


if __name__ == "__main__":
    account = ReliableAccount("Elimu Brian Joshua", 10000, 8000)
    run_test("valid deposit", lambda: account.deposit(5000), "Balance increases to UGX 15,000")
    run_test("invalid deposit", lambda: account.deposit(-200), "ValueError is caught")
    run_test("valid payment", lambda: account.make_payment(3000, "PRINTING"), "Payment accepted")
    run_test("payment greater than balance", lambda: account.make_payment(50000, "CAFETERIA"), "ValueError is caught")
    run_test("non-numeric input", lambda: read_money("five thousand"), "Input is rejected without crashing")
    run_test("invalid spending limit", lambda: ReliableAccount("Test student", 1000, -1), "ValueError is caught")
    print("Final balance: UGX", f"{account.balance:,.0f}")
