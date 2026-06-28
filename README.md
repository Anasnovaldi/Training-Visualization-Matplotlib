# 📊 Data Visualization CLI with Python

A simple Command Line Interface (CLI) application for visualizing data from **CSV** and **Excel** files using **Python**, **Pandas**, and **Matplotlib**.

## ✨ Features

* 📈 Line Chart (Plot Chart)
* 📊 Bar Chart
* 🥧 Pie Chart
* Support **CSV (.csv)** and **Excel (.xlsx)** files
* Compare two data series on Bar Chart and Line Chart
* Custom chart title, labels, and colors through terminal input

---

## 🛠️ Built With

* Python 3.x
* Pandas
* Matplotlib
* Openpyxl (for Excel files)

---

## 📦 Installation

Clone this repository

```bash
git clone https://github.com/yourusername/your-repository.git
```

Move into the project folder

```bash
cd your-repository
```

Install the required libraries

```bash
pip install pandas matplotlib openpyxl
```

---

## 🚀 How to Run

Run the program using:

```bash
python LatihanMatplotlib.py
```

---

## 📁 Supported File Formats

### CSV

```csv
Day,Week1,Week2
Monday,10,15
Tuesday,15,20
Wednesday,20,25
Thursday,30,35
Friday,40,45
```

### Excel

The Excel file should have the same table structure as the CSV example above.

---

## 🥧 Pie Chart Format

Pie Chart requires **only two columns**:

| Category  | Value |
| --------- | ----: |
| Product A |    20 |
| Product B |    35 |
| Product C |    45 |

Example CSV:

```csv
Product,Sales
Product A,20
Product B,35
Product C,45
```

---

## 📊 Bar Chart & Line Chart Format

These charts require:

* One column as the X-axis
* One or two numeric columns as the Y-axis

Example:

```csv
Day,Week1,Week2
Monday,10,15
Tuesday,20,18
Wednesday,15,22
Thursday,25,30
Friday,35,40
```

---

## 📌 Notes

* Make sure the CSV or Excel file is in the same folder as the program.
* Column names are case-sensitive.
* Pie Chart is designed for proportional (part-to-whole) data.

---

## 👨‍💻 Author

Developed as a learning project for Python data visualization using Pandas and Matplotlib.
