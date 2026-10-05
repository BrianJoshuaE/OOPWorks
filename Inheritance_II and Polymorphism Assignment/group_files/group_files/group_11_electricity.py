# =====================================================================
# OOP WITH PYTHON: INHERITANCE II + POLYMORPHISM (GROUP ACTIVITY)
# Group 11: Electricity Customer Records
#
# Full requirements and marking criteria: see the activity document.
# =====================================================================

GROUP_NUMBER = 11   # do not change

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
#   An electricity distributor is updating its customer records:
#   customers, domestic customers, prepaid customers, and green homes
#   with BOTH solar panels and a smart meter.

# =====================================================================
# MARKS (20)
#   A  Multilevel inheritance ........ 4    D  Duck typing ......... 3
#   B  Multiple inheritance + MRO .... 5    E  Questions ........... 4
#   C  Polymorphism .................. 3    File runs, no errors ... 1
# =====================================================================


# GIVEN: do not change
class Customer:
    def __init__(self, name, meter_no):
        self.name = name
        self.meter_no = meter_no

    def describe(self):
        print(f"Customer: {self.name} | Meter No: {self.meter_no}")

    def role(self):
        return "Customer"


# =====================================================================
# PART A: MULTILEVEL INHERITANCE (4 marks)
# ---------------------------------------------------------------------
# A1. class DomesticCustomer(Customer)
#       __init__(self, name, meter_no, district)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   District: {self.district}")
#       role(self)      -> override: return "Domestic customer"
#
# A2. class PrepaidCustomer(DomesticCustomer)
#       __init__(self, name, meter_no, district, units)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Units: {self.units}")
#       role(self)      -> override: return "Prepaid customer"
# =====================================================================


# =====================================================================
# PART B: MULTIPLE INHERITANCE + MRO (5 marks)
# ---------------------------------------------------------------------
# B1. class SolarUser        (no parent class, no __init__)
#       tariff(self)  -> return "Solar feed-in tariff"
#       feed_in(self, kwh)
#           -> print(f"{self.name} sells {kwh} back to the grid")
#
# B2. class SmartMeterUser        (no parent class, no __init__)
#       tariff(self)  -> return "Smart time-of-use tariff"
#       read_remotely(self, month)
#           -> print(f"Meter of {self.name} read remotely for {month}")
#
# B3. class GreenHome(PrepaidCustomer, SolarUser, SmartMeterUser)
#       (parents in EXACTLY this order)
#       __init__(self, name, meter_no, district, units, panels)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Solar panels: {self.panels}")
#                          print(f"   Tariff: {self.tariff()}")
#       role(self)      -> override: return "Green home"
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
#         Customer("Tumusiime Ivan", "04512338791")
#         DomesticCustomer("Tumusiime Ivan", "04512338791", "Mukono")
#         PrepaidCustomer("Tumusiime Ivan", "04512338791", "Mukono", 120)
#         GreenHome("Tumusiime Ivan", "04512338791", "Mukono", 120, 6)
# =====================================================================


# =====================================================================
# PART D: DUCK TYPING (3 marks)
# ---------------------------------------------------------------------
# D1. class Generator        (no parent class: NOT related to Customer)
#       __init__(self, model)
#       role(self)      -> return "Backup power"
#       describe(self)  -> print(f"Generator: {self.model}")
#
# D2. Add these two objects to the list in build_items():
#       Generator("5 kVA diesel")
#       ElectricPole("MK-1187")
#
# D3. ElectricPole (given below) has no role() method. Change show_all() so it
#     prints "[no role]" for such an item, and still calls its describe().
# =====================================================================


# GIVEN: do not change
class ElectricPole:
    def __init__(self, pole_no):
        self.pole_no = pole_no

    def describe(self):
        print(f"ElectricPole: {self.pole_no}")


# =====================================================================
# PART E: QUESTIONS (4 marks)
# Answer inside the quotes. Explain WHY, not just what.
# =====================================================================

# GIVEN: do not change
#               Bill
#             /      \
#     EnergyBill    WaterBill
#             \      /
#           CombinedBill
class Bill:
    def print_bill(self):
        print("Bill saved")


class EnergyBill(Bill):
    def print_bill(self):
        print("Adding electricity charges")
        super().print_bill()


class WaterBill(Bill):
    def print_bill(self):
        print("Adding water charges")
        super().print_bill()


class CombinedBill(EnergyBill, WaterBill):
    def print_bill(self):
        print("Printing COMBINED bill header")
        super().print_bill()


# E1. What is the MRO of GreenHome? Why does Customer come before SolarUser?
E1_ANSWER = """

"""

# E2. What does tariff() return for a GreenHome object, and why?
#     What changes if the parents are written in this order instead:
#     (PrepaidCustomer, SmartMeterUser, SolarUser)? Why?
E2_ANSWER = """

"""

# E3. What does CombinedBill().print_bill() print, in order? Which class's print_bill()
#     does super() inside EnergyBill call, and why? How many times does
#     Bill.print_bill() run?
E3_ANSWER = """

"""

# E4. Is an object of class Generator an instance of Customer? Why does
#     show_all() still work for it, and what is this called? Why did
#     ElectricPole fail before D3?
E4_ANSWER = """

"""


# =====================================================================
# YOUR TEST CODE: create objects and call their methods here
# =====================================================================
if __name__ == "__main__":
    pass
