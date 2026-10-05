# =====================================================================
# OOP WITH PYTHON: INHERITANCE II + POLYMORPHISM (GROUP ACTIVITY)
# Group 4: Mukono Community Bank Accounts
#
# Full requirements and marking criteria: see the activity document.
# =====================================================================

GROUP_NUMBER = 4   # do not change

# =====================================================================
# GROUP MEMBERS (full name, reg. number)
# =====================================================================
#  1.
#  2.
#  3.
#  4.
#  5.
#  6.
#  7.
#  8.
#  9.
# 10.
# 11.
# 12.
# Submitted by:

# =====================================================================
# SCENARIO
# =====================================================================
#   A community bank in Mukono is modelling its accounts: basic
#   accounts, savings, gold savings, and premium accounts linked to
#   BOTH mobile money and a Visa card.

# =====================================================================
# MARKS (20)
#   A  Multilevel inheritance ........ 4    D  Duck typing ......... 3
#   B  Multiple inheritance + MRO .... 5    E  Questions ........... 4
#   C  Polymorphism .................. 3    File runs, no errors ... 1
# =====================================================================


# GIVEN: do not change
class Account:
    def __init__(self, holder, account_no):
        self.holder = holder
        self.account_no = account_no

    def describe(self):
        print(f"Account: {self.holder} | Account No: {self.account_no}")

    def role(self):
        return "Bank account"


# =====================================================================
# PART A: MULTILEVEL INHERITANCE (4 marks)
# ---------------------------------------------------------------------
# A1. class SavingsAccount(Account)
#       __init__(self, holder, account_no, interest_rate)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Interest rate: {self.interest_rate}")
#       role(self)      -> override: return "Savings account"
#
# A2. class GoldSavings(SavingsAccount)
#       __init__(self, holder, account_no, interest_rate, minimum_balance)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Minimum balance: {self.minimum_balance}")
#       role(self)      -> override: return "Gold savings account"
# =====================================================================


# =====================================================================
# PART B: MULTIPLE INHERITANCE + MRO (5 marks)
# ---------------------------------------------------------------------
# B1. class MobileMoneyLinked        (no parent class, no __init__)
#       channel(self)  -> return "Mobile money"
#       send_to_phone(self, phone)
#           -> print(f"{self.holder} sends money to {phone}")
#
# B2. class CardEnabled        (no parent class, no __init__)
#       channel(self)  -> return "Visa card"
#       swipe(self, shop)
#           -> print(f"{self.holder} swipes card at {shop}")
#
# B3. class PremiumAccount(GoldSavings, MobileMoneyLinked, CardEnabled)
#       (parents in EXACTLY this order)
#       __init__(self, holder, account_no, interest_rate, minimum_balance, manager)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Relationship manager: {self.manager}")
#                          print(f"   Main channel: {self.channel()}")
#       role(self)      -> override: return "Premium account"
# =====================================================================


# =====================================================================
# PART C: POLYMORPHISM (3 marks)
# ---------------------------------------------------------------------
# C1. show_all(items)
#       -> for each item: print(f"[{item.role()}]"), then item.describe(),
#          then print(). No isinstance() or type() checks.
#
# C2. build_items()
#       -> return a list with one object of each class, using these values:
#         Account("Namusoke Ruth", "0123456789")
#         SavingsAccount("Namusoke Ruth", "0123456789", "6%")
#         GoldSavings("Namusoke Ruth", "0123456789", "6%", "UGX 1,000,000")
#         PremiumAccount("Namusoke Ruth", "0123456789", "6%", "UGX 1,000,000", "Ssali Paul")
# =====================================================================


# =====================================================================
# PART D: DUCK TYPING (3 marks)
# ---------------------------------------------------------------------
# D1. class SaccoShare        (no parent class: NOT related to Account)
#       __init__(self, sacco)
#       role(self)      -> return "SACCO shares"
#       describe(self)  -> print(f"SaccoShare: {self.sacco}")
#
# D2. Add these two objects to the list in build_items():
#       SaccoShare("Mukono Teachers SACCO")
#       ATM("Mukono town branch")
#
# D3. ATM (given below) has no role() method. Change show_all() so it
#     prints "[no role]" for such an item, and still calls its describe().
# =====================================================================


# GIVEN: do not change
class ATM:
    def __init__(self, location):
        self.location = location

    def describe(self):
        print(f"ATM: {self.location}")


# =====================================================================
# PART E: QUESTIONS (4 marks)
# Answer inside the quotes. Explain WHY, not just what.
# =====================================================================

# GIVEN: do not change
#               Report
#              /      \
#     DailyReport    AuditReport
#              \      /
#           MonthEndReport
class Report:
    def generate(self):
        print("Report saved")


class DailyReport(Report):
    def generate(self):
        print("Adding today's transactions")
        super().generate()


class AuditReport(Report):
    def generate(self):
        print("Adding audit checks")
        super().generate()


class MonthEndReport(DailyReport, AuditReport):
    def generate(self):
        print("Adding MONTH-END totals")
        super().generate()


# E1. What is the MRO of PremiumAccount? Why does Account come before MobileMoneyLinked?
E1_ANSWER = """

"""

# E2. What does channel() return for a PremiumAccount object, and why?
#     What changes if the parents are written in this order instead:
#     (GoldSavings, CardEnabled, MobileMoneyLinked)? Why?
E2_ANSWER = """

"""

# E3. What does MonthEndReport().generate() print, in order? Which class's generate()
#     does super() inside DailyReport call, and why? How many times does
#     Report.generate() run?
E3_ANSWER = """

"""

# E4. Is an object of class SaccoShare an instance of Account? Why does
#     show_all() still work for it, and what is this called? Why did
#     ATM fail before D3?
E4_ANSWER = """

"""


# =====================================================================
# YOUR TEST CODE: create objects and call their methods here
# =====================================================================
if __name__ == "__main__":
    pass
