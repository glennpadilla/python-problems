<<<<<<< HEAD
# Complete the fizzbuzz function to return
# * The word "fizzbuzz" if number is evenly divisible by
#   by both 3 and 5
# * The word "fizz" if number is evenly divisible by only
#   3
# * The word "buzz" if number is evenly divisible by only
#   5
# * The number if it is not evenly divisible by 3 nor 5
#
# Try to combine what you have done in the last two problems
# from memory.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def fizzbuzz(number):
    # if number is evenly divisible by 3 and 5
        # return "fizzbuzz"
    # if number is evenly divisible by 3
        # return "fizz"
    # if number is evenly divisible by 5
        # return "buzz"
    if number % 5 == 0 and number % 3 == 0:
        return "fizzbuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return number

print(fizzbuzz(5))
print(fizzbuzz(3))
print(fizzbuzz(0))
print(fizzbuzz(8))
=======
# Complete the fizzbuzz function to return
# * The word "fizzbuzz" if number is evenly divisible by
#   by both 3 and 5
# * The word "fizz" if number is evenly divisible by only
#   3
# * The word "buzz" if number is evenly divisible by only
#   5
# * The number if it is not evenly divisible by 3 nor 5
#
# Try to combine what you have done in the last two problems
# from memory.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def fizzbuzz(number):
    # if number is evenly divisible by 3 and 5
        # return "fizzbuzz"
    # if number is evenly divisible by 3
        # return "fizz"
    # if number is evenly divisible by 5
        # return "buzz"
    if number % 5 == 0 and number % 3 == 0:
        return "fizzbuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return number

print(fizzbuzz(5))
print(fizzbuzz(3))
print(fizzbuzz(0))
print(fizzbuzz(8))
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
