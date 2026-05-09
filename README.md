# Asteroids

A playable clone of the classic Asteroids arcade game, built in Python with Pygame.

## What it does
- A triangular player ship spawns in the center of the screen
- Asteroids continuously spawn from the edges and drift across the screen
- Shooting an asteroid splits it into two smaller ones; small asteroids are destroyed completely
- Colliding with any asteroid ends the game
- Runs at 60 FPS with delta-time movement for smooth, frame-rate-independent physics

## Setup
1. Clone the repo
2. Install dependencies:
```bash
uv sync
```
3. Run the game:
```bash
uv run main.py
```

## How to play
| Key | Action |
|---|---|
| `W` | Thrust forward |
| `S` | Thrust backward |
| `A` | Rotate left |
| `D` | Rotate right |
| `Space` | Shoot |

Shoot asteroids to split them into smaller pieces. Don't let them hit you — it's game over instantly.

## What I learned
- Game loop fundamentals — input, update, draw
- Delta-time physics for frame-rate-independent movement
- Object-oriented design with inheritance (`CircleShape` as a base class for `Player`, `Asteroid`, and `Shot`)
- Pygame sprite groups for managing entities
- 2D vector math for movement, rotation, and collision detection
