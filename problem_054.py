<<<<<<< HEAD
# Write a function that meets these requirements.
#
# Name:       check_input
# Parameters: one parameter that can hold any value
# Returns:    if the value of the parameter is the
#             string "raise", then it should raise
#             a ValueError. otherwise, it should
#             just return the value of the parameter
#
# Examples
#    * input:   3
#      returns: 3
#    * input:   "this is a string"
#      returns: "this is a string"
#    * input:   "raise"
#      RAISES:  ValueError

def check_input(input):
    if input == "raise":
        raise ValueError
    return input

print(check_input(3))
print(check_input("this is a string"))
print(check_input("raise"))
=======
# Write a function that meets these requirements.
#
# Name:       check_input
# Parameters: one parameter that can hold any value
# Returns:    if the value of the parameter is the
#             string "raise", then it should raise
#             a ValueError. otherwise, it should
#             just return the value of the parameter
#
# Examples
#    * input:   3
#      returns: 3
#    * input:   "this is a string"
#      returns: "this is a string"
#    * input:   "raise"
#      RAISES:  ValueError

def check_input(input):
    if input == "raise":
        raise ValueError
    return input

print(check_input(3))
print(check_input("this is a string"))
print(check_input("raise"))
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
