import random

class Admin:
    def __init__(self, name = None, home = None, job = None):
        self.company = Company(list_of_companies)
        self.name = name
        self.home = home
        self.has_home = 0
        self.money = 100
        self.job = job
        self.has_job = 0
        self.cheerfulness = 70
        self.job = random.choice(list(list_of_jobs))
    def job_from_begin(self):
        if self.has_job == 0:
            if self.money >= 3000 and self.cheerfulness >= 80 and self.has_home == 0:
                self.home = random.choice(list(type_of_home))
                self.money -= type_of_home[self.home]["money"]
                print(f"Maybe I should buy a {self.home}")
                self.has_home = 1
            if self.money >= 5000 and self.cheerfulness >= 70 and self.has_home == 1:
                print(f"Maybe I gonna buy {self.company.company}")
                self.money -= self.company.company_price
                self.has_job = 1
        else:
            pass

    def vacation(self):
        if self.has_job == 0:
            print("To have vacation I need to work more")
            self.work()
            pass
        elif self.has_job == 1 and self.money < 2500:
            print("I don't have enough money for this, so I just gonna work")
            self.work()
            pass
        else:
            self.money -= 2500
            self.cheerfulness += 20
            self.money += self.company.salary_chill

    def restaurant(self):
        if self.money >= 1000 and self.has_job == 1:
            print("I wanna eat something delicious")
            self.money -= 1000
            self.cheerfulness += 10
            self.money += self.company.salary_chill
        elif self.has_job == 0:
            print("Let's eat some pizza")
            self.money -= 30
            self.cheerfulness += 8
        else:
            print("I don't have enough money for this, so I need to work")
            self.work()
            pass
    def chill(self):
        self.cheerfulness += 7
        pay_or_not = random.randint(1, 2)
        if pay_or_not == 1 and self.has_job == 0:
            print("So I gonna eat some street food ")
            self.money -= 15
            self.cheerfulness += 3
        elif pay_or_not == 1 and self.has_job == 1:
            print("Let's go shopping")
            self.money -= 200
            self.cheerfulness += 10
            self.money += self.company.salary_chill
        else:
            pass


    def work(self):
        if self.has_job == 1:
            self.money += self.company.salary
            self.cheerfulness -= random.randint(5, 10)
            self.company.popularity += 0.7
        elif self.has_job == 0:
            self.money += list_of_jobs[self.job]["money"]
            self.cheerfulness -= list_of_jobs[self.job]["cheerfulness_less"]
              
    def is_alive(self):
        if self.cheerfulness <= 0:
            print("I'm so sad (")
            return False
        elif self.money <= -100:
            print("I have become a bankrupt")
            return False
        elif self.has_job == 1:
            if self.company.popularity <= -1:
                print("My company isn't popular right now")
                return False

    def day_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}", "\n")
        admin_indexes = self.name + "'s indexes"
        print(f"{admin_indexes:^50}", "\n")
        if self.has_job == 1:
            if self.cheerfulness > 100:
                self.cheerfulness = 100
            print(f"Money - {self.money}")
            print(f"Cheerfulness - {self.cheerfulness}")
            company_indexes = "Company indexes"
            print(f"{company_indexes:^50}", "\n")
            print(f"Company - {self.company.company}")
            self.company.popularity -= self.company.popularity_less
            if self.company.popularity > 10:
                self.company.popularity = 10
            print(f"Popularity - {round(self.company.popularity, 2)}")
        else:
            print(f"Money - {self.money}")
            if self.cheerfulness > 100:
                self.cheerfulness = 100
            print(f"Cheerfulness - {self.cheerfulness}")
            print(f"Job - {self.job}")

    def live(self, day):
        if self.is_alive() == False:
            return False
        self.day_indexes(day)

        if self.has_job == 0:
            self.job_from_begin()
        else:
            pass
        if self.money <= 0:
            print("I need to start working immediately!")
            self.work()
        elif self.cheerfulness <= 15:
            print("I need to chill!")
            self.chill()
        elif self.has_job == 1:
            if self.company.popularity <= 0:
                print("I don't want to lose my company, so I need to work")
                self.work()

        cube = random.randint(1, 4)
        if cube == 1:
            print("Let's earn money baby")
            self.work()
        if cube == 2:
            print("Today I wanna chill")
            self.chill()
        if cube == 3:
            self.restaurant()

        if cube == 4:
            self.vacation()


type_of_home = {
"Flat":
      {"money":1500},
"House":
      {"money":2500}
}

list_of_jobs = {
"Software tester":
                {"money": 550, "cheerfulness_less":7},
"Dark web worker":
                {"money": 470, "cheerfulness_less": 5}
}

list_of_companies = {
"Discord":
         {"cost": 3500, "popularity": 7.5, "popularity_less": 0.15, "salary": 1000},
"Youtube":
         {"cost": 4750, "popularity": 10, "popularity_less": 0.3, "salary": 1500},
"Viber":
        {"cost": 3150, "popularity": 7, "popularity_less": 0.1, "salary": 900},
"Telegram":
        {"cost": 4000, "popularity": 8.5, "popularity_less": 0.2, "salary": 950}
}

class Company:
    def __init__(self, list_of_companies):
        self.company = random.choice(list(list_of_companies))
        self.company_price = list_of_companies[self.company]["cost"]
        self.popularity = list_of_companies[self.company]["popularity"]
        self.popularity_less = list_of_companies[self.company]["popularity_less"]
        self.salary = list_of_companies[self.company]["salary"]
        self.salary_chill = list_of_companies[self.company]["salary"] / 2

admin = Admin(name = "Ilya")
for day in range(365):
    if admin.live(day) == False:
        break
