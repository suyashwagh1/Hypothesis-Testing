Employee Training Impact Analysis using Hypothesis Testing (Python)

This project evaluates whether a company’s training program improves employee performance scores.

Using a dataset of 1000 employees containing demographic information, training participation, and performance scores, we perform a structured statistical analysis to determine whether trained employees perform significantly better than untrained employees.

This project demonstrates:

Statistical hypothesis testing

Assumption validation

Effect size interpretation

Business conclusion translation

End-to-end reproducible analysis in Python

🎯 Business Problem

The company invested in a training program and wants to know:

Does the training program significantly improve employee performance?

If the improvement is statistically significant and meaningful in magnitude, the company can justify continued investment in training.

📂 Dataset Description

The dataset contains 1000 employee records with the following features:

EmployeeID

Age

Department

Education

ExperienceYears

TrainingAttended (Yes / No)

PerformanceScore (0–100 scale)

The target variable for this analysis is:

PerformanceScore

The grouping variable is:

TrainingAttended

🧠 Statistical Approach
Step 1: Define Hypotheses (One-Tailed Test)

We are specifically testing if training improves performance.

Null Hypothesis (H₀):
μ(Trained) ≤ μ(Untrained)

Alternative Hypothesis (H₁):
μ(Trained) > μ(Untrained)

This is a one-tailed test because we are only interested in improvement (not just any difference).

Step 2: Data Preparation

The dataset is:

Loaded using pandas

Cleaned for missing values

Split into two independent groups:

Trained employees

Untrained employees

Step 3: Assumption Checks

Before applying a t-test, we verify assumptions.

🔹 1. Normality Check — Shapiro-Wilk Test

Applied to both groups (sample up to 300 observations for stability)

If p-value > 0.05 → data is approximately normal

Results:

Both groups passed the normality test.

🔹 2. Equal Variance Check — Levene’s Test

Tests whether both groups have equal variance

p-value was borderline (~0.0547)

To remain statistically robust, we used:

✅ Welch’s t-test (does not assume equal variances)

Step 4: Hypothesis Testing — Welch’s T-Test

We performed an independent two-sample Welch’s t-test.

Since SciPy returns a two-tailed p-value by default, we converted it to a one-tailed p-value because our alternative hypothesis is directional (Yes > No).

📈 Results
Metric	Value
Trained Mean	70.2
Untrained Mean	64.3
Sample Size (Yes)	608
Sample Size (No)	392
Welch t-statistic	9.188
One-tailed p-value	1.43e-19
Cohen’s d	0.587
📊 Effect Size Interpretation

Cohen’s d = 0.587

Interpretation:

0.2 → small effect

0.5 → medium effect

0.8 → large effect

This indicates a moderate practical impact.

This is important because:

Statistical significance alone is not enough.

We must evaluate real-world impact.

✅ Final Conclusion

Since:

One-tailed p-value < 0.05

t-statistic is strongly positive

Effect size is moderate

We reject the null hypothesis.

🔥 Training is associated with significantly higher employee performance.

This suggests that the company’s training program has both:

Statistical significance

Meaningful practical impact

📊 Visualization

A boxplot comparing trained vs untrained performance scores is generated and saved in:

reports/performance\_boxplot.png

🛠 Technologies Used

Python

Pandas

NumPy

SciPy

Matplotlib

How to Run
pip install -r requirements.txt
python src/analysis.py

