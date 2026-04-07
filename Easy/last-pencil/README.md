# ✏️ Last Pencil

A small console-based **Python project** built as part of the **Hyperskill Python track**.  
The goal is to progressively build a two-player pencil game where the player who takes the last pencil loses — and eventually face off against an unbeatable bot.

---

## 🚀 Project Progress

- [x] **Stage 1** — Print the pencils
- [x] **Stage 2** — Initial conditions
- [x] **Stage 3** — Take turns
- [x] **Stage 4** — Validation & winner
- [x] **Stage 5** — The bot

---

## 📚 About the Stages

Each stage introduces a new concept and expands the program's functionality — from simply printing pencils to implementing a bot that plays with a winning strategy.

---

<details>
<summary><strong>📌 Stage 1 — Print the Pencils</strong></summary>

### 📝 Description

You and your friend decided to play a simple pen-and-paper game, but you're out of paper! Your friend dumps all the pencils on the table and says: "Your turn!" This stage is about getting the game started — no input needed yet.

### 🎯 Objectives

- Print any number of vertical bar symbols (`|`) representing pencils;
- Print `Your turn!` on the next line.

### 💡 Example Output

```
||||||||
Your turn!
```

</details>

---

<details>
<summary><strong>📌 Stage 2 — Initial Conditions</strong></summary>

### 📝 Description

Instead of hardcoding the pencils, it's time to let the players set up the game. Ask how many pencils to use and who goes first, then display the starting state.

### 🎯 Objectives

1. Ask for the number of pencils with `How many pencils would you like to use:`;
2. Ask who goes first with `Who will be the first (Name1, Name2):`;
3. Print the pencils as vertical bars;
4. Print `{Name} is going first!`.

### 💡 Examples

**Example 1:**

```
How many pencils would you like to use:
> 5
Who will be the first (John, Jack):
> John
|||||
John is going first!
```

**Example 2:**

```
How many pencils would you like to use:
> 20
Who will be the first (John, Jack):
> Jack
||||||||||||||||||||
Jack is going first!
```

</details>

---

<details>
<summary><strong>📌 Stage 3 — Take Turns</strong></summary>

### 📝 Description

The game is now playable! Players alternate turns, each removing pencils from the table. The game ends as soon as no pencils remain.

### 🎯 Objectives

1. Loop through turns, alternating between players;
2. Each iteration prints the remaining pencils and `{Name}'s turn:`;
3. Read the number of pencils the current player takes;
4. If no pencils remain after a move, break the loop — no additional output.

### 💡 Examples

**Example 1:**

```
How many pencils would you like to use:
> 5
Who will be the first (John, Jack):
> John
|||||
John's turn:
> 2
|||
Jack's turn:
> 1
||
John's turn:
> 2
```

**Example 2:**

```
How many pencils would you like to use:
> 15
Who will be the first (John, Jack):
> John
|||||||||||||||
John's turn:
> 8
|||||||
Jack's turn:
> 7
```

</details>

---

<details>
<summary><strong>📌 Stage 4 — Validation & Winner</strong></summary>

### 📝 Description

No more cheating! This stage adds full input validation and determines the winner. Players can only take 1, 2, or 3 pencils per turn, and the player who takes the last pencil loses.

### 🎯 Objectives

Validate the following and re-prompt on error:

| Situation                      | Message                                    |
| ------------------------------ | ------------------------------------------ |
| Initial pencils not numeric    | `The number of pencils should be numeric`  |
| Initial pencils equal to 0     | `The number of pencils should be positive` |
| First player name invalid      | `Choose between 'Name1' and 'Name2'`       |
| Pencils taken not 1, 2, or 3   | `Possible values: '1', '2' or '3'`         |
| Pencils taken exceed remaining | `Too many pencils were taken`              |

After the game ends, print `{Winner} won!`

### 💡 Examples

**Example 1: Non-numeric input**

```
How many pencils would you like to use:
> a
The number of pencils should be numeric
> 5
Who will be the first (John, Jack):
>
```

**Example 2: Zero pencils**

```
How many pencils would you like to use:
> 0
The number of pencils should be positive
> 20
Who will be the first (John, Jack):
>
```

**Example 3: Invalid player name**

```
How many pencils would you like to use:
> 5
Who will be the first (John, Jack):
> JohnJack
Choose between 'John' and 'Jack'
> John
|||||
John's turn!
>
```

**Example 4: John wins**

```
How many pencils would you like to use:
> 5
Who will be the first (John, Jack):
> John
|||||
John's turn!
> 3
||
Jack's turn!
> 3
Too many pencils were taken
> 2
John won!
```

</details>

---

<details>
<summary><strong>📌 Stage 5 — The Bot</strong></summary>

### 📝 Description

Time to face a worthy opponent! The second player (Jack) is now a bot that follows a mathematically optimal winning strategy. The key insight: if the number of pencils is a multiple of 4, the current player is in a losing position — no matter what they do.

**Bot strategy:**

| Pencils on table                   | Bot's move         |
| ---------------------------------- | ------------------ |
| Multiple of 4 (losing position)    | Random: 1, 2, or 3 |
| Multiple of 4 + 1 (e.g. 2, 6, 10…) | Takes 1            |
| Multiple of 4 + 2 (e.g. 3, 7, 11…) | Takes 2            |
| Multiple of 4 + 3 (e.g. 4, 8, 12…) | Takes 3            |

### 🎯 Objectives

1. Jack is always the bot — if it's Jack's turn, no input is required;
2. Print the bot's move (1, 2, or 3) as output;
3. Apply the winning strategy when in a winning position;
4. Take any number randomly when in a losing position.

### 💡 Examples

**Example 1: Jack goes first**

```
How many pencils would you like to use:
> 10
Who will be the first (John, Jack):
> Jack
||||||||||
Jack's turn:
1
|||||||||
John's turn!
> 2
|||||||
Jack's turn:
2
|||||
John's turn!
> 1
||||
Jack's turn:
3
|
John's turn!
> 1
Jack won!
```

**Example 2: John goes first**

```
How many pencils would you like to use:
> 6
Who will be the first (John, Jack):
> John
||||||
John's turn!
> 1
|||||
Jack's turn:
2
|||
John's turn!
> 2
|
Jack's turn:
1
John won!
```

</details>

---

## ▶️ How to Run

Make sure you have Python installed, then run:

```
python last_pencil.py
```
