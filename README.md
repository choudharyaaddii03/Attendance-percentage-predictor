# Attendance Percentage Predictor

**Author:** Aditya Choudhary
**PS No.:** 96
**University:** Rungta International Skills University
**School:** School of Computer Science and Engineering
**Program:** Bachelor of Technology, Computer Science and Engineering
**Language:** Python 3
**Concepts:** Pandas, NumPy, Regression Basics

---

## Table of Contents

1. [Overview](#1-overview)
2. [Problem Statement](#2-problem-statement)
3. [Objectives](#3-objectives)
4. [Technologies Used](#4-technologies-used)
5. [How It Works](#5-how-it-works)
6. [Algorithm](#6-algorithm)
7. [Input Validation](#7-input-validation)
8. [Installation and Setup](#8-installation-and-setup)
9. [How to Run](#9-how-to-run)
10. [Worked Example](#10-worked-example)
11. [Code Explanation](#11-code-explanation)
12. [Test Cases](#12-test-cases)
13. [Project Files](#13-project-files)
14. [Troubleshooting](#14-troubleshooting)
15. [Limitations](#15-limitations)
16. [Future Improvements](#16-future-improvements)
17. [Conclusion](#17-conclusion)

---

## 1. Overview

Many colleges require students to keep at least 75% attendance. This project takes a student's weekly attendance percentages, finds the trend, and predicts what the attendance will be in a future week. It then tells the student whether that predicted value is **Safe** or needs a **Warning**.

## 2. Problem Statement

Use weekly attendance percentages to fit a straight line with `np.polyfit` and predict attendance for a future week (limit 0-100). At least 2 weeks of data are needed. Show **Safe** if the prediction is 75 or more, else **Warning: below 75%**.

## 3. Objectives

- Accept weekly attendance from user input or from a CSV file.
- Validate the data (at least 2 weeks, every value between 0 and 100).
- Fit a straight line to the data using `np.polyfit` and get the slope and intercept.
- Predict attendance for a chosen future week and limit the result to 0-100.
- Display Safe or Warning based on the 75% threshold.

## 4. Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming language |
| NumPy | `np.polyfit` to fit the straight line |
| Pandas | `pd.read_csv` to read attendance from a CSV file |

## 5. How It Works

The program uses **simple linear regression**. A straight line has the equation:

```
attendance = slope x week + intercept
```

- **Slope** is how much the attendance changes each week. A negative slope means attendance is falling, a positive slope means it is rising.
- **Intercept** is the line's value at week 0.

`np.polyfit(weeks, attendance, 1)` finds the slope and intercept of the line that best fits all the data points (least squares method). The program then puts the future week into the equation to get the prediction, and limits it to between 0 and 100 because attendance cannot be below 0% or above 100%.

## 6. Algorithm

1. Start the program and ask the user to choose manual input or CSV input.
2. Read the week numbers and the attendance values.
3. If fewer than 2 weeks are given, print an error and stop.
4. If any attendance value is below 0 or above 100, print an error and stop.
5. Ask for the future week to predict.
6. Calculate the slope and intercept with `np.polyfit(weeks, attendance, 1)`.
7. Predict: `slope x future_week + intercept`.
8. Limit the prediction to the range 0-100.
9. Print the slope, intercept and predicted attendance.
10. If the prediction is 75 or more print `Safe`, otherwise print `Warning: below 75%`.

## 7. Input Validation

| Check | Message shown |
|-------|---------------|
| Fewer than 2 weeks of data | `At least 2 weeks of data are required.` |
| Any attendance below 0 or above 100 | `Attendance must be between 0 and 100.` |
| Number of weeks and attendance values do not match | `Number of weeks and attendance values must match.` |
| Non-numeric input | `Please enter numbers only.` |
| Future week is not a number | `Week must be a number.` |

## 8. Installation and Setup

1. Install Python 3 from https://www.python.org.
2. Download or copy `attendance_predictor.py` into a folder.
3. Open a terminal in that folder (in VS Code: Terminal, then New Terminal).
4. Install the required libraries:

```
pip install numpy pandas
```

If `pip` is not recognised, use:

```
python -m pip install numpy pandas
```

## 9. How to Run

```
python attendance_predictor.py
```

On some systems use `python3` instead of `python`.

### Option 1: Type the data

1. Choose `1`.
2. Enter week numbers separated by commas, e.g. `1,2,3,4,5`.
3. Enter attendance values separated by commas, e.g. `90,88,86,84,82`.
4. Enter the future week to predict, e.g. `10`.

### Option 2: Load a CSV file

1. Choose `2`.
2. Enter the path of the CSV file.
3. Enter the future week to predict.

The CSV file must have the columns `Week` and `Attendance`:

```
Week,Attendance
1,90
2,88
3,86
4,84
5,82
```

## 10. Worked Example

Input: weeks `1,2,3,4,5`, attendance `90,88,86,84,82`, predict week `10`.

- Attendance drops by 2 every week, so the slope is **-2.00**.
- Working back to week 0 gives an intercept of **92.00**.
- Prediction for week 10: `-2 x 10 + 92 = 72.00`.
- 72.00 is below 75, so the program shows a warning.

Output:

```
Slope: -2.00 | Intercept: 92.00
Predicted attendance for week 10: 72.00%
Warning: below 75%
```

## 11. Code Explanation

| Part of the code | What it does |
|------------------|--------------|
| Imports | Loads NumPy and Pandas |
| Step 1: Take input | Asks for manual input or a CSV file and builds the `weeks` and `attendance` lists |
| Step 2: Validate | Checks the number of weeks, matching lengths and the 0-100 range |
| Step 3: Fit a straight line | `np.polyfit(weeks, attendance, 1)` returns `slope` and `intercept` |
| Step 4: Predict | Calculates `slope * future_week + intercept` and limits it with `max(0, min(100, predicted))` |
| Step 5: Show result | Prints slope, intercept, prediction and the Safe / Warning message |

## 12. Test Cases

| Test Case | Input | Expected Output | Result |
|-----------|-------|-----------------|--------|
| 1. Normal input | Weeks 1-5, Attendance 90, 88, 86, 84, 82; predict week 10 | Slope -2.00, Intercept 92.00, 72.00%, Warning: below 75% | Pass |
| 2. Boundary / minimum input | Weeks 1-2, Attendance 90, 80; predict week 3 | Slope -10.00, Intercept 100.00, 70.00%, Warning: below 75% | Pass |
| 3a. Invalid input | Week 1 only, Attendance 90 | At least 2 weeks of data are required. | Pass |
| 3b. Invalid input | Weeks 1-3, Attendance 90, 105, 80 | Attendance must be between 0 and 100. | Pass |
| 4. Different valid scenario | Weeks 1-5, Attendance 70, 74, 78, 82, 86; predict week 9 | Slope 4.00, Intercept 66.00, 100.00% (capped at 100), Safe | Pass |

Screenshots of these runs are in `Attendance_Predictor_Summary.docx`.

## 13. Project Files

| File | Description |
|------|-------------|
| `attendance_predictor.py` | Main program |
| `Attendance_Predictor_Summary.docx` | Project summary report with test case screenshots |
| `README.md` | This file |

## 14. Troubleshooting

| Problem | Fix |
|---------|-----|
| `ModuleNotFoundError: No module named 'numpy'` (or pandas) | Run `python -m pip install numpy pandas` |
| `python` is not recognised | Use `python3`, or reinstall Python and tick "Add Python to PATH" |
| Wrong Python used in VS Code | Press Ctrl+Shift+P, choose "Python: Select Interpreter" and pick the one where you installed the libraries |
| CSV file not found | Check the file path, or keep the CSV in the same folder as the program |
| "Please enter numbers only." | Use digits and commas only, with no letters or symbols (e.g. `90,88,86`) |

## 15. Limitations

- A straight line is a simple model, so real attendance may not follow it exactly.
- Predictions for weeks far in the future are less reliable.
- Holidays, exams and other factors are not considered.

## 16. Future Improvements

- Plot the data and the fitted line with Matplotlib.
- Predict attendance for several future weeks at once.
- Tell the student how many classes they need to attend to reach 75%.
- Build a simple GUI or web interface.

## 17. Conclusion

The Attendance Percentage Predictor fits a straight line to weekly attendance, validates the input, predicts attendance for a future week within 0-100 and gives a clear Safe or Warning message. All four test cases from the problem statement give the expected output.

---

**Author:** Aditya Choudhary
