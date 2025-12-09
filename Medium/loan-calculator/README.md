# 🧮 Loan Calculator  
A small console-based **Python project** built as part of the **Hyperskill Python track**.  
The goal is to progressively implement a fully functional loan calculator by completing four tasks.

---

## 🚀 Project Progress  
- [x] **Task 1** — Display Item Prices  
- [x] **Task 2** — Dreamworld
- [ ] **Task 3**  
- [ ] **Task 4**

---

## 📚 About the Tasks  
Each task introduces a new concept and expands the program's functionality — from simple input/output to full loan repayment logic.

---

<details>
<summary><strong>📌 Task 1 — Display Item Prices</strong></summary>

### 📝 Description  
The first step is understanding the basic idea behind a loan calculator:  
ask for the loan principal, ask for the monthly payment, and compute how many months are needed to repay it.

### 🎯 Objectives  
- Ask the user for:
  - the **loan principal**
  - the **monthly payment**
- Compute the number of months required to repay the loan using simple division
- Display the result in the console

### 💡 Example Output

```
Enter the loan principal:
> 1000
Enter the monthly payment:
> 200

It will take 5 months to repay the loan
```

</details>

---

<details>
<summary><strong>📌 Task 2 — Monthly Payments or Number of Months</strong></summary>

### 📝 Description  
In this task, the calculator becomes more flexible.  
The user can now choose **what** to calculate:

- the **number of monthly payments**, or  
- the **monthly payment amount**.

The program must then ask for the missing parameter and compute the result.  
If the calculated payment is a floating-point value, it should be **rounded up**, since no monthly payment can exceed the fixed amount — the final payment may differ instead.

### 🎯 Objectives  
- Ask for the **loan principal**.  
- Ask what the user wants to calculate:  
  - `"m"` → number of months  
  - `"p"` → monthly payment  
- Ask for the required missing parameter.  
- Output the correct result.  
- If rounding occurs, display both the regular payment and the last payment.

### 💡 Examples

**Example — number of months**

```
Enter the loan principal:
> 1000
What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:
> m
Enter the monthly payment:
> 150

It will take 7 months to repay the loan
```

**Example — monthly payment with rounding**

```
Enter the loan principal:
> 1000
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:
> p
Enter the number of months:
> 9

Your monthly payment = 112 and the last payment = 104
```

</details>

---