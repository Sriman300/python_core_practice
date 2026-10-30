# def hotel():
#     print("New hotel is ")

# name = "Sri_Sawariya"
# hotel()
# print(name)

# def greet(to):
#     print("Hello! \t",to)

# name=input("What's your name")
# greet(name)

# def hello(to="world"):
#     print("Hii",to)

# name = input("Enter your name")
# hello(name)
# hello()

# def main():
#     name = input("Enter your name")
#     hello(name)
#     hello()

# def hello(to="world"):
#     print("Welcome",to)
# main()

# def main():
#     x = int(input("Enter a num:"))
#     print(f"square of the num {x} is ",square(x))

# def square(n):
#     return n*n

# main()


#Pass by Reference
#Mutable objects like lists can be modified inside functions.

# def myFun(x):
#     x[0] = 20

# b = [10, 11, 12, 13]
# myFun(b)
# print(b)

#Pass by Value
#Immutable objects like integers and strings remain unchanged.

# def myFun2(x):
#     x = 20

# a = 10
# myFun2(a)
# print(a)

#Returning a list from a function

# def fun(n):
#     return[n*n,n*n+5]
# print(fun(5))

#Function returning another function
# def fun1(msg):
#     def fun2():
#         return msg
#     return fun2

# f = fun1("hello")
# print(f())

#Inner function
# def process_data(data):
#     def clean_data():
#         return [item.strip() for item in data] 
#     return clean_data()
# print(process_data(["  Python  ", "  Inner Function  "]))

#Passing Function as an Argument in Python

# def fun(f1,name):
#     return f1(name)
# def f2(name):
#     return name.upper()
# print(fun(f2,"Sriman"))

# def msg(name):
#     return f"Hello, {name}!"
# def fun1(fun2, name):
#     return fun2(name)
# print(fun1(msg, "Sriman"))

# def fun(func, num):
#     return func(num)
# def f2(x):
#     return x * 5
# print(fun(f2,10))

#Higher order function
# def process(func):
#     return func("python")

# def to_upper(text):
#     return text.upper()

# print(process(to_upper))

# def multiplier(n): 
#     return lambda x: x * n

# double = multiplier(2)
# triple = multiplier(3)

# print(double(5))
# print(triple(5))

#Map function
# a = [1,2,4,5,7,9]
# res = list(map(lambda x: x*x,a))
# print(res)
