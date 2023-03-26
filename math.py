import random

list_of_symbols = ["+", "-", "*", "/"]

class Enter:
    def __init__(self):
        self.n1 = random.randint(1,100)
        self.n2 = random.randint(1,100)
        self.symbol = random.choice(list_of_symbols)
class Quit(Enter):
    def math(self):
        self.s = "---------------"
        if self.symbol == "+":
            result = self.n1 + self.n2
            print(result)
            print(f"{self.s:-^50}", "\n")
            print(f"Выполненное действие : +")
        elif self.symbol == "-":
            result = self.n1 - self.n2
            print(result)
            print(f"{self.s:-^50}", "\n")
            print(f"Выполненное действие : -")
        elif self.symbol == "*":
            result = self.n1 * self.n2
            print(result)
            print(f"{self.s:-^50}", "\n")
            print(f"Выполненное действие : *")
        else:
            result = self.n1 / self.n2
            print(result)
            print(f"{self.s:-^50}", "\n")
            print(f"Выполненное действие : /")

math_result = Quit()
math_result.math()



