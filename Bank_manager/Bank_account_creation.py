from Bank_class import Bank
from Bank_Commands import console_hide


def creat_account(original_liste, multiple=False):
    if multiple:
        accounts_num = int(input("Wie viele Accounts wollen sie Erstellen?\n\t"))
    else:
        accounts_num = 1
    if multiple:
        account_owner = input("Ihr Standart Benutzername für die Accounts:\n\t")
        account_balance = int(input("Ihr Standart Kontostand für die Accounts:\n\t"))
        account_pw = input("Ihr Standart Passwort für die Accounts:\n\t")
    else:
        account_owner = input("Ihr Benutzername für den Account:\n\t")
        account_balance = int(input("Ihr Kontostand für den Account:\n\t"))
        account_pw = input("Ihr Passwort für den Account:\n\t")

    console_hide()

    num = 0
    for _ in range(0, accounts_num):
        num += 1
        if multiple:
            original_liste.append(Bank(original_liste, account_owner + f" ({num})", account_pw, account_balance))
        else:
            original_liste.append(Bank(original_liste, account_owner, account_pw, account_balance))

    print(f"\n\nSuccessfully created {accounts_num} Account(s)\n")
    return original_liste
