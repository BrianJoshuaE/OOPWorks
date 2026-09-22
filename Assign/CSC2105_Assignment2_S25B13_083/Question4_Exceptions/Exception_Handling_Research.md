# Question 4(a): Exception Handling Research

- `try` surrounds code that may fail, such as `float("five thousand")`.
- `except` catches a selected error so the program can respond instead of terminating. `ValueError` is raised when a value has the right general type but an unsuitable format or value, for example `float("five thousand")`.
- `else` runs only when the `try` block succeeds. In this program it reports that numeric input was accepted.
- `finally` runs whether an error happened or not. It is suitable for cleanup or a message that input processing has finished.
- `raise ValueError("Deposit amount must be greater than zero.")` deliberately creates an exception when a business rule is broken. This prevents a negative deposit from corrupting the account.

Example:

```python
try:
    amount = float(user_text)
except ValueError:
    print("Enter a number")
else:
    print("Input accepted")
finally:
    print("Input processing finished")
```

The runnable implementation and five test cases are in `reliable_account.py`.

Reference: Python Software Foundation, [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html).