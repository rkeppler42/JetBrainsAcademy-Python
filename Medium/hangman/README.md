# 🪢 Hangman

A small console-based **Python project** built as part of the **Hyperskill Python track**.  
The goal is to progressively build the classic Hangman game — from a simple announcement to a fully functional game with a scoreboard, input validation, and a main menu.

---

## 🚀 Project Progress

- [x] **Stage 1** — Announcement
- [x] **Stage 2** — Let's play a game
- [x] **Stage 3** — Make your choice
- [x] **Stage 4** — Hints
- [x] **Stage 5** — Keep trying
- [ ] **Stage 6** — The value of life
- [ ] **Stage 7** — Error!
- [ ] **Stage 8** — Menu, please

---

## 📚 About the Stages

Each stage introduces a new concept and expands the program's functionality — from printing a greeting to a complete game with a scoreboard and seamless replay.

---

<details>
<summary><strong>📌 Stage 1 — Announcement</strong></summary>

### 📝 Description

The very first version of the game simply greets the player with an announcement. No input needed yet.

### 🎯 Objectives

- Print the game title and a coming-soon message.

### 💡 Example Output

```
H A N G M A N
The game will be available soon.
```

</details>

---

<details>
<summary><strong>📌 Stage 2 — Let's Play a Game</strong></summary>

### 📝 Description

The game now has simple gameplay. The computer has a single fixed word — `python` — and the player must guess it. Two outcomes are possible: win or lose.

### 🎯 Objectives

1. Ask the player to guess the word;
2. Print `You survived!` if they guess correctly;
3. Print `You lost!` otherwise.

### 💡 Examples

**Example 1:**

```
H A N G M A N
Guess the word: > python
You survived!
```

**Example 2:**

```
H A N G M A N
Guess the word: > java
You lost!
```

</details>

---

<details>
<summary><strong>📌 Stage 3 — Make Your Choice</strong></summary>

### 📝 Description

One word makes the game predictable. In this stage the computer picks a word at random from a list — adding replayability.

### 🎯 Objectives

1. Create a word list: `python`, `java`, `swift`, `javascript`;
2. Pick a word at random using the `random` module;
3. Ask the player to guess the full word;
4. Print `You survived!` or `You lost!` accordingly.

### 💡 Examples

**Example 1: computer chose `python`**

```
H A N G M A N
Guess the word: > python
You survived!
```

**Example 2: computer chose something else**

```
H A N G M A N
Guess the word: > python
You lost!
```

</details>

---

<details>
<summary><strong>📌 Stage 4 — Hints</strong></summary>

### 📝 Description

To make the game fairer, the computer now reveals the first three letters of the chosen word. The remaining letters are hidden with hyphens (`-`).

### 🎯 Objectives

1. Pick a word at random from the list;
2. Show the first three letters and replace the rest with `-`;
3. Ask the player to guess the full word;
4. Print the result.

### 💡 Examples

**Example 1:**

```
H A N G M A N
Guess the word jav-: > java
You survived!
```

**Example 2:**

```
H A N G M A N
Guess the word pyt---: > pythia
You lost!
```

</details>

---

<details>
<summary><strong>📌 Stage 5 — Keep Trying</strong></summary>

### 📝 Description

The game is now iterative. Instead of guessing the whole word, the player guesses one letter at a time. They have exactly eight attempts — whether they guess correctly or not.

### 🎯 Objectives

1. Hide the entire word with hyphens at the start;
2. Ask for one letter at a time with `Input a letter:`;
3. If the letter is in the word, reveal it;
4. If not, print `That letter doesn't appear in the word.` and reduce attempts;
5. After all eight attempts, print `Thanks for playing!`.

### 💡 Example

```
H A N G M A N

----------
Input a letter: > a

-a-a------
Input a letter: > o
That letter doesn't appear in the word.

-a-a------
Input a letter: > z
That letter doesn't appear in the word.

...

Thanks for playing!
```

</details>

---

<details>
<summary><strong>📌 Stage 6 — The Value of Life</strong></summary>

### 📝 Description

Now attempts only decrease when the player makes a mistake — guessing a wrong letter or repeating a previously guessed one. Win and lose conditions are properly implemented.

### 🎯 Objectives

1. Reduce attempts only on wrong or repeated guesses;
2. Print `That letter doesn't appear in the word.` for wrong guesses;
3. Print `No improvements.` for repeated correct guesses;
4. If the word is fully uncovered, print the word, `You guessed the word!`, and `You survived!`;
5. If attempts run out, print `You lost!`.

### 💡 Examples

**Example 1: loss**

```
H A N G M A N

------
Input a letter: > t

--t---
Input a letter: > z
That letter doesn't appear in the word.

--t---
Input a letter: > t
No improvements.

...

You lost!
```

**Example 2: win**

```
H A N G M A N

----
Input a letter: > j

j---
Input a letter: > a

ja-a
Input a letter: > v

java
You guessed the word!
You survived!
```

</details>

---

<details>
<summary><strong>📌 Stage 7 — Error!</strong></summary>

### 📝 Description

Input validation is added. Invalid inputs no longer cost the player an attempt. The win message is also updated to include the guessed word.

### 🎯 Objectives

Validate input in this order — none of these should reduce attempts:

| Situation                               | Message                                                       |
| --------------------------------------- | ------------------------------------------------------------- |
| Input is not a single character         | `Please, input a single letter.`                              |
| Input is not a lowercase English letter | `Please, enter a lowercase letter from the English alphabet.` |
| Letter already guessed (correct or not) | `You've already guessed this letter.`                         |

On win, print `You guessed the word <word>!` followed by `You survived!`.

### 💡 Example

```
H A N G M A N

----
Input a letter: > +
Please, enter a lowercase letter from the English alphabet.

----
Input a letter: > ii
Please, input a single letter.

----
Input a letter: > j

j---
Input a letter: > a

ja-a
Input a letter: > v
You guessed the word java!
You survived!
```

</details>

---

<details>
<summary><strong>📌 Stage 8 — Menu, Please</strong></summary>

### 📝 Description

The final stage adds a main menu that lets players replay, check their score, or exit — making the game seamlessly replayable.

### 🎯 Objectives

1. Show the menu prompt: `Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:`;
2. Re-show the menu on invalid input;
3. On `play`, start a game session; return to menu when finished;
4. On `results`, print wins and losses:
   - `You won: N times.`
   - `You lost: N times.`
5. On `exit`, terminate the program.

### 💡 Example

```
H A N G M A N
Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > play

...

You guessed the word python!
You survived!
Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > results
You won: 1 times.
You lost: 0 times.
Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > exit
```

</details>

---

## ▶️ How to Run

Make sure you have Python installed, then run:

```bash
python hangman.py
```
