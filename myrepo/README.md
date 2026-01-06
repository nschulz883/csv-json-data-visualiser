# CSV / JSON Data Visualiser

## Overview
This project is a portfolio-focused Python application designed to demonstrate foundational data analysis and visualisation skills.  
It allows users to load CSV or JSON datasets, inspect the data, and automatically generate summary statistics and visual insights.

## Key Skills Demonstrated
- Python programming fundamentals
- Data handling with pandas
- Exploratory data analysis (EDA)
- Data visualisation using matplotlib
- Input validation and error handling
- Writing clear and professional documentation

## Features
- Load and parse CSV or JSON files
- Display the first five rows of a dataset
- Generate descriptive statistics for numeric data
- Automatically produce bar charts and histograms

## Tech Stack
- Python
- pandas
- matplotlib

## Sample Data
A small CSV file `sample_data.csv` is included for testing. Example content:

```csv
Name,Age,Score,Hours_Studied
Alice,18,85,5
Bob,19,90,7
Charlie,20,78,6
Diana,21,88,8
Ethan,22,92,4
Fiona,19,81,3
George,20,95,9
Hannah,21,87,6
Ian,22,80,5
Julia,18,89,7

```

## Installation
```bash
git clone https://github.com/nschulz883/csv-json-data-visualiser.git
cd csv-json-data-visualiser
pip install -r requirements.txt
```

## Usage

After installing the project dependencies, follow these steps to use the script:

1. **Run the program**:

```bash
python main.py
Enter a filename (.csv or .json): sample_data.csv
