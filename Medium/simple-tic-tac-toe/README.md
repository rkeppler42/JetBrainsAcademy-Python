# ❌ Simple Tic-Tac-Toe with Python

A small console-based **Python project** built as part of the **Hyperskill Python track**.  
The goal is to progressively build a fully functional Tic-Tac-Toe game — from printing a static grid to a complete two-player game with input validation and win detection.

---

## 🚀 Project Progress

- [ ] **Stage 1** — Welcome to the battlefield!
- [ ] **Stage 2** — The user is the gamemaster
- [ ] **Stage 3** — What's up on the field?
- [ ] **Stage 4** — First move!
- [ ] **Stage 5** — Fight!

---

## 📚 About the Stages

Each stage introduces a new concept and progressively expands the program — from printing a hardcoded grid to a complete interactive two-player game with state analysis and input validation.

---

<details>
<summary><strong>📌 Stage 1 — Welcome to the Battlefield!</strong></summary>

### 📝 Description

The first version of the program simply prints a static 3x3 tic-tac-toe grid to the console. No user input is required yet. A `for` loop must be used to iterate through the grid rows.

### 🎯 Objectives

- Print a 3x3 grid of `X`s and `O`s using a `for` loop.

### 💡 Example Output

```
X O X
O X O
X X O
```

</details>

---

<details>
<summary><strong>📌 Stage 2 — The User Is the Gamemaster</strong></summary>

### 📝 Description

The program now reads a 9-character string from the user and displays it as a formatted 3x3 grid with borders. The grid can contain `X`, `O`, and `_` symbols (where `_` represents an empty cell).

### 🎯 Objectives

1. Read a string of 9 symbols from user input (`X`, `O`, `_`);
2. Display the grid with:
   - A line of `---------` above and below the grid;
   - A pipe `|` at the beginning and end of each row;
   - A space between all characters.

### 💡 Examples

**Example 1:**

```
> O_OXXO_XX
---------
| O _ O |
| X X O |
| _ X X |
---------
```

**Example 2:**

```
> OXO__X_OX
---------
| O X O |
| _ _ X |
| _ O X |
---------
```

**Example 3:**

```
> _XO__X___
---------
| _ X O |
| _ _ X |
| _ _ _ |
---------
```

</details>

---

<details>
<summary><strong>📌 Stage 3 — What's Up on the Field?</strong></summary>

### 📝 Description

The program now analyzes the current game state after displaying the grid. It determines whether the game is still ongoing, ended in a draw, was won by a player, or represents an impossible state.

### 🎯 Objectives

1. Read a 9-character string and print the grid as in Stage 2;
2. Analyze the game state and print one of the following results:
   - `Game not finished` — no winner yet and empty cells remain;
   - `Draw` — no winner and no empty cells remain;
   - `X wins` — X has three in a row (including diagonals);
   - `O wins` — O has three in a row (including diagonals);
   - `Impossible` — both players have three in a row, or the difference between X count and O count is greater than 1.

### 💡 Examples

**Example 1: X wins**

```
> XXXOO__O_
---------
| X X X |
| O O _ |
| _ O _ |
---------
X wins
```

**Example 2: O wins**

```
> XOOOXOXXO
---------
| X O O |
| O X O |
| X X O |
---------
O wins
```

**Example 3: Draw**

```
> XOXOOXXXO
---------
| X O X |
| O O X |
| X X O |
---------
Draw
```

**Example 4: Game not finished**

```
> XO_OOX_X_
---------
| X O   |
| O O X |
|   X   |
---------
Game not finished
```

**Example 5: Impossible**

```
> XO_XO_XOX
---------
| X O _ |
| X O _ |
| X O X |
---------
Impossible
```

</details>

---

<details>
<summary><strong>📌 Stage 4 — First Move!</strong></summary>

### 📝 Description

The program becomes interactive. The user provides an initial board state and is then prompted to enter coordinates for their move as `X`. The program validates the input and updates the grid.

### 🎯 Objectives

1. Read the initial 9-character board state and display it;
2. Prompt the user to enter move coordinates (row and column, from 1 to 3);
3. Validate the input:
   - Print `You should enter numbers!` if the input is not numeric;
   - Print `Coordinates should be from 1 to 3!` if the coordinates are out of range;
   - Print `This cell is occupied! Choose another one!` if the cell is already taken;
4. Keep prompting until valid input is received;
5. Update the grid with the move and print the result.

### 💡 Examples

**Example 1: Valid move**

```
> _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
> 1 1
---------
| X X X |
| O O   |
| O X   |
---------
```

**Example 2: Occupied cell**

```
> _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
> 3 1
This cell is occupied! Choose another one!
> 1 1
---------
| X X X |
| O O   |
| O X   |
---------
```

**Example 3: Non-numeric input**

```
> _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
> one one
You should enter numbers!
> 1 1
---------
| X X X |
| O O   |
| O X   |
---------
```

**Example 4: Out of range**

```
> _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
> 4 1
Coordinates should be from 1 to 3!
> 1 1
---------
| X X X |
| O O   |
| O X   |
---------
```

</details>

---

<details>
<summary><strong>📌 Stage 5 — Fight!</strong></summary>

### 📝 Description

The final stage combines everything into a complete two-player game. The game starts with an empty grid, alternates turns between `X` and `O`, validates each move, and ends when a player wins or the game is a draw.

### 🎯 Objectives

1. Print an empty 3x3 grid at the start;
2. Run a game loop alternating between `X` and `O`;
3. Validate each move (non-numeric, out of range, occupied cell);
4. Update and print the grid after each valid move;
5. End the game and print the result when:
   - A player wins (`X wins` or `O wins`);
   - The game ends in a `Draw`.

### 💡 Example

```
---------
|       |
|       |
|       |
---------
> 2 2
---------
|       |
|   X   |
|       |
---------
> 1 1
---------
| O     |
|   X   |
|       |
---------
> 3 3
---------
| O     |
|   X   |
|     X |
---------
> 2 1
---------
| O     |
| O X   |
|     X |
---------
> 3 1
---------
| O     |
| O X   |
| X   X |
---------
> 2 3
---------
| O     |
| O X O |
| X   X |
---------
> 3 2
---------
| O     |
| O X O |
| X X X |
---------
X wins
```

</details>

---

## ▶️ How to Run

Make sure you have Python installed, then run:

```bash
python tic_tac_toe.py
```
