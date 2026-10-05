import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv('data/students.csv')

# Features and target
X = df[['study_hours_per_day', 'attendance_percentage',
        'previous_grade', 'sleep_hours', 'extracurricular']]
y = df['final_grade']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("=== MODEL PERFORMANCE ===")
print(f"Mean Squared Error : {mse:.2f}")
print(f"R² Score           : {r2:.2f}")
print("\n=== FEATURE IMPORTANCE ===")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature:30s}: {coef:.4f}")

# Plot Actual vs Predicted
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()],
         'r--', linewidth=2)
plt.title('Actual vs Predicted Grades')
plt.xlabel('Actual Grade')
plt.ylabel('Predicted Grade')
plt.tight_layout()
plt.savefig('data/actual_vs_predicted.png')
plt.show()
print("\nModel plot saved!")
print("\n=== MODEL COMPLETE ===")