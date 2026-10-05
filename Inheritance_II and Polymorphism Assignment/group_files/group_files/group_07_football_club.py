# =====================================================================
# OOP WITH PYTHON: INHERITANCE II + POLYMORPHISM (GROUP ACTIVITY)
# Group 7: Football Club Squad Manager
#
# Full requirements and marking criteria: see the activity document.
# =====================================================================

GROUP_NUMBER = 7   # do not change

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
#   A Uganda Premier League club is building a squad manager: team
#   members, players, strikers, and star strikers who take BOTH
#   penalties and free kicks.

# =====================================================================
# MARKS (20)
#   A  Multilevel inheritance ........ 4    D  Duck typing ......... 3
#   B  Multiple inheritance + MRO .... 5    E  Questions ........... 4
#   C  Polymorphism .................. 3    File runs, no errors ... 1
# =====================================================================


# GIVEN: do not change
class TeamMember:
    def __init__(self, name, jersey_no):
        self.name = name
        self.jersey_no = jersey_no

    def describe(self):
        print(f"TeamMember: {self.name} | Jersey: {self.jersey_no}")

    def role(self):
        return "Team member"


# =====================================================================
# PART A: MULTILEVEL INHERITANCE (4 marks)
# ---------------------------------------------------------------------
# A1. class Player(TeamMember)
#       __init__(self, name, jersey_no, position)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Position: {self.position}")
#       role(self)      -> override: return "Player"
#
# A2. class Striker(Player)
#       __init__(self, name, jersey_no, position, goals)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Goals: {self.goals}")
#       role(self)      -> override: return "Striker"
# =====================================================================


# =====================================================================
# PART B: MULTIPLE INHERITANCE + MRO (5 marks)
# ---------------------------------------------------------------------
# B1. class PenaltyTaker        (no parent class, no __init__)
#       set_piece(self)  -> return "Penalties"
#       take_penalty(self, keeper)
#           -> print(f"{self.name} takes a penalty against {keeper}")
#
# B2. class FreeKickSpecialist        (no parent class, no __init__)
#       set_piece(self)  -> return "Free kicks"
#       take_free_kick(self, distance)
#           -> print(f"{self.name} curls a free kick from {distance}")
#
# B3. class StarStriker(Striker, PenaltyTaker, FreeKickSpecialist)
#       (parents in EXACTLY this order)
#       __init__(self, name, jersey_no, position, goals, nickname)
#           -> use super().__init__ for the inherited attributes
#       describe(self)  -> extend: parent's output, then
#                          print(f"   Nickname: {self.nickname}")
#                          print(f"   Set piece: {self.set_piece()}")
#       role(self)      -> override: return "Star striker"
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
#         TeamMember("Okello Denis", 9)
#         Player("Okello Denis", 9, "Forward")
#         Striker("Okello Denis", 9, "Forward", 14)
#         StarStriker("Okello Denis", 9, "Forward", 14, "The Bullet")
# =====================================================================


# =====================================================================
# PART D: DUCK TYPING (3 marks)
# ---------------------------------------------------------------------
# D1. class Referee        (no parent class: NOT related to TeamMember)
#       __init__(self, referee_name)
#       role(self)      -> return "Match official"
#       describe(self)  -> print(f"Referee: {self.referee_name}")
#
# D2. Add these two objects to the list in build_items():
#       Referee("Kasirye Alex")
#       Stadium("Mandela National Stadium")
#
# D3. Stadium (given below) has no role() method. Change show_all() so it
#     prints "[no role]" for such an item, and still calls its describe().
# =====================================================================


# GIVEN: do not change
class Stadium:
    def __init__(self, stadium_name):
        self.stadium_name = stadium_name

    def describe(self):
        print(f"Stadium: {self.stadium_name}")


# =====================================================================
# PART E: QUESTIONS (4 marks)
# Answer inside the quotes. Explain WHY, not just what.
# =====================================================================

# GIVEN: do not change
#                  Training
#                 /        \
#     FitnessTraining    TacticsTraining
#                 \        /
#                 MatchPrep
class Training:
    def start(self):
        print("Training logged")


class FitnessTraining(Training):
    def start(self):
        print("Running fitness drills")
        super().start()


class TacticsTraining(Training):
    def start(self):
        print("Going through tactics")
        super().start()


class MatchPrep(FitnessTraining, TacticsTraining):
    def start(self):
        print("Starting MATCH preparation")
        super().start()


# E1. What is the MRO of StarStriker? Why does TeamMember come before PenaltyTaker?
E1_ANSWER = """

"""

# E2. What does set_piece() return for a StarStriker object, and why?
#     What changes if the parents are written in this order instead:
#     (Striker, FreeKickSpecialist, PenaltyTaker)? Why?
E2_ANSWER = """

"""

# E3. What does MatchPrep().start() print, in order? Which class's start()
#     does super() inside FitnessTraining call, and why? How many times does
#     Training.start() run?
E3_ANSWER = """

"""

# E4. Is an object of class Referee an instance of TeamMember? Why does
#     show_all() still work for it, and what is this called? Why did
#     Stadium fail before D3?
E4_ANSWER = """

"""


# =====================================================================
# YOUR TEST CODE: create objects and call their methods here
# =====================================================================
if __name__ == "__main__":
    pass
