<<<<<<< HEAD
# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

def gear_for_day(is_workday, is_sunny):
    gear = []
    if is_workday and not is_sunny:
        gear.append("umbrella")
    if is_workday:
        gear.append("laptop")
    else:
        gear.append("surfboard")
    return gear

print(gear_for_day(is_workday=True,is_sunny=False))
print(gear_for_day(is_workday=True,is_sunny=True))
print(gear_for_day(is_workday=False,is_sunny=True))
print(gear_for_day(is_workday=False,is_sunny=False))
=======
# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

def gear_for_day(is_workday, is_sunny):
    gear = []
    if is_workday and not is_sunny:
        gear.append("umbrella")
    if is_workday:
        gear.append("laptop")
    else:
        gear.append("surfboard")
    return gear

print(gear_for_day(is_workday=True,is_sunny=False))
print(gear_for_day(is_workday=True,is_sunny=True))
print(gear_for_day(is_workday=False,is_sunny=True))
print(gear_for_day(is_workday=False,is_sunny=False))
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
