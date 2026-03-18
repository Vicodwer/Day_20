D1 — Prompt Given to AI
Prompt: "Explain normal distribution, Z-score, and hypothesis testing with a simple Python example."

D2 — AI Output (Documented)
AI Explanation Summary
The AI explained the three topics as follows:
•	Normal Distribution: A bell-shaped, symmetric probability distribution defined by mean and standard deviation. Most real-world data (heights, test scores, errors) follow this pattern.
•	Z-Score: A standardised score showing how many standard deviations a data point is from the mean. Formula: Z = (X − μ) / σ.
•	Hypothesis Testing: A method to test claims about populations. We define H₀ (null), compute a test statistic, and use the p-value to decide.

AI-Generated Python Example
import random, math

# Simulate data from a normal distribution
data = [random.gauss(50, 10) for _ in range(100)]

# Compute mean and std manually
mean = sum(data) / len(data)
std  = math.sqrt(sum((x - mean)**2 for x in data) / len(data))

# Z-scores
z_scores = [(x - mean) / std for x in data]
print(f'Mean of Z-scores : {sum(z_scores)/len(z_scores):.4f}')  # ≈ 0
print(f'Std of Z-scores  : {math.sqrt(sum(z**2 for z in z_scores)/len(z_scores)):.4f}') # ≈ 1

# One-sample Z-test: H0: mu = 50
mu0    = 50
z_stat = (mean - mu0) / (std / math.sqrt(len(data)))
p_val  = 2 * (1 - 0.5 * math.erfc(-abs(z_stat) / math.sqrt(2)))
print(f'Z-stat: {z_stat:.4f}  |  p-value: {p_val:.4f}')
print('Reject H0' if p_val < 0.05 else 'Fail to reject H0')

D3 — Evaluation of AI Output
Criterion	Result	Notes
Is the explanation correct?	Yes ✓	All three concepts explained accurately and in beginner-friendly language.
Is the code logically correct?	Yes ✓	The Z-score loop is correct; Z-test uses proper formula with math.erfc.
Is the code runnable?	Yes ✓	Tested in Python 3.10 — runs without errors or warnings.
Z-score mean ≈ 0, std ≈ 1?	Yes ✓	Confirmed empirically after running the code.
Suggested improvement	Minor	AI used random.gauss() (a built-in); for the assignment's manual requirement, Box-Muller is preferred.
Missing concept?	Minor	AI did not cover outlier detection or false positive rate simulation — added in our own code.
