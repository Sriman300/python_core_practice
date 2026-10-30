#Strings

# # name = input("What's your name")
# name = name.strip()
# name = name.title()
# print(f"hello {name}")
# name = name.strip().title()
#name = input("What's your name? ").strip().title()

#Integers

# x = input("What's x? ")
# y = input("What's y? ")
# z = int(x) + int(y)
# print(z)

#Float
# x = float(input("What's x? "))
# y = float(input("What's y? "))
# z = round(x + y)
# print(z)

# Get the user's input
# x = float(input("What's x? "))
# y = float(input("What's y? "))
# z = round(x + y)
# print(f"{z:,}")   #answers will appear with a comma eg:1,000

# x = float(input("x"))
# y = float(input("y"))
# z = x/y
# print(z)

# x = float(input("x"))
# y = float(input("y"))
# z = round(x/y,2)
# print(z)

#Functions
# def So():
#     print("hello")

# name = "Sriman"
# So()
# print(name)


# def so(to):
#     print("Hii,",to)

# name=input("What's your name? ")
# so(name)

# def hello(to = "world"):
#     print("hello,", to)

# name = input("What's your name?")
# hello(name)

# hello()

#first main func then def any other func

# def main():
#     name = input("What's is your name ?")
#     Hii(name)

#     Hii()

# def Hii(to="Avengers"):
#     print("Hii,",to)

# main()



# def main():
#     x =int(input("What's is x? "))
#     print("x squared is", square(x))

#None

# def hello(name=None):
#     if name == None:
#         print("Hello!,Moto")
#     else:
#         print("Hello!",name)
# hello()
# hello("IOS")

#Reassigning Variables

# x = 5
# y = x
# x = "Geeks"
# print(x)
# print(y)

# L1 = [1, 2, 3, 4, 5]
# L2 = L1
# L1[0] = 0
# print(L1)
# print(L2)

#If separate objects are needed, create a copy instead of a shared reference
# L1 = [1, 2, 3, 4, 5]
# L2 = L1[:]
# L1[0] = 0
# print(L1)
# print(L2)

# L1 = [1, 2, 3]
# L2 = L1
# print(L1 == L2)
# print(L1 is L2)

# L1 = [1, 2, 3]
# L2 = [1, 2, 3]
# print(L1 == L2)
# print(L1 is L2)

#Strings are catched
# a = 50
# b = 50
# print(a == b)
# print(a is b)

#Assignment vs Copying in Python
#Operation	Creates New Object?	Shared Reference?
#b = a	No	Yes
#b = a[:]	Yes (lists only)	No
#b = a.copy()	Yes	No

#python_scope_variable
#Local_variable: Variable defined inside the func

# def f():
#     # local variable
#     s = "I love Sriman"
#     print(s)
# f()

# def f():
#     s = "I love Sriman"
#     print(s)
# f()
# print(s)

#Global_var: Variable defined outside the func
# def f():
#     print(s)
# # Global scope
# s = "Sriman is prince_of_hearts"
# f()

# def f():
#     s = "Sona:Me too"
#     print(s)

# # Global scope
# s = "I love Sriman"
# f()
# print(s)

# def f():
#     print(s)
#     s = "Me too."
#     print(s)


# # Global scope
# s = "Sriman:I love Sona"
# f()
# print(s)

# def f():
#     global s
#     print(s)
#     s = "Look for Sriman's Python_repo"
#     print(s)


# # Global Scope
# s = "Python is great !,Sriman is the GOAT!"
# f()
# print(s)





# def square(n):
#     return n * n

# main()

