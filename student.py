# Define a function to calculate the average grade
def calculate_average(grades):
    return sum(grades) / len(grades)

# List of students with their grades
students = [
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [92, 88, 84]},
    {"name": "Charlie", "grades": [70, 75, 80]},
    {"name": "Diana", "grades": [95, 90, 93]}
]

# Open a file to write the results
with open("student_averages.txt", "w") as file:
    for student in students:
        # Calculate the average grade for each student
        average_grade = calculate_average(student["grades"])
        # Write the student's name and average grade to the file
        file.write(f"{student['name']}: {average_grade:.2f}\n")

print("Student averages have been written to 'student_averages.txt'")

