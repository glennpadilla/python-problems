<<<<<<< HEAD
# Complete the sum_of_squares function which accepts
# a list of numerical values and returns the sum of
# each item squared
#
# If the list of values is empty, the function should
# return None
#
# Examples:
#   * [] returns None
#   * [1, 2, 3] returns 1*1+2*2+3*3=14
#   * [-1, 0, 1] returns (-1)*(-1)+0*0+1*1=2
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def sum_of_squares(values):
    if len(values) <= 1:
        return None
    result = 0
    for value in values:
        result += value * value
    return result

print(sum_of_squares([]))
print(sum_of_squares([1,2,3]))
print(sum_of_squares([-1,0,1]))
print(sum_of_squares([2,4,6]))
=======
# Complete the sum_of_squares function which accepts
# a list of numerical values and returns the sum of
# each item squared
#
# If the list of values is empty, the function should
# return None
#
# Examples:
#   * [] returns None
#   * [1, 2, 3] returns 1*1+2*2+3*3=14
#   * [-1, 0, 1] returns (-1)*(-1)+0*0+1*1=2
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def sum_of_squares(values):
    if len(values) <= 1:
        return None
    result = 0
    for value in values:
        result += value * value
    return result

print(sum_of_squares([]))
print(sum_of_squares([1,2,3]))
print(sum_of_squares([-1,0,1]))
print(sum_of_squares([2,4,6]))
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
