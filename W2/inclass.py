## Analysis
# Come up with an expression that describes the resource consumption of the algorithm.
# We will do this by attempting to describe it in terms of what the code is doing in a conside
# and accurate manner.

### Example 1
# Perform an analysis of this function with respect to size of the array
def add(array):
    rc = 0                          # 1
    for i in range(len(array)):     # n + 2
                                        # n is for changing i n times
                                        # 2 is for call to range and call to len

        rc+= array[i]               # n
    return rc                       # 1
# ---> T(n) = 1 + (n+2) + n + 1 = 2n + 4

#### Solution
# Let n represents the size of the array
# Let T(n) represents the number of operations performed by the 
# add function when given an array of size n.

def add(array):                     # count how many operation:
    rc = 0                          # 1
    for i in range(len(array)):     # n
        rc+= array[i]               # n because 1 op n loop iterations
    return rc                       # 1

### Example 2
# Let n represents the length of s
# Let T(n) represents the number of operations done by so;; given string of length s

#C++
# void silly(const char *s){
#     int rc = 0;                         // 1
#     for(int i = 0 ; i <strlen(s);i++){  // 1 for i == 0
#                                         // n for i++
#                                         // n for the <
#                                         // n*n for strlen() 
#                                         // n
#         rc+=s[i];
#     }
#     return rc;                          // 1
# }
# --> T(n) = 1 + 1 + n + n + (n*n) + n + 1 = n^2 + 3n + 3

## NOTE STUFF: same task but performance is different
# void silly2(const char *s){
#     int rc = 0;                         // 1
#     int len = strlen(s)                 // n
#     for(int i = 0 ; i < len ;i++){      // 1 for i == 0
#                                         // n for i++
#                                         // n for the <

#                                        
#         rc+=s[i];                       // n
#     }
#     return rc;                          // 1
# }
# --> T(n) =  1  + n + 1 + n + n + n + 1 = 4n + 3
# DONT PUT THE CONSTANT IN BIG O
# --> Dont declare uneccessary variable
