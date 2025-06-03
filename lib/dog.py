approved_breeds = [
    "Mastiff", "Chihuahua", "Corgi", "Shar Pei",
    "Beagle", "French Bulldog", "Pug", "Pointer"
]

class Dog:
    def __init__(self, name="Unknown", breed="Mastiff"):
        self.name = name      # Use property setter
        self.breed = breed    # Use property setter

    # Name property
    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # Breed property
    def get_breed(self):
        return self._breed

    def set_breed(self, value):
        if value in approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)
