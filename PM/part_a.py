# ============================================================
#  Dependencies: numpy, matplotlib
#  Run: python3 assignment2.py
# ============================================================
 
import random
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
 
# ── reproducibility ──────────────────────────────────────────
random.seed(42)
 
print("=" * 65)
print("  Python Assignment — Statistics & Hypothesis Testing")
print("=" * 65)
 
 
# ============================================================
# PART A — Concept Application
# ============================================================
print("\n" + "=" * 65)
print("PART A — Concept Application")
print("=" * 65)
 
 
# ──────────────────────────────────────────────────────────────
# A1 — Generate dataset, compute stats manually, plot histogram
# ──────────────────────────────────────────────────────────────
print("\n--- A1: Generate Dataset (N=1000) from Normal Distribution ---")
 
# Box-Muller transform — generates normally distributed values
# without using numpy.random.normal
def generate_normal(mean=0, std=1, size=1000):
    """Generate 'size' samples from N(mean, std) via Box-Muller."""
    samples = []
    for _ in range(size // 2 + 1):
        u1 = random.random() or 1e-10   # avoid log(0)
        u2 = random.random()
        z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        z1 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)
        samples.extend([mean + std * z0, mean + std * z1])
    return samples[:size]
 
dataset = generate_normal(mean=50, std=10, size=1000)
 
# Manual mean
def calc_mean(data):
    total = 0
    for x in data:
        total += x
    return total / len(data)
 
# Manual variance (population)
def calc_variance(data):
    m = calc_mean(data)
    total = 0
    for x in data:
        total += (x - m) ** 2
    return total / len(data)
 
# Manual standard deviation
def calc_std(data):
    return math.sqrt(calc_variance(data))
 
mean_A1    = calc_mean(dataset)
var_A1     = calc_variance(dataset)
std_A1     = calc_std(dataset)
 
print(f"  Dataset size : 1000  |  Target: mean=50, std=10")
print(f"  Computed mean     : {mean_A1:.4f}  (expected ≈ 50)")
print(f"  Computed variance : {var_A1:.4f}  (expected ≈ 100)")
print(f"  Computed std dev  : {std_A1:.4f}  (expected ≈ 10)")
 
# ── Histogram ────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
 
axes[0].hist(dataset, bins=30, color='steelblue', edgecolor='white', alpha=0.85)
axes[0].axvline(mean_A1, color='red',    linestyle='--', linewidth=1.8, label=f'Mean = {mean_A1:.1f}')
axes[0].axvline(mean_A1 - std_A1, color='orange', linestyle=':', linewidth=1.5, label=f'±1 SD')
axes[0].axvline(mean_A1 + std_A1, color='orange', linestyle=':', linewidth=1.5)
axes[0].set_title("A1 — Dataset Histogram (Normal Distribution)", fontweight='bold')
axes[0].set_xlabel("Value"); axes[0].set_ylabel("Frequency")
axes[0].legend()
 
# ──────────────────────────────────────────────────────────────
# A2 — Convert to Standard Normal (Z-scores)
# ──────────────────────────────────────────────────────────────
print("\n--- A2: Z-Score Standardisation ---")
 
def z_score_transform(data):
    """Manually compute Z-scores for every element in data."""
    m   = calc_mean(data)
    s   = calc_std(data)
    return [(x - m) / s for x in data]
 
z_data     = z_score_transform(dataset)
z_mean     = calc_mean(z_data)
z_std      = calc_std(z_data)
 
print(f"  Z-score mean : {z_mean:.6f}  (expected ≈ 0)")
print(f"  Z-score std  : {z_std:.6f}  (expected ≈ 1)")
 
axes[1].hist(z_data, bins=30, color='mediumseagreen', edgecolor='white', alpha=0.85)
axes[1].axvline(z_mean, color='red',    linestyle='--', linewidth=1.8, label=f'Mean = {z_mean:.4f}')
axes[1].set_title("A2 — Standardised (Z-Score) Distribution", fontweight='bold')
axes[1].set_xlabel("Z-Score"); axes[1].set_ylabel("Frequency")
axes[1].legend()
 
plt.tight_layout()
plt.savefig("part_a_distributions.png", dpi=120, bbox_inches='tight')
plt.close()
print("  Saved → part_a_distributions.png")
 
 
# ──────────────────────────────────────────────────────────────
# A3 — Descriptive Statistics & Outlier Detection on Marks
# ──────────────────────────────────────────────────────────────
print("\n--- A3: Descriptive Statistics — Student Marks ---")
 
marks = [
    45, 67, 72, 55, 89, 91, 34, 78, 65, 82,
    70, 48, 95, 60, 77, 53, 88, 62, 74, 58,
    100, 15, 3, 99, 71, 66, 80, 57, 73, 69
]
 
def calc_median(data):
    s = sorted(data)
    n = len(s)
    mid = n // 2
    return (s[mid - 1] + s[mid]) / 2 if n % 2 == 0 else s[mid]
 
m_mean   = calc_mean(marks)
m_median = calc_median(marks)
m_var    = calc_variance(marks)
m_std    = calc_std(marks)
 
