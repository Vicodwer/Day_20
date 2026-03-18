# 📊 Python Assignment — Statistics & Hypothesis Testing
### Normal Distribution · Standard Normal · Z-Score · Descriptive Statistics · Hypothesis Testing

---

## 📁 File Structure

```
assignment2/
├── assignment2.py            # All Python code — Parts A, B, C
├── python_assignment2.docx   # Full submission document
├── part_a_distributions.png  # Histogram: Normal & Z-score (A1, A2)
├── part_a3_marks.png         # Student marks with outliers (A3)
├── part_b1_comparison.png    # Normal vs Standard Normal side-by-side (B1)
└── README.md                 # This file
```

---

## 🗂️ Assignment Structure

### Part A — Concept Application (40%)

| Task | Method |
|------|--------|
| Generate 1000 samples from N(50, 10) | Box-Muller transform (manual, no `numpy.random`) |
| Compute mean, variance, std | Manual loop accumulation |
| Plot histogram | `matplotlib` |
| Z-score standardisation | Manual formula: `Z = (X − μ) / σ` |
| Verify Z-data: mean ≈ 0, std ≈ 1 | Manual stats on transformed data |
| Descriptive stats on student marks | Mean, median, variance, std — all manual |
| Outlier detection | Z-score threshold `\|Z\| > 2` and `\|Z\| > 3` |
| One-sample Z-test (H₀: μ = 70) | Manual Z-statistic + p-value via `math.erfc` |
| Simulate 1000 tests → false positive rate | Monte Carlo simulation under H₀ true |

### Part B — Stretch Problem (30%)

| Task | Description |
|------|-------------|
| Normal vs Std. Normal comparison | Side-by-side histogram; shape vs scale discussion |
| Two-group hypothesis test | Pooled SE, Z-statistic, p-value, interpretation |
| When to standardise? | Conceptual: scale-sensitive ML algorithms |
| Z-score in ML | Feature scaling, gradient descent, PCA, outlier detection |

### Part C — Interview Ready (20%)

| Question | Topic |
|----------|-------|
| Q1 | Normal distribution vs Standard Normal distribution |
| Q2 | `z_score(x, mean, std)` function applied on a dataset |
| Q3 | Hypothesis testing: H₀, H₁, p-value, α |

### Part D — AI-Augmented Task (10%)

- Prompt documented with full AI output
- AI-generated example tested and verified
- Evaluation table: correctness, runnable code, clarity, improvements suggested

---

## ▶️ How to Run

### Install dependencies
```bash
pip install matplotlib
```
> `math` and `random` are part of Python's standard library — no additional install needed.

### Run the assignment
```bash
python3 assignment2.py
```

Requires **Python 3.6+**. Three `.png` chart files will be generated in the same directory.

---

## 📈 Charts Generated

| File | Contents |
|------|----------|
| `part_a_distributions.png` | Left: raw dataset histogram · Right: Z-score histogram |
| `part_a3_marks.png` | Student marks distribution with outliers highlighted |
| `part_b1_comparison.png` | Normal distribution vs Standard Normal side-by-side |

---

## ✅ Sample Output

```
--- A1: Generate Dataset (N=1000) ---
  Computed mean     : 49.9255  (expected ≈ 50)
  Computed variance : 97.2915  (expected ≈ 100)
  Computed std dev  : 9.8636   (expected ≈ 10)

--- A2: Z-Score Standardisation ---
  Z-score mean : 0.000000  (expected ≈ 0)
  Z-score std  : 1.000000  (expected ≈ 1)

--- A3: Descriptive Statistics ---
  Mean: 66.53  |  Median: 69.50  |  Std: 21.97
  Outliers (|Z| > 2): [(15, -2.346), (3, -2.892)]

--- A4: One-Sample Z-Test (H₀: μ = 70) ---
  Z-statistic : -0.8643  |  p-value: 0.3874
  Result      : FAIL TO REJECT H₀

--- A5: Simulation ---
  False positive rate : 6.10%  (expected ≈ 5%)  ✓
```

---

## 📌 Key Concepts

**Normal Distribution** — A symmetric bell-shaped probability distribution defined by mean (μ) and standard deviation (σ). About 68% of values fall within ±1σ, 95% within ±2σ, and 99.7% within ±3σ.

**Standard Normal Distribution** — A special case of the normal distribution with μ = 0 and σ = 1. Used as a universal reference for comparison.

**Z-Score** — Measures how many standard deviations a value is from the mean:  
`Z = (X − μ) / σ`

**Hypothesis Testing** — A statistical method to decide if observed data supports a claim:
- **H₀ (Null)** — The default assumption (no difference/effect)
- **H₁ (Alternative)** — What we are trying to prove
- **p-value** — Probability of results this extreme if H₀ were true
- **α (alpha)** — Decision threshold; reject H₀ if p-value < α

**False Positive Rate** — The proportion of times we incorrectly reject H₀ when it is actually true. Over many simulations, this rate converges to α.

---

> 💡 All statistical calculations (mean, variance, std, Z-score, Z-statistic, p-value) are implemented manually using loops and `math` — no `numpy`, `scipy`, or `statistics` module used.
