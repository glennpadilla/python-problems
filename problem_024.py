<<<<<<< HEAD
# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

def calculate_average(values):
    if len(values) == 0:
        return None
    sum = 0
    for item in values:
        sum = sum + item
    return sum / len(values)

print(calculate_average([]))
print(calculate_average([2,4,6,8]))
=======
# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

def calculate_average(values):
    if len(values) == 0:
        return None
    sum = 0
    for item in values:
        sum = sum + item
    return sum / len(values)

print(calculate_average([]))
print(calculate_average([2,4,6,8]))
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
