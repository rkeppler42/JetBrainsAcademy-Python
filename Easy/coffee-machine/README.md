# ☕ Coffee Machine

A small console-based **Python project** built as part of the **Hyperskill Python track**.  
The goal is to progressively simulate a real coffee machine — from brewing a single cup to a fully object-oriented machine that manages supplies, accepts payments, and handles multiple actions through a state machine.

---

## 🚀 Project Progress

- [x] **Stage 1** — Making coffee
- [x] **Stage 2** — Ingredient calculator
- [x] **Stage 3** — Estimate the number of servings
- [x] **Stage 4** — Buy, fill, take!
- [x] **Stage 5** — Keep track of the supplies
- [x] **Stage 6** — Brush up your code

---

## 📚 About the Stages

Each stage introduces a new concept and expands the program's functionality — from printing a fixed sequence of steps to a fully object-oriented coffee machine driven by a state machine.

---

<details>
<summary><strong>📌 Stage 1 — Making Coffee</strong></summary>

### 📝 Description

The first version of the program simply simulates making a cup of coffee by printing each step of the process. No input needed yet.

### 🎯 Objectives

- Print each step of the coffee-making process to the console.

### 💡 Example Output

```
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
```

</details>

---

<details>
<summary><strong>📌 Stage 2 — Ingredient Calculator</strong></summary>

### 📝 Description

Now the machine scales up. Given the number of cups a user wants, the program calculates the exact amount of each ingredient needed. One cup requires 200 ml of water, 50 ml of milk, and 15 g of coffee beans.

### 🎯 Objectives

1. Ask the user how many cups of coffee they need;
2. Calculate the required amounts of water, milk, and coffee beans;
3. Print the results.

### 💡 Examples

**Example 1:**

```
Write how many cups of coffee you will need:
> 25
For 25 cups of coffee you will need:
5000 ml of water
1250 ml of milk
375 g of coffee beans
```

**Example 2:**

```
Write how many cups of coffee you will need:
> 125
For 125 cups of coffee you will need:
25000 ml of water
6250 ml of milk
1875 g of coffee beans
```

</details>

---

<details>
<summary><strong>📌 Stage 3 — Estimate the Number of Servings</strong></summary>

### 📝 Description

A real coffee machine has limited supplies. This stage checks whether the machine has enough resources to fulfill the user's request and reports accordingly.

### 🎯 Objectives

1. Ask the user for the current amounts of water, milk, and coffee beans;
2. Ask how many cups they want;
3. Output one of three responses:
   - `"Yes, I can make that amount of coffee"` — if supplies are exactly enough;
   - `"Yes, I can make that amount of coffee (and even N more than that)"` — if there are leftovers;
   - `"No, I can make only N cups of coffee"` — if supplies fall short.

### 💡 Examples

**Example 1: Exact amount**

```
Write how many ml of water the coffee machine has:
> 300
Write how many ml of milk the coffee machine has:
> 65
Write how many grams of coffee beans the coffee machine has:
> 100
Write how many cups of coffee you will need:
> 1
Yes, I can make that amount of coffee
```

**Example 2: Not enough**

```
Write how many ml of water the coffee machine has:
> 500
Write how many ml of milk the coffee machine has:
> 250
Write how many grams of coffee beans the coffee machine has:
> 200
Write how many cups of coffee you will need:
> 10
No, I can make only 2 cups of coffee
```

**Example 3: More than enough**

```
Write how many ml of water the coffee machine has:
> 1550
Write how many ml of milk the coffee machine has:
> 299
Write how many grams of coffee beans the coffee machine has:
> 300
Write how many cups of coffee you will need:
> 3
Yes, I can make that amount of coffee (and even 2 more than that)
```

</details>

---

<details>
<summary><strong>📌 Stage 4 — Buy, Fill, Take!</strong></summary>

### 📝 Description

The machine now supports three actions: buying coffee, refilling supplies, and collecting money. Each drink type has specific ingredient requirements and a price.

| Drink      | Water  | Milk   | Beans | Price |
| ---------- | ------ | ------ | ----- | ----- |
| Espresso   | 250 ml | —      | 16 g  | $4    |
| Latte      | 350 ml | 75 ml  | 20 g  | $7    |
| Cappuccino | 200 ml | 100 ml | 12 g  | $6    |