print(f"  Marks dataset : {len(marks)} students")
print(f"  Mean          : {m_mean:.2f}")
print(f"  Median        : {m_median:.2f}")
print(f"  Variance      : {m_var:.2f}")
print(f"  Std Deviation : {m_std:.2f}")
 
# Outlier detection — Z-score threshold
def find_outliers(data, threshold=2):
    m = calc_mean(data)
    s = calc_std(data)
    outliers = []
    for x in data:
        z = (x - m) / s
        if abs(z) > threshold:
            outliers.append((x, round(z, 3)))
    return outliers
 
outliers_2 = find_outliers(marks, threshold=2)
outliers_3 = find_outliers(marks, threshold=3)
 
print(f"\n  Outliers (|Z| > 2): {outliers_2}")
print(f"  Outliers (|Z| > 3): {outliers_3}")
 
# Plot marks distribution
fig, ax = plt.subplots(figsize=(9, 4))
ax.hist(marks, bins=12, color='mediumpurple', edgecolor='white', alpha=0.85)
for val, z in outliers_2:
    ax.axvline(val, color='red', linestyle='--', linewidth=1.4,
               label=f'Outlier: {val} (Z={z})')
ax.axvline(m_mean, color='navy', linestyle='-', linewidth=2, label=f'Mean={m_mean:.1f}')
ax.set_title("A3 — Student Marks with Outliers Marked", fontweight='bold')
ax.set_xlabel("Marks"); ax.set_ylabel("Frequency")
handles, labels = ax.get_legend_handles_labels()
# deduplicate legend
seen = set()
unique = [(h, l) for h, l in zip(handles, labels) if not (l in seen or seen.add(l))]
ax.legend(*zip(*unique))
plt.tight_layout()
plt.savefig("part_a3_marks.png", dpi=120, bbox_inches='tight')
plt.close()
print("  Saved → part_a3_marks.png")
 
 
# ──────────────────────────────────────────────────────────────
# A4 — One-Sample Hypothesis Test (Z-test)
# ──────────────────────────────────────────────────────────────
print("\n--- A4: One-Sample Z-Test ---")
 
# Null hypothesis H₀: population mean μ = 70
# Data: our 30 student marks
 
def one_sample_z_test(data, mu0, alpha=0.05):
    """
    One-sample Z-test.
    H₀: population mean = mu0
    Returns z_stat, p_value (two-tailed), reject flag.
    """
    n      = len(data)
    x_bar  = calc_mean(data)
    sigma  = calc_std(data)
    z_stat = (x_bar - mu0) / (sigma / math.sqrt(n))
 
    # Cumulative standard normal via error function
    def phi(z):
        """P(Z <= z) using math.erfc."""
        return 0.5 * math.erfc(-z / math.sqrt(2))
 
    p_value = 2 * (1 - phi(abs(z_stat)))   # two-tailed
    reject  = p_value < alpha
    return z_stat, p_value, reject, x_bar, sigma
 
mu_null = 70
z_stat, p_val, reject, x_bar, sigma = one_sample_z_test(marks, mu0=mu_null)
 
print(f"  H₀ : μ = {mu_null}  |  H₁ : μ ≠ {mu_null}")
print(f"  Sample mean (x̄) : {x_bar:.4f}")
print(f"  Sample std  (σ)  : {sigma:.4f}")
print(f"  Z-statistic      : {z_stat:.4f}")
print(f"  p-value          : {p_val:.4f}")
print(f"  α = 0.05  →  {'REJECT H₀' if reject else 'FAIL TO REJECT H₀'}")
if reject:
    print("  Conclusion: Evidence suggests the mean is NOT equal to 70.")
else:
    print("  Conclusion: Not enough evidence to reject H₀; mean may be 70.")
 
 
# ──────────────────────────────────────────────────────────────
# A5 — Simulate 1000 Tests Under H₀ True → False Positive Rate
# ──────────────────────────────────────────────────────────────
print("\n--- A5: Simulation — Estimating False Positive Rate ---")
 
def simulate_false_positives(n_simulations=1000, sample_size=30,
                              true_mean=70, true_std=10, alpha=0.05):
    false_positives = 0
    for _ in range(n_simulations):
        sample = generate_normal(mean=true_mean, std=true_std, size=sample_size)
        _, p_val, reject, _, _ = one_sample_z_test(sample, mu0=true_mean, alpha=alpha)
        if reject:
            false_positives += 1
    return false_positives / n_simulations
 
fp_rate = simulate_false_positives(n_simulations=1000)
print(f"  Simulations      : 1000")
print(f"  H₀ true (μ = 70, σ = 10)")
print(f"  False positive rate : {fp_rate:.4f}  ({fp_rate*100:.2f}%)")
print(f"  Significance level α: 0.0500  (5.00%)")
print(f"  → FP rate ≈ α  ✓" if abs(fp_rate - 0.05) < 0.03 else
      f"  → FP rate deviates from α (acceptable due to randomness)")
 
 
