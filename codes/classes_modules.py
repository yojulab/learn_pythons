# 같은 폴더에 있는 class and functions 호출

# 1. import : 같은 파일에 있을 경우 생략
import classes_fomats
# 2. class instance
person = classes_fomats.Person()
arithmetics = classes_fomats.Arithmetics()
class_name = classes_fomats.Class_name()
# 3. call function    
person.add_age()

## import 시 주로 사용하는 방식
from classes_fomats import Person, Arithmetics, Class_name
person_second = Person()
arithmetics_second = Arithmetics()
pass