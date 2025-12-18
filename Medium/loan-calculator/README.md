# 🧮 Loan Calculator  
A small console-based **Python project** built as part of the **Hyperskill Python track**.  
The goal is to progressively implement a fully functional loan calculator by completing four tasks.

---

## 🚀 Project Progress  
- [x] **Task 1** — Display Item Prices  
- [x] **Task 2** — Dreamworld
- [x] **Task 3**  
- [x] **Task 4**

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

<details>
<summary><strong>📌 Task 3 — Annuity Loan Calculations (Command-Line Version)</strong></summary>

### 📝 Description  
In this task, the loan calculator becomes fully functional:  
it must compute **any missing loan parameter** using command-line arguments.

This stage introduces **annuity payments**, where the user pays a fixed amount every month.  
Depending on which argument is missing, the program must calculate:

- the **number of monthly payments** (`--periods`)
- the **monthly annuity payment** (`--payment`)
- the **loan principal** (`--principal`)

The **interest rate (`--interest`) must always be provided**, and it must be treated as a *nominal monthly rate*:

```
i = interest / 100 / 12
```


### 🎯 Objectives  
- Parse command-line arguments (`--principal`, `--payment`, `--periods`, `--interest`).
- Detect which parameter is missing.
- Calculate it using the appropriate annuity formula.
- If computing the number of months, format the output as:
  - `"X years and Y months"`,
  - `"X years"`, or
  - `"Y months"`  
  (avoid awkward outputs like “0 years and 11 months”).

### 🔢 Key Formulas  

**Monthly payment (annuity):**

```
A = P * i * (1 + i)^n / ((1 + i)^n – 1)
```

**Loan principal:**

```
P = A / (i * (1 + i)^n / ((1 + i)^n – 1))
```

**Number of payments:**

```
n = log(A / (A – i * P)) / log(1 + i)
```


### 💡 Examples

**Calculate number of months**

```
> python creditcalc.py --principal=1000000 --payment=15000 --interest=10
It will take 8 years and 2 months to repay this loan!
```

**Calculate monthly payment**

```
> python creditcalc.py --principal=1000000 --periods=60 --interest=10
Your monthly payment = 21248!
```

**Calculate loan principal**

```
> python creditcalc.py --payment=8721.8 --periods=120 --interest=5.6
Your loan principal = 800000!
```

</details>

---

<details>
<summary><strong>📌 Task 4 — Differentiated Payments, Validation & Overpayment</strong></summary>

### 📝 Description  
In the final stage, the loan calculator supports **two types of repayment**:

- **Annuity payments** (`--type=annuity`): fixed monthly payment  
- **Differentiated payments** (`--type=diff`): decreasing payments over time  

The program must now:
- parse **command-line arguments**,
- validate input parameters,
- compute **monthly payments**, **loan principal**, or **number of periods**,
- and calculate the **overpayment** (total interest paid).

The `--type` argument is mandatory, and incorrect or insufficient parameters must result in:

```
Incorrect parameters.
```

### 🎯 Objectives  
- Support both **annuity** and **differentiated** payment types.
- Validate all input parameters:
  - missing arguments
  - invalid combinations
  - negative values
- Calculate:
  - monthly payments
  - loan principal
  - number of periods
- Compute and display **overpayment**.
- Round up all floating-point values.

### 🔢 Differentiated Payment Formula  

```
Dₘ = P / n + i * (P − P * (m − 1) / n)
```


Where:
- `P` — loan principal  
- `n` — number of payments  
- `i` — nominal monthly interest rate  
- `m` — current month  

### 💡 Examples

**Differentiated payments**

```
> python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10

Month 1: payment is 108334
Month 2: payment is 107500
Month 3: payment is 106667
...
Month 10: payment is 100834
Overpayment = 45837
```


**Annuity payment**

```
> python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10

Your annuity payment = 21248!
Overpayment = 274880
```


**Invalid parameters**

```
> python creditcalc.py --type=diff --principal=1000000 --payment=104000

Incorrect parameters.
```

</details>
