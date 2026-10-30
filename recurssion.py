# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(10))


# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(9))

# def tail_fact(n, acc=1):
#     if n == 0:
#         return acc
#     else:
#         return tail_fact(n-1, acc * n)

# def nontail_fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * nontail_fact(n-1)
        
# print(tail_fact(5))  
# print(nontail_fact(5))

#RecWhen to Avoid Recursion
# When the problem can be solved easily with loops.
# When recursion depth is large enough to risk a stack overflow.
# When performance is critical and function call overhead matters.urssion 












