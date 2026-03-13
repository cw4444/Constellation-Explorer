# codex-explore
# Constellation Explorer

A tiny Python CLI that procedurally generates fictional star systems from a seed.

## Why this project?
I picked something playful: deterministic world-building you can rerun and share by seed.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
constellation --seed andromeda --systems 3
```

## Example output

```text
System: Vela-98
  Star class: K
  Habitable planets: 1
  Notable feature: ringed gas giant with ion storms
```

## Run tests

```bash
python -m unittest discover -s tests
```
