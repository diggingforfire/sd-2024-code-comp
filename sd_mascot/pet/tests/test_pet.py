import pytest

from pet.models import Pet, HealthState


@pytest.mark.django_db
def test_feed():
    pet = Pet(hunger=100)
    pet.feed(amount=35)
    assert pet.hunger == 65

@pytest.mark.django_db
def test_play():
    pet = Pet(happiness=15)
    pet.play(amount=40)
    assert pet.happiness == 55

def test_decay_health_hungry():
    pet = Pet(health=50, hunger=70)
    pet.decay_health()
    assert pet.health == 48

def test_decay_health_not_hungry():
    pet = Pet(health=50, hunger=50)
    pet.decay_health()
    assert pet.health == 50

def test_decay_health_happy():
    pet = Pet(health=20,happiness=80, hunger=50)
    pet.decay_health()
    assert pet.health == 20

def test_decay_health_not_happy():
    pet = Pet(health=20,happiness=30, hunger=50)
    pet.decay_health()
    assert pet.health == 16

@pytest.mark.parametrize("health,expected_state", [
    (100, HealthState.AMAZEBALLS),
    (90, HealthState.OK),
    (80, HealthState.OK),
    (79, HealthState.NEUTRAL),
    (50, HealthState.NEUTRAL),
    (49, HealthState.BAD),
    (0, HealthState.BAD),
])
def test_health_state_ok(health, expected_state):
    pet = Pet(health=health)
    assert pet.health_state == expected_state

