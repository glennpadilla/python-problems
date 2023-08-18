<<<<<<< HEAD
# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]

# def halve_the_list(list):
#     # cut the list in half and return both lists
#     first_half = []
#     second_half = []
#     length = len(list)
#     for index in range(len(list)):
#         # how do we know if we've reached the halfway point?
#         # check if current index is less than halway point
#         if index < (length / 2):
#             first_half.append(list[index])
#         else:
#             second_half.append(list[index])

#     return first_half, second_half
#     # if list length is odd, then extra element lives inside of first list

# def halve_the_list(input):
#     first_list = []
#     second_list = []
#     first_list_len = len(input) // 2 + (len(input) % 2)
#     for i in range(first_list_len):
#         first_list.append(input[i])
#     for i in range(len(input) // 2):
#         index = i + first_list_len
#         second_list.append(input[index])
#     return first_list, second_list

def halve_the_list(input):
    return(
        input[0:len(input) // 2 + (len(input) % 2)],
        input[len(input) // 2 + (len(input) % 2):],
    )

print(halve_the_list([1,2,3,4]))
print(halve_the_list([1,2,3]))
=======
# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]

# def halve_the_list(list):
#     # cut the list in half and return both lists
#     first_half = []
#     second_half = []
#     length = len(list)
#     for index in range(len(list)):
#         # how do we know if we've reached the halfway point?
#         # check if current index is less than halway point
#         if index < (length / 2):
#             first_half.append(list[index])
#         else:
#             second_half.append(list[index])

#     return first_half, second_half
#     # if list length is odd, then extra element lives inside of first list

# def halve_the_list(input):
#     first_list = []
#     second_list = []
#     first_list_len = len(input) // 2 + (len(input) % 2)
#     for i in range(first_list_len):
#         first_list.append(input[i])
#     for i in range(len(input) // 2):
#         index = i + first_list_len
#         second_list.append(input[index])
#     return first_list, second_list

def halve_the_list(input):
    return(
        input[0:len(input) // 2 + (len(input) % 2)],
        input[len(input) // 2 + (len(input) % 2):],
    )

print(halve_the_list([1,2,3,4]))
print(halve_the_list([1,2,3]))
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
