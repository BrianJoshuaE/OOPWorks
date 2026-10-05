# =====================================================================
# OOP WITH PYTHON: INHERITANCE II + POLYMORPHISM (GROUP ACTIVITY)
# Group 9: Phone Shop Inventory
#
# Full requirements and marking criteria: see the activity document.
# =====================================================================

GROUP_NUMBER = 9   # do not change

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
#   A phone shop on Kampala Road is tracking its stock: devices,
#   phones, smartphones, and flagship phones with BOTH a great camera
#   and an FM radio.

# =====================================================================
# MARKS (20)
#   A  Multilevel inheritance ........ 4    D  Duck typing ......... 3
#   B  Multiple inheritance + MRO .... 5    E  Questions ........... 4
#   C  Polymorphism .................. 3    File runs, no errors ... 1
# =====================================================================


# GIVEN: do not change
class Device:
    def __init__(self, brand, serial_no):
        self.brand = brand
        self.serial_no = serial_no

    def describe(self):
        print(f"Device: {self.brand} | Serial: {self.serial_no}")

    def role(self):
        return "Electronic device"


# =====================================================================
# PART A: MULTILEVEL INHERITANCE (4 marks)
# ---------------------------------------------------------------------
# A1. class Phone(Device)
#       __init__(self, brand, serial_no, sim_slots)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   SIM slots: {self.sim_slots}")
#       role(self)      -> override: return "Phone"
#
# A2. class Smartphone(Phone)
#       __init__(self, brand, serial_no, sim_slots, os)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   OS: {self.os}")
#       role(self)      -> override: return "Smartphone"
# =====================================================================


# =====================================================================
# PART B: MULTIPLE INHERITANCE + MRO (5 marks)
# ---------------------------------------------------------------------
# B1. class Camera        (no parent class, no __init__)
#       main_feature(self)  -> return "50MP camera"
#       take_photo(self, subject)
#           -> print(f"{self.brand} photographs {subject}")
#
# B2. class RadioReceiver        (no parent class, no __init__)
#       main_feature(self)  -> return "FM radio"
#       tune(self, station)
#           -> print(f"{self.brand} tunes to {station}")
#
# B3. class FlagshipPhone(Smartphone, Camera, RadioReceiver)
#       (parents in EXACTLY this order)
#       __init__(self, brand, serial_no, sim_slots, os, storage_gb)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Storage GB: {self.storage_gb}")
#                          print(f"   Main feature: {self.main_feature()}")
#       role(self)      -> override: return "Flagship phone"
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
#         Device("Tecno", "SN-77812")
#         Phone("Tecno", "SN-77812", 2)
#         Smartphone("Tecno", "SN-77812", 2, "Android 15")
#         FlagshipPhone("Tecno", "SN-77812", 2, "Android 15", 256)
# =====================================================================


# =====================================================================
# PART D: DUCK TYPING (3 marks)
# ---------------------------------------------------------------------
# D1. class Laptop        (no parent class: NOT related to Device)
#       __init__(self, model)
#       role(self)      -> return "Portable computer"
#       describe(self)  -> print(f"Laptop: {self.model}")
#
# D2. Add these two objects to the list in build_items():
#       Laptop("HP EliteBook 840")
#       Charger(33)
#
# D3. Charger (given below) has no role() method. Change show_all() so it
#     prints "[no role]" for such an item, and still calls its describe().
# =====================================================================


# GIVEN: do not change
class Charger:
    def __init__(self, watts):
        self.watts = watts

    def describe(self):
        print(f"Charger: {self.watts}")


# =====================================================================
# PART E: QUESTIONS (4 marks)
# Answer inside the quotes. Explain WHY, not just what.
# =====================================================================

# GIVEN: do not change
#                  Update
#                /        \
#     SecurityUpdate      AppUpdate
#                \        /
#               MajorUpdate
class Update:
    def install(self):
        print("Update recorded")


class SecurityUpdate(Update):
    def install(self):
        print("Installing security patch")
        super().install()


class AppUpdate(Update):
    def install(self):
        print("Updating apps")
        super().install()


class MajorUpdate(SecurityUpdate, AppUpdate):
    def install(self):
        print("Starting MAJOR system update")
        super().install()


# E1. What is the MRO of FlagshipPhone? Why does Device come before Camera?
E1_ANSWER = """

"""

# E2. What does main_feature() return for a FlagshipPhone object, and why?
#     What changes if the parents are written in this order instead:
#     (Smartphone, RadioReceiver, Camera)? Why?
E2_ANSWER = """

"""

# E3. What does MajorUpdate().install() print, in order? Which class's install()
#     does super() inside SecurityUpdate call, and why? How many times does
#     Update.install() run?
E3_ANSWER = """

"""

# E4. Is an object of class Laptop an instance of Device? Why does
#     show_all() still work for it, and what is this called? Why did
#     Charger fail before D3?
E4_ANSWER = """

"""


# =====================================================================
# YOUR TEST CODE: create objects and call their methods here
# =====================================================================
if __name__ == "__main__":
    pass
