<<<<<<< HEAD
# Complete the max_of_three function so that returns the
# maximum of three values.
#
# If two values are the same maximum value, return either of
# them.
# If all of the values are the same, return any of them
#
# Use the >= operator for greater than or equal to

def max_of_three(value1, value2, value3):
    if value1 >= value2 and value1 >= value3:
        return value1
    if value2 >= value1 and value2 >= value3:
        return value2
    else:
        return value3

print(max_of_three(1,2,3))
=======
# Complete the max_of_three function so that returns the
# maximum of three values.
#
# If two values are the same maximum value, return either of
# them.
# If all of the values are the same, return any of them
#
# Use the >= operator for greater than or equal to

def max_of_three(value1, value2, value3):
    if value1 >= value2 and value1 >= value3:
        return value1
    if value2 >= value1 and value2 >= value3:
        return value2
    else:
        return value3

print(max_of_three(1,2,3))
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
