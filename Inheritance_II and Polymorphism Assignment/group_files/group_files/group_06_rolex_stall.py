# =====================================================================
# OOP WITH PYTHON: INHERITANCE II + POLYMORPHISM (GROUP ACTIVITY)
# Group 6: Campus Rolex Stall Menu
#
# Full requirements and marking criteria: see the activity document.
# =====================================================================

GROUP_NUMBER = 6   # do not change

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
#   A rolex stall near campus is going digital. It needs menu items,
#   snacks, rolexes, and special rolexes that can be delivered AND
#   made vegetarian.

# =====================================================================
# MARKS (20)
#   A  Multilevel inheritance ........ 4    D  Duck typing ......... 3
#   B  Multiple inheritance + MRO .... 5    E  Questions ........... 4
#   C  Polymorphism .................. 3    File runs, no errors ... 1
# =====================================================================


# GIVEN: do not change
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        print(f"MenuItem: {self.name} | Price: {self.price}")

    def role(self):
        return "Menu item"


# =====================================================================
# PART A: MULTILEVEL INHERITANCE (4 marks)
# ---------------------------------------------------------------------
# A1. class Snack(MenuItem)
#       __init__(self, name, price, prep_minutes)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Prep minutes: {self.prep_minutes}")
#       role(self)      -> override: return "Snack"
#
# A2. class Rolex(Snack)
#       __init__(self, name, price, prep_minutes, eggs)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Eggs: {self.eggs}")
#       role(self)      -> override: return "Rolex"
# =====================================================================


# =====================================================================
# PART B: MULTIPLE INHERITANCE + MRO (5 marks)
# ---------------------------------------------------------------------
# B1. class Deliverable        (no parent class, no __init__)
#       badge(self)  -> return "Delivery available"
#       deliver(self, address)
#           -> print(f"{self.name} delivered to {address}")
#
# B2. class VegetarianOption        (no parent class, no __init__)
#       badge(self)  -> return "Vegetarian"
#       swap_ingredient(self, ingredient)
#           -> print(f"{self.name} now made with {ingredient}")
#
# B3. class SpecialRolex(Rolex, Deliverable, VegetarianOption)
#       (parents in EXACTLY this order)
#       __init__(self, name, price, prep_minutes, eggs, topping)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Topping: {self.topping}")
#                          print(f"   Badge: {self.badge()}")
#       role(self)      -> override: return "Special rolex"
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
#         MenuItem("Classic rolex", "UGX 3,000")
#         Snack("Classic rolex", "UGX 3,000", 7)
#         Rolex("Classic rolex", "UGX 3,000", 7, 2)
#         SpecialRolex("Classic rolex", "UGX 3,000", 7, 2, "Cheese")
# =====================================================================


# =====================================================================
# PART D: DUCK TYPING (3 marks)
# ---------------------------------------------------------------------
# D1. class DeliveryRider        (no parent class: NOT related to MenuItem)
#       __init__(self, rider)
#       role(self)      -> return "Delivery rider"
#       describe(self)  -> print(f"DeliveryRider: {self.rider}")
#
# D2. Add these two objects to the list in build_items():
#       DeliveryRider("Mugisha Allan")
#       Receipt("R-00981")
#
# D3. Receipt (given below) has no role() method. Change show_all() so it
#     prints "[no role]" for such an item, and still calls its describe().
# =====================================================================


# GIVEN: do not change
class Receipt:
    def __init__(self, number):
        self.number = number

    def describe(self):
        print(f"Receipt: {self.number}")


# =====================================================================
# PART E: QUESTIONS (4 marks)
# Answer inside the quotes. Explain WHY, not just what.
# =====================================================================

# GIVEN: do not change
#              Order
#             /      \
#     PhoneOrder     AppOrder
#             \      /
#            BulkOrder
class Order:
    def process(self):
        print("Order saved")


class PhoneOrder(Order):
    def process(self):
        print("Confirming by phone")
        super().process()


class AppOrder(Order):
    def process(self):
        print("Confirming in the app")
        super().process()


class BulkOrder(PhoneOrder, AppOrder):
    def process(self):
        print("Applying BULK pricing")
        super().process()


# E1. What is the MRO of SpecialRolex? Why does MenuItem come before Deliverable?
E1_ANSWER = """

"""

# E2. What does badge() return for a SpecialRolex object, and why?
#     What changes if the parents are written in this order instead:
#     (Rolex, VegetarianOption, Deliverable)? Why?
E2_ANSWER = """

"""

# E3. What does BulkOrder().process() print, in order? Which class's process()
#     does super() inside PhoneOrder call, and why? How many times does
#     Order.process() run?
E3_ANSWER = """

"""

# E4. Is an object of class DeliveryRider an instance of MenuItem? Why does
#     show_all() still work for it, and what is this called? Why did
#     Receipt fail before D3?
E4_ANSWER = """

"""


# =====================================================================
# YOUR TEST CODE: create objects and call their methods here
# =====================================================================
if __name__ == "__main__":
    pass
