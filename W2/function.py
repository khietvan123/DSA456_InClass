# Write a function that will sum all values from 1 to n and analyze the function:

def sum(n):
    rc = 0                  # 1
    for i in range(1,n+1):  # n + 1
        rc+=i               # n
    return rc               # 1
# T(n) = 1 + (n+1) + n + 1 = 2n + 3

