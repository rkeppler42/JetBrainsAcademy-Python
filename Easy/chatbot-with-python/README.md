# 🤖 Simple Chatty Bot

A playful and progressive Python project where you build a chatbot assistant step by step. Designed to teach fundamentals of programming like I/O, loops, conditionals, and functions.

---

## ✅ Tasks Overview

This project is divided into several tasks, each expanding the bot's capabilities.

---

<details>
<summary><strong>📌 Task 1 – Greet the User</strong></summary>

### 📝 Description

Digital personal assistants help people with daily tasks, from driving cars to online shopping. In this project, you’ll build a simplified AI that interacts with the user in a friendly way.

The first task is about creating a good first impression: your bot should introduce itself with a fixed greeting.

### 🎯 Objectives

- Print two lines:
  1. A greeting that includes the bot’s name;
  2. The year it was created.

- You may hardcode the values for now (e.g. `"Aid"` and `"2025"`).

### 💡 Example Output

```
Hello! My name is Aid.
I was created in 2025.
```

</details>

---

<details>
<summary><strong>📌 Task 2 – Greet the User by Name</strong></summary>

### 📝 Description

Now it’s time to make the bot more personal. In this stage, it will ask for the user’s name and reply with a custom greeting.

You’ll also define two functions: `greet()` for the initial bot intro, and `remind_name()` to ask and respond to the user's name. Use **f-strings** to format the responses clearly and concisely.

### 🎯 Objectives

1. Print the initial greeting (bot name and creation year);
2. Ask for the user’s name using the prompt:  
   `Please, remind me your name.`
3. Read the user input from standard input;
4. Greet the user personally:  
   `What a great name you have, {your_name}!`

### 💡 Example Dialogue

```
Hello! My name is Aid.
I was created in 2025.
Please reming me your name.
> Max
What a great name you have, Max!
```

</details>

---

<details>
<summary><strong>📌 Task 3 – Guess the User's Age</strong></summary>

### 📝 Description

In this stage, your bot will try to guess the user's age using a clever math trick based on the **Chinese Remainder Theorem**. It will ask for the remainders of the user's age when divided by 3, 5, and 7, then calculate the result.

The age is computed with this formula:

`age = (remainder3 \* 70 + remainder5 \* 21 + remainder7 \* 15) % 105`

This formula guarantees correct results for ages between 0 and 104.

### 🎯 Objectives

1. Greet the user and ask for their name as before;
2. Ask:
```
Let me guess your age.\
Enter remainders of dividing your age by 3, 5 and 7.
```
3. Read three integers from the user (on separate lines);
4. Calculate and print their age using the formula above;
5. Output:
```
Your age is {your\_age}; that's a good time to start programming!
```

### 💡 Example Dialogue
```
Hello! My name is Aid.\
I was created in 2025.\
Please, remind me your name.
> Max
What a great name you have, Max!\
Let me guess your age.\
Enter remainders of dividing your age by 3, 5 and 7.
> 1
> 2
> 1
Your age is 22; that's a good time to start programming!
```

</details>

---

<details>
<summary><strong>📌 Task 4 – Count to a Number</strong></summary>

### 📝 Description

Your bot just learned how to do arithmetic! In this stage, it will demonstrate its skills by counting from `0` up to any number the user inputs.

This helps you practice `for` loops and reading integers from input.

### 🎯 Objectives

1. Continue the dialogue as in previous tasks;
2. Add the line:  
   `Now I will prove to you that I can count to any number you want.`
3. Read a positive integer from the user;
4. Count from `0` to that number (inclusive), printing each number followed by an exclamation mark:  
```
0 !  
1 !  
2 !  
...
```
5. After the count, print:  
 `Completed, have a nice day!`

### 💡 Example Dialogue (simplified)

```
> 5
0!
1!
2!
3!
4!
5!
Completed, have a nice day!
```

</details>

---

<details>
<summary><strong>📌 Task 5 – Quiz Time</strong></summary>

### 📝 Description

In the final stage, your bot becomes a teacher! It will quiz the user with a multiple-choice question about programming and only allow the session to end once the correct answer is given.

This task helps you practice `while` loops, input validation, and simple logic.

### 🎯 Objectives

1. Display a multiple-choice question that ends with a `?`
2. Each answer option must start with a number and a dot (`1.`, `2.` etc.)
3. Read user input
4. If the answer is incorrect, print:  
   `Please, try again.`
5. Repeat until the user selects the correct answer
6. Upon success, print:  
   `Congratulations, have a nice day!`

### 💡 Example Dialogue (simplified)

```
Hello! My name is Aid.
I was created in 2025.
Please, remind me your name.
> Max
What a great name you have, Max!
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.
> 1 
> 2
> 1
Your age is 22; that's a good time to start programming!
Now I will prove to you that I can count to any number you want.
> 3
0 !
1 !
2 !
3 !
Let's test your programming knowledge.
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.
> 4
Please, try again.
> 2
Congratulations, have a nice day!
```
