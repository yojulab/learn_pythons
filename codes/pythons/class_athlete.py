# class class_name:
#     def __init__(self):
#
#     def function_name(self):
#         return

class Athlete:
    def __init__(self, value='Jane'):
        self.inner_value = value
        print(self.inner_value)

    def getInnerValue(self):
        return self.inner_value

class InheritanceClass(Athlete):
    def __init__(self):
        super().__init__()

    def setValue(self, first_value):
        self.inherit_value = first_value

    def getValue(self):
        return self.inherit_value

# inherit = InheritanceClass()
#
# print(inherit.getInnerValue())
#
# inherit.setValue(first_value='Sanghun')
#
# print(inherit.getValue())


# athlete = Athlete(value='SangHun')   # == Athlete.__init__()
#
# print(athlete.getInnerValue())