# Note:
# Before class do the following function iteratively and recursively and analyze both
# function return base^n
# def power(base, n)
    
# Challenge: Write power() recursively so that its run time is better than O(n)

# --- Function returns base^n we can assume n is non-negavtive ---
# def power(base, n):
#     rc = 1
#     for i in range(n):
#         rc+= base
#     return rc

# --- Recursive version of power(non-challenge) ---
# How to guide
# 1) Determine if the function has a prototype that supports Recursion
#     - The arguments given to this function needs to support recursion,
#     Can I give it sth that leads it towards a simpler solution
# 2) what value(s) can we provide that will lead to a base case
# 3) What is the recursive case? how can I express a function in terms of itself
# def power(base,n):
#     rc = 1                          
#     if n > 0:
#         rc = base * power(base,n-1)
#     return rc
# ANALYSIS:
# Let n represent the value for the exponent (n) in this function
# Let T(n) repersent the number of operations done by the power() function
# When n is passed as the second argument
# def power(base,n):
#     rc = 1                          # 1       
#     if n > 0:                       # 1
#         rc = base * power(base,n-1) # 1 + 1 + T(n-1) + 1 = 3 + T(n-1)
#                                         # 3 is from the 3 operators(=,*,-)
#                                         #T(n-1) comes from the power() call
#                                         #We call power with n-1 as second an argument so the number of operations done by power(base, n-1)
#                                         #Is that second argument
#     return rc                       # 1
# ---> T(n) = 1 + 1 + 3 + T(n-1) + 1 = 6 + T(n-1)
# Then find T(n-1):
# T(n-1) = 6 + T(n-2)
# T(n-2) = 6 + T(n-3)
# T(n-3) = 6 + T(n-4)
# ...
# T(0) = 3
# # --- T(n) = 1 + 1 + 3 + T(n-1) + 1 = 6 + T(n-1) ---> This expression is true for n > 0
# T(1) = 6 + T(0)
# T(2) = 6 + T(1)
# T(3) = 6 + T(2)
# T(4) = 6 + T(3)
# ...
# T(2) = 6 + 6 + 3
# T(3) = 6 + 6 + 6 + 3
# T(4) = 6 + 6 + 6 + 6 + 3
# T(5) = 6 + 6 + 6 + 6 + 6 + 3
# --> Obviously the number of 6 is equal to n number in T(n)
# --> T(n) = 6n + 3

# --- CHALLENGE ---
# even: b^n = b^(n//2) * b^(n//2)
# odd : b^n = b^(n//2) * b^(n//2) * b

def power(base,n):
    rc = 1                      #1
    if n > 0:                   #1
        temp = power(base,n//2) #1+T(n/2)+ 1
                                    # 2 for the math operator(=,//)
                                    # T(n/2) for the function call
        rc = temp * temp        #1 + 1
        if(n%2==1):             #1+1
            rc=rc*base          #1+1
    return rc                   #1

# --> T(n) = 1 + 1 + 2 + T(n/2) + 2 + 2 + 2 + 1
# --> T(n) = 11 + T(n/2)
# ...
# T(n/2) = 11 + T(n/4)
# T(n/4) = 11 + T(n/8)
# ...
# T(0) = 3
# T(1) = 11 + T(0) = 11 + 3
# T(2) = 11 + T(1) = 11 + 11 + 3
# Thinking through the numbers we keep taling n and dividing by 2.
# Our calls are made with n, n/2, n/4, n/8 ... 1 == n/n

# | argument value | alternate expression |
# |---|---|
# | n | n/1 = n/2 ^ 0 |
# |n/2| n/2^1 |
# |n/4| n/2^2 |
# |...|...|
# |n/n| 1 = n/2^k = n/2^(logn)|

# n/n == n/2^k 
# n = 2^k 
# log(n) == log(2^k)
# log(n) == k * log 2
# log(n) == k * 1

# Therefore k == log(n)

# Therefore it took (logn) + 1 divisions to go from n to 1
# Therefore:
# T(n) = 11(1+logn) + 3
#      = 11 + 11logn + 3
#      = 13 + 11logn


# ANALYSIS:
# Let n represent the value for the exponent (n) in this function
# Let T(n) repersent the number of operations done by the power() function
# When n is passed as the second argument


        

