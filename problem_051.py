<<<<<<< HEAD
# Write a function that meets these requirements.
#
# Name:       safe_divide
# Parameters: two values, a numerator and a denominator
# Returns:    if the denominator is zero, then returns math.inf.
#             otherwise, returns numerator / denominator
#
# Don't for get to import math!

import math

def safe_divide(numerator,denominator):
    if denominator == 0:
        return math.inf
    return numerator/denominator

print(safe_divide(5,0))
print(safe_divide(15,5))
=======
# Write a function that meets these requirements.
#
# Name:       safe_divide
# Parameters: two values, a numerator and a denominator
# Returns:    if the denominator is zero, then returns math.inf.
#             otherwise, returns numerator / denominator
#
# Don't for get to import math!

import math

def safe_divide(numerator,denominator):
    if denominator == 0:
        return math.inf
    return numerator/denominator

print(safe_divide(5,0))
print(safe_divide(15,5))
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
