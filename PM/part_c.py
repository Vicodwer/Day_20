# ============================================================
# PART C — Interview Ready
# ============================================================
print("=" * 65)
print("PART C — Interview Ready")
print("=" * 65)
 
# Q1 — Conceptual (see docx for full answer)
print("""
Q1 — Normal vs Standard Normal Distribution
  Normal Distribution  : Bell-shaped, defined by any mean (μ) and std (σ).
  Standard Normal      : Special case where μ = 0 and σ = 1.
  Conversion           : Z = (X − μ) / σ
  Importance           : Standard normal allows lookup in Z-tables and
                         comparison across datasets with different scales.
""")
 
 
# Q2 — z_score function
print("--- Q2: z_score() Function ---")
 
def z_score(x, mean, std):
    """Return the standardised Z-score for a single value x."""
    if std == 0:
        raise ValueError("Standard deviation cannot be zero.")
    return (x - mean) / std
 
# Apply on a dataset
sample_data  = [55, 70, 80, 45, 65, 90, 35, 75, 60, 50]
ds_mean      = calc_mean(sample_data)
ds_std       = calc_std(sample_data)
z_scores_out = [round(z_score(x, ds_mean, ds_std), 3) for x in sample_data]
 
print(f"  Data    : {sample_data}")
print(f"  Mean    : {ds_mean:.2f}  |  Std: {ds_std:.2f}")
print(f"  Z-scores: {z_scores_out}")
 
 
# Q3 — Hypothesis Testing concepts (see docx for full answer)
print("""
Q3 — Hypothesis Testing Concepts
  Null Hypothesis (H₀)    : The default assumption; no effect or difference.
  Alternative Hypothesis  : The claim we are testing for (H₁ or Hₐ).
  p-value                 : Probability of observing results at least as
                             extreme as ours, assuming H₀ is true.
  Significance Level (α)  : Threshold for rejection; typically 0.05 (5%).
  Decision Rule           : If p-value < α  →  Reject H₀.
""")
 
print("✅  All parts executed successfully.")
 
