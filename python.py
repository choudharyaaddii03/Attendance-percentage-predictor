# Attendance Percentage Predictor
# Uses np.polyfit to fit a straight line on weekly attendance
# and predicts attendance for a future week.

import numpy as np
import pandas as pd

# ---------- Step 1: Take input ----------
print("Attendance Percentage Predictor")
print("1. Enter data manually")
print("2. Load data from CSV file (columns: Week, Attendance)")
choice = input("Choose option (1/2): ").strip()

if choice == "2":
    path = input("Enter CSV file path: ").strip()
    try:
        df = pd.read_csv(path)
    except Exception:
        print("Could not read the CSV file.")
        raise SystemExit
    weeks = df["Week"].tolist()
    attendance = df["Attendance"].tolist()
else:
    weeks_in = input("Enter week numbers (comma separated, e.g. 1,2,3,4,5): ")
    att_in = input("Enter attendance % (comma separated, e.g. 90,88,86,84,82): ")
    try:
        weeks = [float(x) for x in weeks_in.split(",")]
        attendance = [float(x) for x in att_in.split(",")]
    except ValueError:
        print("Please enter numbers only.")
        raise SystemExit

# ---------- Step 2: Validate ----------
if len(weeks) < 2 or len(attendance) < 2:
    print("At least 2 weeks of data are required.")
    raise SystemExit

if len(weeks) != len(attendance):
    print("Number of weeks and attendance values must match.")
    raise SystemExit

for a in attendance:
    if a < 0 or a > 100:
        print("Attendance must be between 0 and 100.")
        raise SystemExit

try:
    future_week = float(input("Predict for week: "))
except ValueError:
    print("Week must be a number.")
    raise SystemExit

# ---------- Step 3: Fit a straight line ----------
slope, intercept = np.polyfit(weeks, attendance, 1)

# ---------- Step 4: Predict (limit 0-100) ----------
predicted = slope * future_week + intercept
predicted = max(0, min(100, predicted))

# ---------- Step 5: Show result ----------
# +0.0 avoids printing "-0.00"
print()
print(f"Slope: {slope + 0.0:.2f} | Intercept: {intercept + 0.0:.2f}")
print(f"Predicted attendance for week {int(future_week)}: {predicted:.2f}%")

if predicted >= 75:
    print("Safe")
else:
    print("Warning: below 75%")