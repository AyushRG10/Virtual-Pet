import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from virtual_pet.pet import Pet
from virtual_pet.cli import _creature_frames, render_creature


def test_creature_frames_exist():
    p = Pet('Tester', hunger=30, happiness=70, energy=50)
    frames = _creature_frames(p)
    assert isinstance(frames, list)
    assert len(frames) >= 2
    assert all(isinstance(f, str) and len(f) > 5 for f in frames)


def test_render_creature_returns_panel():
    p = Pet('Tester', hunger=30, happiness=70, energy=50)
    panel = render_creature(p)
    # The renderer returns a Panel-like object (we just ensure it's not None)
    assert panel is not None
