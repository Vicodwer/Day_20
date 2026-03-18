# 🐍 Python Assignment
### Loops · Dictionaries · Tuples · *args / **kwargs · Classes · Dunder Methods

---

## 📁 Files

| File | Description |
|------|-------------|
| `assignment.py` | All Python code — Parts A, B, and C |
| `python_assignment.docx` | Full submission document with explanations, code, and output |
| `README.md` | This file |

---

## 🗂️ Assignment Structure

### Part A — Concept Application (40%)
| Task | Technique Used |
|------|---------------|
| Max & Min in a list | `for` loop, manual comparison |
| Frequency count | `for` loop + dictionary |
| Reverse a number | `while` loop, modulo arithmetic |
| Palindrome check | `while` loop, digit reversal |
| List of tuples → dict | `for` loop, no `dict()` built-in |
| Key with highest value | `for` loop, no `max()` built-in |
| Sum & average | `*args`, manual accumulation |
| Top-scoring student | `**kwargs`, `.items()` iteration |

### Part B — Stretch Problem (30%)
Custom `Vector` class with dunder methods:
- `__init__` — stores components as a tuple
- `__repr__` — readable output e.g. `Vector(1, 2, 3)`
- `__add__` — element-wise vector addition
- `__sub__` — element-wise vector subtraction
- `__mul__` / `__rmul__` — scalar multiplication (both sides)

### Part C — Interview Ready (20%)
- **Q1** — *args vs **kwargs: differences, use cases, comparison table
- **Q2** — `Student` class with `calculate_grade()` and `__str__`
- **Q3** — Dunder methods explained with examples table

### Part D — AI-Augmented Task (10%)
- Prompt documented and AI output recorded
- AI-generated `Book` class tested and evaluated
- Evaluation table: correctness, working implementation, clarity, improvements

---

## ▶️ How to Run

```bash
python3 assignment.py
```

Requires **Python 3.6+**. No external libraries needed.

---

## ✅ Sample Output

```
PART A — Concept Application
Maximum: 88  |  Minimum: 1
Frequency: {1: 3, 2: 3, 3: 2, 4: 1, 5: 1}
reverse(123) → 321
121 → palindrome: True

PART B — Vector Class
v1 + v2         = Vector(5, 7, 9)
v1 * 3          = Vector(3, 6, 9)
(v1 + v2) * 0.5 = Vector(2.5, 3.5, 4.5)

PART C — Student Class
Student : Alice  |  Marks: 92  |  Grade: A
Student : Bob    |  Marks: 74  |  Grade: B
Student : Charlie|  Marks: 55  |  Grade: C
```

---

## 📌 Key Concepts

**`*args`** — Collects extra positional arguments into a **tuple**. Use when the number of inputs is unknown.

**`**kwargs`** — Collects extra keyword arguments into a **dictionary**. Use when argument names matter.

**Dunder methods** — Special `__double_underscore__` methods that Python calls automatically for operators, printing, and built-in functions. They make custom classes behave like native Python types.

---

> 💡 No restricted built-ins (`sum()`, `max()`, `min()`, `dict()`) were used in the loop-only sections.
