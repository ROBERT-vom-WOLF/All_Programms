import time as t


def load(text, time):
    t.sleep(time)
    print(f"{text}", end="")
    t.sleep(time)
    print(". ", end="")
    t.sleep(time)
    print(". ", end="")
    t.sleep(time)
    print(".")
    t.sleep(time)