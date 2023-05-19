class Pet:
    """Represents a pet that has a species and a name."""

    def __init__(self, species, name): #these parameters are customizeable
        """creates a new Pet with the specified species and name."""
        self._species = species #this is stating that species matches whats put in up there
        self._name = name
        self._legs = '4'  #this is noncustomizable.
    
    def growl(self):
        return 'woof'

pet_1 = Pet("capybara", "Beatrice")
pet_2 = Pet("kangaroo", "Joey")


print(pet_1._name)
print(pet_2._name)
print(pet_1.growl())