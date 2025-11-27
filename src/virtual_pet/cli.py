from __future__ import annotations
import time
import json
from pathlib import Path
from rich.live import Live
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
from rich.align import Align
from rich.spinner import Spinner
from .pet import Pet

console = Console()

SAVE_FILE = Path("pet_save.json")


def _creature_frames(pet: Pet) -> list[str]:
    """Return two small ASCII frames for a dog-cat hybrid creature.

    The creature is purposely simple so it fits comfortably into small terminals.
    Frames differ by a small tail/ear/eye change to give a subtle animation.
    We also vary the eyes slightly based on happiness (bright eyes when happy).
    """

    # choose eye char based on happiness
    eye_open = "o"
    eye_sleep = "-"
    eye = eye_open if pet.happiness > 40 else eye_sleep

    # two frames: tail-left and tail-right
    frame_a = fr"""
         /\_/\   (
        ( {eye}.{eye} )  ~ Woof-Cat
         (  =^= )  
        (  )  
         UU   /|
            / |
        """.strip("\n")

    frame_b = fr"""
         /\_/\   (
        ( {eye}.{eye} )  ~ Meow-Dog
         (  =^= )
          (  )  
           UU    |\
            | \
        """.strip("\n")

    return [frame_a, frame_b]


def render_creature(pet: Pet) -> Panel:
    """Create a Panel containing a small animated creature (selects frame by time)."""
    frames = _creature_frames(pet)
    # turn-over rate ~ 2 frames / sec — use current time to pick a frame
    index = int(time.time() * 2) % len(frames)
    art = frames[index]

    # add a small status line hinting at the pet's mood
    mood = "happy" if pet.happiness > 60 else "content" if pet.happiness > 30 else "grumpy"
    title = f"{pet.name} — {mood}"
    return Panel(Align.center(Text(art, justify="center"), vertical="middle"), title=title, padding=(0,1))


def render_pet(pet: Pet) -> Table:
    # left: property table, right: creature panel
    left = Table(expand=True)
    left.add_column("Property")
    left.add_column("Value", justify="right")
    left.add_row("Name", pet.name)
    left.add_row("Hunger", f"{pet.hunger}/100")
    left.add_row("Happiness", f"{pet.happiness}/100")
    left.add_row("Energy", f"{pet.energy}/100")

    # outer grid: two columns (properties + creature)
    outer = Table.grid(expand=True)
    outer.add_column(ratio=2)
    outer.add_column(ratio=1)
    outer.add_row(left, render_creature(pet))
    return outer


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
