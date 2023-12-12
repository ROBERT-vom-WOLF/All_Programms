class Bank:
    def __init__(self, user_list, besitzer, password, geld=0):
        self.owner = besitzer
        self.password = password
        self.balance = geld
        self.user_id = len(user_list)

    def deposit(self):
        addition = int(input(f"Ihre Buchung auf das Konto {self.owner}: \n\t"))
        self.balance += addition
        print(f"Sie haben {addition} € überwiesen")
        print(f"Kontostand des Kontos {self.owner}:")
        print(f"{self.balance:,}\n\n")

    def withdraw(self):
        addition = int(input(f"Ihre Buchung von dem Konto {self.owner}: \n\t"))
        if self.balance - addition >= 0:
            self.balance -= addition
            print(f"Sie haben {addition} € abgehoben")
        else:
            print(f"Nicht möglich, ihr Kontostand beträgt {(self.balance - addition) * -1}€ zu wenig für diese Buchung")
        print(f"Kontostand des Kontos {self.owner}:")
        print(f"{self.balance:,}\n\n")
