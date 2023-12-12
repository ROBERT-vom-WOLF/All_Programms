from bank_account_creation import creat_account
from Bank_Commands import *

usr_list = []
while True:
    eingabe = input("\nBANK---:\t\t")

    if eingabe == "new -m":

        usr_list = (creat_account(usr_list, True))
    elif eingabe == "new":

        usr_list = (creat_account(usr_list, False))
    elif eingabe == "show":

        print_selcet(usr_list)
    elif eingabe == "show -a":
        print_all(usr_list)

    elif eingabe == "len":
        print(f"Bestehende Accounts:\t\t{len(usr_list)}")

    elif eingabe == "clear":
        clear(usr_list)

