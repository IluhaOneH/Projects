import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.balance = 120


    def to_study(self):
        if self.progress > 1.7 or self.balance <= 30:
            self.work = random.choice(list(work_list))
            print(f"Time to work as {self.work}")
            self.progress = 0.25
            self.balance += work_list[self.work]["money"]
            self.gladness -= work_list[self.work]["gladness_less"]
        else:
            print("Time to study")
            self.progress += 0.3
            self.gladness -= 3
            self.balance -= 2


    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.balance -= 10

    def is_alive(self):
        if self.progress < - 0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False
        elif self.balance <= 0:
            print("I am a bankrupt")
            self.alive = False

    def end_of_day(self):
        if self.gladness > 100:
            self.gladness = 100
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Balance = {self.balance}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1 or live_cube == 4:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Nick")
kate = Student(name="Kate")

work_list={
"Waiter":
        {"money": 50, "gladness_less": 5 },
"Courier":
        {"money": 45, "gladness_less": 3 },
"Cashier":
        {"money": 60, "gladness_less": 7},

}
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
    if kate.alive == False:
        break
    kate.live(day)
