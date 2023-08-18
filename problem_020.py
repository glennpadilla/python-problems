<<<<<<< HEAD
# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.

def has_quorum(attendees_list, members_list):
    num_attendees = len(attendees_list)
    num_members = len(members_list)

    if num_attendees / num_members >= 0.5:
        return True
    else:
        return False

print(has_quorum([10],[11]))
=======
# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.

def has_quorum(attendees_list, members_list):
    num_attendees = len(attendees_list)
    num_members = len(members_list)

    if num_attendees / num_members >= 0.5:
        return True
    else:
        return False

print(has_quorum([10],[11]))
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
