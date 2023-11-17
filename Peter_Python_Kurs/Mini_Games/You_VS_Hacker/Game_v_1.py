from Libary import *
uhr_min = 30
uhr_h = 22
Estimated_Time = []
you = Info(False, False, True)
hacker = Info(True, False, True)


def console():
    global uhr_min, uhr_h
    if uhr_min >= 60:
        uhr_min = 00
        uhr_h += 1
    if uhr_h == 24:
        print("Es ist 00:00 Uhr!")
        print("Du hast verloren!")
        exit()
    if uhr_min < 10:
        print(f"\nUhrzeit:\t\t{uhr_h}:0{uhr_min}", end="\t\t")
    else:
        print(f"\nUhrzeit:\t\t{uhr_h}:{uhr_min}", end="\t\t")
    if you.vpn:
        print("VPN on", end="\t\t")
    else:
        print("VPN off", end="\t\t")
    user = input("\nSuperUser/System/Windows32/-\t\t")
    return user


def run_line_command(command):
    global Estimated_Time

    if command == "ping":
        if ping(hacker):        # Winning sequence
            print("Looks like his connection crashed!")
            print("You Won!")
            exit()

    if hacker.connected:
        if command == "quit":
            exit()
        if command == "grab.ip":
            initiate_grab_ip(uhr_h, uhr_min)
            complete = (uhr_h + 1) * uhr_min
            Estimated_Time.append(complete)
        if command == "vpn.switch":
            vpn_switch(you)
        if command == "spam":
            if spam(hacker):
                hacker.vpn = False
                hacker.spammed = True
                hacker.bots_count += 500

    else:
        loading("", 1.4)
        print("Response_timed_out")


def commands(user_input):
    global uhr_min
    command_error_answer = "y"
    command_li = user_input.split(" ")
    if "help" in command_li:
        print_commands()
    else:
        for char in command_li:
            if char not in command_collection:
                print(f"Command not found:\t\t\t'{char}'")
                command_error_answer = input("Do you still want to execute?[Y]\t\t").lower()
        if command_error_answer == "y":
            for char in command_li:
                if char in command_collection:
                    print(f"\n-----------------{char}-----------------")
                    run_line_command(char)
                    print(f"-----------------{char}-----------------\n")
            uhr_min += 5
            t.sleep(0.8)


# intro()
while True:
    check_grab_ip(hacker, uhr_h, uhr_min, Estimated_Time)
    user = console()
    commands(user)
    # aktionen, die mit dem Hacker passieren
    # ------------------------------------------------------------------------------------------------------------------
    if hacker.bots_count >= 1000:            # falls zu viele bots inm System sind, crashed er + sein VPN
        hacker.connected = False
        hacker.vpn = False

    if hacker.vpn:                          # falls der VPN an ist, bekommt er jeden durchlauf eine neue IP Adresse
        hacker.ip = generate_ip()
    # ------------------------------------------------------------------------------------------------------------------
