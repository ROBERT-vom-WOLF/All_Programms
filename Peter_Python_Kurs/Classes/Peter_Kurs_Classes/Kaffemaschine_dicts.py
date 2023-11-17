resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# DONE: verwende die dictionaries resources und MENU
# DONE: die kaffee maschine: verfügt selbst über resourcen wie wasser, milch, kaffee und geld
# DONE: die kaffee maschine bietet dem benutzer eine auswahl an kaffee sorten an
# DONE: wählt der benutzer eine kaffee sorte, so wird zunächst geprüft, ob ausreichend resourcen vorhanden sind
# DONE: ist das der fall bezahlt der benutzer mit münzen
# DONE: er wird der reihe nach gefragt nach einer anzahl von münzsorten gefragt
# DONE: die 1. sorte ist der quarter = 0.25 Dollar
# DONE: dann folgt der dime = 0.10 Dollar
# DONE: dann folgt der nickle = 0.05 Dollar
# DONE: anschließend der penny = 0.01 Dollar
# DONE: er wird geprüft, ob ausreichend bezahlt wurde, der preis für die kaffee sorte steht auch im MENU dicitionary
# DONE: falls zu wenig gezahlt wurde, wird eine meldung ausgegeben und die kaffee auswahl gestartet
# DONE: falls zu wenig gezahlt wurde, werden keine resourcen abgezogen und auch kein geld gut geschrieben
# DONE: falls zu viel bezahlt wurde wird eine meldung ausgegeben und der restbetrag zurück gegeben
# DONE: wurde ausreichend bezahlt werden die resourcen abgezogen und das geld gut geschrieben
# DONE: danach kann eine weitere kaffee sorte ausgewählt werden
# DONE: bei eingabe "report" in der kaffee auswahl, wird der aktuelle stand der resourcen der maschine ausgegeben
# DONE: gibt der benutzer "off" ein, wird das prog
