import pytest

from src.animal import Animal

@pytest.fixture
def dog():
    return Animal("Buddy", "dog")

@pytest.fixture
def cat():
    return Animal("Whiskers", "cat")

@pytest.fixture
def human():
    return Animal("Bob", "human")

@pytest.fixture(params=[("Buddy", "dog"), ("Oreo", "cat")])
def animal(request):
    name, species = request.param[0], request.param[1]
    return Animal(name, species)

@pytest.fixture
def make_animal():
    def _make_animal(name, species):
        return Animal(name, species)
    return _make_animal