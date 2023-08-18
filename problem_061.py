<<<<<<< HEAD
# Write a function that meets these requirements.
#
# Name:       remove_duplicates
# Parameters: a list of values
# Returns:    a copy of the list removing all
#             duplicate values and keeping the
#             original order
#
# Examples:
#     * input:   [1, 1, 1, 1]
#       returns: [1]
#     * input:   [1, 2, 2, 1]
#       returns: [1, 2]
#     * input:   [1, 3, 3, 20, 3, 2, 2]
#       returns: [1, 3, 20, 2]

def remove_duplicates(values):
    output = []
    for value in values:
        if value not in output:
            output.append(value)
    return output

print(remove_duplicates([1,1,1,1]))
print(remove_duplicates([1,2,2,1]))
print(remove_duplicates([1,3,3,20,3,2,2]))
=======
# Write a function that meets these requirements.
#
# Name:       remove_duplicates
# Parameters: a list of values
# Returns:    a copy of the list removing all
#             duplicate values and keeping the
#             original order
#
# Examples:
#     * input:   [1, 1, 1, 1]
#       returns: [1]
#     * input:   [1, 2, 2, 1]
#       returns: [1, 2]
#     * input:   [1, 3, 3, 20, 3, 2, 2]
#       returns: [1, 3, 20, 2]

def remove_duplicates(values):
    output = []
    for value in values:
        if value not in output:
            output.append(value)
    return output

print(remove_duplicates([1,1,1,1]))
print(remove_duplicates([1,2,2,1]))
print(remove_duplicates([1,3,3,20,3,2,2]))
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
