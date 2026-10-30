#Global
 
# x = [2,4,5,7,9]
# def display():
#     global x
#     x = [20,30,40]
# print("Before:",x)
# display()
# print("After:",x)

# nums = [2,4,5,7,9]
# def display():
#     for i in range(len(nums)):
#         nums[i] += 10
# print("Former:",nums)
# display()
# print("Later:",nums)


#Modifying Global within function

# insz = "insta"
# def display():
#     global insz
#     insz += 'hackathon'
#     print(insz)
#     insz = "Yt.Whatsapp" #Reassign
#     print(insz)
# display()
# print(insz)

#Global vs Local with same name

# a = 1
# def f():
#     print("f()",a)
# def g():
#     a=2
#     print("f()",a)
# def h():
#     global a
#     a=3
#     print("f()",a)
# print("global",a)
# f()
# print("global",a)
# g()
# print("global",a)
# h()
# print("global",a)









