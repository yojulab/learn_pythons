from sub02_dir.print_all import print_result 

class AddMinusCal:
    def __init__(self, first=0, second=0):

        self.first = first

        self.second = second

    def setdata(self, first, second):

        self.first = first

        self.second = second

    def add(self):

        result = self.first + self.second

        return result

    def add_printresult(self):

        result = self.first + self.second
        print_result = print_all()
        print_result.print_all('add', result)


class MultipleDivideCal:
    def __init__(self, first=0, second=0):

        self.first = first

        self.second = second

    def setdata(self, first, second):

        self.first = first

        self.second = second

    def multiple(self):

        result = self.first * self.second

        return result
