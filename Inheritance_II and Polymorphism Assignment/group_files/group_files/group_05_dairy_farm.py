# =====================================================================
# OOP WITH PYTHON: INHERITANCE II + POLYMORPHISM (GROUP ACTIVITY)
# Group 5: Dairy Farm Animal Register
#
# Full requirements and marking criteria: see the activity document.
# =====================================================================

GROUP_NUMBER = 5   # do not change

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
#   A dairy farm in Mbarara keeps records of its animals: every farm
#   animal, cattle, dairy cows, and prize cows that are BOTH
#   vaccinated and insured.

# =====================================================================
# MARKS (20)
#   A  Multilevel inheritance ........ 4    D  Duck typing ......... 3
#   B  Multiple inheritance + MRO .... 5    E  Questions ........... 4
#   C  Polymorphism .................. 3    File runs, no errors ... 1
# =====================================================================


# GIVEN: do not change
class Animal:
    def __init__(self, name, tag_no):
        self.name = name
        self.tag_no = tag_no

    def describe(self):
        print(f"Animal: {self.name} | Tag No: {self.tag_no}")

    def role(self):
        return "Farm animal"


# =====================================================================
# PART A: MULTILEVEL INHERITANCE (4 marks)
# ---------------------------------------------------------------------
# A1. class Cattle(Animal)
#       __init__(self, name, tag_no, breed)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Breed: {self.breed}")
#       role(self)      -> override: return "Cattle"
#
# A2. class DairyCow(Cattle)
#       __init__(self, name, tag_no, breed, litres_per_day)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Litres per day: {self.litres_per_day}")
#       role(self)      -> override: return "Dairy cow"
# =====================================================================


# =====================================================================
# PART B: MULTIPLE INHERITANCE + MRO (5 marks)
# ---------------------------------------------------------------------
# B1. class Vaccinated        (no parent class, no __init__)
#       certificate(self)  -> return "Vaccination certificate"
#       vaccinate(self, vaccine)
#           -> print(f"{self.name} receives {vaccine}")
#
# B2. class Insured        (no parent class, no __init__)
#       certificate(self)  -> return "Insurance certificate"
#       claim(self, reason)
#           -> print(f"Insurance claim for {self.name}: {reason}")
#
# B3. class PrizeCow(DairyCow, Vaccinated, Insured)
#       (parents in EXACTLY this order)
#       __init__(self, name, tag_no, breed, litres_per_day, award)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Award: {self.award}")
#                          print(f"   Certificate: {self.certificate()}")
#       role(self)      -> override: return "Prize cow"
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
#         Animal("Kyakuwa", "UG-COW-0457")
#         Cattle("Kyakuwa", "UG-COW-0457", "Ankole")
#         DairyCow("Kyakuwa", "UG-COW-0457", "Ankole", 18)
#         PrizeCow("Kyakuwa", "UG-COW-0457", "Ankole", 18, "Best Dairy Cow, Jinja Show")
# =====================================================================


# =====================================================================
# PART D: DUCK TYPING (3 marks)
# ---------------------------------------------------------------------
# D1. class MilkingMachine        (no parent class: NOT related to Animal)
#       __init__(self, model)
#       role(self)      -> return "Milking equipment"
#       describe(self)  -> print(f"MilkingMachine: {self.model}")
#
# D2. Add these two objects to the list in build_items():
#       MilkingMachine("Two-bucket milker")
#       FeedBag(50)
#
# D3. FeedBag (given below) has no role() method. Change show_all() so it
#     prints "[no role]" for such an item, and still calls its describe().
# =====================================================================


# GIVEN: do not change
class FeedBag:
    def __init__(self, kg):
        self.kg = kg

    def describe(self):
        print(f"FeedBag: {self.kg}")


# =====================================================================
# PART E: QUESTIONS (4 marks)
# Answer inside the quotes. Explain WHY, not just what.
# =====================================================================

# GIVEN: do not change
#               Check
#              /      \
#     HealthCheck    WeightCheck
#              \      /
#             FullCheck
class Check:
    def run_check(self):
        print("Check recorded")


class HealthCheck(Check):
    def run_check(self):
        print("Checking temperature")
        super().run_check()


class WeightCheck(Check):
    def run_check(self):
        print("Weighing the animal")
        super().run_check()


class FullCheck(HealthCheck, WeightCheck):
    def run_check(self):
        print("Starting FULL check-up")
        super().run_check()


# E1. What is the MRO of PrizeCow? Why does Animal come before Vaccinated?
E1_ANSWER = """

"""

# E2. What does certificate() return for a PrizeCow object, and why?
#     What changes if the parents are written in this order instead:
#     (DairyCow, Insured, Vaccinated)? Why?
E2_ANSWER = """

"""

# E3. What does FullCheck().run_check() print, in order? Which class's run_check()
#     does super() inside HealthCheck call, and why? How many times does
#     Check.run_check() run?
E3_ANSWER = """

"""

# E4. Is an object of class MilkingMachine an instance of Animal? Why does
#     show_all() still work for it, and what is this called? Why did
#     FeedBag fail before D3?
E4_ANSWER = """

"""


# =====================================================================
# YOUR TEST CODE: create objects and call their methods here
# =====================================================================
if __name__ == "__main__":
    pass
