# =====================================================================
# OOP WITH PYTHON: INHERITANCE II + POLYMORPHISM (GROUP ACTIVITY)
# Group 1: Mulago Hospital Staff System
#
# Full requirements and marking criteria: see the activity document.
# =====================================================================

GROUP_NUMBER = 1   # do not change

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
#   Mulago Hospital is replacing its paper staff register with a
#   Python system. It must model visitors, staff and doctors, and
#   surgeons who can both prescribe drugs and operate in theatre.

# =====================================================================
# MARKS (20)
#   A  Multilevel inheritance ........ 4    D  Duck typing ......... 3
#   B  Multiple inheritance + MRO .... 5    E  Questions ........... 4
#   C  Polymorphism .................. 3    File runs, no errors ... 1
# =====================================================================


# GIVEN: do not change
class Person:
    def __init__(self, name, id_no):
        self.name = name
        self.id_no = id_no

    def describe(self):
        print(f"Person: {self.name} | ID No: {self.id_no}")

    def role(self):
        return "Visitor"


# =====================================================================
# PART A: MULTILEVEL INHERITANCE (4 marks)
# ---------------------------------------------------------------------
# A1. class Staff(Person)
#       __init__(self, name, id_no, department)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Department: {self.department}")
#       role(self)      -> override: return "Hospital staff"
#
# A2. class Doctor(Staff)
#       __init__(self, name, id_no, department, specialty)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Specialty: {self.specialty}")
#       role(self)      -> override: return "Doctor"
# =====================================================================


# =====================================================================
# PART B: MULTIPLE INHERITANCE + MRO (5 marks)
# ---------------------------------------------------------------------
# B1. class Prescriber        (no parent class, no __init__)
#       clearance(self)  -> return "Pharmacy clearance"
#       prescribe(self, drug)
#           -> print(f"{self.name} prescribes {drug}")
#
# B2. class TheatreQualified        (no parent class, no __init__)
#       clearance(self)  -> return "Theatre clearance"
#       operate(self, patient)
#           -> print(f"{self.name} operates on {patient}")
#
# B3. class Surgeon(Doctor, Prescriber, TheatreQualified)
#       (parents in EXACTLY this order)
#       __init__(self, name, id_no, department, specialty, theatre_no)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Theatre: {self.theatre_no}")
#                          print(f"   Clearance: {self.clearance()}")
#       role(self)      -> override: return "Surgeon"
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
#         Person("Nakato Sarah", "CM-90231")
#         Staff("Nakato Sarah", "CM-90231", "Surgery")
#         Doctor("Nakato Sarah", "CM-90231", "Surgery", "Orthopaedics")
#         Surgeon("Nakato Sarah", "CM-90231", "Surgery", "Orthopaedics", "Theatre 3")
# =====================================================================


# =====================================================================
# PART D: DUCK TYPING (3 marks)
# ---------------------------------------------------------------------
# D1. class Ambulance        (no parent class: NOT related to Person)
#       __init__(self, plate_no)
#       role(self)      -> return "Emergency transport"
#       describe(self)  -> print(f"Ambulance: {self.plate_no}")
#
# D2. Add these two objects to the list in build_items():
#       Ambulance("UG 1234A")
#       HospitalBed("Ward 5, Bed 12")
#
# D3. HospitalBed (given below) has no role() method. Change show_all() so it
#     prints "[no role]" for such an item, and still calls its describe().
# =====================================================================


# GIVEN: do not change
class HospitalBed:
    def __init__(self, bed_no):
        self.bed_no = bed_no

    def describe(self):
        print(f"HospitalBed: {self.bed_no}")


# =====================================================================
# PART E: QUESTIONS (4 marks)
# Answer inside the quotes. Explain WHY, not just what.
# =====================================================================

# GIVEN: do not change
#              Alert
#             /      \
#      SMSAlert     EmailAlert
#             \      /
#          EmergencyAlert
class Alert:
    def send(self):
        print("Alert saved in the log")


class SMSAlert(Alert):
    def send(self):
        print("Sending SMS to the doctor on call")
        super().send()


class EmailAlert(Alert):
    def send(self):
        print("Sending email to the ward")
        super().send()


class EmergencyAlert(SMSAlert, EmailAlert):
    def send(self):
        print("Marking alert as EMERGENCY")
        super().send()


# E1. What is the MRO of Surgeon? Why does Person come before Prescriber?
E1_ANSWER = """

"""

# E2. What does clearance() return for a Surgeon object, and why?
#     What changes if the parents are written in this order instead:
#     (Doctor, TheatreQualified, Prescriber)? Why?
E2_ANSWER = """

"""

# E3. What does EmergencyAlert().send() print, in order? Which class's send()
#     does super() inside SMSAlert call, and why? How many times does
#     Alert.send() run?
E3_ANSWER = """

"""

# E4. Is an object of class Ambulance an instance of Person? Why does
#     show_all() still work for it, and what is this called? Why did
#     HospitalBed fail before D3?
E4_ANSWER = """

"""


# =====================================================================
# YOUR TEST CODE: create objects and call their methods here
# =====================================================================
if __name__ == "__main__":
    pass
