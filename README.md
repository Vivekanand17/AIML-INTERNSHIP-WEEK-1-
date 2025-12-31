Week 1 Assessment – Python Foundations
1️. Task Understanding
The goal of this assessment was to work with a raw CSV file using basic Python only, without using Pandas. The focus was on reading the file manually, handling missing values properly, and performing simple statistical and frequency analysis.

2️. Reading the CSV File (Without Pandas)
The CSV file was read using Python file-handling functions.
open() was used to open the file in read mode, and readlines() was used to read all lines into a list.
The first line was treated as the header, which contains column names. These were separated using split(',').
The remaining lines were considered as data rows, and each row was split into individual values for processing.

3️. Handling Missing Values
The dataset contained missing values in different forms such as empty strings, "NA", "null", and "None".
Before using any value, a simple check was applied. If a value was missing, it was skipped.
This helped avoid errors and ensured that missing data did not affect calculations.

4️. Statistical Calculations Using NumPy
After cleaning the data, one numeric column was selected for analysis.
Valid values were converted into numeric format and then NumPy was used to calculate:
mean
median
standard deviation
NumPy was used only on clean data to get accurate results.

5️. Frequency Analysis of Categorical Data
For a non-numeric column, a dictionary was used to count how many times each value appeared.
Missing values were ignored during counting.
After counting, the data was sorted to find the top five most frequent values along with their counts.

6️. Report and Execution
The final results were saved into a text file called summary_report.txt, which contains the analysis summary.
To run the program: python analysis.py


