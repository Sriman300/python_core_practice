#Class
# class Ganesh:#Class
#     def __init__(self,intelligent,handsome): #Attributes
#         self.intelligent = intelligent
#         self.handsome = handsome

#     def blessing(self): #Method
#         print("Sriman is blessed")

#Object
# class blessings:
#     def __init__(self):
#         self.intelligent = ""
#         self.handsome = ""

#     def blessings_given(self):
#         print(f"Sriman got {self.intelligent}")

#     def blessings_have(self):
#         print(f"Sriman is the {self.handsome}")

# if __name__ == "__main__":
#     my_blessings = blessings()  #Object is defined
#     my_blessings.intelligent = "DSA_expertise(FAANG)"
#     my_blessings.handsome = "prince_of_hearts"

#     print(f"Blessings Sriman got: {my_blessings.intelligent}")
#     print(f"Blessings Sriman have: {my_blessings.handsome}")
#     my_blessings.blessings_given()
#     my_blessings.blessings_have()

#__init__ constructor use(used before creating an object)
# class Employee:#class
#       companyA = "Google"
#       companyB = "Netflix"
#       def __init__(self,name,age,profession): #__init__ constructor
#           self.name = name #instance attribute
#           self.age = age  #instance attribute
#           self.profession = profession   #instance attribute
# A = Employee("Sriman",21,"Python_developer")  #object of Employee class
# B = Employee("Sankar",21,"AI_engineer") #Object of Employee class

# print(A.name,A.age,A.profession)
# print(A.companyA)
# print(B.name,B.age,B.profession)
# print(B.companyB)

#__str__ constructor use

# class Cow:
#     BreedA = "Gir"
#     BreedB = "RedSindhi"
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

# C1 = Cow("Rani",10)
# C2 = Cow("Rama",9)

# print(C1)
# print(C1.BreedA)
# print(C2)
# print(C2.BreedB)

#Instance method 
# class person:
#     def __init__(self,name):
#         self.name = name
#     def say_hi(self):
#         print(f"Helo,My name is {self.name}")
# p = person("Sriman")
# p.say_hi()

# class Car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color

#     def show(self):
#         print("Model:", self.model)
#         print("Color:", self.color)

# audi = Car("Audi A4", "Blue")
# ferrari = Car("Ferrari 488", "Green")

# audi.show()
# ferrari.show()

#Using self for modifying self attributes
# class Counter:
#     def __init__(self):
#         self.count = 0

#     def increment(self):
#         self.count += 1

#     def decrement(self):
#         self.count -= 1

#     def mul(self):
#         self.count *=5

#     def get_count(self):
#         return self.count

# counter = Counter()
# counter.increment()
# counter.increment()
# counter.decrement()
# counter.mul()
# print(counter.get_count())

#Deleting an Object
# class Employee:
#     def __init__(self, name):
#         self.name = name

# employee = Employee("Emma")
# del employee
# print(employee.name)

#INHERITANCE
# class Fruits:
#     def __init__(self,color,taste):
#         self.color = color
#         self.taste = taste
#     def properties(self):
#         print("Fruit color is:", self.color)
# class Apple(Fruits):
#     def colour(self):
#         print(f"{self.color} is {self.taste}")
# F = Apple("Red","Sweet")
# F.properties()
# F.colour()

#Method overriding in INHERITANCE
# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def info(self):
#         print("Cow name is",self.name)

# class Cow(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed

#     def details(self):
#         print(f"{self.name} is a {self.breed}")
# C = Cow("Heera","RedSindhi")
# C.info()
# C.details()

#METHOD OVERRIDING
# class Animal:
#     def display(self):
#         print("This is an animal")

# class Dog(Animal):
#     def display(self):
#         print("This is a dog")

# obj = Dog()
# obj.display()

#METHOD OVERRIDING USING CONSTRUCTOR
# class Employee:
#     def __init__(self):
#         self.role = 'Manager'
#     def display(self):
#         print("Role is:", self.role)
# class Manager(Employee):
#     def __init__(self):
#         super().__init__()
#         self.role='Manager'
#     def display(self):
#         print("Role is:", self.role)
# E1=Employee()
# E2=Manager()
# E1.display()

# E2.display()



