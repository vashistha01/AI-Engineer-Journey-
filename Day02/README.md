# Day 2

## Part 1: Reusable Missing Value Cleaner

Today’s focus was on transforming a one-off data cleaning script into a **reusable and interactive function** that can handle missing values in any CSV file.

### Task 1: Build a Reusable Function

Created a function `reusable_data_cleaner()` that:
- Accepts a file path to any CSV.
- Displays a heatmap of missing values **before and after cleaning**.
- Prints missing value stats and column data types.

### Task 2: Make It Interactive

Enhanced the function with:
- **User input** to choose how to fill missing numeric values: `mean`, `median`, or `mode`.
- Auto-fill for missing **text values** with `"Unknown"`.
- Option to **drop rows where all values are missing**.
- Prompts user to optionally **save the cleaned dataset** as a new CSV.

---

## Micro-Project: “Missing Value Handler 1.0”

### Objective:
Build a flexible, interactive Python tool that can clean messy CSV files with minimal manual work.

### Input:
CSV with:
- Missing numeric and text values.
- Potentially entire rows of missing data.

### Output:
- Cleaned DataFrame with:
  - Missing numeric values filled based on user choice.
  - Text values filled with `"Unknown"`.
  - Fully missing rows removed.
- Visual heatmaps showing missing data **before and after** cleaning.
- Optional export to a new CSV file.

### Skills Gained:
- Writing reusable Python functions
- Handling missing data
- User interaction via `input()`
- Data visualization using `seaborn` and `matplotlib`
- Practical pandas usage

---

## Part 2: Visual Feedback

Used **heatmaps** to visually show the state of missing data:
- Before cleaning: Identify problem areas.
- After cleaning: Confirm cleaning effectiveness.

Tool can be reused on any dataset simply by changing the file path.

---

## Example Usage:

```python
cleaned_df = reusable_data_cleaner("path/to/your/dataset.csv")


