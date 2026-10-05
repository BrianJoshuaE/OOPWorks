# =====================================================================
# OOP WITH PYTHON: INHERITANCE II + POLYMORPHISM (GROUP ACTIVITY)
# Group 12: Supermarket Product Catalogue
#
# Full requirements and marking criteria: see the activity document.
# =====================================================================

GROUP_NUMBER = 12   # do not change

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
#   A supermarket in Kampala is cataloguing its stock: products, food
#   products, dairy products, and imported cheese that is BOTH
#   imported and on offer.

# =====================================================================
# MARKS (20)
#   A  Multilevel inheritance ........ 4    D  Duck typing ......... 3
#   B  Multiple inheritance + MRO .... 5    E  Questions ........... 4
#   C  Polymorphism .................. 3    File runs, no errors ... 1
# =====================================================================


# GIVEN: do not change
class Product:
    def __init__(self, name, barcode):
        self.name = name
        self.barcode = barcode

    def describe(self):
        print(f"Product: {self.name} | Barcode: {self.barcode}")

    def role(self):
        return "Product"


# =====================================================================
# PART A: MULTILEVEL INHERITANCE (4 marks)
# ---------------------------------------------------------------------
# A1. class FoodProduct(Product)
#       __init__(self, name, barcode, expiry_date)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Expiry date: {self.expiry_date}")
#       role(self)      -> override: return "Food product"
#
# A2. class DairyProduct(FoodProduct)
#       __init__(self, name, barcode, expiry_date, fat_percent)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Fat %: {self.fat_percent}")
#       role(self)      -> override: return "Dairy product"
# =====================================================================


# =====================================================================
# PART B: MULTIPLE INHERITANCE + MRO (5 marks)
# ---------------------------------------------------------------------
# B1. class Imported        (no parent class, no __init__)
#       shelf_tag(self)  -> return "Imported"
#       clear_customs(self, port)
#           -> print(f"{self.name} cleared customs at {port}")
#
# B2. class Discounted        (no parent class, no __init__)
#       shelf_tag(self)  -> return "On offer"
#       apply_discount(self, percent)
#           -> print(f"{self.name} discounted by {percent}")
#
# B3. class ImportedCheese(DairyProduct, Imported, Discounted)
#       (parents in EXACTLY this order)
#       __init__(self, name, barcode, expiry_date, fat_percent, country)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Country: {self.country}")
#                          print(f"   Shelf tag: {self.shelf_tag()}")
#       role(self)      -> override: return "Imported cheese"
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
#         Product("Gouda cheese", "6001234567890")
#         FoodProduct("Gouda cheese", "6001234567890", "30 Nov 2026")
#         DairyProduct("Gouda cheese", "6001234567890", "30 Nov 2026", 28)
#         ImportedCheese("Gouda cheese", "6001234567890", "30 Nov 2026", 28, "Netherlands")
# =====================================================================


# =====================================================================
# PART D: DUCK TYPING (3 marks)
# ---------------------------------------------------------------------
# D1. class GiftVoucher        (no parent class: NOT related to Product)
#       __init__(self, code)
#       role(self)      -> return "Gift voucher"
#       describe(self)  -> print(f"GiftVoucher: {self.code}")
#
# D2. Add these two objects to the list in build_items():
#       GiftVoucher("GV-50000")
#       ShoppingBasket("20 items")
#
# D3. ShoppingBasket (given below) has no role() method. Change show_all() so it
#     prints "[no role]" for such an item, and still calls its describe().
# =====================================================================


# GIVEN: do not change
class ShoppingBasket:
    def __init__(self, capacity):
        self.capacity = capacity

    def describe(self):
        print(f"ShoppingBasket: {self.capacity}")


# =====================================================================
# PART E: QUESTIONS (4 marks)
# Answer inside the quotes. Explain WHY, not just what.
# =====================================================================

# GIVEN: do not change
#             Promotion
#              /      \
#      RadioPromo    SocialPromo
#              \      /
#            LaunchPromo
class Promotion:
    def run_promo(self):
        print("Promotion saved")


class RadioPromo(Promotion):
    def run_promo(self):
        print("Playing advert on the radio")
        super().run_promo()


class SocialPromo(Promotion):
    def run_promo(self):
        print("Posting on social media")
        super().run_promo()


class LaunchPromo(RadioPromo, SocialPromo):
    def run_promo(self):
        print("Adding LAUNCH discount banner")
        super().run_promo()


# E1. What is the MRO of ImportedCheese? Why does Product come before Imported?
E1_ANSWER = """

"""

# E2. What does shelf_tag() return for a ImportedCheese object, and why?
#     What changes if the parents are written in this order instead:
#     (DairyProduct, Discounted, Imported)? Why?
E2_ANSWER = """

"""

# E3. What does LaunchPromo().run_promo() print, in order? Which class's run_promo()
#     does super() inside RadioPromo call, and why? How many times does
#     Promotion.run_promo() run?
E3_ANSWER = """

"""

# E4. Is an object of class GiftVoucher an instance of Product? Why does
#     show_all() still work for it, and what is this called? Why did
#     ShoppingBasket fail before D3?
E4_ANSWER = """

"""


# =====================================================================
# YOUR TEST CODE: create objects and call their methods here
# =====================================================================
if __name__ == "__main__":
    pass
