# 3 Tests
# dog -> make_sound
# cat -> make_sound
# other -> make_sound
# 3 different fixtures

import pytest

class TestAnimal:
    def test_dog_make_sound(self, dog, capsys):
        assert dog.make_sound() == "Woof!"
        assert capsys.readouterr().out == "Woof!\n"

    def test_cat_make_sound(self, cat):
        assert cat.make_sound() == "Meow!"

    def test_other_make_sound(self, human):
        assert human.make_sound() == "Unknown sound"

    @pytest.mark.parametrize(["name", "species", "answer"],
                             [
                                 ("Buddy", "dog", "Woof!"),
                                 ("Oreo", "cat", "Meow!"),
                                 ("Human", "human", "Unknown sound"),
                             ])
    def test_animal_make_sound(self, make_animal, name, species, answer):
        animal = make_animal(name, species)
        assert animal.make_sound() == answer

    