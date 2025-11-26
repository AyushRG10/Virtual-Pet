import os
import sys

# Ensure `src` is on sys.path so tests can import virtual_pet during local test runs
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from virtual_pet.pet import Pet


def test_feed_reduces_hunger():
    p = Pet("Fluffy", hunger=80, happiness=10, energy=50)
    p.feed(30)
    assert p.hunger == 50
    assert p.happiness >= 10


def test_play_changes_stats():
    p = Pet("Buddy", hunger=20, happiness=20, energy=50)
    p.play(15)
    assert p.happiness == 35
    assert p.energy < 50
    assert p.hunger > 20


def test_rest_increases_energy():
    p = Pet("Cat", hunger=40, happiness=40, energy=10)
    p.rest(25)
    assert p.energy == 35


def test_tick_time_effects():
    p = Pet("Timey", hunger=0, happiness=50, energy=50)
    p.tick()
    assert p.hunger >= 0
    assert p.energy <= 50
    assert 0 <= p.happiness <= 100


def test_serialization_roundtrip():
    p = Pet("Sparky", hunger=10, happiness=90, energy=70)
    s = p.to_json()
    p2 = Pet.from_json(s)
    assert p == p2
