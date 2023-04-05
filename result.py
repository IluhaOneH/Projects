result = []
def divider(a, b):
    try:
        return a / b
    except TypeError:
        print("Один из делителей не является числом!")
        return 'Error'
    except ZeroDivisionError:
        print("Невозможно выполнить деление на 0!")
        return 'Error'

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)

