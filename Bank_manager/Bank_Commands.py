import time as t

commands_list = [
    "help",
    "stop",
    "new",
    "new -m",
    "show",
    "show -a",
    "len",
    "clear",
    "login",
    "logout",
    "exit",
    "break",
    "deposit",
 ]


def show_accounts_stats(account, show_money=False, show_pw=False, show_all=False):
    print("\t\t\t\t\t\t\t-----------------------------------")
    print(f"\t\t\t\t\t\t\t|--- ID: ------------ {account.user_id}")
    print(f"\t\t\t\t\t\t\t|--- Besitzer: ------ {account.owner}")
    if show_money or show_all:
        print(f"\t\t\t\t\t\t\t|--- Kontostand: ---- {account.balance:,}")
    if show_pw or show_all:
        print(f"\t\t\t\t\t\t\t|--- Password: ------ {account.password}")
    print("\t\t\t\t\t\t\t-----------------------------------\n\n")


def help():                     # help
    print(f"All Commands:\t\t", end="")
    for x in commands_list:
        print(f"{x}, ", end="")


def print_all(users):           # show -a
    for x in users:
        if x.user_id > 0:
            show_accounts_stats(x)


def print_selcet(users, acc):        # show
    if acc:
        show_accounts_stats(acc, show_all=True)
    else:
        id_found = False
        id_eingabe = int(input("Gesuchte ID:\t"))
        for x in users:
            if x.user_id == id_eingabe:
                id_found = True
                show_accounts_stats(x)
        if not id_found:
            print(f"\nCan't find ID {id_eingabe} in Accounts\n")


def clear(users):               # clear
    second_input = input("Wollen sie wirklich unwiederruflich alle Accounts löschen? [Y/N]:\t\t")

    if second_input.lower() == "y":
        users = []
        print("Successfully cleared all accounts")

    else:
        print("Cleaning progress canceled")

    return users


def user_login(user_list):
    login_data = str(input("Username or ID:\t\t"))

    for x in user_list:
        if x.owner == login_data or str(x.user_id) == login_data:
            pw = input("Password:\t\t")

            if x.password == pw:
                print(f"\n\n\t\t\t\t\t\t\tLogged in into {x.owner}\n")
                show_accounts_stats(x)
                return x
            else:
                print("Incorrect Password!")
                return None

    print(f"login '{login_data} not available'")
    return None


def command_prep(account):             # only user in main_loop to get an command line
    if account:
        command_ln = input(f"{account.owner}   :\t\t")
    else:
        command_ln = input(f"Bank   :\t\t")

    liste = command_ln.split("/")
    command_error = False

    for char in liste:
        if char not in commands_list:
            print(f'Command "{char}" not found!')
            command_error = True

    if command_error:
        user = input("Wollen sie ihre eingabe Zwangsausführen? [Y/N]:\t\t")
        if user.lower() == "y":
            return liste
        else:
            return []
    return liste


def command_error(command):     # displays an command error, that skipps the current command
    print(f'\n\ncould not execute "{command}" !')
    t.sleep(1.3)
    print(f"skipping command '{command}'...")
    t.sleep(1.3)
    print("Forcing next command...\n\n")


