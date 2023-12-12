from bank_class import Bank


def creat_account(original_liste, multiple=False):
    if multiple:
        accounts_num = int(input("Wie viele Accounts wollen sie Erstellen?\n\t"))
    else:
        accounts_num = 1

    accounts_default_owner = input("Ihr Standart Benutzername für die Accounts:\n\t")
    accounts_default_balance = int(input("Ihr Standart Kontostand für die Accounts:\n\t"))

    num = 0
    for _ in range(0, accounts_num):
        num += 1
        original_liste.append(Bank(original_liste, accounts_default_owner + f" ({num})", accounts_default_balance))

    print(f"\n\nSuccessfully created {len(original_liste)} Accounts\n")
    return original_liste
