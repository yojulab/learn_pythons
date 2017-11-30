from ..ClassAthlete import Athlete

class Point:
    def __init__( self, x=0, y=0):
        self.x = x
        self.y = y
pass

sarah = Athlete('Sarah Sweeney', '2002-6-17', ['2:58', '2.58', '1.56'])
james = Athlete('James Jones')
sarah.Aprint()
james.Aprint()