# ♟️ Python Chess Game

A text-based chess game built in Python as part of my **CSSE1001 coursework at the University of Queensland**.

The game allows two players to play chess through the terminal using standard chess coordinates such as `e2 e4`. It implements chess movement rules, move validation, check detection, checkmate, stalemate, and special chess moves.

---

## About the Project

This project was developed to practise fundamental Python programming concepts, including:

- Functions and modular programming
- Conditional statements and loops
- Tuples and string manipulation
- User input handling
- Game state management
- Move validation
- Testing and debugging

The chess board is represented using a tuple of eight strings. Each character represents either a chess piece or an empty square.

For example:

```text
rnbqkbnr
pppppppp
........
........
........
........
PPPPPPPP
RNBQKBNR
```

Uppercase characters represent **White's pieces**, while lowercase characters represent **Black's pieces**.

---

## Features

The game supports:

- Two-player chess through the terminal
- Standard chess piece movement
- Turn-based gameplay
- Move validation
- Piece capturing
- Check detection
- Checkmate detection
- Stalemate detection
- Pawn promotion
- Castling
- En passant
- Help command
- Quit confirmation

The program also prevents illegal moves, including moves that would leave the player's own king in check.

---

## How It Was Made

The project was written in **Python** and uses a text-based interface rather than a graphical interface.

The main game logic is contained in `a1.py`, while `a1_support.py` contains supporting functionality used by the game.

The program maintains the current state of the chess board and updates it after each valid move.

For each turn, the program:

1. Asks the current player for a move.
2. Converts chess coordinates into board positions.
3. Checks whether the selected piece belongs to the current player.
4. Validates the movement of the selected chess piece.
5. Checks whether the move would leave the player's king in check.
6. Updates the board if the move is valid.
7. Checks for check, checkmate, or stalemate.
8. Switches to the other player's turn.

---

## How to Run

### Requirements

- Python 3.12
- A terminal or code editor such as VS Code

### 1. Clone the Repository

Clone the repository using:

```bash
git clone YOUR_REPOSITORY_URL
```

Then enter the project folder:

```bash
cd YOUR_REPOSITORY_NAME
```

Alternatively, you can download the repository as a ZIP file and extract it.

### 2. Run the Game

Open the project folder in VS Code.

Open a terminal using:

**Terminal → New Terminal**

Then run:

```bash
python a1.py
```

On Windows, you can also use:

```bash
py a1.py
```

The chess board will appear in the terminal and White will be prompted to make the first move.

---

## How to Play

The game starts with the standard chess board:

```text
rnbqkbnr  8
pppppppp  7
........  6
........  5
........  4
........  3
PPPPPPPP  2
RNBQKBNR  1

abcdefgh
```

White moves first.

Moves are entered using standard chess coordinates in the following format:

```text
from_square to_square
```

For example, to move White's pawn from **e2** to **e4**:

```text
White's move: e2 e4
```

Black can then make a move:

```text
Black's move: e7 e5
```

After every valid move, the board is updated and displayed again.

---

## Board Coordinates

The columns are labelled:

```text
a b c d e f g h
```

The rows are numbered from `1` to `8`.

For example:

- `a1` is the bottom-left square from White's perspective.
- `e2` is White's king pawn starting position.
- `e8` is Black's king starting position.

A move such as:

```text
g1 f3
```

moves the piece currently located at `g1` to `f3`.

---

## Game Commands

### Help

Enter:

```text
h
```

or:

```text
H
```

to display the game's help information.

### Quit

Enter:

```text
q
```

or:

```text
Q
```

to quit the game.

The program will ask for confirmation before ending the game.

---

## Gameplay

The game follows a turn-based structure, beginning with White.

Each player enters a move using the starting and destination coordinates.

For example:

```text
White's move: e2 e4
Black's move: e7 e5
White's move: g1 f3
```

After a valid move, the board is updated and the turn switches to the other player.

### Invalid Moves

If an invalid move is entered, the game does not switch turns. Instead, the same player is asked to enter another move.

A move may be rejected if:

- The input format is incorrect.
- The selected square does not contain the current player's piece.
- The destination contains another piece belonging to the same player.
- The selected chess piece cannot legally move to the destination.
- Another piece is blocking the movement.
- The move would leave the player's own king in check.

---

### Check

A player is in **check** when their king is under attack by an opposing piece.

If the king is in check but the player still has a valid move to escape, the game informs the player that they are in check and gameplay continues.

Example:

```text
White is in check
```

The player must make a move that removes the threat to their king.

---

### Checkmate

A **checkmate** occurs when a player's king is in check and there are no valid moves available to escape the check.

When checkmate is detected, the game displays:

```text
Checkmate
```

The game then ends.

---

### Stalemate

A **stalemate** occurs when the current player is not in check but has no valid legal moves available.

When this occurs, the game displays:

```text
Stalemate
```

The game then ends.

---

### Special Moves

The game also implements several special chess moves.

### Pawn Promotion

When a pawn reaches the opposite end of the board, the player can promote the pawn to another piece.

The game asks the player which piece they would like:

```text
What piece would you like (q, n, r, b)?
```

The pawn can be promoted to a:

- Queen
- Knight
- Rook
- Bishop

### Castling

Castling is supported when the required conditions are satisfied.

This includes conditions such as:

- The king has not previously moved.
- The selected rook has not previously moved.
- There are no pieces between the king and rook.
- The relevant positions are not under attack.

The player performs castling by entering the king's move.

For example:

```text
e1 g1
```

### En Passant

The game also supports **en passant**.

This move can occur when an opposing pawn has just moved two squares from its starting position and the conditions for an en passant capture are satisfied.

---

## Project Structure

```text
python-chess-game/
│
├── a1.py
├── a1_support.py
├── gameplay/
│   └── example gameplay files
│
└── README.md
```

### `a1.py`

Contains the main implementation of the chess game, including:

- Board management
- User input
- Move processing
- Move validation
- Game state updates
- Check, checkmate, and stalemate handling
- Special chess moves

### `a1_support.py`

Contains supporting functions and constants used by the chess game.

### `gameplay/`

Contains example gameplay files that were used to test different game situations and expected behaviour.

---

## Technologies Used

**Python 3.12**

---

## What I Learned

Through this project, I gained experience with:

- Building a larger program using multiple functions
- Breaking complex game logic into smaller components
- Representing and updating application state
- Validating different types of user input
- Implementing rule-based logic
- Testing different gameplay scenarios
- Debugging Python programs
- Working with tuples, strings, loops, and conditional statements

One of the main challenges was implementing chess rules while making sure that each move was correctly validated before updating the board.

---

## Author

**Febriani Patricia**

Bachelor of Information Technology  
The University of Queensland
2024
