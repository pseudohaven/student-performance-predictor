import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load dataset
df = pd.read_csv('data/students.csv')

#Basic Info 
print("=== DATASET OVERVIEW ===")
print(df.head())
print(f"\nShape: {df.shape}")
print(f"\nColumn Types:\n{df.dtypes}")
print(f"\nMissing Values:\n{df.isnull().sum()}")
print(f"\nBasic Statistics:\n{df.describe()}")

#Plot 1: Study Hours vs Final Grade
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='study_hours_per_day', 
                y='final_grade', color='blue', alpha=0.6)
plt.title('Study Hours vs Final Grade')
plt.xlabel('Study Hours Per Day')
plt.ylabel('Final Grade')
plt.tight_layout()
plt.savefig('data/study_vs_grade.png')
plt.show()
print("Plot 1 saved!")

#Plot 2: Attendance vs Final Grade
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='attendance_percentage',
                y='final_grade', color='green', alpha=0.6)
plt.title('Attendance vs Final Grade')
plt.xlabel('Attendance Percentage')
plt.ylabel('Final Grade')
plt.tight_layout()
plt.savefig('data/attendance_vs_grade.png')
plt.show()
print("Plot 2 saved!")

#Plot 3: Grade Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['final_grade'], bins=20, color='orange')
plt.title('Distribution of Final Grades')
plt.xlabel('Final Grade')
plt.ylabel('Number of Students')
plt.tight_layout()
plt.savefig('data/grade_distribution.png')
plt.show()
print("Plot 3 saved!")

#Correlation Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Between All Features')
plt.tight_layout()
plt.savefig('data/correlation_matrix.png')
plt.show()
print("Correlation matrix saved!")

print("\n=== ANALYSIS COMPLETE ===")