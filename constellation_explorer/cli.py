"""Command-line interface for Constellation Explorer."""

from __future__ import annotations

import argparse

from .generator import generate_systems


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate fictional star systems")
    parser.add_argument("--seed", required=True, help="Seed for deterministic generation")
    parser.add_argument("--systems", type=int, default=3, help="How many systems to generate")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    systems = generate_systems(args.seed, args.systems)
    for system in systems:
        print(f"System: {system.name}")
        print(f"  Star class: {system.star_class}")
        print(f"  Habitable planets: {system.habitable_planets}")
        print(f"  Notable feature: {system.feature}")


if __name__ == "__main__":
    main()