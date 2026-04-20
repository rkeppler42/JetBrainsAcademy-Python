# 🁣 Dominoes

A console-based **Python project** built as part of the **Hyperskill Python track**.  
The goal is to progressively build a fully playable domino game against the computer — from setting up the pieces to implementing a smart AI opponent.

---

## 🚀 Project Progress

- [x] **Stage 1** — Setting Up the Game
- [ ] **Stage 2** — The Interface
- [ ] **Stage 3** — Playing the Game
- [ ] **Stage 4** — Enforcing Rules
- [ ] **Stage 5** — The AI

---

## 📚 About the Stages

Each stage introduces a new concept and expands the program's functionality — from generating and distributing domino pieces to building an AI that makes educated decisions based on basic statistics.

---

<details>
<summary><strong>📌 Stage 1 — Setting Up the Game</strong></summary>


### 📝 Description

Before the game begins, the full set of 28 unique domino pieces must be generated, randomly distributed between the players and the stock, and the starting piece must be determined. The player with the highest double donates it as the starting piece; their opponent goes first. If no one has a double, the pieces are reshuffled and redistributed.

### 🎯 Objectives

1. Generate a full domino set of 28 unique pieces, each represented as a list of two numbers (0–6).
2. Split the set randomly into: **Stock** (14 pieces), **Computer** (7 pieces), and **Player** (7 pieces).
3. Determine the starting piece (highest double) and the first player. Adjust the piece counts accordingly.
4. If no double exists, reshuffle and redistribute until one is found.
5. Output all five variables.

### 💡 Examples

**Example 1: Player goes first**

```
Stock pieces: [[2, 5], [1, 2], [3, 6], [0, 0], [0, 2], [5, 6], [3, 5], [2, 4], [3, 4], [1, 5], [0, 4], [2, 6], [3, 3], [1, 1]]
Computer pieces: [[1, 4], [1, 3], [2, 3], [4, 5], [2, 2], [0, 3]]
Player pieces: [[0, 6], [5, 5], [4, 4], [4, 6], [0, 1], [0, 5], [1, 6]]
Domino snake: [[6, 6]]
Status: player
```

**Example 2: Computer goes first**

```
Stock pieces: [[2, 6], [3, 4], [5, 6], [0, 5], [1, 2], [4, 6], [2, 3], [0, 6], [0, 0], [6, 6], [2, 4], [2, 2], [0, 1], [3, 3]]
Computer pieces: [[0, 2], [3, 6], [4, 4], [3, 5], [1, 5], [0, 3], [2, 5]]
Player pieces: [[1, 3], [1, 4], [4, 5], [1, 6], [1, 1], [0, 4]]
Domino snake: [[5, 5]]
Status: computer
```

</details>

---

<details>
<summary><strong>📌 Stage 2 — The Interface</strong></summary>


### 📝 Description

With the setup logic in place, it's time to build a user-friendly interface. The player can see the domino snake, their own pieces (enumerated), and basic information about the stock and the computer. The computer's actual pieces remain hidden — only the count is shown.

### 🎯 Objectives

1. Print a header of seventy `=` characters.
2. Print `Stock size: [number]`.
3. Print `Computer pieces: [number]`.
4. Print the domino snake.
5. Print `Your pieces:` followed by each piece on its own line, enumerated starting from 1.
6. Print the game status:
   - `Status: It's your turn to make a move. Enter your command.` — if `status = "player"`.
   - `Status: Computer is about to make a move. Press Enter to continue...` — if `status = "computer"`.

### 💡 Examples

**Example 1: Player's turn**

```
======================================================================
Stock size: 14
Computer pieces: 6

[6, 6]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[4, 6]
5:[0, 1]
6:[0, 5]
7:[1, 6]

Status: It's your turn to make a move. Enter your command.
```

**Example 2: Computer's turn**

```
======================================================================
Stock size: 14
Computer pieces: 7

[5, 5]

Your pieces:
1:[1, 3]
2:[1, 4]
3:[4, 5]
4:[1, 6]
5:[1, 1]
6:[0, 4]

Status: Computer is about to make a move. Press Enter to continue...
```

</details>

---

<details>
<summary><strong>📌 Stage 3 — Playing the Game</strong></summary>


### 📝 Description

The game comes to life with a full game loop. Players alternate turns until an end-game condition is met. Moves are represented as integers: a positive number places the domino on the right side of the snake, a negative number places it on the left, and `0` draws from the stock (or skips if the stock is empty). At this stage there are no placement rules — pieces can be placed freely. The computer picks a random valid move.

### 🎯 Objectives

1. Add a game loop that repeats until the game ends.
2. On each iteration, display the current interface (Stage 2).
3. On the player's turn: prompt for an integer move. If input is invalid (non-integer or out of range), print `Invalid input. Please try again.` and prompt again.
4. On the computer's turn: prompt the user to press Enter, then generate a random move between `-computer_size` and `computer_size`.
5. Apply the move and switch turns.
6. If the snake exceeds six dominoes, display only the first and last three, separated by `...`.
7. Print the appropriate end-game status:
   - `Status: The game is over. You won!`
   - `Status: The game is over. The computer won!`
   - `Status: The game is over. It's a draw!`

