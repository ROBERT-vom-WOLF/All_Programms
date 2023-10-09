import time
from fnc_tkinter_memory import *
zeit = 0
while zeit < 3720:
    time.sleep(0.0002)
    zeit += 1
    if zeit % 600 == 0:
        print(f"{zeit / 60} Minuten vergangen")
giu()
print("Fertig")
