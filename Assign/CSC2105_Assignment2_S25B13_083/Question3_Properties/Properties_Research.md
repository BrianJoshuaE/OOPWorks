# Question 3(c): Research on `@property`

Python's `@property` turns a method into an attribute-style interface. Code can read `account.daily_limit` instead of calling a getter such as `account.get_daily_limit()`.

A property getter is the method marked with `@property`. It calculates or returns the value when the property is read. A property setter is connected using `@daily_limit.setter`; it runs when code assigns a new value. The setter can validate the new value before storing it, so invalid data does not replace the last valid value.

Properties are useful because they keep simple attribute syntax while preserving controlled access. Existing client code can use `account.daily_limit`, and the class can later add validation without changing the way callers read the value. A property without a setter is read-only through the normal attribute interface. The `transaction_count` property in `controlled_account.py` demonstrates this pattern.

Reference: Python Software Foundation, [Built-in Functions: `property`](https://docs.python.org/3/library/functions.html#property).