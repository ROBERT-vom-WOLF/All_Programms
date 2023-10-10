import time
from fnc_tkinter_memory import *
zeit = 0
print("Start")
while zeit < 360:
    time.sleep(1)
    zeit += 1
    if zeit % 60 == 0:
        print(f"{zeit / 60} Minuten vergangen")
giu()
print("Fertig")
