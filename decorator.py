# def decorator(func):
#     def wrapper():
#         print("Before calling a func")
#         func()
#         print("After calling a func")
#     return wrapper

# @decorator
# def greet():
#     print("Hello,World")
# greet()

# def decorator_name(func):
#     def wrapper(*args, **kwargs):
#         print("Before exeution")
#         result = func(*args, **kwargs)
#         print("After execution")
#         return result 
#     return wrapper

# @decorator_name
# def add(a,b):
#     return a + b
# print(add(5, 4))

# def greet(n):
#     return f"Hello, {n}!"
# hii = greet
# print(hii("Sriman"))

# def apply(f,v):
#     return f(v)
# res = apply(hii,"prince_of_hearts")
# print(res)

#returning a func from another func
# def steady(f):
#     def stuart(x):
#         return x * f
#     return stuart
# tom = steady(7)
# print("chest : inch ->",tom(8))

#Higher order func
# def fun(f, x):
#     return f(x)

# def sq(x):
#     return x * x
# r = fun(sq,5)
# print(r)

#Func_decorator

# def simple_dec(func):
#     def wrap():
#         print("Func start")
#         func()
#         print("func finished")
#     return wrap

# @simple_dec
# def greet():
#     print("Hello, World!")
# greet()

#Method_dec

# def method_decorator(func):
#     def wrapper(self,*args,**kwargs):
#         print("before exec")
#         res = func(self,*args,**kwargs)
#         print("after exec")
#         return res
#     return wrapper

# class Cls:
#     @method_decorator
#     def greet(self):
#         print("Hello!")
# jamy = Cls()
# jamy.greet()

#Class_dec

# def fun(Cls):
#     Cls.class_name = Cls.__name__
#     return Cls

# @fun
# class person:
#     pass
# print(person.class_name)
