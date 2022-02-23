# Creating the class
class Pet(object):
    """Class object for a pet."""
    def __init__(self, species, name):
        """Initialize a Pet."""
        self.species = species
        self.name = name
    
# Creating an instance of a class
my_dog = Pet(species="dog",
name="Scooby")
print (my_dog)
print (my_dog.name)
# # <__main__.Pet object at 0x7f16e31ba210>
# # Scooby

# # Creating the class
class Pet(object):
    """Class object for a pet."""
def __init__(self, species, name):
    """Initialize a Pet."""
    self.species = species
    self.name = name
def __str__(self):
    """Output when printing an instance of a Pet."""
    return f"{self.species} named {self.name}"

# Creating an instance of a class
my_dog = Pet(species="dog",
name="Scooby")
print (my_dog)
print (my_dog.name)
# dog named Scooby
# Scooby

# Creating the class
class Pet(object):
    """Class object for a pet."""
def __init__(self, species, name):
    """Initialize a Pet."""
    self.species = species
    self.name = name
def __str__(self):
    """Output when printing an instance of a Pet."""
    return f"{self.species} named {self.name}"
def change_name(self, new_name):
    """Change the name of your Pet."""
    self.name = new_name

# Creating an instance of a class
my_dog = Pet(species="dog", name="Scooby")
print (my_dog)
print (my_dog.name)
# dog named Scooby
# Scooby

# Using a class's function
my_dog.change_name(new_name="Scrappy")
print (my_dog)
print (my_dog.name)
# dog named Scrappy
# Scrappy

#Inheritance
class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(species="dog", name=name)
        self.breed = breed
def __str__(self):
    return f"A {self.breed} doggo named {self.name}"
scooby = Dog(breed="Great Dane", name="Scooby")
print (scooby)
# A Great Dane doggo named Scooby
scooby.change_name("Scooby Doo")
print (scooby)
# A Great Dane doggo named Scooby Doo
def filterVowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(letter in vowels):
        return True
    else:
        return False
letters = "oop python"
filteredVowels = filter(filterVowels, letters)
print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)
# The filtered vowels are:
# o
# o
# o