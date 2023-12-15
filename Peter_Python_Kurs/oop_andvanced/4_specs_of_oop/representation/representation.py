class Human:

    def __init__(self, name, age):
        self.name = str(name).title()
        self.age = age

    def __repr__(self):
        output = f'''
        Name: {self.name}
        Alter: {self.age}
        '''
        return output


james = Human("james bond", 57)
print(james)
