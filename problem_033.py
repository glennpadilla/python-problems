<<<<<<< HEAD
# Complete the sum_of_first_n_even_numbers function which
# accepts a numerical count n and returns the sum of the
# first n even numbers
#
# If the value of the limit is less than 0, then it should
# return None
#
# Examples:
#   * -1 returns None
#   * 0 returns 0
#   * 1 returns 0+2=2
#   * 2 returns 0+2+4=6
#   * 5 returns 0+2+4+6+8+10=30
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def sum_of_first_n_even_numbers(n):
    if n < 0:
        return None
    sum = 0
    for i in range(n + 1):
        sum = sum + i * 2
    return sum

print(sum_of_first_n_even_numbers(-1))
print(sum_of_first_n_even_numbers(0))
print(sum_of_first_n_even_numbers(1))
print(sum_of_first_n_even_numbers(2))
print(sum_of_first_n_even_numbers(5))
=======
# Complete the sum_of_first_n_even_numbers function which
# accepts a numerical count n and returns the sum of the
# first n even numbers
#
# If the value of the limit is less than 0, then it should
# return None
#
# Examples:
#   * -1 returns None
#   * 0 returns 0
#   * 1 returns 0+2=2
#   * 2 returns 0+2+4=6
#   * 5 returns 0+2+4+6+8+10=30
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def sum_of_first_n_even_numbers(n):
    if n < 0:
        return None
    sum = 0
    for i in range(n + 1):
        sum = sum + i * 2
    return sum

print(sum_of_first_n_even_numbers(-1))
print(sum_of_first_n_even_numbers(0))
print(sum_of_first_n_even_numbers(1))
print(sum_of_first_n_even_numbers(2))
print(sum_of_first_n_even_numbers(5))
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
