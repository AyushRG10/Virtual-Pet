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
        return not (self.hunger >= 100 and self.energy <= 0)

    def status(self) -> Dict[str, int]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(asdict(self))

    @staticmethod
    def from_json(data: str) -> "Pet":
        obj = json.loads(data)
        return Pet(**obj)
