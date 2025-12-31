import numpy as np

# -------- STEP 1: Read CSV manually --------
file = open("data.csv", "r")
lines = file.readlines()
file.close()

header = lines[0].strip().split(",")
rows = lines[1:]

marks_index = header.index("Marks")
dept_index = header.index("Department")

marks_list = []
dept_list = []
missing_count = 0
total_rows = 0

missing_values = ["", "NA", "null", "None"]

# -------- STEP 2: Process data & handle missing --------
for row in rows:
    total_rows += 1
    values = row.strip().split(",")

    # Handle Marks
    mark = values[marks_index]
    if mark in missing_values:
        missing_count += 1
    else:
        marks_list.append(int(mark))

    # Handle Department
    dept = values[dept_index]
    if dept not in missing_values:
        dept_list.append(dept)

# -------- STEP 3: Statistics using NumPy --------
marks_array = np.array(marks_list)

mean_marks = np.mean(marks_array)
median_marks = np.median(marks_array)
std_marks = np.std(marks_array)

# -------- STEP 4: Frequency count (dictionary) --------
dept_count = {}

for d in dept_list:
    if d in dept_count:
        dept_count[d] += 1
    else:
        dept_count[d] = 1

top_departments = sorted(dept_count.items(), key=lambda x: x[1], reverse=True)

# -------- STEP 5: Write summary report --------
report_str = ""
report_str += "Column Analyzed: Marks\n"
report_str += "Category Analyzed: Department\n\n"

report_str += f"Total Records: {total_rows}\n"
report_str += f"Missing Marks: {missing_count}\n\n"

report_str += f"Mean Marks: {round(mean_marks,2)}\n"
report_str += f"Median Marks: {median_marks}\n"
report_str += f"Standard Deviation: {round(std_marks,2)}\n\n"

report_str += "Department Wise Count:\n"
for dept, count in top_departments:
    report_str += f"{dept} - {count}\n"

report = open("summary_report.txt", "w")
report.write(report_str)
report.close()

print(report_str)
print("Report created successfully.")
