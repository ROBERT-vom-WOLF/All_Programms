def print_all(users):
    for x in users:
        print(f"ID:          {x.user_id}")
        print(f"Besitzer:    {x.owner}")
        print(f"Geld:        {x.balance}\n\n")


def print_selcet(users):
    id_found = False
    id_eingabe = int(input("Gesuchte ID:\t"))
    for x in users:
        if x.user_id == id_eingabe:
            id_found = True
            print(f"ID:          {x.user_id}")
            print(f"Besitzer:    {x.owner}")
            print(f"Geld:        {x.balance}\n")
    if not id_found:
        print(f"\nCan't find ID {id_eingabe} in Accounts\n")


def clear(users):
    second_input = input("Wollen sie wirklich unwiederruflich alle Accounts löschen? [Y/N]:\t\t")
    if second_input.lower() == "y":
        users = []
        print("Successfully cleared all accounts")
    return users
