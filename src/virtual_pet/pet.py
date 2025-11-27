from __future__ import annotations
from dataclasses import dataclass, asdict
import json
from typing import Dict

@dataclass
class Pet:
    name: str
    hunger: int = 50  # 0 = full, 100 = starving
    happiness: int = 50  # 0 = sad, 100 = ecstatic
    energy: int = 50  # 0 = exhausted, 100 = full of energy

    def feed(self, amount: int = 20) -> None:
        """Feed the pet reducing hunger and slightly increasing happiness."""
        self.hunger = max(0, self.hunger - amount)
        self.happiness = min(100, self.happiness + amount // 4)

    def play(self, amount: int = 15) -> None:
        """Play with the pet increasing happiness but costing energy and slightly increasing hunger."""
        self.happiness = min(100, self.happiness + amount)
        self.energy = max(0, self.energy - amount // 2)
        self.hunger = min(100, self.hunger + amount // 3)

    def rest(self, amount: int = 20) -> None:
        """Let the pet rest to restore energy, but may decrease hunger slightly."""
        self.energy = min(100, self.energy + amount)
        self.hunger = min(100, max(0, self.hunger - amount // 10))

    def tick(self) -> None:
        """Advance time by one tick: hunger increases, energy decreases, happiness drifts."""
        self.hunger = min(100, self.hunger + 3)
        self.energy = max(0, self.energy - 2)
        # If very hungry or exhausted, happiness drops
        if self.hunger > 80 or self.energy < 20:
            self.happiness = max(0, self.happiness - 5)
        else:
            self.happiness = min(100, self.happiness + 1)

    def is_alive(self) -> bool:
        """Return True while pet is alive.

        The pet dies if hunger reaches or exceeds 100 OR energy falls to 0 or below.
        Previously the pet only died if both conditions were true which let the
        pet stay alive in clearly fatal states.
        """
        if self.hunger >= 100:
            return False
        if self.energy <= 0:
            return False
        return True

    def status(self) -> Dict[str, int]:
        return asdict(self)

    def to_json(self) -> str:
        # Include a simple schema version so future changes can be handled.
        obj = asdict(self)
        obj["__schema_version"] = 1
        return json.dumps(obj)

    @staticmethod
    def from_json(data: str) -> "Pet":
        obj = json.loads(data)
        # accept either raw fields or full object with schema version
        # tolerate missing keys with reasonable defaults
        name = obj.get("name")
        if name is None:
            raise ValueError("Missing 'name' in pet JSON")
        hunger = int(obj.get("hunger", 50))
        happiness = int(obj.get("happiness", 50))
        energy = int(obj.get("energy", 50))
        return Pet(name=name, hunger=hunger, happiness=happiness, energy=energy)
