# Alien Invasion

## Author

Miles Wanner

## Project Description

Alien Invasion is a 2D game built with Python and Pygame. For Track 1: Custom Game Mechanics, the original Alien Invasion gameplay is being redesigned into a side-scrolling format. The player controls a ship positioned along the left edge of the screen, moves it up and down, and fires bullets horizontally toward the right side of the screen.

This project reinforces object-oriented programming, event handling, collision detection, game states, scoring, and version-control practices.

## Controls

- Up Arrow: Move the ship up

- Down Arrow: Move the ship down

- Spacebar: Fire a bullet

- Q: Quit the game

- Mouse: Click the Play button to start or restart the game

## Final Project — Chosen Track

For my Final Project, I chose Track 1: Custom Game Mechanics. This track changes the ship's orientation, movement, projectile direction, alien behavior, and loss conditions.

### Milestone 1 — New Ship Mechanics

For Milestone 1, I changed the ship so it:

- Faces east toward the right side of the screen

- Starts along the left edge of the game window

- Moves vertically using the Up and Down Arrow keys

- Fires bullets horizontally from its right side

I also updated the display caption, used pathlib for asset paths, added complete docstrings and type hints, and maintained small, meaningful commits throughout development.

### Milestone 2 — Fleet and Collision Logic

For Milestone 2, I plan to update the alien fleet so it is consistent with the side-scrolling mechanics. The aliens will spawn toward the right side of the screen and move west toward the player's ship. Bullet-alien collisions will continue to remove aliens, and the loss conditions will be updated so the player loses a life when:

- An alien collides with the ship

- An alien reaches the edge behind the ship

### Final Submission — UI and Game States

For the final submission, I plan to complete the game with:

- A Play button

- Active and inactive game states

- A HUD showing score, high score, level, and lives remaining

- A hidden mouse cursor while the game is active

- Finalized side-scrolling fleet behavior and loss conditions

## Installation

Install the required dependency with:

```text
pip install -r requirements.txt
```

## Running the Game

Run the main game file with:

```text
python alien_invasion.py
```

## Starter Code

This project was adapted from the Alien Invasion starter repository provided for the course:

https://github.com/RedBeard41/alien_Invasion_starter