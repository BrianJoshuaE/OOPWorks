# =====================================================================
# OOP WITH PYTHON: INHERITANCE II + POLYMORPHISM (GROUP ACTIVITY)
# Group 10: Lakeside Hotel Rooms
#
# Full requirements and marking criteria: see the activity document.
# =====================================================================

GROUP_NUMBER = 10   # do not change

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
#   A hotel in Entebbe is modelling its rooms: rooms, standard rooms,
#   suites, and presidential suites that have BOTH a balcony and a
#   kitchen.

# =====================================================================
# MARKS (20)
#   A  Multilevel inheritance ........ 4    D  Duck typing ......... 3
#   B  Multiple inheritance + MRO .... 5    E  Questions ........... 4
#   C  Polymorphism .................. 3    File runs, no errors ... 1
# =====================================================================


# GIVEN: do not change
class Room:
    def __init__(self, number, floor):
        self.number = number
        self.floor = floor

    def describe(self):
        print(f"Room: {self.number} | Floor: {self.floor}")

    def role(self):
        return "Hotel room"


# =====================================================================
# PART A: MULTILEVEL INHERITANCE (4 marks)
# ---------------------------------------------------------------------
# A1. class StandardRoom(Room)
#       __init__(self, number, floor, beds)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Beds: {self.beds}")
#       role(self)      -> override: return "Standard room"
#
# A2. class Suite(StandardRoom)
#       __init__(self, number, floor, beds, view)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   View: {self.view}")
#       role(self)      -> override: return "Suite"
# =====================================================================


# =====================================================================
# PART B: MULTIPLE INHERITANCE + MRO (5 marks)
# ---------------------------------------------------------------------
# B1. class HasBalcony        (no parent class, no __init__)
#       extra_charge(self)  -> return "Balcony fee"
#       open_balcony(self, time)
#           -> print(f"Room {self.number}: balcony opened at {time}")
#
# B2. class HasKitchen        (no parent class, no __init__)
#       extra_charge(self)  -> return "Kitchen fee"
#       cook(self, meal)
#           -> print(f"Room {self.number}: cooking {meal}")
#
# B3. class PresidentialSuite(Suite, HasBalcony, HasKitchen)
#       (parents in EXACTLY this order)
#       __init__(self, number, floor, beds, view, butler)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Butler: {self.butler}")
#                          print(f"   Extra charge: {self.extra_charge()}")
#       role(self)      -> override: return "Presidential suite"
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
#         Room(204, 2)
#         StandardRoom(204, 2, 2)
#         Suite(204, 2, 2, "Lake Victoria")
#         PresidentialSuite(204, 2, 2, "Lake Victoria", "Wasswa Henry")
# =====================================================================


# =====================================================================
# PART D: DUCK TYPING (3 marks)
# ---------------------------------------------------------------------
# D1. class SafariVan        (no parent class: NOT related to Room)
#       __init__(self, plate_no)
#       role(self)      -> return "Tour transport"
#       describe(self)  -> print(f"SafariVan: {self.plate_no}")
#
# D2. Add these two objects to the list in build_items():
#       SafariVan("UAX 909T")
#       KeyCard("KC-4410")
#
# D3. KeyCard (given below) has no role() method. Change show_all() so it
#     prints "[no role]" for such an item, and still calls its describe().
# =====================================================================


# GIVEN: do not change
class KeyCard:
    def __init__(self, code):
        self.code = code

    def describe(self):
        print(f"KeyCard: {self.code}")


# =====================================================================
# PART E: QUESTIONS (4 marks)
# Answer inside the quotes. Explain WHY, not just what.
# =====================================================================

# GIVEN: do not change
#                  Service
#                 /        \
#     CleaningService      RoomService
#                 \        /
#                 VIPService
class Service:
    def serve(self):
        print("Service logged")


class CleaningService(Service):
    def serve(self):
        print("Cleaning the room")
        super().serve()


class RoomService(Service):
    def serve(self):
        print("Bringing food to the room")
        super().serve()


class VIPService(CleaningService, RoomService):
    def serve(self):
        print("Adding VIP welcome pack")
        super().serve()


# E1. What is the MRO of PresidentialSuite? Why does Room come before HasBalcony?
E1_ANSWER = """

"""

# E2. What does extra_charge() return for a PresidentialSuite object, and why?
#     What changes if the parents are written in this order instead:
#     (Suite, HasKitchen, HasBalcony)? Why?
E2_ANSWER = """

"""

# E3. What does VIPService().serve() print, in order? Which class's serve()
#     does super() inside CleaningService call, and why? How many times does
#     Service.serve() run?
E3_ANSWER = """

"""

# E4. Is an object of class SafariVan an instance of Room? Why does
#     show_all() still work for it, and what is this called? Why did
#     KeyCard fail before D3?
E4_ANSWER = """

"""


# =====================================================================
# YOUR TEST CODE: create objects and call their methods here
# =====================================================================
if __name__ == "__main__":
    pass
