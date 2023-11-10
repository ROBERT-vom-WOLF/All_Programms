nummer = 5


def add():
    global nummer
    if nummer == 5:
        nummer += 5
    return nummer


print(add())
print(nummer)
