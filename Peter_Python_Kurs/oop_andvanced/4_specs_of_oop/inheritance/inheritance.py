class A:
    def mach_etwas(self):
        print("Methode kommt aus der Klasse A")


class B(A):
    def mach_etwas(self):
        print("Methode kommt aus der Klasse B")


class C(A):
    def mach_etwas(self):
        print("Methode kommt aus der Klasse C")


class D(B, C):

    def mach_etwas(self):
        print("Methode kommt aus der Klasse D")


d1 = D()
d1.mach_etwas()

# MRO = Method Resolution Order
#print(D.__mro__)
#print(D.mro())

#help(D)

# Diamant Problem:
#       A
#      / \
#     B   C
#     \   /
#       D