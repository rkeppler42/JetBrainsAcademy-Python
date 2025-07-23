# 🛒 Corner Shop Calculator

A beginner-friendly console program simulating a corner shop’s earnings and net income over time.

---

## ✅ Tasks Overview

This project is divided into three progressive tasks. Each task builds upon the previous one.

---

<details>
<summary><strong>📌 Task 1 – Display Item Prices</strong></summary>

### 📝 Description

You've just opened a small corner shop. It offers only a few products: bubblegum, toffee, ice cream, milk chocolate, doughnuts, and pancakes.

### 🎯 Objectives

- Print a line with: `Prices:`
- Print the item names and their corresponding prices, following the format below.

### 💡 Example Output

```
Prices:
Bubblegum: $2
Toffee: $0.2
Ice cream: $5
Milk chocolate: $4
Doughnut: $2.5
Pancake: $3.2
```

</details>

---

<details>
<summary><strong>📌 Task 2 – Calculate Monthly Income</strong></summary>

### 📝 Description

One month later, you know how much each item earned. Use the table below to calculate the total income for the period.

| Item            | Earned |
|-----------------|--------:|
| Bubblegum       | $202    |
| Toffee          | $118    |
| Ice cream       | $2250   |
| Milk chocolate  | $1680   |
| Doughnut        | $1075   |
| Pancake         | $80     |

### 🎯 Objectives

1. Print a line with: `Earned amount:`
2. Print the item names and earned amounts
3. Print the total income in the format: `Income: $<total>`

### 💡 Example Output

```
Earned amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80

Income: $5405
```
</details>

---

<details>
<summary><strong>📌 Task 3 – Calculate Net Income</strong></summary>

### 📝 Description

Finally, let’s calculate your shop’s **net income**. Ask the user for expenses and subtract them from the total income.

### 🎯 Objectives

1. Reuse the earnings output from Task 2
2. Prompt the user for:
   - `Staff expenses:`
   - `Other expenses:`
3. Calculate and print the net income using the format: `Net income: $<amount>`

### 💡 Example Output 1



```
Earned amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80

Income: $5405
Staff expenses:
> 2000
Other expenses:
> 205
Net income: $3200
```

### 💡 Example Output 2 (Negative Result)

```
Earned amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80

Income: $5405
Staff expenses:
> 5203
Other expenses:
> 400
Net income: $-198
```
</details>

---

## ▶️ How to Run

Make sure you have Python installed, then run:

```bash
python corner_shop_calculator.py
```