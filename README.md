# Virtual Pet — Terminal Edition

A small Python terminal virtual pet that uses Rich for tiny line animations and live updates.

Features
- Pet model with hunger, happiness, and energy
- Actions: feed, play, rest
- Time progression (tick)
- Save and load to JSON
- Simple CLI with small animations using Rich's Spinner and Live

Quick start (Windows PowerShell)

Create a virtualenv and install dependencies:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Run the CLI:

From the workspace root you can run the package directly (recommended) if you have installed dependencies:

```powershell
python -m virtual_pet
```

Or run the CLI module directly:

```powershell
python -m src.virtual_pet.cli
```

Run tests:

```powershell
pip install -r requirements.txt
pytest -q
```

Enjoy your virtual pet! 🐾

Animation library: This project uses the `rich` library to provide small line animations (spinners and live table updates) for a more pleasant terminal experience.
