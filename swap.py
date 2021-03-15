# a = 10
# b = 15
# c = a
# a = b
# b = c
# class Counter:
#     def start_from(self, count):
#         self.count = count
#         count = 0
#         return self.count
#
#     def increment(self):
#         self.count += 1
#         return self.count
#
#     def display(self):
#         print(f"текущее значение счетчика={self.count}")
#
#     def reset(self):
#         self.count = 1
#         return self.count

# class Counter:
#     d = 0
#
#     def start_from(self, d=0):
#         self.d = d
#
#     def increment(self):
#         self.d += 1
#
#     def display(self):
#         print(f"Текущее значение счетчика = {self.d}")
#
#     def reset(self):
#         self.d = 0


class SoccerPlayer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0
    def score(self, goals=1):
        self.goals += goals        
    def make_assist(self, assists=1):
        self.assists += assists
    def statistics(self):
        print(f"{self.surname}{self.name}'-голы:'{self.goals},'передачи:'{self.assists}")