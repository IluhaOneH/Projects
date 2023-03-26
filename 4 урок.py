import random
list_of_symbols = ["+", "-", "*", "/"]
class Enter:
    n1 = random.randint(1,100)
    n2 = random.randint(1,100)
    symbol = random.choice(list_of_symbols)
class Quit(Enter):
    s = "---------------"
    if Enter.symbol == "+":
        result = Enter.n1 + Enter.n2
        print(result)
        print(f"{s:-^50}", "\n")
        print(f"Выполненное действие : +")
    elif Enter.symbol == "-":
        result = Enter.n1 - Enter.n2
        print(result)
        print(f"{s:-^50}", "\n")
        print(f"Выполненное действие : -")
    elif Enter.symbol == "*":
        result = Enter.n1 * Enter.n2
        print(result)
        print(f"{s:-^50}", "\n")
        print(f"Выполненное действие : *")
    else:
        result = Enter.n1 / Enter.n2
        print(result)
        print(f"{s:-^50}", "\n")
        print(f"Выполненное действие : /")






