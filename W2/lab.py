# Let n represent the value being passed to the factorial
# Let T(n) represent the number of operations done by the
# factorial function given the value n

#This function returns n!
# def Factorial(n):             
#     rc = 1                    # 1  
#     for i in range(2,n+1):    # (n-1) + 1 + 1
                                    #(n-1) for changes to i
                                    #1 for range() call
                                    #1 for + of n+1
#         rc = rc*i             # 2(n-1)
                                    # 2 operators = and *
                                    # n-1 times of loop runs (changes of i)
#     return rc                 # 1

#--> T(n) = 1 + ((n-1)+1+1) + 2(n-1) + 1 = 3n + 1
# Therefore, T(n) is O(n) --> Dominating term of 3n + 1 is 3n, so we use 3n but drop constant for our function


#Recursion:
# HOW TO DO RECURSION:
# 1: Come up w base case
def Factorial(n):
    if n <= 1:                  # 2
        return 1                # 1
    else:
        return n*Factorial(n-1) # 1 + 1 + T(n)

#--> T(n) = 2 + 1 + 1 = 4

#Analysis
def Factorial(n):
    rc = 1                      # 1
    if n > 1:                   # 1
        rc = n*Factorial(n-1)   # 3 + T(n-1)
                                    # 3 for operations = * and -
                                    # T(n) is a function that returns a number of operations done by the Factorial function
                                    # when Factorial is given n. Here we are calling Factorial() with n-1 so, the number
                                    # of operations doe by that is T(n-1)
    return rc                   # 1

#--> T(n) = 1 + 1 + 3 + T(n-1) + 1 = T(n-1) + 6
# T(n-1) = 6 - T((n-1)-n-1) = 6 - T(n-2)
# T(n-2) = 6 - T(n - 3)
# T(n-3) = 6 - T(n - 4)
# ...
# T(4) = 6 - T(3)
# T(3) = 6 - T(2)
# T(2) = 6 - T(1)

# T(1) = 3

# T(2) = 6+3
# T(3) = 6 + 6 + 3
# T(4) = 6 + 6 + 6 + 3
# T(5) = 6 + 6 + 6 + 6 + 3
#...

#T(n) = 6 + 6 + ... + 6 + 3 <--- There are n-1 6's here
#     = 6(n-1) + 3
#     = 6n - 3          For all n > 1
#     = 3n - 1

# Therefore T(n) is 0(n)


print(Factorial(4))
        
