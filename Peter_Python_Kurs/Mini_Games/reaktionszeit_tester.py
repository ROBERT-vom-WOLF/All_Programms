import time
import random
from fnc_ask_again import *
while True:
    start = 0
    end = 0
    info_1 = random.randint(2, 5)
    info_2 = random.randint(2, 5)
    timer_1 = random.randint(5, 20)
    timer_2 = random.random()
    wait = timer_1 * timer_2
    print(f"Es geht los in etwa {int(wait - info_1)} bis {int(wait + info_2)} Sekunden!")
    time.sleep(wait)
    start += time.time()
    input("\n\nJetzt!\n\n")
    end += time.time()
    print(f"Gebrauchte Zeit:\t\t", end="")
    print(end - start)
    ask("dich testen", "DE")
