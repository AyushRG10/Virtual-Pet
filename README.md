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

Run the CLI (interactive):

From the workspace root you can run the module directly (no install required):

```powershell
python -m src.virtual_pet.cli
```

If you install the package (pip install -e . or a built package) you can run the installed console script:

```powershell
virtual-pet
```

Run tests:

```powershell
pip install -r requirements.txt
pytest -q
```

Enjoy your virtual pet! 🐾

Animation library: This project uses the `rich` library to provide small line animations (spinners and live table updates) for a more pleasant terminal experience.

Creature art: The CLI shows a small ASCII art pet (a dog–cat hybrid) that animates subtly while the UI updates. The artwork appears in the right-hand panel of the UI and changes frames to give a little movement.

Save location: The CLI saves state to a user-local path by default so your saves persist between runs and avoid cluttering the project folder. On Windows the default is `%USERPROFILE%\\.virtual_pet\\pet_save.json` and on Unix/macOS it is `$HOME/.virtual_pet/pet_save.json`.
