#*args: It accepts any number of positional arguments(non-keyword arguments).

# def num(*args):
#     return sum(args)
# print(num(2,4,5,7,0))

#*args - Accept multiple function arguments
#*argv - Read command-line arguments

# def fun(*argv):
#     for arg in argv:
#         print(arg)
# fun('Hii!','Sriman')

# def mul(*args):
#     res = 1
#     for num in args:
#         res *= num
#     return res
# print(mul(2,4,5,7,9)) 

#**kwargs - allows a function to accept any number of keyword arguments.

# def fun(**kwargs):
#     for k, v in kwargs.items():
#         print(k , v)
# fun(s1='Python',s2='Anaconda',s3='R')

# def int(**kwargs):
#     det = []
#     for k, v in kwargs.items():
#         det.append(k + ":" +str(v))
#     return " , ".join(det)
# print(int(Name="Sriman",Age=21))

#def Student(**kwargs):
#     info=[]
#     for k, v in kwargs.items():
#         info.append(k + " : "+str(v))
#     return " ".join(info)
# print(Student(name="Som",age=19,id=5579))













