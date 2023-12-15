class Mutter:

    def __init__(self):
        self.augenfarbe = "Braun"
        self.haarfarbe = "Dunkelbraun"
        self.haartyp = "Locken"


class Vater:

    def __init__(self):
        self.augenfarbe = "Blau"
        self.haarfarbe = "Blond"
        self.haartyp = "Glatt"


class Kind(Mutter, Vater):
    pass


mum = Mutter()
dad = Vater()
son = Kind()

print("\n\nMutter:")
print(mum.augenfarbe)
print(mum.haarfarbe)
print(mum.haartyp)

print("\n\nVater:")
print(dad.augenfarbe)
print(dad.haarfarbe)
print(dad.haartyp)

print("\n\nSohn:")
print(son.augenfarbe)
print(son.haarfarbe)
print(son.haartyp)
