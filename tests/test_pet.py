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


def test_is_alive_behavior():
    p = Pet("DeadHungry", hunger=100, energy=50)
    assert not p.is_alive()

    p2 = Pet("DeadTired", hunger=10, energy=0)
    assert not p2.is_alive()

    p3 = Pet("Alive", hunger=10, energy=10)
    assert p3.is_alive()


def test_from_json_missing_fields():
    s = '{"name": "Mystery"}'
    p = Pet.from_json(s)
    assert p.name == "Mystery"
    assert p.hunger == 50 and p.energy == 50 and p.happiness == 50
