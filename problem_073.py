<<<<<<< HEAD
# Write a class that meets these requirements.
#
# Name:       Student
#
# Required state:
#    * name, a string
#
# Behavior:
#    * add_score(score)   # Adds a score to their list of scores
#    * get_average()      # Gets the average of the student's scores
#
# Example:
#    student = Student("Malik")
#
#    print(student.get_average())    # Prints None
#    student.add_score(80)
#    print(student.get_average())    # Prints 80
#    student.add_score(90)
#    student.add_score(82)
#    print(student.get_average())    # Prints 84
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_scores(self, score):
        self.scores.append(score)

    def get_average(self):
        if len(self.scores) == 0:
            return None
        return sum(self.scores) / len(self.scores)

student = Student("Malik")

print(student.get_average())
student.add_scores(80)
print(student.get_average())
student.add_scores(90)
student.add_scores(82)
print(student.get_average())
=======
# Write a class that meets these requirements.
#
# Name:       Student
#
# Required state:
#    * name, a string
#
# Behavior:
#    * add_score(score)   # Adds a score to their list of scores
#    * get_average()      # Gets the average of the student's scores
#
# Example:
#    student = Student("Malik")
#
#    print(student.get_average())    # Prints None
#    student.add_score(80)
#    print(student.get_average())    # Prints 80
#    student.add_score(90)
#    student.add_score(82)
#    print(student.get_average())    # Prints 84
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_scores(self, score):
        self.scores.append(score)

    def get_average(self):
        if len(self.scores) == 0:
            return None
        return sum(self.scores) / len(self.scores)

student = Student("Malik")

print(student.get_average())
student.add_scores(80)
print(student.get_average())
student.add_scores(90)
student.add_scores(82)
print(student.get_average())
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
