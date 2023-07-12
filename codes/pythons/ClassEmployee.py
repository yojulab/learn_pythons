#!/usr/bin/python3

class Employee:
   'Common base class for all employees'
   empCount = 0
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)
   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

class Point:
    def __init__( self, x=0, y=0):
        self.x = x
        self.y = y

#This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
print ("Total Employee %d" % Employee.empCount)
#This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
print ("Total Employee %d" % Employee.empCount)
emp1.displayEmployee()
emp2.displayEmployee()
