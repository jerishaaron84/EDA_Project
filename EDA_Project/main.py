import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("cleaned_data.csv")

# Statistical summary
print(df.describe())

# -------- Heatmap --------
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.close()

# -------- Histogram --------
df.hist(figsize=(12,10))
plt.tight_layout()
plt.savefig("histogram.png")
plt.close()

# -------- Bar Chart --------
avg_marks = [df["G1"].mean(), df["G2"].mean(), df["G3"].mean()]
labels = ["G1", "G2", "G3"]

plt.figure(figsize=(6,5))
plt.bar(labels, avg_marks)
plt.title("Average Grades")
plt.xlabel("Grade")
plt.ylabel("Average Score")
plt.savefig("bar_chart.png")
plt.close()

print("EDA Completed Successfully!")
