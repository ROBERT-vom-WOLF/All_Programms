import time
seconds = 0
minutes = 0
hours = 0
while True:
    time.sleep(0.96)
    seconds += 1
    if seconds >= 60:
        minutes += 1
        seconds = 0
    if minutes >= 60:
        hours += 1
        seconds = 0
    print(f"{hours} : {minutes} : {seconds}", end="")
    if hours >= 1:
        print("\t\t\tMittagspause vorbei")
    print("\n")
