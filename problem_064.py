<<<<<<< HEAD
# Write a function that meets these requirements.
#
# Name:       temperature_differences
# Parameters: highs: a list of daily high temperatures
#             lows: a list of daily low temperatures
# Returns:    a new list containing the difference
#             between each high and low temperature
#
# The two lists will be the same length
#
# Example:
#     * inputs:  highs: [80, 81, 75, 80]
#                lows:  [72, 78, 70, 70]
#       result:         [ 8,  3,  5, 10]

def temperature_differences(highs, lows):
    differences = []
    for high, low in zip(highs, lows):
        differences.append(high - low)
    return differences

print(temperature_differences([80,81,75,80],[72,78,70,70]))
=======
# Write a function that meets these requirements.
#
# Name:       temperature_differences
# Parameters: highs: a list of daily high temperatures
#             lows: a list of daily low temperatures
# Returns:    a new list containing the difference
#             between each high and low temperature
#
# The two lists will be the same length
#
# Example:
#     * inputs:  highs: [80, 81, 75, 80]
#                lows:  [72, 78, 70, 70]
#       result:         [ 8,  3,  5, 10]

def temperature_differences(highs, lows):
    differences = []
    for high, low in zip(highs, lows):
        differences.append(high - low)
    return differences

print(temperature_differences([80,81,75,80],[72,78,70,70]))
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
