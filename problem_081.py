<<<<<<< HEAD
# Write four classes that meet these requirements.
#
# Name:       Animal
#
# Required state:
#    * number_of_legs, the number of legs the animal has
#    * primary_color, the primary color of the animal
#
# Behavior:
#    * describe()       # Returns a string that describes that animal
#                         in the format
#                                self.__class__.__name__
#                                + " has "
#                                + str(self.number_of_legs)
#                                + " legs and is primarily "
#                                + self.primary_color
#
#
# Name:       Dog, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Bark!"
#
#
#
# Name:       Cat, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Miao!"
#
#
#
# Name:       Snake, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Sssssss!"

class Animal:
    def __init__(self, number_of_legs, primary_color):
        self.number_of_legs = number_of_legs
        self.primary_color = primary_color

    def describe(self):
        return(
            self.__class__.__name__
            + " has "
            + str(self.number_of_legs)
            + " legs and is primarily "
            + self.primary_color
            +". "
        )

class Dog(Animal):
    def speak(self):
        return "barks!"

class Cat(Animal):
    def speak(self):
        return "meows!"

class Snake(Animal):
    def speak(self):
        return "hisses!"

dog = Dog(4, "white")
cat = Cat(4, "orange")
snake = Snake(0, "black")

print(dog.describe() + "The dog " + dog.speak())
print(cat.describe() + "The cat " + cat.speak())
print(snake.describe() + "The snake " + snake.speak())
=======
# Write four classes that meet these requirements.
#
# Name:       Animal
#
# Required state:
#    * number_of_legs, the number of legs the animal has
#    * primary_color, the primary color of the animal
#
# Behavior:
#    * describe()       # Returns a string that describes that animal
#                         in the format
#                                self.__class__.__name__
#                                + " has "
#                                + str(self.number_of_legs)
#                                + " legs and is primarily "
#                                + self.primary_color
#
#
# Name:       Dog, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Bark!"
#
#
#
# Name:       Cat, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Miao!"
#
#
#
# Name:       Snake, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Sssssss!"

class Animal:
    def __init__(self, number_of_legs, primary_color):
        self.number_of_legs = number_of_legs
        self.primary_color = primary_color

    def describe(self):
        return(
            self.__class__.__name__
            + " has "
            + str(self.number_of_legs)
            + " legs and is primarily "
            + self.primary_color
            +". "
        )

class Dog(Animal):
    def speak(self):
        return "barks!"

class Cat(Animal):
    def speak(self):
        return "meows!"

class Snake(Animal):
    def speak(self):
        return "hisses!"

dog = Dog(4, "white")
cat = Cat(4, "orange")
snake = Snake(0, "black")

print(dog.describe() + "The dog " + dog.speak())
print(cat.describe() + "The cat " + cat.speak())
print(snake.describe() + "The snake " + snake.speak())
>>>>>>> 6890c8f5fa8daba58f58887c821d440a15b9ee8d
