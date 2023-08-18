<<<<<<< HEAD
# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):
    if len(values) == 0:
        return None
    max_value = values[0]
    for item in values:
        if item > max_value:
            max_value = item
    return max_value

print(max_in_list([]))
print(max_in_list([1,2,3,4,5]))
print(max_in_list([5,10,2,400,8,17]))
=======
# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):
    if len(values) == 0:
        return None
    max_value = values[0]
    for item in values:
        if item > max_value:
            max_value = item
    return max_value

print(max_in_list([]))
print(max_in_list([1,2,3,4,5]))
print(max_in_list([5,10,2,400,8,17]))
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
