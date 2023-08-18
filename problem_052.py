<<<<<<< HEAD
# Write a function that meets these requirements.
#
# Name:       generate_lottery_numbers
# Parameters: none
# Returns:    a list of six random unique numbers
#             between 1 and 40, inclusive
#
# Example bad results:
#    [4, 2, 3, 3, 1, 5] duplicate numbers
#    [1, 2, 3, 4, 5] not six numbers
#
# You can use randint from random, here, or any of
# the other applicable functions from the random
# package.
#
# https://docs.python.org/3/library/random.html

import random

# def generate_lottery_numbers():
#     numbers = []
#     while len(numbers) < 6:
#         number = random.randint(1,40)
#         if number not in numbers:
#             numbers.append(number)
#     return numbers

def generate_lottery_numbers():
    numbers = list(range(1,41))
    random.shuffle(numbers)
    return numbers[0:6]

print(generate_lottery_numbers())
=======
# Write a function that meets these requirements.
#
# Name:       generate_lottery_numbers
# Parameters: none
# Returns:    a list of six random unique numbers
#             between 1 and 40, inclusive
#
# Example bad results:
#    [4, 2, 3, 3, 1, 5] duplicate numbers
#    [1, 2, 3, 4, 5] not six numbers
#
# You can use randint from random, here, or any of
# the other applicable functions from the random
# package.
#
# https://docs.python.org/3/library/random.html

import random

# def generate_lottery_numbers():
#     numbers = []
#     while len(numbers) < 6:
#         number = random.randint(1,40)
#         if number not in numbers:
#             numbers.append(number)
#     return numbers

def generate_lottery_numbers():
    numbers = list(range(1,41))
    random.shuffle(numbers)
    return numbers[0:6]

print(generate_lottery_numbers())
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
