# =====================================================================
# OOP WITH PYTHON: INHERITANCE II + POLYMORPHISM (GROUP ACTIVITY)
# Group 2: UCU Campus Members System
#
# Full requirements and marking criteria: see the activity document.
# =====================================================================

GROUP_NUMBER = 2   # do not change

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
#   UCU wants one system for everyone on campus: members, students,
#   postgraduates, and graduate assistants who both tutor courses and
#   do research.

# =====================================================================
# MARKS (20)
#   A  Multilevel inheritance ........ 4    D  Duck typing ......... 3
#   B  Multiple inheritance + MRO .... 5    E  Questions ........... 4
#   C  Polymorphism .................. 3    File runs, no errors ... 1
# =====================================================================


# GIVEN: do not change
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def describe(self):
        print(f"Member: {self.name} | Member ID: {self.member_id}")

    def role(self):
        return "University member"


# =====================================================================
# PART A: MULTILEVEL INHERITANCE (4 marks)
# ---------------------------------------------------------------------
# A1. class Student(Member)
#       __init__(self, name, member_id, programme)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Programme: {self.programme}")
#       role(self)      -> override: return "Student"
#
# A2. class Postgraduate(Student)
#       __init__(self, name, member_id, programme, research_area)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Research area: {self.research_area}")
#       role(self)      -> override: return "Postgraduate student"
# =====================================================================


# =====================================================================
# PART B: MULTIPLE INHERITANCE + MRO (5 marks)
# ---------------------------------------------------------------------
# B1. class Tutor        (no parent class, no __init__)
#       building_access(self)  -> return "Teaching block"
#       teach(self, course)
#           -> print(f"{self.name} teaches {course}")
#
# B2. class Researcher        (no parent class, no __init__)
#       building_access(self)  -> return "Research lab"
#       publish(self, paper)
#           -> print(f"{self.name} publishes '{paper}'")
#
# B3. class GraduateAssistant(Postgraduate, Tutor, Researcher)
#       (parents in EXACTLY this order)
#       __init__(self, name, member_id, programme, research_area, supervisor)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Supervisor: {self.supervisor}")
#                          print(f"   Building access: {self.building_access()}")
#       role(self)      -> override: return "Graduate assistant"
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
#         Member("Achieng Grace", "M-2041")
#         Student("Achieng Grace", "M-2041", "BSIT")
#         Postgraduate("Achieng Grace", "M-2041", "BSIT", "Computer networks")
#         GraduateAssistant("Achieng Grace", "M-2041", "BSIT", "Computer networks", "Dr. Mukasa Peter")
# =====================================================================


# =====================================================================
# PART D: DUCK TYPING (3 marks)
# ---------------------------------------------------------------------
# D1. class LibraryKiosk        (no parent class: NOT related to Member)
#       __init__(self, location)
#       role(self)      -> return "Self-service kiosk"
#       describe(self)  -> print(f"LibraryKiosk: {self.location}")
#
# D2. Add these two objects to the list in build_items():
#       LibraryKiosk("Main library, ground floor")
#       Timetable("Semester 1, 2026/27")
#
# D3. Timetable (given below) has no role() method. Change show_all() so it
#     prints "[no role]" for such an item, and still calls its describe().
# =====================================================================


# GIVEN: do not change
class Timetable:
    def __init__(self, semester):
        self.semester = semester

    def describe(self):
        print(f"Timetable: {self.semester}")


# =====================================================================
# PART E: QUESTIONS (4 marks)
# Answer inside the quotes. Explain WHY, not just what.
# =====================================================================

# GIVEN: do not change
#                Notice
#               /       \
#     BoardNotice     PortalNotice
#               \       /
#              ExamNotice
class Notice:
    def post(self):
        print("Notice archived")


class BoardNotice(Notice):
    def post(self):
        print("Pinning on the notice board")
        super().post()


class PortalNotice(Notice):
    def post(self):
        print("Posting on the student portal")
        super().post()


class ExamNotice(BoardNotice, PortalNotice):
    def post(self):
        print("Stamping notice as EXAM")
        super().post()


# E1. What is the MRO of GraduateAssistant? Why does Member come before Tutor?
E1_ANSWER = """

"""

# E2. What does building_access() return for a GraduateAssistant object, and why?
#     What changes if the parents are written in this order instead:
#     (Postgraduate, Researcher, Tutor)? Why?
E2_ANSWER = """

"""

# E3. What does ExamNotice().post() print, in order? Which class's post()
#     does super() inside BoardNotice call, and why? How many times does
#     Notice.post() run?
E3_ANSWER = """

"""

# E4. Is an object of class LibraryKiosk an instance of Member? Why does
#     show_all() still work for it, and what is this called? Why did
#     Timetable fail before D3?
E4_ANSWER = """

"""


# =====================================================================
# YOUR TEST CODE: create objects and call their methods here
# =====================================================================
if __name__ == "__main__":
    pass
