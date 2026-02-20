class Animal:
    def __init__(self, name, species):
        self._name = name
        self._species = species

    def make_sound(self):
        if self._species == "dog":

            msg =  "Woof!"
        elif self._species == "cat":
            msg = "Meow!"
        else:
            msg = "Unknown sound"
        
        print(msg)
        return msg
