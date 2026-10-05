
import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Number of students
n = 200

# Generate dataset
data = {
    'student_id': range(1, n + 1),
    'study_hours_per_day': np.round(np.random.uniform(1, 10, n), 1),
    'attendance_percentage': np.round(np.random.uniform(50, 100, n), 1),
    'previous_grade': np.round(np.random.uniform(40, 100, n), 1),
    'sleep_hours': np.round(np.random.uniform(4, 9, n), 1),
    'extracurricular': np.random.randint(0, 2, n)
}

df = pd.DataFrame(data)

# Generate final grade based on the features
df['final_grade'] = np.round(
    (df['study_hours_per_day'] * 3) +
    (df['attendance_percentage'] * 0.3) +
    (df['previous_grade'] * 0.3) +
    (df['sleep_hours'] * 1.5) +
    np.random.uniform(-5, 5, n),
    1
)

# Clip grades to 0-100 range
df['final_grade'] = df['final_grade'].clip(0, 100)

# Save to CSV
df.to_csv('data/students.csv', index=False)
print("Dataset created successfully!")
print(df.head())
print(f"\nShape: {df.shape}")
