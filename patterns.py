# for i in range(0,4):
#     for j in range(0,4):
#         print("*",end="")
#     print()

# def pat1():
#     for i in range(0,4):
#         for j in range(0,4):
#             print("*",end="")
#         print()
# def main():
#     pat1()
# if __name__=="__main__":
#     main()


# def pat2(n):
#     for i in range(n):
#         for j in range(i+1):
#             print("*",end="")
#         print()

# def main():
#     n = int(input("Enter a value: "))    
#     pat2(n)

# if __name__ == "__main__":
#     main()                                         
                                           
# for i in range(0,5):
#     for j in range(1,i+2):
#         print(j,end="")
#     print()

# def pat4():
#     for i in range(0,6):
#         for  j in range(1,i+1):
#             print(i,end="")
#         print()
# def main():
#     pat4()

# if __name__ == "__main__":
#     main()       

# for i in range(0,5):
#     for j in range(5,i,-1):
#         print("*",end="")
#     print()

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# for i in range(5,0,-1):
#     for j in range(5,5-i,-1):
#         print(j,end="")
#     print()

# def pyramid(n):
#     for i in range(0,n):
#         for j in range(n-i-1):
#             print(" ",end="")
#         for j in range(2*i+1):
#             print("*",end="")
#         print()
# def main():
#     n = int(input("Enter a value:"))
#     pyramid(n)
# if __name__ == "__main__":
#     main()

# def rev_pyramid(n):
#     for i in range(n,0,-1):
#         for j in range(n-i):
#             print(" ",end="")
#         for j in range(2*i-1):
#             print("*",end="")
#         print()
# def main():
#     n = int(input("Enter a value:"))
#     rev_pyramid(n)
# if __name__ == "__main__":
#     main()

# def diamond(n):
#     for i in range(n):
#         for j in range(n-i-1):
#             print(" ",end="")
#         for j in range(2*i+1):
#             print("*",end="")
#         print()
#     for i in range(n,0,-1):
#         for j in range(n-i):
#             print(" ",end="")
#         for j in range(2*i-1):
#             print("*",end="")
#         print()
# def main():
#     n = int(input("Enter a value"))
#     diamond(n)
# if __name__ == "__main__":
#     main()

# def pat(n):
#     for i in range(0,n):
#         for j in range(i+1):
#             print("*",end="")
#         print()
#     for i in range(n-1,0,-1):
#         for j in range(i):
#             print("*",end="")
#         print()
# def main():
#     n = int(input("Enter value of n:"))
#     pat(n)
# if __name__ == "__main__":
#     main()

# def pat(n):
#     for i in range(n):
#         for j in range(i+1):
#             if (i+j)%2 ==0:
#                 print(1,end="")
#             else:
#                 print(0,end="")
#         print()
# def main():
#     n = int(input("Enter the value of n"))
#     pat(n)
# if __name__ == "__main__":
#     main()

# def pat(n):
#     for i in range(n):
#         for j in range(i+1):
#             if i%2 ==0:
#                 print(1,end="")
#             else:
#                 print(0,end="")
#         print()
# def main():
#     n = int(input("Enter the value of n"))
#     pat(n)
# if __name__ == "__main__":
#     main()
