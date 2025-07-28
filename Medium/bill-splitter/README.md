# 🍽️ Bill Splitter

A Python project that helps split a bill fairly between friends. This project explores data structures, input validation, and randomization through a series of interactive steps.

---

## ✅ Tasks Overview

This project is divided into multiple stages. Each task incrementally builds a complete bill-splitting assistant.

---

<details>
<summary><strong>📌 Task 1 – Create the Guest List</strong></summary>

### 📝 Description

You’ve planned a dinner with friends and want to manage the group in your program. In this stage, you’ll collect everyone’s name and store them in a dictionary for future use.

### 🎯 Objectives

1. Ask:  
   `Enter the number of friends joining (including you):`

2. If the number is **zero or negative**, print:  
   `No one is joining for the party`

3. Otherwise:
   - Prompt for names:  
     `Enter the name of every friend (including you), each on a new line:`
   - Read that many names from the user;
   - Store the names as keys in a dictionary, each with the value `0`;
   - Print the resulting dictionary.

### 💡 Example 1: Valid Input

```
Enter the number of friends joining (including you):
> 5
Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason

{'Marc': 0, 'Jem': 0, 'Monica': 0, 'Anna': 0, 'Jason': 0}
```

### 💡 Example 2: Invalid Input

```
Enter the number of friends joining (including you):
> 0
No one is joining the party
```