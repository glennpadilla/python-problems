<<<<<<< HEAD
# Write a function that meets these requirements.
#
# Name:       only_odds
# Parameters: a list of numbers
# Returns:    a copy of the list that only includes the
#             odd numbers from the original list
#
# Examples:
#     * input:   [1, 2, 3, 4]
#       returns: [1, 3]
#     * input:   [2, 4, 6, 8]
#       returns: []
#     * input:   [1, 3, 5, 7]
#       returns: [1, 3, 5, 7]

def only_odds(nums):
    output = []
    for num in nums:
        if num % 2 == 1:
            output.append(num)
    return output

print(only_odds([1,2,3,4]))
print(only_odds([2,4,6,8]))
print(only_odds([1,3,5,7]))
=======
# Write a function that meets these requirements.
#
# Name:       only_odds
# Parameters: a list of numbers
# Returns:    a copy of the list that only includes the
#             odd numbers from the original list
#
# Examples:
#     * input:   [1, 2, 3, 4]
#       returns: [1, 3]
#     * input:   [2, 4, 6, 8]
#       returns: []
#     * input:   [1, 3, 5, 7]
#       returns: [1, 3, 5, 7]

def only_odds(nums):
    output = []
    for num in nums:
        if num % 2 == 1:
            output.append(num)
    return output

print(only_odds([1,2,3,4]))
print(only_odds([2,4,6,8]))
print(only_odds([1,3,5,7]))
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
