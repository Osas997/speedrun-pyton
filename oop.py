class Person:
   # constructor
   def __init__(self, kepet, age):
      self.name = kepet
      self.age = age

   # representasi
   def __str__(self):
      return "Hello my name is " + self.name


# inheritance
class Employee(Person):
   def __init__(self, name, age, salary):
      super().__init__(name, age)
      self.salary = salary

   def welcome(self):
      print("Welcome " + self.name + " " + str(self.age) + " years old " + " your salary is " + str(self.salary))

p1 = Employee("John", 36, 3000)
# p1.welcome()

print(p1)