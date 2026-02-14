import traceback

try:
    print("✅ imports next...")
    import os
    import numpy as np
    import pandas as pd
    from scipy import stats
    import matplotlib.pyplot as plt
    print("✅ imports successful")
except Exception:
    traceback.print_exc()
    raise


def cohens_d(x, y):
    nx = len(x)
    ny = len(y)
    pooled_std = np.sqrt(
        ((nx - 1) * np.var(x, ddof=1) + (ny - 1) * np.var(y, ddof=1)) / (nx + ny - 2)
    )
    return (np.mean(x) - np.mean(y)) / pooled_std


def main():
    print("✅ main() started")

    # dataset is in project root, file is in src/
    data_path = os.path.join(os.path.dirname(__file__), "..",
                             "Employee_Training_and_Performance_Dataset.csv")
    data_path = os.path.abspath(data_path)

    print("✅ Loading dataset from:", data_path)

    df = pd.read_csv(data_path)
    print("✅ Dataset loaded. Rows:", len(df))

    # clean
    df = df.dropna(subset=["TrainingAttended", "PerformanceScore"])

    group_yes = df[df["TrainingAttended"] == "Yes"]["PerformanceScore"]
    group_no = df[df["TrainingAttended"] == "No"]["PerformanceScore"]

    print("\n--- Group Summary ---")
    print("Yes count:", len(group_yes), " mean:", round(group_yes.mean(), 2))
    print("No  count:", len(group_no),  " mean:", round(group_no.mean(), 2))

    # normality
    sample_size = min(len(group_yes), len(group_no), 300)
    shapiro_yes = stats.shapiro(group_yes.sample(sample_size, random_state=1))
    shapiro_no = stats.shapiro(group_no.sample(sample_size, random_state=1))

    print("\n--- Shapiro Test ---")
    print("Yes p-value:", shapiro_yes.pvalue)
    print("No  p-value:", shapiro_no.pvalue)

    # levene
    levene = stats.levene(group_yes, group_no)
    print("\n--- Levene Test ---")
    print("p-value:", levene.pvalue)

    # welch t-test
    t_stat, p_two = stats.ttest_ind(group_yes, group_no, equal_var=False)

    # convert to one-tailed for H1: mean_yes > mean_no
    if t_stat > 0:
        p_one = p_two / 2
    else:
        p_one = 1 - (p_two / 2)

    print("\n--- Welch T-Test ---")
    print("t-stat:", t_stat)
    print("two-tailed p:", p_two)
    print("one-tailed  p:", p_one)

    # effect size
    d = cohens_d(group_yes, group_no)
    print("\n--- Effect Size ---")
    print("Cohen's d:", round(d, 3))

    # conclusion
    alpha = 0.05
    print("\n--- Conclusion ---")
    if p_one < alpha:
        print("✅ Reject H0: Training improves performance (statistically significant).")
    else:
        print("❌ Fail to reject H0: No strong evidence training improves performance.")

    # plot save
    reports_dir = os.path.join(os.path.dirname(__file__), "..", "reports")
    os.makedirs(reports_dir, exist_ok=True)

    plt.figure(figsize=(6, 5))
    df.boxplot(column="PerformanceScore", by="TrainingAttended")
    plt.title("Performance Score by Training Attendance")
    plt.suptitle("")
    plt.xlabel("Training Attended")
    plt.ylabel("Performance Score")
    plt.tight_layout()

    plot_path = os.path.join(reports_dir, "performance_boxplot.png")
    plt.savefig(plot_path, dpi=200)
    plt.close()

    print("\n📌 Plot saved to:", os.path.abspath(plot_path))


if __name__ == "__main__":
    main()
