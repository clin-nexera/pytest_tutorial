import pytest
from src.animal import Animal


@pytest.fixture
def dog() -> Animal:
    return Animal("Buddy", "dog")

@pytest.fixture
def cat() -> Animal:
    return Animal("Princess", "cat")

@pytest.fixture
def alien() -> Animal:
    return Animal("ET", "alien")

@pytest.fixture
def make_animal():
    def _make_animal(name, species):
        return Animal(name, species)
    return _make_animal

@pytest.fixture(
        params=[("Buddy", "dog"), ("Princess", "cat"), ("ET", "alien")],
        ids=["dog", "cat", "alien"]
)
def animal(request):
    name, species = request.param[0], request.param[1]
    return Animal(name, species)

class TestAnimal:
    def test_make_sound_dog(self, capsys, dog: Animal):
        assert dog.make_sound() == "Woof!"
        assert capsys.readouterr().out == "Woof!\n"

    def test_make_sound_cat(self, cat: Animal):
        assert cat.make_sound() == "Meow!"

    def test_make_sound_other(self, alien: Animal):
        assert alien.make_sound() == "Unknown sound"

    @pytest.mark.parametrize(["name", "species", "answer"],
                            [
                                ("Buddy", "dog", "Woof!"),
                                ("Princess", "cat", "Meow!"),
                                ("ET", "alien", "Unknown sound"),
                            ])
    def test_animal_sound(self, make_animal, name, species, answer):
        animal = make_animal(name, species)
        assert animal.make_sound() == answer

    def test_animal_sound_2(self, animal):
        if animal._species == "dog":
            expected = "Woof!"
        elif animal._species == "cat":
            expected = "Meow!"
        else:
            expected = "Unknown sound"
        
        assert animal.make_sound() == expected