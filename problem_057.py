<<<<<<< HEAD
# Write a function that meets these requirements.
#
# Name:       sum_fraction_sequence
# Parameters: a number
# Returns:    the sum of the fractions of the
#             form 1/2+2/3+3/4+...+number/number+1
#
# Examples:
#     * input:   1
#       returns: 1/2
#     * input:   2
#       returns: 1/2 + 2/3
#     * input:   3
#       returns: 1/2 + 2/3 + 3/4

def sum_fraction_sequence(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i / (i + 1)
    return sum

print(sum_fraction_sequence(1))
print(sum_fraction_sequence(2))
print(sum_fraction_sequence(3))
=======
# Write a function that meets these requirements.
#
# Name:       sum_fraction_sequence
# Parameters: a number
# Returns:    the sum of the fractions of the
#             form 1/2+2/3+3/4+...+number/number+1
#
# Examples:
#     * input:   1
#       returns: 1/2
#     * input:   2
#       returns: 1/2 + 2/3
#     * input:   3
#       returns: 1/2 + 2/3 + 3/4

def sum_fraction_sequence(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i / (i + 1)
    return sum

print(sum_fraction_sequence(1))
print(sum_fraction_sequence(2))
print(sum_fraction_sequence(3))
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
