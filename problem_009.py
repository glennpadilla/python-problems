<<<<<<< HEAD
# Complete the is_palindrome function to check if the value in
# the word parameter is the same backward and forward.
#
# For example, the word "racecar" is a palindrome because, if
# you write it backwards, it's the same word.

# It uses the built-in function reversed and the join method
# for string objects.

def is_palindrome(word):
    # how can i reverse this string?
    # we can loop over a string from left to right
    # what if we could loop in reverse?
    # then maybe we could create a new string with the characters
    # reversed
    # how do we build a new string?
    # we start with an empty string and we add to it with concatenation
    # add the characters one by one for each iteration of the loop
    # to the new_str variable

    reverse_str = ""
    for char in word:
        reverse_str = char + reverse_str
    print(reverse_str)
    return word == reverse_str
print(is_palindrome("racecar"))

def is_palindrome(word):
    # how can i reverse this string?
    # we can loop over a string from left to right
    # what if we could loop in reverse?
    # then maybe we could create a new string with the characters
    # reversed
    # how do we build a new string?
    # we start with an empty string and we add to it with concatenation
    # how can we loop right to left?

    reversed_str = ""
    index = len(word) - 1
    while index >= 0:
        reversed_str = reversed_str + word[index]
    print(reversed_str)
    return word == reversed_str
=======
# Complete the is_palindrome function to check if the value in
# the word parameter is the same backward and forward.
#
# For example, the word "racecar" is a palindrome because, if
# you write it backwards, it's the same word.

# It uses the built-in function reversed and the join method
# for string objects.

def is_palindrome(word):
    # how can i reverse this string?
    # we can loop over a string from left to right
    # what if we could loop in reverse?
    # then maybe we could create a new string with the characters
    # reversed
    # how do we build a new string?
    # we start with an empty string and we add to it with concatenation
    # add the characters one by one for each iteration of the loop
    # to the new_str variable

    reverse_str = ""
    for char in word:
        reverse_str = char + reverse_str
    print(reverse_str)
    return word == reverse_str
print(is_palindrome("racecar"))

def is_palindrome(word):
    # how can i reverse this string?
    # we can loop over a string from left to right
    # what if we could loop in reverse?
    # then maybe we could create a new string with the characters
    # reversed
    # how do we build a new string?
    # we start with an empty string and we add to it with concatenation
    # how can we loop right to left?

    reversed_str = ""
    index = len(word) - 1
    while index >= 0:
        reversed_str = reversed_str + word[index]
    print(reversed_str)
    return word == reversed_str
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