The machine starts with: 400 ml water, 540 ml milk, 120 g beans, 9 cups, $550.

### 🎯 Objectives

1. Print the machine's current state;
2. Ask the user for an action: `buy`, `fill`, or `take`;
3. Execute the action and print the updated state.

### 💡 Examples

**Example 1: Buy cappuccino**

```
Write action (buy, fill, take):
> buy
What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:
> 3

The coffee machine has:
200 ml of water
440 ml of milk
108 g of coffee beans
8 disposable cups
$556 of money
```

**Example 2: Take money**

```
Write action (buy, fill, take):
> take
I gave you $550

The coffee machine has:
400 ml of water
540 ml of milk
120 g of coffee beans
9 disposable cups
$0 of money
```

</details>

---

<details>
<summary><strong>📌 Stage 5 — Keep Track of the Supplies</strong></summary>

### 📝 Description

The machine now runs in a loop, accepting multiple actions until the user types `"exit"`. Two new commands are introduced: `"remaining"` to display current supplies, and `"back"` to cancel a purchase and return to the main menu. The machine also checks if it has enough resources before making coffee.

### 🎯 Objectives

1. Run a loop accepting `buy`, `fill`, `take`, `remaining`, and `exit`;
2. On `remaining`, display all current supplies;
3. On `buy`, allow the user to type `back` to return to the main menu;
4. If resources are insufficient, print which ingredient is missing;
5. Terminate on `exit`.

### 💡 Example

```
Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
400 ml of water
540 ml of milk
120 g of coffee beans
9 disposable cups
$550 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
Sorry, not enough water!

Write action (buy, fill, take, remaining, exit):
> exit
```

</details>

---

<details>
<summary><strong>📌 Stage 6 — Brush Up Your Code</strong></summary>

### 📝 Description

The final stage is a full refactor into an object-oriented design. The coffee machine is represented as a class with a state machine that interprets user input differently depending on the current state — whether the machine is idle, processing a purchase, or being refilled.

### 🎯 Objectives

1. Create a `CoffeeMachine` class with attributes: `water`, `milk`, `beans`, `cups`, and `money`;
2. Implement a single input-handling method that interprets input based on the machine's current state;
3. Use constants or an inner class to represent the machine's states;
4. Keep the main loop outside the class — it handles all I/O and passes input to the machine;
5. Wrap the main loop in `if __name__ == '__main__':`.

### 🗂️ Class Structure

| Member               | Type            | Description                           |
| -------------------- | --------------- | ------------------------------------- |
| `state`              | `State`         | Current state of the machine          |
| `water`              | `int`           | Water available in ml                 |
| `milk`               | `int`           | Milk available in ml                  |
| `beans`              | `int`           | Coffee beans available in g           |
| `cups`               | `int`           | Disposable cups available             |
| `money`              | `int`           | Money collected in $                  |
| `process_input()`    | public method   | Single entry point for all user input |
| `_handle_main()`     | private method  | Handles main menu commands            |
| `_handle_buy()`      | private method  | Handles coffee selection              |
| `_handle_fill_*()`   | private methods | Handles each fill step                |
| `_check_resources()` | private method  | Validates resource availability       |
| `_status()`          | private method  | Returns current machine status        |

### 🔄 State Machine

The `State` inner class defines the following states:

| State        | Description                       |
| ------------ | --------------------------------- |
| `MAIN`       | Waiting for a main menu command   |
| `BUY`        | Waiting for coffee type selection |
| `FILL_WATER` | Waiting for water amount          |
| `FILL_MILK`  | Waiting for milk amount           |
| `FILL_BEANS` | Waiting for beans amount          |
| `FILL_CUPS`  | Waiting for cups amount           |
| `EXIT`       | Termination signal                |

**Transitions:**

- `MAIN` → `BUY` on input `"buy"`
- `MAIN` → `FILL_WATER` on input `"fill"`
- `FILL_WATER` → `FILL_MILK` → `FILL_BEANS` → `FILL_CUPS` → `MAIN`
- `BUY` → `MAIN` after valid purchase or `"back"`
- `MAIN` → `EXIT` on input `"exit"`

### 💡 Example

```
Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
400 ml of water
540 ml of milk
120 g of coffee beans
9 disposable cups
$550 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
> exit
```

</details>

---

## ▶️ How to Run

Make sure you have Python installed, then run:

```bash
python coffee_machine.py
```
