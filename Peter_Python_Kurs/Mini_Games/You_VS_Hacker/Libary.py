import random as rnd
import time as t
command_collection = [
    "help",
    "quit",
    "grab.ip",
    "vpn.switch",
    "spam",
    "ping",
]


def print_commands():
    counter = 1
    for char in command_collection:
        print(f"{counter}:\t\t{char}")
        counter += 1


def intro():
    print("Achtung eine Warnung!")
    input("~~~Enter für weiter~~~")
    print("Dein PC wurde gehackt!")
    print("Aber kein Stress.")
    input("")
    print("Weil der Hacker auf deinem System ist, hast du die oberhand!")
    print("Verwende deine Konsole um den Hack zu verhindern!")
    input("")
    print("---------------------------------------")
    print_commands()
    print("---------------------------------------")
    print("Das sind alle Befehle! Du kannst auch mehrere auf einmal verwenden!\nTrenne sie einfach mit einem Komma!")
    input("")
    print("Verwende den Befehl 'help' um dir alle Funktionen anzeigen zu lassen.")
    input("")
    print("Die Zeit reicht nicht aus, um dir alles zu erklären!")
    input("")
    print("Wenn du es nicht bis 24:00 Uhr schaffst, ist dein PC für immer verseucht.")
    print("Viel Glück!\n\n\n\n\n")


def loading(text, time):
    t.sleep(time)
    print(f"{text}", end="")
    t.sleep(time)
    print(". ", end="")
    t.sleep(time)
    print(". ", end="")
    t.sleep(time)
    print(".")
    t.sleep(time)


def generate_ip():
    adress = ""
    for _ in range(0, 3):
        number = rnd.randint(0, 255)
        if number < 100:
            adress += "0" + str(number) + "."
        elif number < 10:
            adress += "00" + str(number) + "."
        else:
            adress += str(number) + "."
    adress += str(rnd.randint(0, 6))
    return adress


def check_grab_ip(ziel, Stunden, Minuten, Estimated_Time):
    _time = Stunden * Minuten
    if _time in Estimated_Time:
        Estimated_Time.remove(_time)
        print(f"\n-----------------Trace-----------------")
        print("Trace Complete!")
        if not ziel.VPN:
            print(f"Adress:\t\t{ziel.ip}")
        else:
            print(f"Adress:\t\t{ziel.ip}\nVPN recognized!")
        print(f"-----------------Trace-----------------\n")


def vpn_switch(user):
    loading("connecting", 1)
    if not user.VPN:
        user.VPN = True
        print("VPN toggel: On")
    else:
        user.VPN = False
        print("VPN toggel: Off")


def spam(ziel):
    target = input("Target:\t\t")
    loading("Installing Bots", 2.5)
    if target == ziel.ip:
        print("Spam successful!")
        print("VPN crashed!")
        return True
    else:
        print("Spam successful!")


def ping(ziel):
    target = input("Target:\t\t")
    loading(f"ping at {target} ", 1)
    if not ziel.connected:
        return True      # Winning sequence

    elif ziel.connected and target == ziel.ip:
        for _ in range(0, 5):
            print("Ping <1ms")
            t.sleep(0.7)
        print("\t\t\tTarget Online")
        return False

    else:
        print(f"Adress '{target}' not found!")
        return False


def initiate_grab_ip(Stunde, Minute):
    loading("Tracing ", 1.3)
    loading("Calculating", 0.7)
    print(f"Estimated Time for Tracing completion: {Stunde + 1}:{Minute}")


class Info:
    VPN = False
    ip = generate_ip()
    spammed = False
    connected = True
    bots_count = 0

    def __init__(self, VPN=False, spammed=False, online=True):
        self.VPN = VPN
        self.spammed = spammed
        self.connected = online