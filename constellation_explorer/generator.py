"""Deterministic procedural generator for fictional star systems."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import random
from typing import List

STAR_CLASSES = ["O", "B", "A", "F", "G", "K", "M"]
FEATURES = [
    "ringed gas giant with ion storms",
    "binary moon resonance field",
    "ancient derelict observatory",
    "glittering asteroid belt rich in cobalt",
    "ocean world with bioluminescent tides",
    "rogue comet nursery",
]
PREFIXES = ["Vela", "Orion", "Lyra", "Cygnus", "Draco", "Aquila", "Perseus"]


@dataclass(frozen=True)
class StarSystem:
    """A generated star system."""

    name: str
    star_class: str
    habitable_planets: int
    feature: str


def _seed_to_int(seed: str) -> int:
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    return int(digest[:16], 16)


def generate_systems(seed: str, count: int = 3) -> List[StarSystem]:
    """Generate `count` deterministic systems from `seed`."""
    if count <= 0:
        raise ValueError("count must be positive")

    rng = random.Random(_seed_to_int(seed))
    systems: List[StarSystem] = []
    for _ in range(count):
        prefix = rng.choice(PREFIXES)
        suffix = rng.randint(10, 999)
        systems.append(
            StarSystem(
                name=f"{prefix}-{suffix}",
                star_class=rng.choice(STAR_CLASSES),
                habitable_planets=rng.randint(0, 4),
                feature=rng.choice(FEATURES),
            )
        )
    return systems