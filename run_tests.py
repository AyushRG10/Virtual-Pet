import os
import sys

# ensure src/ is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from virtual_pet.pet import Pet

failures = []

def expect(cond, msg):
    if not cond:
        failures.append(msg)


def test_feed_reduces_hunger():
    p = Pet("Fluffy", hunger=80, happiness=10, energy=50)
    p.feed(30)
    expect(p.hunger == 50, f"feed did not reduce hunger: {p.hunger}")
    expect(p.happiness >= 10, "happiness did not increase")


def test_play_changes_stats():
    p = Pet("Buddy", hunger=20, happiness=20, energy=50)
    p.play(15)
    expect(p.happiness == 35, f"unexpected happiness: {p.happiness}")
    expect(p.energy < 50, "energy not decreased")
    expect(p.hunger > 20, "hunger not increased")


def test_rest_increases_energy():
    p = Pet("Cat", hunger=40, happiness=40, energy=10)
    p.rest(25)
    expect(p.energy == 35, f"unexpected energy: {p.energy}")


def test_tick_time_effects():
    p = Pet("Timey", hunger=0, happiness=50, energy=50)
    p.tick()
    expect(p.hunger >= 0, "hunger negative")
    expect(p.energy <= 50, "energy increased unexpectedly")
    expect(0 <= p.happiness <= 100, "happiness out of bounds")


def test_serialization_roundtrip():
    p = Pet("Sparky", hunger=10, happiness=90, energy=70)
    s = p.to_json()
    p2 = Pet.from_json(s)
    expect(p == p2, "roundtrip serialization mismatch")


if __name__ == '__main__':
    test_feed_reduces_hunger()
    test_play_changes_stats()
    test_rest_increases_energy()
    test_tick_time_effects()
    test_serialization_roundtrip()

    if failures:
        print('\n'.join(['FAIL: ' + f for f in failures]))
        sys.exit(1)
    else:
        print('All tests passed ✅')
        sys.exit(0)
