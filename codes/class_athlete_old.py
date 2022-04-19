class Athlete:
    def __init__(self, value='Jane'):
        self.inner_value = value
        print(self.inner_value)

    def getInnerValue(self):
        return self.inner_value

class InheritanceClass(Athlete):
    def __init__(self):
        super().__init__('good')

    def setValue(self, first_value):
        self.inherit_value = first_value

    def getValue(self):
        return self.inherit_value


athlete = Athlete(value='SangHun')   # == Athlete.__init__()

print(athlete.getInnerValue())

# InheritanceClass.mro()
# [<class '__main__.Inh...nceClass'>, <class '__main__.Athlete'>, <class 'object'>]

inheritance = InheritanceClass()

print(inheritance.getInnerValue())

inheritance.setValue(first_value='Oh')

print(inheritance.getValue())