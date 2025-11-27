import os
import sys
import time

# Use the local src/ for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from virtual_pet.pet import Pet
from virtual_pet.cli import console, render_pet, show_animation
from rich.live import Live


def demo():
    pet = Pet('DemoInteractive', hunger=40, happiness=55, energy=60)

    console.rule('[bold cyan]Automated Demo — Watch the animations[/bold cyan]')
    with Live(render_pet(pet), refresh_per_second=8, transient=False, console=console) as live:
        console.print('\nStarting actions: feed, play, rest...')

        # Feed
        time.sleep(0.6)
        show_animation('Feeding...', seconds=1.2)
        pet.feed(25)
        live.update(render_pet(pet))

        # Play
        time.sleep(0.6)
        show_animation('Playing...', seconds=1.6)
        pet.play(20)
        live.update(render_pet(pet))

        # Rest
        time.sleep(0.6)
        show_animation('Resting...', seconds=1.2)
        pet.rest(35)
        live.update(render_pet(pet))

        console.print('\nDemo finished — pet status shown above.')


if __name__ == '__main__':
    demo()
