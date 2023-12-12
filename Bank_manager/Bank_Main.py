from Bank_account_creation import creat_account
from Bank_Commands import *
from Bank_class import Bank
account = None
usr_list = []
usr_list.append(Bank(usr_list, "root_user", "root", 0))


while True:
    eingabe = command_prep(account)
    for command in eingabe:
        if "stop" in command:
            print(f"Stopped executing")
            break

        elif "help" in command:
            help()

        elif "new -m" in command:
            usr_list = (creat_account(usr_list, True))

        elif "new" in command:
            usr_list = (creat_account(usr_list, False))

        elif "show -a" in command:
            print_all(usr_list)

        elif "show" in command:
            print_selcet(usr_list, account)

        elif "len" in command:
            print(f"Bestehende Accounts:\t\t{len(usr_list)}")

        elif "clear" in command:
            clear(usr_list)

        elif "login" in command:
            account = user_login(usr_list)

        elif "logout" in command:
            if account:
                print(f"\n\n\t\t\t\t\t\t\tLogged out of {account.owner} successfully\n")
                account = None
            else:
                print("\n\n\t\t\t\t\t\t\tYou are not logged in yet!")

        elif "exit" in command or "quit" in command:
            print("\n\n\n\t\t\tSee you soon!")
            exit()

        elif "deposit" in command:
            if account:
                account.deposit()
            else:
                print("\n\n\t\t\t\t\t\t\tYou are not logged in yet!")
        else:
            command_error(command)
