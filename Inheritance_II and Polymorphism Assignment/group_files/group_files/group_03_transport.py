# =====================================================================
# OOP WITH PYTHON: INHERITANCE II + POLYMORPHISM (GROUP ACTIVITY)
# Group 3: Upcountry Bus Company Fleet
#
# Full requirements and marking criteria: see the activity document.
# =====================================================================

GROUP_NUMBER = 3   # do not change

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
#   A bus company running Kampala - Mbarara wants to model its fleet:
#   vehicles, buses, coach buses, and luxury coaches that carry
#   parcels AND offer on-board Wi-Fi.

# =====================================================================
# MARKS (20)
#   A  Multilevel inheritance ........ 4    D  Duck typing ......... 3
#   B  Multiple inheritance + MRO .... 5    E  Questions ........... 4
#   C  Polymorphism .................. 3    File runs, no errors ... 1
# =====================================================================


# GIVEN: do not change
class Vehicle:
    def __init__(self, plate_no, owner):
        self.plate_no = plate_no
        self.owner = owner

    def describe(self):
        print(f"Vehicle: {self.plate_no} | Owner: {self.owner}")

    def role(self):
        return "Vehicle"


# =====================================================================
# PART A: MULTILEVEL INHERITANCE (4 marks)
# ---------------------------------------------------------------------
# A1. class Bus(Vehicle)
#       __init__(self, plate_no, owner, seats)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Seats: {self.seats}")
#       role(self)      -> override: return "Bus"
#
# A2. class CoachBus(Bus)
#       __init__(self, plate_no, owner, seats, route)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Route: {self.route}")
#       role(self)      -> override: return "Coach bus"
# =====================================================================


# =====================================================================
# PART B: MULTIPLE INHERITANCE + MRO (5 marks)
# ---------------------------------------------------------------------
# B1. class ParcelService        (no parent class, no __init__)
#       service_desk(self)  -> return "Parcel desk"
#       send_parcel(self, item)
#           -> print(f"{self.plate_no} carries parcel: {item}")
#
# B2. class WifiOnBoard        (no parent class, no __init__)
#       service_desk(self)  -> return "Wi-Fi help desk"
#       connect(self, device)
#           -> print(f"{self.plate_no} connects {device} to Wi-Fi")
#
# B3. class LuxuryCoach(CoachBus, ParcelService, WifiOnBoard)
#       (parents in EXACTLY this order)
#       __init__(self, plate_no, owner, seats, route, lounge)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Lounge: {self.lounge}")
#                          print(f"   Service desk: {self.service_desk()}")
#       role(self)      -> override: return "Luxury coach"
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
#         Vehicle("UBE 482K", "Kato John")
#         Bus("UBE 482K", "Kato John", 67)
#         CoachBus("UBE 482K", "Kato John", 67, "Kampala - Mbarara")
#         LuxuryCoach("UBE 482K", "Kato John", 67, "Kampala - Mbarara", "VIP lounge, Kampala park")
# =====================================================================


# =====================================================================
# PART D: DUCK TYPING (3 marks)
# ---------------------------------------------------------------------
# D1. class Ferry        (no parent class: NOT related to Vehicle)
#       __init__(self, vessel)
#       role(self)      -> return "Lake transport"
#       describe(self)  -> print(f"Ferry: {self.vessel}")
#
# D2. Add these two objects to the list in build_items():
#       Ferry("MV Kalangala")
#       FuelStation("Seeta")
#
# D3. FuelStation (given below) has no role() method. Change show_all() so it
#     prints "[no role]" for such an item, and still calls its describe().
# =====================================================================


# GIVEN: do not change
class FuelStation:
    def __init__(self, location):
        self.location = location

    def describe(self):
        print(f"FuelStation: {self.location}")


# =====================================================================
# PART E: QUESTIONS (4 marks)
# Answer inside the quotes. Explain WHY, not just what.
# =====================================================================

# GIVEN: do not change
#                  Announcement
#                  /          \
#     RadioAnnouncement     AppAnnouncement
#                  \          /
#               DelayAnnouncement
class Announcement:
    def announce(self):
        print("Announcement recorded")


class RadioAnnouncement(Announcement):
    def announce(self):
        print("Reading it on the radio")
        super().announce()


class AppAnnouncement(Announcement):
    def announce(self):
        print("Pushing it to the app")
        super().announce()


class DelayAnnouncement(RadioAnnouncement, AppAnnouncement):
    def announce(self):
        print("Adding DELAY warning")
        super().announce()


# E1. What is the MRO of LuxuryCoach? Why does Vehicle come before ParcelService?
E1_ANSWER = """

"""

# E2. What does service_desk() return for a LuxuryCoach object, and why?
#     What changes if the parents are written in this order instead:
#     (CoachBus, WifiOnBoard, ParcelService)? Why?
E2_ANSWER = """

"""

# E3. What does DelayAnnouncement().announce() print, in order? Which class's announce()
#     does super() inside RadioAnnouncement call, and why? How many times does
#     Announcement.announce() run?
E3_ANSWER = """

"""

# E4. Is an object of class Ferry an instance of Vehicle? Why does
#     show_all() still work for it, and what is this called? Why did
#     FuelStation fail before D3?
E4_ANSWER = """

"""


# =====================================================================
# YOUR TEST CODE: create objects and call their methods here
# =====================================================================
if __name__ == "__main__":
    pass
