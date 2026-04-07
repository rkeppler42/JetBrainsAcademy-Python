# 🍽️ Bill Splitter

A small console-based **Python project** built as part of the **Hyperskill Python track**.  
The goal is to progressively build a program that splits a restaurant bill among friends — with a fun twist: one lucky person might not have to pay at all.

---

## 🚀 Project Progress

- [x] **Stage 1** — Build the friends dictionary
- [x] **Stage 2** — Split the bill
- [x] **Stage 3** — Who is lucky?
- [x] **Stage 4** — Update the dictionary

---

## 📚 About the Stages

Each stage introduces a new concept and expands the program's functionality — from storing names in a dictionary to randomly selecting a lucky friend who gets a free meal.

---

<details>
<summary><strong>📌 Stage 1 — Build the Friends Dictionary</strong></summary>

### 📝 Description

Before splitting anything, you need to know who's coming to dinner. This stage is about collecting names from user input and storing them in a dictionary initialized with zeros — one entry per friend.

### 🎯 Objectives

1. Ask the user how many people are joining (including themselves);
2. If the number is zero or negative, print `"No one is joining for the party"`;
3. Otherwise, collect each friend's name iteratively;
4. Store all names in a dictionary with `0` as the initial value;
5. Print the resulting dictionary.

### 💡 Examples

**Example 1: Valid input**

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

**Example 2: Invalid input**

```
Enter the number of friends joining (including you):
> 0

No one is joining for the party
```

**Example 3: Invalid input**

```
Enter the number of friends joining (including you):
> -1

No one is joining for the party
```

</details>

---

<details>
<summary><strong>📌 Stage 2 — Split the Bill</strong></summary>

### 📝 Description

Time to settle up! This stage adds bill input and divides it equally among all friends. To keep things practical, the split amount is rounded to two decimal places and stored back into the dictionary.

### 🎯 Objectives

1. If the number of friends is invalid, print `"No one is joining for the party"`;
2. Otherwise, ask the user for the total bill amount;
3. Divide the bill equally among all friends;
4. Round the result to two decimal places;
5. Update all dictionary values with the split amount;
6. Print the updated dictionary.

### 💡 Examples

**Example 1: Five people joining**

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

**Example 2: Seven people, uneven split**

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

</details>

---

<details>
<summary><strong>📌 Stage 3 — Who is Lucky?</strong></summary>

### 📝 Description

Make it a lucky day for someone! This stage introduces an optional feature that randomly picks one friend from the dictionary — their share will be covered by the others. The user chooses whether to activate this feature or not.

### 🎯 Objectives

1. If the number of friends is invalid, print `"No one is joining for the party"`;
2. Otherwise, ask the user whether they want to use the `"Who is lucky?"` feature;
3. If the answer is `Yes`, randomly select a name from the dictionary keys;
4. Print `"{Name} is the lucky one!"`;
5. If the answer is anything else, print `"No one is going to be lucky"`.

### 💡 Examples

**Example 1: Feature activated**

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

**Example 2: Feature skipped**

```
Do you want to use the "Who is lucky?" feature? Write Yes/No:
> No

No one is going to be lucky
```

</details>

---

<details>
<summary><strong>📌 Stage 4 — Update the Dictionary</strong></summary>

### 📝 Description

The final stage ties everything together. If the lucky feature is used, the bill is recalculated among the remaining `n-1` friends and the lucky person's share is set to `0`. If the feature is skipped, the original split is printed instead.

### 🎯 Objectives

1. If the number of friends is invalid, print `"No one is joining for the party"`;
2. If the user chose `Yes`, recalculate the split for `n-1` friends;
3. Round the new split value to two decimal places;
4. Set the lucky person's value to `0` and update everyone else;
5. Print the updated dictionary;
6. If the user chose anything other than `Yes`, print the original dictionary.

### 💡 Examples

**Example 1: Feature activated**

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

{'Marc': 25, 'Jem': 0, 'Monica': 25, 'Anna': 25, 'Jason': 25}
```

**Example 2: Feature skipped**

```
Do you want to use the "Who is lucky?" feature? Write Yes/No:
> No

No one is going to be lucky

{'Marc': 20, 'Jem': 20, 'Monica': 20, 'Anna': 20, 'Jason': 20}
```

</details>

---

## ▶️ How to Run

Make sure you have Python installed, then run:

```bash
python bill_splitter.py
```
