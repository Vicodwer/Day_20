 ============================================================
# PART B — Stretch Problem
# ============================================================
print("\n" + "=" * 65)
print("PART B — Stretch Problem")
print("=" * 65)
 
 
# ──────────────────────────────────────────────────────────────
# B1 — Normal vs Standard Normal: Plot Comparison
# ──────────────────────────────────────────────────────────────
print("\n--- B1: Normal vs Standard Normal Distribution ---")
 
normal_data = generate_normal(mean=50, std=10, size=2000)
std_normal  = z_score_transform(normal_data)
 
fig, axes = plt.subplots(1, 2, figsize=(12, 4), sharey=False)
 
axes[0].hist(normal_data, bins=40, color='steelblue', edgecolor='white', alpha=0.85)
axes[0].set_title("Normal Distribution\nμ = 50, σ = 10", fontweight='bold')
axes[0].set_xlabel("Value"); axes[0].set_ylabel("Frequency")
 
axes[1].hist(std_normal, bins=40, color='coral', edgecolor='white', alpha=0.85)
axes[1].set_title("Standard Normal Distribution\nμ = 0, σ = 1", fontweight='bold')
axes[1].set_xlabel("Z-Score"); axes[1].set_ylabel("Frequency")
 
plt.suptitle("B1 — Normal vs Standard Normal", fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig("part_b1_comparison.png", dpi=120, bbox_inches='tight')
plt.close()
print("  Saved → part_b1_comparison.png")
 
print("""
  Differences:
  • Normal       → mean = 50, std = 10  (arbitrary scale)
  • Std. Normal  → mean = 0,  std = 1   (dimensionless Z-scores)
  • Shape is identical; only location and spread differ
  • Std. Normal allows comparison across different datasets
""")
 
 
# ──────────────────────────────────────────────────────────────
# B2 — Two-Group Hypothesis Test
# ──────────────────────────────────────────────────────────────
print("--- B2: Two-Group Comparison (Difference in Means) ---")
 
group_A = generate_normal(mean=70, std=8, size=50)   # Class A
group_B = generate_normal(mean=74, std=9, size=50)   # Class B
 
mean_A = calc_mean(group_A)
mean_B = calc_mean(group_B)
std_A  = calc_std(group_A)
std_B  = calc_std(group_B)
 
# Pooled standard error
se = math.sqrt((std_A**2 / len(group_A)) + (std_B**2 / len(group_B)))
z_two = (mean_A - mean_B) / se
 
def phi(z):
    return 0.5 * math.erfc(-z / math.sqrt(2))
 
p_two = 2 * (1 - phi(abs(z_two)))
 
print(f"  Group A — mean: {mean_A:.2f},  std: {std_A:.2f},  n: 50")
print(f"  Group B — mean: {mean_B:.2f},  std: {std_B:.2f},  n: 50")
print(f"  Difference in means : {mean_A - mean_B:.4f}")
print(f"  Z-statistic         : {z_two:.4f}")
print(f"  p-value             : {p_two:.4f}")
print(f"  Conclusion          : {'Significant difference (reject H₀)' if p_two < 0.05 else 'No significant difference (fail to reject H₀)'}")
 
 
# ──────────────────────────────────────────────────────────────
# B3 — Conceptual Explanation (printed)
# ──────────────────────────────────────────────────────────────
print("""
--- B3: Conceptual Questions ---
 
When should you standardise data?
  • When features have different units or scales (e.g. height in cm vs weight in kg).
  • Before applying ML algorithms sensitive to scale: SVM, KNN, PCA, Logistic Regression.
  • When comparing measurements across different distributions.
  • In hypothesis testing to use the standard normal table.
 
Why is Z-score important in Machine Learning?
  • Ensures no single feature dominates due to large magnitude.
  • Speeds up gradient descent convergence.
  • Makes model coefficients comparable and interpretable.
  • Helps detect and flag outliers before training.
  • Required for dimensionality reduction (PCA) to work correctly.
""")
