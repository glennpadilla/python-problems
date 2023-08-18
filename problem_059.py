<<<<<<< HEAD
# Write a function that meets these requirements.
#
# Name:       specific_random
# Parameters: none
# Returns:    a random number between 10 and 500, inclusive,
#             that is divisible by 5 and 7
#
# Examples:
#     * returns: 35
#     * returns: 105
#     * returns: 70
#
# Guidance:
#   * Generate all the numbers that are divisible by 5
#     and 7 into a list
#   * Use random.choice to select one

import random

def specific_random():
    good_numbers = []
    for i in range(1,500):
        if i % 35 == 0:
            good_numbers.append(i)
    return random.choice(good_numbers)

print(specific_random())
=======
# Write a function that meets these requirements.
#
# Name:       specific_random
# Parameters: none
# Returns:    a random number between 10 and 500, inclusive,
#             that is divisible by 5 and 7
#
# Examples:
#     * returns: 35
#     * returns: 105
#     * returns: 70
#
# Guidance:
#   * Generate all the numbers that are divisible by 5
#     and 7 into a list
#   * Use random.choice to select one

import random

def specific_random():
    good_numbers = []
    for i in range(1,500):
        if i % 35 == 0:
            good_numbers.append(i)
    return random.choice(good_numbers)

print(specific_random())
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
