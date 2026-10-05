# =====================================================================
# OOP WITH PYTHON: INHERITANCE II + POLYMORPHISM (GROUP ACTIVITY)
# Group 8: University Library Catalogue
#
# Full requirements and marking criteria: see the activity document.
# =====================================================================

GROUP_NUMBER = 8   # do not change

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
#   The university library is rebuilding its catalogue: library items,
#   books, textbooks, and hybrid textbooks that can be borrowed on
#   paper AND read online.

# =====================================================================
# MARKS (20)
#   A  Multilevel inheritance ........ 4    D  Duck typing ......... 3
#   B  Multiple inheritance + MRO .... 5    E  Questions ........... 4
#   C  Polymorphism .................. 3    File runs, no errors ... 1
# =====================================================================


# GIVEN: do not change
class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

    def describe(self):
        print(f"LibraryItem: {self.title} | Item ID: {self.item_id}")

    def role(self):
        return "Library item"


# =====================================================================
# PART A: MULTILEVEL INHERITANCE (4 marks)
# ---------------------------------------------------------------------
# A1. class Book(LibraryItem)
#       __init__(self, title, item_id, author)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Author: {self.author}")
#       role(self)      -> override: return "Book"
#
# A2. class Textbook(Book)
#       __init__(self, title, item_id, author, course_code)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Course code: {self.course_code}")
#       role(self)      -> override: return "Textbook"
# =====================================================================


# =====================================================================
# PART B: MULTIPLE INHERITANCE + MRO (5 marks)
# ---------------------------------------------------------------------
# B1. class Borrowable        (no parent class, no __init__)
#       access_rule(self)  -> return "Two-week loan"
#       borrow(self, member)
#           -> print(f"{self.title} is borrowed by {member}")
#
# B2. class Digital        (no parent class, no __init__)
#       access_rule(self)  -> return "Online reading only"
#       download(self, device)
#           -> print(f"{self.title} opened on {device}")
#
# B3. class HybridTextbook(Textbook, Borrowable, Digital)
#       (parents in EXACTLY this order)
#       __init__(self, title, item_id, author, course_code, platform)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Platform: {self.platform}")
#                          print(f"   Access rule: {self.access_rule()}")
#       role(self)      -> override: return "Hybrid textbook"
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
#         LibraryItem("Python Basics", "LIB-3301")
#         Book("Python Basics", "LIB-3301", "Kizza Ronald")
#         Textbook("Python Basics", "LIB-3301", "Kizza Ronald", "CSC2101")
#         HybridTextbook("Python Basics", "LIB-3301", "Kizza Ronald", "CSC2101", "UCU e-Library")
# =====================================================================


# =====================================================================
# PART D: DUCK TYPING (3 marks)
# ---------------------------------------------------------------------
# D1. class Newspaper        (no parent class: NOT related to LibraryItem)
#       __init__(self, date)
#       role(self)      -> return "Daily newspaper"
#       describe(self)  -> print(f"Newspaper: {self.date}")
#
# D2. Add these two objects to the list in build_items():
#       Newspaper("2 October 2026")
#       ReadingTable(14)
#
# D3. ReadingTable (given below) has no role() method. Change show_all() so it
#     prints "[no role]" for such an item, and still calls its describe().
# =====================================================================


# GIVEN: do not change
class ReadingTable:
    def __init__(self, table_no):
        self.table_no = table_no

    def describe(self):
        print(f"ReadingTable: {self.table_no}")


# =====================================================================
# PART E: QUESTIONS (4 marks)
# Answer inside the quotes. Explain WHY, not just what.
# =====================================================================

# GIVEN: do not change
#                Reminder
#               /        \
#     EmailReminder     SMSReminder
#               \        /
#            OverdueReminder
class Reminder:
    def remind(self):
        print("Reminder saved")


class EmailReminder(Reminder):
    def remind(self):
        print("Emailing the borrower")
        super().remind()


class SMSReminder(Reminder):
    def remind(self):
        print("Texting the borrower")
        super().remind()


class OverdueReminder(EmailReminder, SMSReminder):
    def remind(self):
        print("Adding OVERDUE fine notice")
        super().remind()


# E1. What is the MRO of HybridTextbook? Why does LibraryItem come before Borrowable?
E1_ANSWER = """

"""

# E2. What does access_rule() return for a HybridTextbook object, and why?
#     What changes if the parents are written in this order instead:
#     (Textbook, Digital, Borrowable)? Why?
E2_ANSWER = """

"""

# E3. What does OverdueReminder().remind() print, in order? Which class's remind()
#     does super() inside EmailReminder call, and why? How many times does
#     Reminder.remind() run?
E3_ANSWER = """

"""

# E4. Is an object of class Newspaper an instance of LibraryItem? Why does
#     show_all() still work for it, and what is this called? Why did
#     ReadingTable fail before D3?
E4_ANSWER = """

"""


# =====================================================================
# YOUR TEST CODE: create objects and call their methods here
# =====================================================================
if __name__ == "__main__":
    pass
