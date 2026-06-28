![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Library-150458?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![License](https://img.shields.io/badge/License-MIT-green)

# Data Visualization CLI

A command-line application built with **Python** for visualizing data from **CSV** and **Excel** files using **Pandas** and **Matplotlib**.

## Language

* Python 3

## Libraries

* pandas
* matplotlib
* openpyxl

Install dependencies:

```bash
pip install pandas matplotlib openpyxl
```

## Features

* Bar Chart
* Line Chart
* Pie Chart
* CSV and Excel support
* Single or multiple data comparison
* Custom chart title, labels, and colors

## Usage

Run the application:

```bash
python LatihanMatplotlib.py
```

Place your `.csv` or `.xlsx` file in the same directory as the program, then follow the prompts displayed in the terminal.

## Data Format

**Bar Chart / Line Chart**

| Category | Value 1 | Value 2 |
| -------- | ------: | ------: |
| A        |      10 |      15 |
| B        |      20 |      25 |
| C        |      30 |      35 |

**Pie Chart**

| Category | Value |
| -------- | ----: |
| A        |    20 |
| B        |    35 |
| C        |    45 |

## Notes

* Column names are case-sensitive.
* Pie Chart supports one label column and one numeric value column.
* CSV and Excel files should be located in the same directory as the application.

## License

This project is intended for learning purposes and personal use.
