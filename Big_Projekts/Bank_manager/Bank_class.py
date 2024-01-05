import random as rnd


class Bank:
    def __init__(self, user_list, besitzer, password, geld=0):
        self.owner = str(besitzer).title()
        self.password = password
        self.balance = int(geld)
        self.user_id = len(user_list)


    def deposit(self, ammount):
        ammount = int(ammount)
        self.balance -= ammount

    def withdraw(self, ammount):
        ammount = int(ammount)
        self.balance -= ammount

    def addition(self, ammount):
        ammount = int(ammount)
        self.balance += ammount
