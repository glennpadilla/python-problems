<<<<<<< HEAD
# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average

def calculate_grade(values):
    if len(values) == 0:
        return None
    sum = 0
    for item in values:
        sum = sum + item
    average = sum / len(values)
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

print(calculate_grade([90]))
print(calculate_grade([80]))
print(calculate_grade([70]))
print(calculate_grade([60]))
print(calculate_grade([50]))
print(calculate_grade([]))
=======
# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average

def calculate_grade(values):
    if len(values) == 0:
        return None
    sum = 0
    for item in values:
        sum = sum + item
    average = sum / len(values)
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

print(calculate_grade([90]))
print(calculate_grade([80]))
print(calculate_grade([70]))
print(calculate_grade([60]))
print(calculate_grade([50]))
print(calculate_grade([]))
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
