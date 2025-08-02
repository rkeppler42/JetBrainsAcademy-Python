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

</details>

---

<details>
<summary><strong>📌 Task 2 – Split the Bill</strong></summary>

### 📝 Description

It's time to split the bill! In this stage, your program will take the total bill, divide it equally among all friends, and update the dictionary created in Task 1 with the split values.

### 🎯 Objectives

1. Continue from Task 1.  
2. If there are **no friends**, output the same message as before.  
3. Otherwise:
   - Ask for the **total bill value**;
   - Split the bill equally among all friends;
   - **Round** the result to two decimal places;
   - Update the dictionary with the split values;
   - Print the updated dictionary.

### 💡 Example 1: Five People

```
Enter the number of friends joining (including you):
> 5
Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason
Enter the total bill value:
> 100
{'Marc': 20, 'Jem': 20, 'Monica': 20, 'Anna': 20, 'Jason': 20}
```

### 💡 Example 2: Seven People

```
Enter the number of friends joining (including you):
> 7
Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason
> Ben
> Ned
Enter the total bill value:
> 41
{'Marc': 5.86, 'Jem': 5.86, 'Monica': 5.86, 'Anna': 5.86, 'Jason': 5.86, 'Ben': 5.86, 'Ned': 5.86}
```

### 💡 Example 3: Invalid Input

```
Enter the number of friends joining (including you):
> 0
No one is joining for the party
```

</details>

---

<details>
<summary><strong>📌 Task 3 – Lucky One</strong></summary>

### 📝 Description

Time to add some fun! In this stage, your program will allow users to **randomly select one friend** who will not have to pay their share of the bill. Everyone else will cover the cost equally.

The feature is **optional** — users decide if they want to use it.

### 🎯 Objectives

1. Continue from the previous stage:
   - Handle invalid input (0 or negative friends) with:
     `No one is joining for the party`

2. Ask the user:
   `Do you want to use the "Who is lucky?" feature? Write Yes/No:`

3. Behavior:
   - If the user enters `Yes`:
     - Randomly select a friend;
     - Print: `{Name} is the lucky one!`
   - Otherwise:
     - Print: `No one is going to be lucky`

4. **Do not** print outputs from previous tasks again.

### 💡 Example 1: The feature is used

```
Enter the number of friends joining (including you):
> 5
Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason
Enter the total bill value:
> 100
Do you want to use the "Who is lucky?" feature? Write Yes/No:
> Yes

Jem is the lucky one!
```

### 💡 Example 2: The feature is skipped

```
Enter the number of friends joining (including you):
> 5
Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason
Enter the total bill value:
> 100
Do you want to use the "Who is lucky?" feature? Write Yes/No:
> No

No one is going to be lucky
```

### 💡 Example 3: Invalid Input

```
Enter the number of friends joining (including you):
> 0

No one is joining for the party
```

</details>
