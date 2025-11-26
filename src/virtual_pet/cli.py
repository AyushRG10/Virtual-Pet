from __future__ import annotations
import time
import json
from pathlib import Path
from rich.live import Live
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.spinner import Spinner
from .pet import Pet

console = Console()

SAVE_FILE = Path("pet_save.json")


def render_pet(pet: Pet) -> Table:
    t = Table(expand=True)
    t.add_column("Property")
    t.add_column("Value", justify="right")
    t.add_row("Name", pet.name)
    t.add_row("Hunger", f"{pet.hunger}/100")
    t.add_row("Happiness", f"{pet.happiness}/100")
    t.add_row("Energy", f"{pet.energy}/100")
    return t


def show_animation(message: str, seconds: float = 1.0) -> None:
    """Show a tiny animated spinner with a short message using Rich."""
    spinner = Spinner("dots", text=Text(message))
    with Live(spinner, refresh_per_second=12, transient=True, console=console):
        time.sleep(seconds)


def save_pet(pet: Pet) -> None:
    SAVE_FILE.write_text(pet.to_json())


def load_pet() -> Pet | None:
    if SAVE_FILE.exists():
        return Pet.from_json(SAVE_FILE.read_text())
    return None


def run_cli() -> None:
    console.print("[bold green]Welcome to Virtual Pet![/bold green]")

    pet = load_pet()
    if pet:
        console.print(f"Loaded pet [bold]{pet.name}[/bold] from save.")
    else:
        name = console.input("Enter your new pet's name: ")
        pet = Pet(name=name)
        console.print(f"Created pet [bold]{name}[/bold].")

    with Live(render_pet(pet), refresh_per_second=4, transient=False, console=console) as live:
        try:
            while pet.is_alive():
                console.print()
                console.print("Actions: [1] Feed  [2] Play  [3] Rest  [4] Save & Exit")
                choice = console.input("Choose an action (number): ")
                if choice.strip() == "1":
                    pet.feed()
                    show_animation("Feeding...")
                elif choice.strip() == "2":
                    pet.play()
                    show_animation("Playing...")
                elif choice.strip() == "3":
                    pet.rest()
                    show_animation("Resting...")
                elif choice.strip() == "4":
                    save_pet(pet)
                    show_animation("Saving...")
                    console.print("Saved — bye!")
                    return
                else:
                    console.print("Unknown choice — try again")

                # time passes
                pet.tick()
                live.update(render_pet(pet))

            console.print("[bold red]Oh no! Your pet didn't make it.[/bold red]")
        except KeyboardInterrupt:
            save_pet(pet)
            console.print("\nSaved on interrupt — bye!")


if __name__ == "__main__":
    run_cli()