The draw condition is met when both ends of the snake show the same number and that number appears 8 times across the snake.

### 💡 Examples

**Example 1: Typical gameplay**

```
======================================================================
Stock size: 14
Computer pieces: 6

[6, 6]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[4, 6]
5:[0, 1]
6:[0, 5]
7:[1, 6]

Status: It's your turn to make a move. Enter your command.
> 4
======================================================================
Stock size: 14
Computer pieces: 6

[6, 6][4, 6]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[0, 1]
5:[0, 5]
6:[1, 6]

Status: Computer is about to make a move. Press Enter to continue...
>
```

**Example 2: Invalid input**

```
Status: It's your turn to make a move. Enter your command.
> Hello
Invalid input. Please try again.
>
```

**Example 3: Snake truncation**

```
======================================================================
Stock size: 7
Computer pieces: 4

[6, 6][6, 3][3, 0]...[4, 2][2, 3][3, 6]

Your pieces:
1:[0, 0]
2:[1, 2]
3:[5, 5]

Status: It's your turn to make a move. Enter your command.
```

**Example 4: Player wins**

```
Status: It's your turn to make a move. Enter your command.
> 1
======================================================================
Stock size: 13
Computer pieces: 2

[3, 5][2, 2][6, 6]...[0, 3][3, 4][4, 4]

Your pieces:

Status: The game is over. You won!
```

</details>

---

<details>
<summary><strong>📌 Stage 4 — Enforcing Rules</strong></summary>


### 📝 Description

Every domino game has rules. Two neighboring pieces in the snake must share a matching number at their touching ends. This stage introduces validation for the player's moves and correct domino orientation for both players. The computer still picks randomly but now only from legal moves.

### 🎯 Objectives

1. When it's the player's turn:
   - Verify that the chosen domino contains the number at the corresponding end of the snake.
   - If not, print `Illegal move. Please try again.` and prompt again.
   - Place the domino with the correct orientation so that matching numbers are neighbors.
2. When it's the computer's turn:
   - Randomly try moves until a legal one is found.
   - Skipping (`0`) is always legal.
   - Place the domino with the correct orientation.

### 💡 Examples

**Example 1: Illegal move**

```
======================================================================
Stock size: 14
Computer pieces: 6

[6, 6]

Your pieces:
1:[0, 5]
2:[1, 5]
3:[2, 4]
4:[2, 6]
5:[0, 1]
6:[1, 6]
7:[5, 6]

Status: It's your turn to make a move. Enter your command.
> 5
Illegal move. Please try again.
>
```

**Example 2: Legal move with orientation correction**

```
Status: It's your turn to make a move. Enter your command.
> 7
======================================================================
Stock size: 14
Computer pieces: 6

[6, 6][6, 1]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[4, 6]
5:[0, 1]
6:[0, 5]

Status: Computer is about to make a move. Press Enter to continue...
>
```

</details>

---

<details>
<summary><strong>📌 Stage 5 — The AI</strong></summary>


### 📝 Description

Random choices are replaced with a score-based AI. The computer evaluates each domino in its hand by counting how often each number appears across its own pieces and the snake. Higher-frequency numbers yield higher scores. The AI always attempts to play the highest-scoring legal domino; if none can be played, it draws from the stock (or skips).

### 🎯 Objectives

Replace the random move generator with the following algorithm:

1. Count the occurrences of each number (0–6) across the computer's hand and the snake.
2. Score each domino as the sum of the occurrence counts of its two numbers.
3. Sort dominoes by score in descending order.
4. Try each domino (highest score first) on both sides of the snake. Play the first legal move found.
5. If no domino can be legally placed, draw from the stock or skip the turn.

### 💡 Examples

**Example 1: Computer plays a domino**

```
======================================================================
Stock size: 12
Computer pieces: 3

[4, 4][4, 2][2, 1][1, 0][0, 0][0, 2]

Your pieces:
1:[2, 2]
2:[3, 3]
3:[5, 5]
4:[6, 6]
5:[4, 5]
6:[3, 6]
7:[5, 6]

Status: Computer is about to make a move. Press Enter to continue...
>
======================================================================
Stock size: 12
Computer pieces: 2

[4, 4][4, 2][2, 1]...[0, 0][0, 2][2, 5]

Your pieces:
1:[2, 2]
...

Status: It's your turn to make a move. Enter your command.
```

**Example 2: Computer skips the turn**

```
Status: Computer is about to make a move. Press Enter to continue...
>
======================================================================
Stock size: 11
Computer pieces: 4

[4, 4][4, 2][2, 1][1, 0][0, 0][0, 2]

Your pieces:
...

Status: It's your turn to make a move. Enter your command.
```

</details>

---

## ▶️ How to Run

Make sure you have Python installed, then run:

```bash
python dominoes.py
```
