# 🎓 Student Performance Predictor

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikit-learn)
![pandas](https://img.shields.io/badge/pandas-data-green?logo=pandas)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

> A machine learning project that predicts student final grades
> based on study habits, attendance, and academic history.
> Achieves **94% accuracy (R² = 0.94)**

---

## 📌 Project Overview

This project analyzes key factors affecting student academic
performance and builds a Linear Regression model to predict
final grades. The dataset contains 200 students with 6 features.

---

## 📊 Features Used

| Feature                 | Description                 |
| ----------------------- | --------------------------- |
| `study_hours_per_day`   | Daily study hours           |
| `attendance_percentage` | Class attendance rate       |
| `previous_grade`        | Prior academic performance  |
| `sleep_hours`           | Daily sleep hours           |
| `extracurricular`       | Participation in activities |

---

## 📁 Project Structure

```
student-performance-predictor/
│
├── 📂 data/
│   ├── students.csv
│   ├── study_vs_grade.png
│   ├── attendance_vs_grade.png
│   ├── grade_distribution.png
│   ├── correlation_matrix.png
│   └── actual_vs_predicted.png
│
├── 📂 src/
│   ├── generate_data.py
│   ├── analyze_data.py
│   └── model.py
│
└── 📄 README.md
```

---

## 🛠️ Technologies Used

| Tool         | Purpose              |
| ------------ | -------------------- |
| Python 3.14  | Core language        |
| pandas       | Data manipulation    |
| numpy        | Numerical operations |
| matplotlib   | Data visualization   |
| seaborn      | Statistical plots    |
| scikit-learn | Machine learning     |

---

## 🚀 How to Run

### 1️⃣ Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 2️⃣ Generate dataset

```bash
python src/generate_data.py
```

### 3️⃣ Analyze data

```bash
python src/analyze_data.py
```

### 4️⃣ Train model

```bash
python src/model.py
```

---

## 📈 Results

| Metric             | Value                   |
| ------------------ | ----------------------- |
| R² Score           | **0.94 (94% accuracy)** |
| Mean Squared Error | 7.15                    |

### 🔍 Feature Importance

| Feature             | Weight | Impact       |
| ------------------- | ------ | ------------ |
| Study Hours Per Day | 2.9553 | 🔴 Strongest |
| Sleep Hours         | 1.2521 | 🟠 High      |
| Extracurricular     | 0.5219 | 🟡 Moderate  |
| Previous Grade      | 0.3074 | 🟢 Moderate  |
| Attendance          | 0.3039 | 🟢 Moderate  |

### 💡 Key Finding

> Study hours per day is the **strongest predictor** of final grade,
> followed by sleep hours. Consistent study habits and adequate
> rest are the most critical factors in academic performance.

---

## 👨‍💻 Author

**Erick Kanja**
_Undergraduate Software Engineering Student_

[![GitHub](https://img.shields.io/badge/GitHub-pseudohaven-black?logo=github)](https://github.com/pseudohaven)

---

⭐ _If you found this project useful, consider giving it a star!_
